Overview
--------

The purpose of this tiny project is just to package the logic needed to build 
both CA certificates and a regulary, signed certificate.

I find that I often need to do this, and/or need to do this as part of other 
projects as a starting example. This project assumes some defaults, and makes 
it easy to establish a CA and build certificates.

The include scripts are largely Python. So, for those who'd like a quick 
tutorial on how to do these tasks via Python, they might also use this project
as a roadmap.


Scripts
-------

This project encapsulates four executable scripts, three of them Python:

| Name                  | Description                                             |
| --------------------- | --------------------------------------------------------|
| create_ca.py          | Create CA keys and certificate                          |
| create.py             | Create normal keys                                      |
| sign.py               | Create a signed certificate using the CA identity       |
| verify_ca.sh          | Verify that the signed certificate was issued by the CA |

The Python scripts use M2Crypto to manipulate the keys/certificates.


Installation
------------

This project can not be installed. Clone it from the GitHub project, and run 
the following to install the dependencies:

```
$ sudo pip install -r requirements.txt
```


Usage
-----

1. Create the CA:

   ```
   $ ./create_ca.py
   ```

   This generates:

   *output/ca.crt.pem*<br />
   *output/ca.csr.pem*<br />
   *output/ca.key.pem*<br />
   *output/ca.public.pem*<br />

2. Create the normal keys:

   ```
   $ ./create.py
   ```

   This generates:

   *output/normal.csr.pem*<br />
   *output/normal.key.pem*<br />
   *output/normal.public.pem*<br />

3. Sign the identity:

   ```
   $ ./sign.py
   ```

   This generates:

   *normal.crt.pem*<br />

4. You can also verify that the identity was signed by our CA:

   ```
   $ ./verify_ca.sh 
   output/normal.crt.pem: OK
   ```
