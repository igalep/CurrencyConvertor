FROM python:3.7
WORKDIR /opt/app
COPY . .
EXPOSE 5050
RUN pip3 install --no-cache-dir -r requirements.txt
CMD [ "python3", "../convertor/convertor_service.py"]
