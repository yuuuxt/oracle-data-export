from pathlib import Path

from oracle_data_export.env import (
    get_sample_conn_args,
    get_sample_data_path,
    get_sample_query,
)
from oracle_data_export.main import export_to_parquet

sample_query = get_sample_query()
export_file_path = Path(get_sample_data_path(), "test.parquet")
conn_args = get_sample_conn_args()

export_to_parquet(
    query=sample_query,
    export_path=export_file_path,
    fetch_batch_size=10,
    db_conn_args=conn_args,
)
