import mysql.connector

#Classe exlcuiva para os métodos de elogios

class Compliment:

    #Método para registrar novos elogios e inseri-las diretamente no BD

    def add_new_compliment(self, user, register):
        connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'guerra91',
            database = 'ouvidoria'
            )
        
        cursor = connection.cursor()

        sql = "INSERT INTO occurrences (user, type, register) VALUES(%s, %s, %s)"
        data = (user, 'Elogio', register)

        cursor.execute(sql, data)
        connection.commit()

        cursor.close()
        connection.close()

        print(f'Elogio registrado com sucesso por {user}')

    #Método para listar todos os elogios registrados no BD

    def list_all_compliments(self):
        connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'guerra91',
            database = 'ouvidoria'
            )
        
        cursor = connection.cursor()

        sql = "SELECT * FROM occurrences WHERE type = 'Elogio' "

        cursor.execute(sql)
        complimentList = cursor.fetchall()

        for compliment in complimentList:
            print(f'{compliment[0]} - {compliment[1]} - {compliment[2]} - {compliment[3]}')

    #Método para exlcuir um elogio específico escolhido pelo usuário

    def delete_especifc_compliment(self, deleteOption):
        connection =  mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'guerra91',
            database = 'ouvidoria'
            )

        cursor = connection.cursor()

        sql = "DELETE FROM occurrences WHERE id = %s AND type = 'Elogio'"
        data = (deleteOption,)

        cursor.execute(sql, data)
        connection.commit()

        cursor.close()
        connection.close()

        print(f'Elogio {deleteOption} excluído com sucesso!')

        #Método para excluir todas os elogios registrados no BD

    def delete_all_compliments(self):
        connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'guerra91',
            database = 'ouvidoria'
            )
        
        cursor = connection.cursor()

        sql = "DELETE FROM occurrences WHERE type = 'Elogio'"
        cursor.execute(sql)
        connection.commit()

        cursor.close()
        connection.close()

        print('Todas os elogios foram excluídos!')
