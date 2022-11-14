from psycopg2 import connect

class Database:
    def __init__(self, host: str, database: str, user: str, password: str, port: int):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

    def connect(self):
        return connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password,
            port=self.port,
        )
    
    def disconnect(self):
        conn = self.connect()
        conn.close()
    
    def get_status(self):
        conn = self.connect()
        if conn:
            return {"db": "connected"}
        else:
            return {"db": "failed"}
    
    def run_query(self, query: str):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    
    def get_user(self):
        query = "SELECT name FROM data Where id=1;"
        name = self.run_query(query)[0][0]
        return {"name": name}
