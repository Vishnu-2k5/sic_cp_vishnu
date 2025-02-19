import pymysql
def connect_db():
    try:
        connection=pymysql.Connect(host='localhost',port=3306,user='root',password='root',database='vishnu_db',charset='utf8')
        print('DB Connected')
    except:
        print('DB Connection failed')
    return connection
def disconnect_db(connection):
    try:
        connection.close()
        print('DB Disconnecetd')
    except:
        print("DB Disconnection failed")
connection=connect_db()
if connection:
    disconnect_db(connection)