FROM python:3.10

ENV PYTHON_VERSION=3.10 \
    PYTHONUNBUFFERED=1 \
    WORKDIR=/app/
WORKDIR $WORKDIR

COPY . .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

ENTRYPOINT ["uvicorn", "main:app", "--port", "8080", "--reload", "--log-level", "info", "--host", "0.0.0.0" ]
EXPOSE 8080:8080
