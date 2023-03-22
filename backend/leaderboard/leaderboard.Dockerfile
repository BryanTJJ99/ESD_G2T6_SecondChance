FROM python:3-slim
WORKDIR /usr/src/app
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app.py .
COPY ./consumer-leaderboard.py .
# COPY ./error.py .
COPY .env .
CMD [ "python", "./app.py" ]