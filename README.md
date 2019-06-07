## portscan.py
### a simple tcp portscanner

This a very basic and simple portscanner that makes use of python3's
sockets and threading to scan a host for listening tcp ports.

Usage:
```
$ ./portscan.py  -h localhost -p 22
Usage: Usage of program:-H <target host> -p <target port(s)

Options:
  -h, --help  show this help message and exit
  -H TGTHOST  specify target hosts
  -p TGTPORT  specify target ports seperated by comma
```