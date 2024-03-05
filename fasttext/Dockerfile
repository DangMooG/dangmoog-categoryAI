FROM python:3.9

COPY . /home/fasttext-server
WORKDIR /home/fasttext-server

RUN apt-get update
RUN pip install -r requirements.txt

CMD ["python","main.py"]
