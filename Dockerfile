FROM ubuntu:14.04
# RUN apt-get update && apt-get install -y python-pip python-opencv && pip install flask && pip install tornado
RUN pip install -U flask-cors
ADD app.py /
ADD cvfy.py /
ENTRYPOINT python app.py

