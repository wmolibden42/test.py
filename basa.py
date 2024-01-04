import sqlite3 as sq

async def db_start():
    global db, cur

    db = sq.connect('tableone.db')
    cur = db.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS profile(user_id TEXT PRIMARY KEY, 
    date_day INTEGER, 
    up_time INTEGER, 
    down_time INTEGER, 
    happy_stat TEXT  
                """)
    db.commit()

async def create_profile():
    user = cur.execute("SELECT 1 FROM profile WHERE user_id == '{key}".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO profile VALUES(?, ?, ?, ?, ?)", (user_id, '', '', '', '', ''))
        cur.commit()

async def edit_profile(state, user_id):
    async with state.proxy () as data:
        cur.execute("UPDATE profile WHERE user_id == '{}' SET  date_day = '{}', up_time = '{}', down_time = '{}', happy_stat = '{}'".format(
            user_id, data['data_day'], data['up_time'], data['down_time'], data['happy_stat']))
        db.commit()
