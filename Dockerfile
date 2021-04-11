FROM python:3.9-buster AS pysnake

RUN echo 'root:pysnake' | chpasswd

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    python-pygame


COPY requirements/base.txt /usr/local/pip-requirements/
RUN pip3 install \
    --quiet \
    --no-binary :none: \
    -r /usr/local/pip-requirements/base.txt

RUN useradd -m -U -s /bin/bash pygame
RUN usermod -a -G audio pygame
WORKDIR /app
ENV SHELL /bin/bash
USER pygame

COPY app /app/

FROM pysnake AS pysnake-dev

USER root
COPY requirements/dev.txt /usr/local/pip-requirements/
RUN pip3 install \
    --quiet \
    --no-binary :none: \
    -r /usr/local/pip-requirements/dev.txt

USER pygame
