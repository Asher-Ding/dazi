# Dockerfile
# docker build -t flask -f Dockerfile .
# docker run -it --rm -v $(pwd)/:/backend -p 5000:5000 flask

FROM python:3.8.16

WORKDIR /backend

VOLUME [ "/backend/src" ]

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python", './app/app.py']


