FROM python:3.10

EXPOSE 5000

RUN mkdir -p /opt/services/bot/serega
WORKDIR /opt/services/bot/serega



COPY . /opt/services/bot/serega

RUN pip install -r requirements.txt

CMD['python', '/opt/services/bot/serega/main.py']