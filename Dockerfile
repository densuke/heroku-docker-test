FROM python:3
COPY hello.py requirements.txt /
RUN pip install -r /requirements.txt
ENTRYPOINT ["python", "/hello.py"]
