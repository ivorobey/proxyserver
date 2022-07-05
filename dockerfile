FROM python:latest
RUN pip install dnslib
COPY . .
CMD ["python","proxy_server_dns.py"]
