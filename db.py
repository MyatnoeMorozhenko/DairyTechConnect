"""import psycopg2
import PGDATABASE, PGHOST, PGPASSWORD,PGPORT, PGUSER

db = psycopg2.connect(host = PGHOST, port = PGPORT, user = PGUSER, password = PGPASSWORD, database = PGDATABASE)
cur = db.cursor()

async def db_start():
    cur.execute("CREATE TABLE IF NOT EXISTS users("
    "id INTEGER PRIMARY KEY, "
    "username TEXT, "
    "tg_id INTEGER )")
    db.commit()

#Собираю id юзеров
async def cmd_start_db(user_id):
    user = cur.execute("SELECT * FROM users WHERE tg_id == {key}".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO users (tg_id) VALUES ({key})".format(key=user_id))
    db.commit()
    cur.close()
    db.close()
"""
