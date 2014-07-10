--------
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


-------
Scripts
-------

This project encapsulates four executable scripts, three of them Python:

------------   -------------------------------------------------------
Name           Description
------------   -------------------------------------------------------
ck_create_ca   Create CA keys and certificate
ck_create      Create normal keys
ck_sign        Create a signed certificate using the CA identity
ck_verify_ca   Verify that the signed certificate was issued by the CA
------------   -------------------------------------------------------

The Python scripts use M2Crypto to manipulate the keys/certificates.


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

3. Sign the identity::

      $ ck_sign
      Please confirm output directory []: output

   This generates:

   - *normal.crt.pem*

4. You can also verify that the identity was signed by our CA::

      $ ck_verify_ca
      Please confirm input directory []: output
      Verified.
