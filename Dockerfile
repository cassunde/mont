FROM python:3.10

WORKDIR /app

COPY *.py .
COPY requirements.txt .
COPY config.yml .
RUN mkdir exported
RUN mkdir config
RUN pip install --upgrade pip && pip install -r requirements.txt
ENTRYPOINT ["python", "main.py"]
EXPOSE 8000
CMD ["tail", "-f", "/var/log/app.log"]