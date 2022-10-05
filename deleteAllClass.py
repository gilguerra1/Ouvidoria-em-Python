import mysql.connector


#Classe criada exclusivamente para deletar todas as ocorrências no BD

class DeleteAll:

    def delete_all_occurrences(self):
        connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'guerra91',
            database = 'ouvidoria'
            )
        
        cursor = connection.cursor()

        sql = "DELETE FROM occurrences"
        cursor.execute(sql)
        connection.commit()

        cursor.close()
        connection.close()

        print('Todas as ocorrências foram excluídas!')