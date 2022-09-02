def PontosSQL(login, senha):
    from unittest import skip
    import mysql.connector
    
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "lolper51",
        auth_plugin = "mysql_native_auth")

    cursor = mydb.cursor()
    cursor.execute(f"SELECT pontos FROM login WHERE nome = '{login}' AND senha = '{senha}'")
    for x in cursor:
        pontos = x
    return pontos
