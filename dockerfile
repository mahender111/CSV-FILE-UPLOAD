FROM python:3.11 

ENV PYTHONUNBUFFERED=1

WORKDIR /csv_upload

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /csv_upload

EXPOSE 8000

CMD ["python","manage.py", "runserver", "0.0.0.0:8000"]

