#!/usr/bin/env python2.7

import time
import hashlib
import random
import datetime

import M2Crypto.X509
import M2Crypto.EVP
import M2Crypto.ASN1
import M2Crypto.RSA
import M2Crypto.BIO

_SERIAL_NUMBER_GENERATOR_CB = lambda: \
                                hashlib.sha1(str(time.time()) + str(random.random())).\
                                    hexdigest()

def pem_private_to_rsa(private_key_pem, passphrase=None):
    def passphrase_cb(*args):
        return passphrase

    rsa = M2Crypto.RSA.load_key_string(
            private_key_pem, 
            callback=passphrase_cb)

    return rsa

def pem_csr_to_csr(csr_pem):
    return M2Crypto.X509.load_request_string(csr_pem)

def pem_certificate_to_x509(cert_pem):
    return M2Crypto.X509.load_cert_string(cert_pem)

def new_cert(ca_private_key_pem, csr_pem, validity_td, issuer_name, bits=2048,
             is_ca=False, passphrase=None):
    ca_rsa = pem_private_to_rsa(
                ca_private_key_pem, 
                passphrase=passphrase)

    def callback(*args):
        pass

    csr = pem_csr_to_csr(csr_pem)

    public_key = csr.get_pubkey()
    name = csr.get_subject()

    cert = M2Crypto.X509.X509()

    sn_hexstring = _SERIAL_NUMBER_GENERATOR_CB()
    sn = int(sn_hexstring, 16)

    cert.set_serial_number(sn)
    cert.set_subject(name)

    now_epoch = long(time.time())

    notBefore = M2Crypto.ASN1.ASN1_UTCTIME()
    notBefore.set_time(now_epoch)

    notAfter = M2Crypto.ASN1.ASN1_UTCTIME()
    notAfter.set_time(now_epoch + long(validity_td.total_seconds()))

    cert.set_not_before(notBefore)
    cert.set_not_after(notAfter)

    cert.set_issuer(issuer_name)
    cert.set_pubkey(public_key) 

    ext = M2Crypto.X509.new_extension('basicConstraints', 'CA:FALSE')
    cert.add_ext(ext)

    pkey = M2Crypto.EVP.PKey()
    pkey.assign_rsa(ca_rsa)

    cert.sign(pkey, 'sha1')
    cert_pem = cert.as_pem()

    return cert_pem

def sign(ca_key_filepath, ca_crt_filepath, csr_filepath, passphrase=None):
    with open(ca_crt_filepath) as f:
        ca_cert_pem = f.read()

    with open(ca_key_filepath) as f:
        ca_private_key_pem = f.read()

    ca_cert = pem_certificate_to_x509(ca_cert_pem)

    issuer_name = ca_cert.get_issuer()

    with open(csr_filepath) as f:
        csr_pem = f.read()

    validity_td = datetime.timedelta(days=400)
    return new_cert(
            ca_private_key_pem, 
            csr_pem, 
            validity_td, 
            issuer_name, 
            passphrase=passphrase)

def new_selfsigned_cert(issuer_name, passphrase, validity_td, bits=2048, 
                        is_ca=False):

    pair = new_key(passphrase)
    (private_key_pem, public_key_pem) = pair

    csr_pem = new_csr(
                private_key_pem, 
                issuer_name, 
                passphrase=passphrase)

    cert_pem = new_cert(
                private_key_pem, 
                csr_pem, 
                validity_td, 
                issuer_name, 
                passphrase=passphrase,
                is_ca=is_ca)

    return (private_key_pem, public_key_pem, csr_pem, cert_pem)

def new_csr(private_key_pem, name, passphrase=None):
    rsa = pem_private_to_rsa(
            private_key_pem, 
            passphrase=passphrase)

    pkey = M2Crypto.EVP.PKey()
    pkey.assign_rsa(rsa)
    rsa = None # should not be freed here

    csr = M2Crypto.X509.Request()
    csr.set_pubkey(pkey)
    csr.set_subject(name)

    csr.sign(pkey, 'sha1')

    return csr.as_pem()

def rsa_to_pem_private(rsa, passphrase=None):
    bio = M2Crypto.BIO.MemoryBuffer()

    private_key_kwargs = {}
    if passphrase is None:
        private_key_kwargs['cipher'] = None
    else:
        def passphrase_cb(arg1):
            return passphrase

        private_key_kwargs['callback'] = passphrase_cb

    rsa.save_key_bio(bio, **private_key_kwargs)
    return bio.read()

def rsa_to_pem_public(rsa):
    bio = M2Crypto.BIO.MemoryBuffer()
    rsa.save_pub_key_bio(bio)
    return bio.read()

def new_key_primitive(bits=2048):
    # This is called during key-generation to provide visual feedback. The 
    # default callback shows progress dots.
    def progress_cb(arg1, arg2):
        pass

    return M2Crypto.RSA.gen_key(bits, 65537, progress_cb)

def new_key(passphrase=None, bits=2048):
    rsa = new_key_primitive(bits)

    private_key_pem = rsa_to_pem_private(rsa, passphrase)
    public_key_pem = rsa_to_pem_public(rsa)

    return (private_key_pem, public_key_pem)

def build_name_from_dict(**kwargs):
    name = M2Crypto.X509.X509_Name()
    for (k, v) in kwargs.items():
        try:
            M2Crypto.X509.X509_Name.nid[k]
        except KeyError as e:
            raise KeyError(k)

        setattr(name, k, v)

    return name

def create_csr(**name_fields):
    pk = M2Crypto.EVP.PKey()
    x = M2Crypto.X509.Request()

    rsa = new_key_primitive()
    pk.assign_rsa(rsa)
    x.set_pubkey(pk)

    name = x.get_subject()

    for k, v in name_fields.items():
        setattr(name, k, v)

    public_key_pem = rsa_to_pem_public(rsa)
    private_key_pem = rsa_to_pem_private(rsa)
    csr_pem = x.as_pem()

    return (private_key_pem, public_key_pem, csr_pem)
