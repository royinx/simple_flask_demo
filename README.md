# Simple Flask Template


## Build
```
docker build -t simple_flask .

# For cpu container
docker run --name=api \
           --rm \
           -dit \
           -v /tmp/.X11-unix:/tmp/.X11-unix \
           -e DISPLAY=unix$DISPLAY \
           -p 2800-2810:2800-2810 \
           -v ${PWD}:/py \
           -w /py \
           simple_flask bash
```
Or 
```
# For nvidia container , needa change base image in Dockerfile 

docker run --runtime=nvidia \
           --name=gpu_api \
           --shm-size 11G \
           --privileged \
           -dit \
           -v ~/Documents:/py/ \
           -v /media/datasets/share_test:/py \
           -v /tmp/.X11-unix:/tmp/.X11-unix \
           -e DISPLAY=unix$DISPLAY \
           -p 2800-2810:2800-2810 \
           -w /py \
           gpu_api bash
```


---

## Run
```
docker run --name=api \
           --rm \
           -it \
           -p 2809:2809 \
           -v ${PWD}:/py \
           -w /py \
           simple_flask python3 server.py 2809

python3 api_test.py
```


---
`TurboJPEG` is a fast library for imencode and decode while i wanna put benchmarking there instead of open a new repo.<br/>
check out `jpg.py`