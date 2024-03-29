#!/usr/bin/python3

from socket import *
import optparse
from threading import *


def connnScan(tgtHost, tgtPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tgtHost,tgtPort))
        print('[+] {}tcp open'.format(tgtPort))
    except:
        print('[+] {}tcp closed'.format(tgtPort))
    finally:
        sock.close()

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print('Unknown Host {}'.format(tgtHost))
    try:
        tgtName = gethostbyaddr(tgtIP)
        print('[+] Scan Results for: {}'.format(tgtName[0]))
    except:
        print('[+] Scan Results for: {}'.format(tgtIP))
    setdefaulttimeout(2)
    for tgtPort in tgtPorts:
        t =Thread(target=connnScan, args=(tgtHost, int(tgtPort)))
        t.start()
        
def main():
    parse = optparse.OptionParser('Usage of program:' + '-H <target host> -p <target port(s)')
    parse.add_option('-H', dest='tgtHost', type='string', help='specify target hosts')
    parse.add_option('-p', dest='tgtPort', type='string', help='specify target ports seperated by comma')
    (options, args) = parse.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if (tgtHost == None) | (tgtPorts[0] == None):
        print(parse.usage)
        exit(0)
    portScan(tgtHost,tgtPorts)

if __name__ == '__main__':
    main()