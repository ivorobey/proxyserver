# dns proxyserver in python

1) On remote VM:
   1)docker build -t somename .
   2)docker run --name somename -d --network host somename

2)On your linux:
  1)change default nameserver in the /etc/resolv.conf to ip your remote VM (nameserver {ip vm})
  2)nslookup yoursite
