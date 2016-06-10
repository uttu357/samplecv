FROM ubuntu:14.04
#RUN apt-get update && apt-get install -y python-pip python-opencv && pip install flask
#RUN pip install -U flask-cors
ADD app.py /
ENV FLASK_APP app.py
EXPOSE 5000
ENTRYPOINT ln -s /dev/null /dev/raw1394;flask run --host=0.0.0.0 --port=5000

