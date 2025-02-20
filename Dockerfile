ARG PYTHON_VERSION="3.12"

FROM python:${PYTHON_VERSION} AS build-env
WORKDIR /app
COPY requirements.txt data.dvc .git ./
RUN python -m venv .venv
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip install --no-cache-dir -r requirements.txt

FROM python:${PYTHON_VERSION}-slim AS app-image
WORKDIR /app
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
COPY --from=build-env /app/.venv /app/.venv
COPY api ./api
COPY .dvc ./.dvc
COPY mlflow ./mlflow
EXPOSE 8080
CMD ["uvicorn", "api.api:app", "--host", "0.0.0.0", "--port", "8080"]