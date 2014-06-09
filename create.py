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

args = parser.parse_args()

name = {
    'C': 'US',
    'ST': 'Florida',
    'O': 'Some Entity',
    'CN': args.name + '.local' }

(private_key_pem, public_key_pem, csr_pem) = ssl_library.create_csr(**name)

if os.path.exists(_OUTPUT_PATH) is False:
    os.mkdir(_OUTPUT_PATH)

with open(os.path.join(_OUTPUT_PATH, args.name + '.key.pem'), 'w') as f:
    f.write(private_key_pem)

with open(os.path.join(_OUTPUT_PATH, args.name + '.public.pem'), 'w') as f:
    f.write(public_key_pem)

with open(os.path.join(_OUTPUT_PATH, args.name + '.csr.pem'), 'w') as f:
    f.write(csr_pem)
