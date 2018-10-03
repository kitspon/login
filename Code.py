import sqlite3
def login(username, password):
    conn = sqlite3.connect('id.db')
    c = conn.cursor()
    u = 0
    p = 0
    if type(username) and type(password) == str:
        for row in c.execute("SELECT username FROM id"):
            if row[0] == username:
                u = 1
        for row in c.execute("SELECT password FROM id"):
            if row[0] == password:
                p = 1
        if u == 1:
            if p == 1:
                print('Login sucess')
                return True
        if u == 0 and p == 1:
            print('User does not exits but correct password')
            return False
        if u == 0:
            if p == 0:
                print('User does not exits and wrong password')
                return False
        if u == 1 and p == 0:
            print('correct Username but wrong password')
            return False
        
                
