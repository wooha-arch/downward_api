FROM python3.9-slim

RUN apt-get update && apt-get install -y curl

WORKDIR /app

COPY app.py /app

RUN pip install Flask

CMD ["python", "app.py"]