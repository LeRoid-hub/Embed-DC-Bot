# set base image (host OS)
FROM python:3.11

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

#install Chrome
RUN apt-get install -y wget
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -y ./google-chrome-stable_current_amd64.deb

# copy the content of the local src directory to the working directory
COPY . .

# command to run on container start
CMD [ "python", "./bot.py" ]
