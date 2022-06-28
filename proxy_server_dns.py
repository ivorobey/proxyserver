import json

from dnslib import RR, A
from dnslib.proxy import ProxyResolver
from dnslib.server import DNSServer


class MyProxResolv(ProxyResolver):
    def __init__(self, address, port, timeout, blacklist, answer, host):
        self.address=address
        self.port=port
        self.timeout=timeout
        self.blacklist = blacklist
        self.answer = answer
        self.host = host

    def resolve(self, request, handler):
        if request.q.qname in self.blacklist:
            answer = RR(rdata=A(self.host))
            answer.set_rname(self.answer)
            reply = request.reply()
            reply.add_answer(answer)    
            return reply 
        else:
            return ProxyResolver.resolve(self, request, handler)


if __name__ == '__main__':
    import time

    config_file = open('config.json')
    config = json.load(config_file)
    config_file.close()

    resolver = MyProxResolv(address=config['upper_dns'],
                            port=config['port'],
                            timeout=config['timeout'],
                            blacklist=config['blacklist'],
                            answer=config['answer'],
                            host=config['host'])
 
    server = DNSServer(resolver,
                       port=config['port'],
                       address=config['host'])
    
    server.start_thread()

    while server.isAlive():
        time.sleep(1)
