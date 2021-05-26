# Dockerfile, Image, Container
FROM python:3.8

WORKDIR ./frits-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY pictures pictures
COPY checkpoints checkpoints

COPY beer_classification.py .
COPY object_detection.py .
COPY get_image.py .
COPY connection.py .
COPY production.py .

CMD ["python", "./production.py"]