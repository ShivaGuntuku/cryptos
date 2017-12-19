import psycopg2
conn = psycopg2.connect(database="historical_data_db",
                        user="postgres",
                        password="pass123",
                        host="127.0.0.1",
                        port="5432")
print("successfully connected...")
