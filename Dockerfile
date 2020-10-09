# first stage
FROM python:3.8 AS builder
WORKDIR /tmp/project-wrapper/
RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc

COPY requirements.txt ./requirements.txt
RUN pip install --user -r requirements.txt

# second unnamed stage
FROM python:3.8-slim-buster
WORKDIR /tmp/

# copy only the dependencies installation from the 1st stage image
COPY --from=builder /root/.local /root/.local
# update PATH environment variable
ENV PATH=/root/.local:/root/.local/bin:$PATH
