FROM python:3.8-slim-buster

WORKDIR /backend

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# 挂载/app目录便于开发
VOLUME ["/app"]

# uses --host=0.0.0.0 to allow connections from outside the container
CMD ["flask", "run", "--host=0.0.0.0"]


