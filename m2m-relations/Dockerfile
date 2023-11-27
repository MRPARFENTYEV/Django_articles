# syntax=docker/dockerfile:1
#установка питона
#FROM nginx:latest
#COPY index.html /usr/share/nginx/html
#CMD ["nginx", "-g", "daemon off;"]
#FROM python:3.9
#COPY . /python
#WORKDIR /python
#RUN pip install --upgrade pip
#COPY requirements.txt /code/
#RUN pip install -r requirements.txt
#
#
#
#RUN pip install --no-cache-dir --upgrade -r requirements.txt
#
#ENV my_env =virtualenv
#EXPOSE 8000
#
#CMD ["python manage.py runserver 0.0.0.0:8000"]
#CMD ["python3","-u","manage.py","--host","0.0.0.0","--port","8000"]

#CMD ["python3","-u", "manage.py", "runserver", "127.0.0.1:5432"]
#прописываю какая команда должна быть выполнена
FROM python:3.9


RUN mkdir /code
WORKDIR /code
RUN pip install --upgrade pip
COPY requirements.txt /code/

RUN pip install -r requirements.txt
COPY . /code/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]