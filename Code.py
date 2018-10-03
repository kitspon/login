import sqlite3
def login(username, password):
    conn = sqlite3.connect('id.db')
    c = conn.cursor()
    if type(username) and type(password) == str:
        for row in c.execute("SELECT username FROM id"):
            if row[0] == username:
                for row in c.execute("SELECT password FROM id"):
                    if row[0] == password:
                        return True
                return False
        return False

        
                
