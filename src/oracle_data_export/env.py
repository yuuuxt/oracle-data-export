import os

from dotenv import load_dotenv

load_dotenv()

INSTANTCLIENT_PATH = os.environ["INSTANTCLIENT_PATH"]


def get_sample_conn_args():
    SAMPLE_CONN_USER = os.environ["SAMPLE_CONN_USER"]
    SAMPLE_CONN_PASSWORD = os.environ["SAMPLE_CONN_PASSWORD"]
    SAMPLE_CONN_DSN = os.environ["SAMPLE_CONN_DSN"]

    return {
        "user": SAMPLE_CONN_USER,
        "password": SAMPLE_CONN_PASSWORD,
        "dsn": SAMPLE_CONN_DSN,
    }


def get_sample_query():
    return os.environ["SAMPLE_QUERY"]


def get_sample_data_path():
    return os.environ["SAMPLE_DATA_PATH"]
