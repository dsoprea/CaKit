#!/bin/sh

if [ "$1" == "" ]; then
    echo "Please provide a name."
    exit 1
fi

openssl verify -verbose -CAfile output/ca.crt.pem output/$1.crt.pem 
