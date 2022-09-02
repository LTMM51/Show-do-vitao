def SomarPontos(login, nova_pontuacao):
    import mysql.connector
    
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "lolper51",
        auth_plugin = "mysql_native_auth")

    cursor = mydb.cursor()
    cursor.execute("USE Login")
    cursor.execute(f"UPDATE Login SET pontos = pontos + {nova_pontuacao} WHERE nome = '{login}'")
    mydb.commit()