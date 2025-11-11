from pathlib import Path

import oracledb
import pyarrow
import pyarrow.parquet as pq
from dotenv import load_dotenv
from loguru import logger

from oracle_data_export.env import INSTANTCLIENT_PATH

load_dotenv()

# thick mode for oracle < 12.1
oracledb.init_oracle_client(lib_dir=INSTANTCLIENT_PATH)


def export_to_parquet(
    query: str,
    export_path: Path,
    fetch_batch_size: int,
    db_conn_args: dict,
):
    logger.info(f"export started  - {export_path}")
    pq_writer = None
    try:
        export_path.parent.mkdir(parents=True, exist_ok=True)

        with oracledb.connect(**db_conn_args) as conn:
            for odf in conn.fetch_df_batches(query, size=fetch_batch_size):
                pyarrow_table = pyarrow.table(odf)
                if not pq_writer:
                    pq_writer = pq.ParquetWriter(export_path, pyarrow_table.schema)
                pq_writer.write_table(pyarrow_table)

        if pq_writer is not None:
            pq_writer.close()
        metadata = pq.read_metadata(export_path)
        logger.info(f"export finished - ({metadata.num_rows},{metadata.num_columns})")
    except Exception as e:
        logger.error(f"{e}")
        if pq_writer is not None:
            pq_writer.close()
