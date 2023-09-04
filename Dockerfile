LABEL org.opencontainers.image.source=https://github.com/Giratina-net/R-Markov-Twitter
FROM debian:bullseye-slim
RUN apt update -y && apt install -y python3 python3-pip
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
CMD ["python3","run.py"]
