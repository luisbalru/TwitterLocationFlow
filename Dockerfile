FROM python:3.6

WORKDIR /twitterlocationflow

COPY . /twitterlocationflow

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 314159265

CMD ["python3", "app.py"]
