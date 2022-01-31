# Dockerfile, Image, Container
FROM python:3.9

ADD project.py .

RUN pip install flask 

CMD ["python", "./project.py"]
