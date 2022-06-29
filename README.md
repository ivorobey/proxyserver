Python DNS proxy server with blacklist support using [dnslib](https://pypi.python.org/pypi/dnslib) library

# dns proxyserver in python

'On remote VM:'

   1) docker build -t somename .
   
   2) docker run --name somename -d --network host somename

'On your linux:'

   1)change default nameserver in the /etc/resolv.conf to ip your remote VM (nameserver {ip vm})
   
   2)nslookup yoursite
