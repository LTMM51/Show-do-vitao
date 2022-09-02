def SQL(login, senha,novo):
    from unittest import skip
    import mysql.connector
    
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "lolper51",
        auth_plugin = "mysql_native_auth")

        

    cursor = mydb.cursor()

    try:
        cursor.execute("CREATE DATABASE Login")
    except:
        skip

    cursor.execute("USE Login")

    try:
        cursor.execute("CREATE TABLE login (nome varchar(20) primary key, senha varchar(30), pontos integer)")
    except:
        skip
    
    if novo:
        try:
            novo_login = login
            nova_senha = senha
            cursor.execute(f"INSERT INTO login (nome, senha) VALUES ('{novo_login}','{nova_senha}');")
            verificador = True
            return verificador 
        except:
            verificador = False
    else:
        try:
            cursor.execute(f"SELECT nome, senha FROM login WHERE nome = '{login}' AND senha = '{senha}'")
            for x in cursor:
                loginSQL = x[0]
                senhaSQL = x[1]
            if login == loginSQL and senha == senhaSQL:
                verificador = True
            else:
                verificador = False
        except:
            skip

    return verificador