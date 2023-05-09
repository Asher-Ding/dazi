# TODO Dockerfile 多阶段构建方案分离开发环境和生产环境
# docker build -t flask -f Dockerfile .
# docker run -it --rm -v $(pwd)/:/backend -p 5000:5000 flask
# Reference: https://github.com/cookiecutter-flask/cookiecutter-flask/blob/master/%7B%7Bcookiecutter.app_name%7D%7D/Dockerfile

# ==================== BUILDER ====================
FROM python:3.8.16

WORKDIR /backend

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# ==================== 生产环境 ====================

# ==================== 开发环境 ====================
VOLUME [ "/backend/app" ]

# ENV PYTHONPATH="${PYTHONPATH}:/backend"
ENV FLASK_ENV=development

EXPOSE 5000

CMD ["flask", "run","--debugger", "--host=0.0.0.0", "--port=5000"]