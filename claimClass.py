import mysql.connector


#Classe exlcuiva para os métodos de reclamação

class Claim:
    
    #Método para registrar novas reclamações e inseri-las diretamente no BD

    def add_new_register(self, user, register):
        connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'guerra91',
            database = 'ouvidoria'
            )
        
        cursor = connection.cursor()

        sql = "INSERT INTO occurrences (user, type, register) VALUES(%s, %s, %s)"
        data = (user, 'Reclamação', register)

        cursor.execute(sql, data)
        connection.commit()

        cursor.close()
        connection.close()

        print(f'Reclamação registrada com sucesso por {user}')

    #Método para listar todas as reclamações registradas no BD

    def list_all_claims(self):
        connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'guerra91',
            database = 'ouvidoria'
            )
        
        cursor = connection.cursor()

        sql = "SELECT * FROM occurrences WHERE type = 'Reclamação' "

        cursor.execute(sql)
        claimList = cursor.fetchall()

        for claims in claimList:
            print(f'{claims[0]} - {claims[1]} - {claims[2]} - {claims[3]}')

    #Método para exlcuir uma reclamação específica escolhida pelo usuário

    def delete_especifc_claim(self, deleteOption):
        connection =  mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'guerra91',
            database = 'ouvidoria'
            )

        cursor = connection.cursor()

        sql = "DELETE FROM occurrences WHERE id = %s AND type = 'Reclamação'"
        data = (deleteOption,)

        cursor.execute(sql, data)
        connection.commit()

        cursor.close()
        connection.close()

        print(f'Reclamação {deleteOption} excluída com sucesso!')

        #Método para excluir todas as reclamações registradas no BD

    def delete_all_claims(self):
        connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'guerra91',
            database = 'ouvidoria'
            )
        
        cursor = connection.cursor()

        sql = "DELETE FROM occurrences WHERE type = 'Reclamação'"
        cursor.execute(sql)
        connection.commit()

        cursor.close()
        connection.close()

        print('Todas as reclamações foram excluídas!')