FROM python:3.9-buster AS pysnake

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    python-pygame

RUN useradd -m -U -s /bin/bash pygame
RUN usermod -a -G audio pygame
USER pygame
WORKDIR /home/pygame
ENV SHELL /bin/bash

COPY requirements/base.txt /usr/local/pip-requirements/
RUN pip3 install \
    --quiet \
    --no-binary :none: \
    -r /usr/local/pip-requirements/base.txt

COPY app /home/pygame/

CMD /bin/bash

FROM pysnake AS pysnake-dev

COPY requirements/dev.txt /usr/local/pip-requirements/

RUN pip3 install \
    --quiet \
    --no-binary :none: \
    -r /usr/local/pip-requirements/dev.txt
