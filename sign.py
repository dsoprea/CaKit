#!/usr/bin/env python2.7

import os.path
import argparse

import ssl_library

_OUTPUT_PATH = 'output'
_CA_PASSPHRASE = 'test'

_CA_KEY_PEM_FILENAME = 'output/ca.key.pem'
_CA_CRT_PEM_FILENAME = 'output/ca.crt.pem'

parser = argparse.ArgumentParser(description='Generate an identity')
parser.add_argument('-n', '--name',
                    default='normal', 
                    help='Name used for the filenames')

# We put this as an option for both the creation -and- the signing. M2Crypto
# doesn't allow us to read the extensions from a CSR, but this is fine for 
# ca_key.
parser.add_argument('-a', '--allow_auth',
                    action='store_true',
                    help='Whether to allow this certificate to be used for '\
                         'authentication.')

args = parser.parse_args()

_NORMAL_CSR_PEM_FILENAME = os.path.join('output', args.name + '.csr.pem')

with open(os.path.join(_OUTPUT_PATH, args.name + '.crt.pem'), 'w') as f:
    crt_pem = ssl_library.sign(
                _CA_KEY_PEM_FILENAME,
                _CA_CRT_PEM_FILENAME,
                _NORMAL_CSR_PEM_FILENAME, 
                passphrase=_CA_PASSPHRASE,
                allow_auth=args.allow_auth)
    f.write(crt_pem)
