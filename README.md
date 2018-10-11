# GT_router

Written by nakajo@west.sd.keio.ac.jp

## Overview

## Installation

## Dependencies
- Python 2.7.10

## Setting at KIDs servers

- sudo apt-get clean
- sudo apt-get update
- sudo apt-get install python-pip
- export LC_ALL="en_US.UTF-8"
- export LC_CTYPE="en_US.UTF-8"
- sudo dpkg-reconfigure locales
- apt update (DO NOT use "pip install --upgrade pip" due to the file managing consistency)
- sudo python -m pip install grpcio
- sudo python -m pip install grpcio-tools googleapis-common-protos

## References

## Initiating .proto
- python -m grpc_tools.protoc -I../../protos --python_out=. --grpc_python_out=. ../../protos/GT_balance.proto


