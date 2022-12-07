# Import the necessary libraries
from psycopg2 import connect

# Create a class to handle the database connection
class Database:
    # Initialize the class
    def __init__(self, host: str, database: str, user: str, password: str, port: int):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

    # Create a function to connect to the database
    def connect(self):
        return connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password,
            port=self.port,
        )
    
    # Create a function to disconnect from the database
    def disconnect(self):
        conn = self.connect()
        conn.close()
    
    # Create a function to get the status the connection to the database
    def get_status(self):
        conn = self.connect()
        if conn:
            return {"db": "connected"}
        else:
            return {"db": "failed"}
    
    # Create a function to run a query
    def run_query(self, query: str):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    # Create a function to get the user
    def get_user(self):
        query = "SELECT name FROM data Where id=1;"
        name = self.run_query(query)[0][0]
        return {"name": name}
