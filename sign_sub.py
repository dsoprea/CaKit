#!/usr/bin/env python2.7

import os.path

import ssl_library

_OUTPUT_PATH = 'output'
_CA_PASSPHRASE = 'test'

_CA_KEY_PEM_FILENAME = 'output/ca.key.pem'
_CA_CRT_PEM_FILENAME = 'output/ca.crt.pem'
_SUB_CSR_PEM_FILENAME = 'output/sub.csr.pem'

with open(os.path.join(_OUTPUT_PATH, 'sub.crt.pem'), 'w') as f:
    crt_pem = ssl_library.sign(
                _CA_KEY_PEM_FILENAME,
                _CA_CRT_PEM_FILENAME,
                _SUB_CSR_PEM_FILENAME, 
                passphrase=_CA_PASSPHRASE)
    f.write(crt_pem)
