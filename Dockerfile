FROM python:3.9-buster AS pysnake
COPY requirements/base.txt /usr/local/pip-requirements/
RUN pip3 install \
    --quiet \
    --no-binary :none: \
    -r /usr/local/pip-requirements/base.txt

FROM pysnake AS pysnake-dev
COPY requirements/dev.txt /usr/local/pip-requirements/
RUN pip3 install \
    --quiet \
    --no-binary :none: \
    -r /usr/local/pip-requirements/dev.txt
