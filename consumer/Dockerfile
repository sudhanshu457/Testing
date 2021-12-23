FROM python:2.7-alpine

# Our requirements are minimal, but it's good practice to install them
# first.  Put things that change less often towards the top of the
# Dockerfile.  Then if you need to rebuild the images, Docker will
# start running partway through the Dockerfile and skip over the steps
# where nothing's changed.
RUN pip install pika
RUN pip install --upgrade pip enum34
# Without this setting, Python never prints anything out.
ENV PYTHONUNBUFFERED=1

RUN mkdir /certificate
WORKDIR /certificate
RUN mkdir /consumer
RUN mkdir /CA
WORKDIR /usr/src/app
RUN mkdir /logs
# Actually install the application

# It's only a single file.  It has to be in the same directory as the
# Dockerfile, or a subdirectory, but not a parent or sibling.
COPY . .

# When you just 'docker run publisher' with no command afterwards,
# default to this:
CMD ["python", "/usr/src/app/consumer.py"]
