FROM ubuntu:16.04
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 5000
COPY . /app
ARG BUILD_DATE
ENV BUILD_DATE=$BUILD_DATE
ENV STUDENT_NAME='Siarhei Kazak'
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
CMD [ "python3", "app/app.py" ]
