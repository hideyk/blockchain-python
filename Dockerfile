FROM python:bullseye

RUN apt-get update && apt-get install -y \
    bc

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN chmod -R 775 /usr/src/app/scripts

EXPOSE 5000
CMD [ "python", "-m", "backend.app" ]
