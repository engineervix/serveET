from pathlib import Path

from util import CONFIG

from . import helper, sql_command

db_file = Path(__file__).parent.parent / f"res/{CONFIG['db_name']}.db"
db_exists = db_file.is_file()


if not db_exists:
    conn = helper.create_connection(db_file)
    helper.init_db(conn)
    conn.close()
