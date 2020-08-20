FROM duruo850/ubuntu18.04-python3.6

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    curl \
    libturbojpeg
RUN pip3 install flask \
                 requests \
                 flask_cors \
                 numpy \
                 PyTurboJPEG \
                 line_profiler \
                 gunicorn


COPY . .