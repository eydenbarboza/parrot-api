FROM python:3.6
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
RUN chmod +x /code/run.py
CMD python3 run.py
