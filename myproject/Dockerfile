FROM python:3
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . /app
ARG BUILD_DATE
ENV BUILD_DATE=$BUILD_DATE
ENV STUDENT_NAME='Siarhei Kazak'
ENTRYPOINT [ "python" ]
CMD [ "app/app.py" ]
