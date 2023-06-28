FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1

ARG app=/app
ENV app ${app}

RUN mkdir ${app}
WORKDIR ${app}
ADD ./ ${app}/

RUN pip install -r ${app}/config/requirements.txt
RUN chmod +x ${app}/run.sh
CMD ${app}/run.sh