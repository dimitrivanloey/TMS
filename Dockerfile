FROM arm64v8/python:3.8.11-buster

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN rm -rf /var/lib/apt/lists/
RUN apt-get update
RUN apt-get install -y nodejs
RUN curl https://cli-assets.heroku.com/install.sh | sh

# for debugging
CMD [ "tail", "-f", "/dev/null" ]

# for running
# CMD ["/usr/local/bin/heroku", "local"]
