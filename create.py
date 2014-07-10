#!/usr/bin/env python2.7

import os
import os.path
import argparse

import ssl_library

_OUTPUT_PATH = 'output'
_CA_PASSPHRASE = 'test'

parser = argparse.ArgumentParser(description='Generate an identity')
parser.add_argument('-n', '--name',
                    default='normal', 
                    help='Name used for the filenames')

parser.add_argument('-c', '--common-name',
                    help='Name used for the filenames')

parser.add_argument('-a', '--allow_auth',
                    action='store_true',
                    help='Whether to allow this certificate to be used for '\
                         'authentication.')

args = parser.parse_args()

common_name = args.common_name if args.common_name else args.name + '.local'

name = {
    'C': 'US',
    'ST': 'Florida',
    'O': 'Some Entity',
    'CN': common_name }

r = ssl_library.create_csr(allow_auth=args.allow_auth, **name)
(private_key_pem, public_key_pem, csr_pem) = r

if os.path.exists(_OUTPUT_PATH) is False:
    os.mkdir(_OUTPUT_PATH)

with open(os.path.join(_OUTPUT_PATH, args.name + '.key.pem'), 'w') as f:
    f.write(private_key_pem)

with open(os.path.join(_OUTPUT_PATH, args.name + '.public.pem'), 'w') as f:
    f.write(public_key_pem)

with open(os.path.join(_OUTPUT_PATH, args.name + '.csr.pem'), 'w') as f:
    f.write(csr_pem)
