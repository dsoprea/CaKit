#!/bin/sh

openssl verify -verbose -CAfile output/ca.crt.pem output/sub.crt.pem 
