
import json
from datetime import datetime
import os
import pandas as pd
import serial
from secret import db_user, db_password, db_host, db_port, db_name

# import mysql.connector
import sqlalchemy as sa


OUTFILE = "data.csv"



def main():
    try:
        # COMポート3を115200bpsで開く
        ser = serial.Serial('COM3', 115200, timeout=1)

        engine = sa.create_engine(
            sa.engine.url.URL.create(
                drivername="mysql+pymysql",
                username = db_user,
                password = db_password,
                host     = db_host,
                port     = db_port,
                database = db_name,
            )
        )
        table_name="sensor_output"

        while True:
                # シリアルポートからデータを読み取る
                line = ser.readline().decode('utf-8').strip()
                if not line: continue

                try:
                    data = json.loads(line)
                    data["time"] = datetime.today()
                    df = pd.DataFrame([data])
                    df = df[["time", "temperature", "humidity", "pressure"]]
                    print(df)
                    if not os.path.exists(OUTFILE):
                        df.to_csv(OUTFILE, index=False)
                    else:
                        df.to_csv(OUTFILE, mode="a", header=False, index=False)
                    
                    
                    df.to_sql(table_name, con=engine, if_exists='append', index=False)

                except json.JSONDecodeError:
                    print(f"JSONデコードエラー: {line}")

    except serial.SerialException as e:
        print(f"シリアルポートエラー: {e}")

if __name__ == "__main__":
    main()
