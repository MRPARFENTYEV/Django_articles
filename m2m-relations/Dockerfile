# syntax=docker/dockerfile:1

FROM python:3.9
WORKDIR /articles
COPY . /articles
RUN pip install --no-cache-dir -r requirements.txt
ENV my_env =virtualenv
EXPOSE 3000
#CMD ["python3","-u","manage.py","--host","0.0.0.0","--port","8000"]
CMD ["python manage.py runserver,0.0.0.0:8000"]
#CMD ["python3","-u", "manage.py", "runserver", "127.0.0.1:5432"]
#прописываю какая команда должна быть выполнена

