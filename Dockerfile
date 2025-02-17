FROM python:3.10
WORKDIR /usr/src/app
ADD . /usr/src/app
CMD ["python", "/book/app/main.py"]
