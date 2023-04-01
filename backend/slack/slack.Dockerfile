FROM python:3-slim
WORKDIR /usr/src/app
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app.py .
COPY ./consumer-slack.py .
# COPY ./error.py .
COPY .env .
CMD ["sh", "-c", "python app.py & python consumer-slack.py"]