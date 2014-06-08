#!/usr/bin/env python2.7

import os
import os.path
import datetime

import ssl_library

_OUTPUT_PATH = 'output'
_CA_PASSPHRASE = 'test'

name_fields = {
    'C': 'US',
    'ST': 'Florida',
    'L': 'Boynton Beach',
    'CN': 'ca.local' }

name = ssl_library.build_name_from_dict(**name_fields)
validity_td = datetime.timedelta(days=1000)

r = ssl_library.new_selfsigned_cert(
        name, 
        _CA_PASSPHRASE, 
        validity_td, 
        is_ca=True)

(private_key_pem, public_key_pem, csr_pem, cert_pem) = r

if os.path.exists(_OUTPUT_PATH) is False:
    os.mkdir(_OUTPUT_PATH)

with open(os.path.join(_OUTPUT_PATH, 'ca.key.pem'), 'w') as f:
    f.write(private_key_pem)

with open(os.path.join(_OUTPUT_PATH, 'ca.public.pem'), 'w') as f:
    f.write(public_key_pem)

with open(os.path.join(_OUTPUT_PATH, 'ca.csr.pem'), 'w') as f:
    f.write(csr_pem)

with open(os.path.join(_OUTPUT_PATH, 'ca.crt.pem'), 'w') as f:
    f.write(cert_pem)
