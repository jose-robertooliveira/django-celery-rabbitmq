FROM python:3.11.3-alpine3.18

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY djsource /djsource
COPY scripts /scripts
# COPY ./djsource /djsource
# COPY ./scripts /scripts

WORKDIR /djsource

EXPOSE 8000

RUN python -m venv /venv && \
  /venv/bin/pip install --upgrade pip && \
  /venv/bin/pip install -r /djsource/requirements.txt && \
  adduser --disabled-password --no-create-home user && \
  mkdir -p /data/web/static && \
  mkdir -p /data/web/media && \
  chown -R user:user /venv && \
  chown -R user:user /data/web/static && \
  chown -R user:user /data/web/media && \
  chmod -R 755 /data/web/static && \
  chmod -R 755 /data/web/media && \
  chmod -R +x /scripts


ENV PATH="/scripts:/venv/bin:$PATH"

# Muda o usuário para user
USER user

CMD ["entrypoint.sh"]

