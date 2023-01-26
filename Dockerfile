
FROM python:3.11

ADD assignment1.py .

RUN pip install pandas

CMD ["python", "./assignment1.py"]