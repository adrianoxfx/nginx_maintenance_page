FROM python:alpine

RUN  apk add curl
COPY ./* /tests/
RUN cd tests && python -m pip install -r requirements.txt


ENTRYPOINT ["python", "-m", "unittest", "/tests/test.py"]
