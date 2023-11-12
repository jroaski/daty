FROM python:3.11

WORKDIR /app

COPY src/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

EXPOSE 8080

ENV FLASK_APP=flask_integration.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

CMD ["flask", "run"]
