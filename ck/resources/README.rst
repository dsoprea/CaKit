--------
Overview
--------

The purpose of this project is to package the logic needed to:

- Build a CA certificates
- Build a regular certificate
- Sign the regular certificate with the CA certificate
- Verify that the regular certificate is signed with the CA certificate

I find that I often need to do this, and/or need to do this as part of other 
projects to prove a design. This project assumes some defaults, and makes it 
ridiculously easy to establish a CA and build certificates. You can pass
parameters to change the name of the output files, and the path that they are
written to.

The scripts are comprised of Python logic. So, for those who'd like a quick 
tutorial on how to do these tasks via Python, they can use this project as a 
roadmap.


-------
Scripts
-------

This project encapsulates four executable scripts.

============   ============================================================
Name           Description
============   ============================================================
ck_create_ca   Create CA keys and certificate
ck_create      Create normal keys
ck_sign        Create a signed certificate using the CA certificate and key
ck_verify_ca   Verify that the signed certificate was issued by the CA
============   ============================================================

The Python scripts use M2Crypto_ to manipulate the keys/certificates.


------------
Installation
------------

This project can not be installed. Clone it from the GitHub project, and run 
the following to install the dependencies::

   $ sudo pip install -r requirements.txt


-----
Usage
-----

To specify a directory, use the "-o" parameter. If none is given, you will be 
prompted to confirm.

1. Create the CA::

      $ ck_create_ca
      Please confirm output directory []: output

   This generates:

   - *ca.crt.pem*
   - *ca.csr.pem*
   - *ca.key.pem*
   - *ca.public.pem*

2. Create the normal keys::

      $ ck_create
      Please confirm output directory []: output

   This generates:

   - *normal.csr.pem*
   - *normal.key.pem*
   - *normal.public.pem*

3. Sign the request::

      $ ck_sign
      Please confirm output directory []: output

   This generates:

   - *normal.crt.pem*

4. Verify that the certificate was signed by our CA::

      $ ck_verify_ca
      Please confirm input directory []: output
      Is valid? True

.. _M2Crypto: https://github.com/martinpaljak/M2Crypto
