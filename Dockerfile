FROM python:3.9-slim

WORKDIR /app
COPY app.py /app/app.py

EXPOSE 80

CMD ["python", "app.py"]
