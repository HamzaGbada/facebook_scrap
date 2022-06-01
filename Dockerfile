FROM python:3.8-slim-buster
WORKDIR /project
ADD . /project
RUN apt-get update
RUN pip install --default-timeout=100 -r requirements.txt
EXPOSE 8000
CMD ["python", "main.py"]
