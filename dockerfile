FROM python:latest
RUN pip install dnslib
EXPOSE 80
COPY . .
CMD ["python","proxy_server_dns.py"]
