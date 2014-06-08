Overview
--------

The purpose of this tiny project is just to package the logic needed to build 
both CA certificates and a signed, subordinate certificate.

I find that I often need to do this, and/or need to do this as part of other 
projects as a starting example. This project assumes some defaults, and makes 
it easy to establish a CA and build certificates.

The include scripts are largely Python. So, for those who'd like a quick 
tutorial on how to do these tasks via Python, they might also use this project
as a roadmap.


Scripts
-------

This project encapsulates four executable scripts, three of them Python:

| Name                  | Description                                                         |
| --------------------- | ------------------------------------------------------------------- |
| create_ca.py          | Create CA keys and certificate                                      |
| create_subordinate.py | Create subordinate keys                                             |
| sign_sub.py           | Create a signed cert from the CA identity                           |
| verify_ca.sh          | Verify that the signed subordinate certificate was issued by the CA |

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

2. Create the subordinate identity:

   ```
   $ ./create_subordinate.py
   ```

   This generates:

   *output/sub.csr.pem*<br />
   *output/sub.public.pem*<br />

3. Sign the subordinate identity:

   ```
   $ ./sign_sub.py
   ```

   This generates:

   *sub.crt.pem*<br />

4. You can also verify that the subordinate identity was signed by our CA:

   ```
   $ ./verify_ca.sh 
   output/sub.crt.pem: OK
   ```
