import mysql.connector


#Classe exclusiva para os métodos de sugestões

class Sugestion:

    #Método para registra novas sugestões e inseri-los ao banco de dados

    def add_new_sugestion(self, user, register):
        connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'guerra91',
            database = 'ouvidoria'
            )

        cursor = connection.cursor()

        sql = "INSERT INTO occurrences (user, type, register) VALUES (%s, %s, %s)"
        data = (user, 'Sugestão', register)

        cursor.execute(sql, data)
        connection.commit()

        cursor.close()
        connection.close()

        print(f'Sugestão registrado com sucessor por {user}')

    #Método para listar todas as sugestões registrados no BD

    def list_all_sugestions(self):
        connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'guerra91',
            database = 'ouvidoria'
            )
        
        cursor = connection.cursor()

        sql = "SELECT * FROM occurrences WHERE type = 'Sugestão' "

        cursor.execute(sql)
        sugestionList = cursor.fetchall()

        for sugestions in sugestionList:
            print(f'{sugestions[0]} - {sugestions[1]} - {sugestions[2]} - {sugestions[3]}')

    #Método para exlcuir uma sugestão específica escolhida pelo usuário

    def delete_especifc_sugestion(self, deleteOption):
        connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'guerra91',
            database = 'ouvidoria'
            )

        cursor = connection.cursor()

        sql = "DELETE FROM occurrences WHERE id = %s AND type = 'Sugestão' "
        data = (deleteOption,)

        cursor.execute(sql, data)
        connection.commit()

        cursor.close()
        connection.close()

        print(f'Sugestão {deleteOption} excluída com sucesso!')

    #Método para excluir todas as sugestões registradas no BD

    def delete_all_sugestions(self):
        connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password  = 'guerra91',
            database = 'ouvidoria'
            )

        cursor = connection.cursor()

        sql = "DELETE FROM occurrences WHERE type = 'Sugestão' "
        cursor.execute(sql)
        connection.commit()

        cursor.close()
        connection.close()

        print('Todas as sugestões foram excluídas')