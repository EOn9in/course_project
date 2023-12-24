import pymysql

try:
    # Установка соединения с базой данных
    connection = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='root',
        database='agency',
        cursorclass=pymysql.cursors.DictCursor,
        charset='utf8'
    )
    print("successfully connected...")
    print("#" * 20)

except Exception as ex:
    print("Connection refused...")
    print(ex)
