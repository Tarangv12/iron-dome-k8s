FROM python:3.9-slim

COPY honeypot.py /app/honeypot.py

WORKDIR /app

CMD ["python" , "honeypot.py"]