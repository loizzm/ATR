FROM python:3.8
COPY . ./app
RUN apt-get install -y libmariadb-dev
RUN pip install -r /app/requirements.txt
EXPOSE 5000
CMD ["python3.8", "/app/app.py"]