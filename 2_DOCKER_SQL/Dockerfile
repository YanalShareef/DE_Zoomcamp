From python:3.9.1

RUN apt-get install wget
Run pip install pandas sqlalchemy psycopg2 pyarrow

WORKDIR /app

COPY ingest_data.py ingest_data.py

# ENTRYPOINT ["bash"]

ENTRYPOINT ["python","ingest_data.py"]
