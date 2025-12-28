import json
import time

import mysql.connector

from back.app.core.tool.hash import hash_
from back.app.core.tx.BaseTx import TxType


def connect_DB():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        port=3306,
        password="uiorew12345"
    )
    cursor = conn.cursor()
    return cursor,conn

def connect_UserDB():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="uiorew12345",
        database="UserDB"
    )
    cursor = conn.cursor()
    return cursor,conn

def init_User():

    ##初始化数据库

    cursor,conn = connect_DB()
    cursor.execute("CREATE DATABASE IF NOT EXISTS UserDB")
    cursor.close()
    conn.close()

    ##新建表

    cursor,conn = connect_UserDB()
    cursor = conn.cursor()
    cursor.execute("""
    create table if not exists tx(
        sender VARCHAR(128) NOT NULL,
        tx_type VARCHAR(32) NOT NULL,
        payload json NOT NULL,
        txhash VARCHAR(128) NOT NULL,
        timestamp  BIGINT NOT NULL,
        nonce  BIGINT NOT NULL,
        signature TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        INDEX idx_sender (sender),
        INDEX idx_type_time (tx_type, timestamp)
    );
    """)

def create_attack_tx_to_DB(tx):
    cursor,conn = connect_UserDB()
    sql = """
    insert into tx(
          sender,
          tx_type,
          payload,
          txhash,
          timestamp,
          nonce,
          signature
    )
    values (%s,%s,%s,%s,%s,%s,%s)
    """
    payload_json = json.dumps(tx.payload,ensure_ascii=False)
    cursor.execute(sql,(
        tx.sender,
        TxType.ATTACK,
        payload_json,
        tx.tx_hash,
        tx.timestamp,
        tx.nonce,
        tx.signature
        ))
    conn.commit()
