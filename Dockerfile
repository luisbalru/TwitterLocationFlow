FROM python:3.6

COPY . ./twitterlocationflow

RUN pip install --upgrade pip
RUN cd ./twitterlocationflow && pip3 install -r requirements.txt

ENTRYPOINT cd ./twitterlocationflow && python3 app.py
