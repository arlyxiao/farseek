FROM node:latest

COPY sources.list /etc/apt/sources.list

RUN apt-get update \
 && apt-get install -y --allow-unauthenticated --no-install-recommends \
        ca-certificates \
        bzip2 \
        libfontconfig \
        language-pack-zh-hans fonts-wqy-zenhei \
        fonts-thai-tlwg fontconfig libfontconfig1 libfreetype6 \
        libjpeg-turbo8 libx11-6 libxext6 libxrender1 \
        xfonts-base xfonts-75dpi \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y --allow-unauthenticated chromium-chromedriver

# set working directory
WORKDIR /var/www

# add `/app/node_modules/.bin` to $PATH
ENV PATH /var/www/ng-cms/node_modules/.bin:$PATH

ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD true
ENV CHROMIUM_PATH /usr/bin/chromium-browser

# install and cache app dependencies
# COPY package.json /var/www/ng-cms/package.json
RUN npm install
RUN npm install -g @angular/cli

# add app
# COPY . /app

# start app
# CMD ng serve --host 0.0.0.0 --port 4200
