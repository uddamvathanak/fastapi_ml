FROM python:3.11.9

WORKDIR /app

RUN apt-get -y update  && apt-get install -y \
  python3-dev \
  apt-utils \
  build-essential \
&& rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade setuptools
RUN python -m pip install \
    cython==0.29.35 \
    numpy==1.24.1 \
    pandas==2.0.1 \
    pystan

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

COPY . .

CMD gunicorn -w 3 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:$PORT