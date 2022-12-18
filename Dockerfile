FROM python:3.7
RUN mkdir /app
WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5050
RUN pip3 install --no-cache-dir -r requirements.txt
CMD [ "python3", "convertor/convertor_service.py"]
