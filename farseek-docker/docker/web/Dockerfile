FROM python:3.8.5


RUN mkdir -p /var/www
WORKDIR /var/www
ADD requirements.txt /var/www/

RUN python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ -r requirements.txt


CMD [ "bash" ]
