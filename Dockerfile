FROM python:3
COPY . .
RUN pip install flask --no-cache-dir
CMD [ "python", "./crash_me.py" ]
