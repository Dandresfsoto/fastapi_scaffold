FROM python:3.11.2 as build

WORKDIR /app
COPY . /app

RUN apt update && apt install -y --no-install-recommends && pip install --upgrade pip
RUN make deps-dev
RUN make lint
RUN make cover

FROM python:3.11.2 as release
WORKDIR /app
COPY --from=build /app /app
RUN make deps

HEALTHCHECK --interval=30s --timeout=10s \
  CMD curl -f http://localhost:$APP_PORT/health || exit 1

EXPOSE $APP_PORT
CMD ["make", "start"]