FROM python:3.9

ENV APP_HOME /app
WORKDIR $APP_HOME

ENV GOOGLE_APPLICATION_CREDENTIALS=eplanner-event-mircro-3a80a2ab0ddb.json
ENV INSTANCE_CONNECTION_NAME=eplanner-event-mircro:us-central1:eventdb
ENV DB_PORT=3306
ENV DB_NAME=event_info
ENV DB_USER=root
ENV DB_PASS=db12345
ENV DATABASE_URL=mysql://root:db12345@//cloudsql/eplanner-event-mircro:us-central1:eventdb/event_info
ENV SECRET_KEY=BGjZehTWFqogqfJfXVDhXpsGleVDjmQXhrfmcBLILXrFFFNhvn


# Removes output stream buffering, allowing for more efficient logging
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt 

# Copy local code to the container image.
COPY . .

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 Eventplanning.wsgi:application