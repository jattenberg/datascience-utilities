FROM python:3.8

WORKDIR /app

ENV PIPX_HOME=/app

ENV PIPX_BIN_DIR=/app

ENV PATH="/app:$PATH"

RUN pip install pipx

COPY ./ ./

RUN pipx install .

CMD ["normal", "|", "shuffle_lines", "|", "reservoir_sample", "-n", "5"]