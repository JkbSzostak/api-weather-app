FROM python:3.12

WORKDIR /Test

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "Test.py"]