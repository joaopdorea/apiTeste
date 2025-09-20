import psycopg2 

class PostgreSQLConnection:

    def __init__(self, dbname, user, password, host = 'localhost', port='5432'):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None
        pass

    def connect(self):
        try:
            self.conn = psycopg2.connect(dbname = self.dbname, user = self.user, password = self.password, host = self.host, port = self.port )
            print("Conexão feita com sucesso!")
        except psycopg2.Error as e:
            print("Deu ruim.", e)

    def select_user(self, query):

        if not self.conn:
            print("Você não está conectado.")
            return None
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            return rows
        except psycopg2.Error as e:
            print("Deu ruim no select.", e)
            return None

    def insert_user(self, id, name, area, job_description, role, salary, is_active, last_evaluation):
        if not self.conn:
            print("Você não está conectado.")
            return None
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO users (id, name, area, job_description, role, salary, is_active, last_evaluation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (id, name, area, job_description, role, salary, is_active, last_evaluation))
            self.conn.commit()
            cursor.close()
        except psycopg2.Error as e:
            print("Não foi possível fazer o INSERT", e)
            
        pass

    def delete_user(self, query):
        
        if not self.conn:
            print("Você não está conectado.")
            return None
        try:
                cursor = self.conn.cursor()
                cursor.execute(query)
                self.conn.commit()
                cursor.close()
        except psycopg2.Error as e:
                print("Deu ruim no select.", e)
                return None
        pass

    def update_user(self, name, area, job_description, role, salary, is_active, last_evaluation, user_id):
        if not self.conn:
            print("Você não está conectado.")
            return None
        try:
            cursor = self.conn.cursor()
            cursor.execute("UPDATE users SET name = %s, area = %s, job_description = %s, role = %s, salary = %s, is_active = %s, last_evaluation = %s WHERE id = %s", (name, area, job_description, role, salary, is_active, last_evaluation, user_id))
            self.conn.commit()
            cursor.close()
        except psycopg2.Error as e:
            print("Não foi possível fazer o INSERT", e)
        pass

    def close(self):
        self.conn.close()
        pass
