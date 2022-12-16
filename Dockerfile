FROM python:3.7
WORKDIR /opt/app
COPY . .
EXPOSE 5050
CMD [ "python", "../convertor/convertor_service.py"]
