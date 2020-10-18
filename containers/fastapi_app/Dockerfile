FROM python:3.7-stretch

COPY containers/fastapi_app/requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

RUN mkdir -p /main
COPY ./fastapi_app /main

COPY containers/fastapi_app/run.sh /run.sh
RUN chmod a+rwx /run.sh
RUN chmod -R a+rwx /main

ENV PORT=8000
EXPOSE $PORT
WORKDIR /main
ENTRYPOINT ["/run.sh"]