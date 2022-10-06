import claimClass
import sugestionClass
import complimentClass
import deleteAllClass


claims = claimClass.Claim()
sugestion = sugestionClass.Sugestion()
compliment = complimentClass.Compliment()
deleteAll = deleteAllClass.DeleteAll()

print('-='*30)
print('             Bem-vindo a ouvidoria! ')
print('-='*30)

user = input('Digite o seu usuário: ')

while True:
    print('''
                                MENU

                        [1] Registrar Ocorrência
                        [2] Listar Ocorrências 
                        [3] Apagar Ocorrências 
                        [4] Alterar Reclamação
                        [5] Sair  
            ''')
    menu = int(input('Selecione uma opção: '))

    if menu == 1:
        print('''
                TIPOS DE OCORRÊNCIAS
                
                [1] Reclamações 
                [2] Elogios
                [3] Sugestões
         ''')
        option = int(input('Digite o número do tipo ocorrência deseja resgitrar? '))

        if option == 1:
            register = input('Digite a sua reclamação: ')
            claims.add_new_register(user, register)

        elif option == 2:
            register = input('Digite o seu elogio: ')
            compliment.add_new_compliment(user, register)

        elif option == 3:
            register = input('Digite sua sugestão: ')
            sugestion.add_new_sugestion(user, register)
    
    elif menu == 2:
        print('''       LISTAR
                
                [1] Todas as ocorrências
                [2] Tipo de ocorrência        
        ''')
        option = int(input('Digite o número da opção que deseja realizar: '))
        
        if option == 1:
            claims.list_all_claims()
            compliment.list_all_compliments()
            sugestion.list_all_sugestions()

        elif option == 2:
            print('''
                    TIPOS DE OCORRÊNCIAS
                    
                    [1] Reclamações 
                    [2] Elogios
                    [3] Sugestões
            ''')
            listOccurrences = int(input('Qual opção deseja listar: '))

            if listOccurrences == 1:
                claims.list_all_claims()
            
            elif listOccurrences == 2:
                compliment.list_all_compliments()

            elif listOccurrences == 3:
                sugestion.list_all_sugestions()
    
    elif menu == 3:
        print(''' 
                APAGAR:
        
        [1] Apagar uma ocorrência 
        [2] Apagar um tipo de ocorrência específico
        [3] Apagar todas as ocorrências
        ''')
        delete = int(input('Digite o número da opção que deseja executar: '))

        if delete == 1:
            print('''
                TIPOS DE OCORRÊNCIAS

        [1] Reclamações 
        [2] Elogios
        [3] Sugestões    
        ''')
            option = int(input('Que tipo de ocorrência deseja excluir: '))
            
            if option == 1:
                claims.list_all_claims()
                deleteOption = int(input('Digite o número da reclamação que deseja excluir: '))
                claims.delete_especifc_claim(deleteOption)

            elif option == 2:
                compliment.list_all_compliments()
                deleteOption = int(input('Digite o número do elogio que deseja excluir: '))
                compliment.delete_especifc_compliment(deleteOption)

            elif option == 3:
                sugestion.list_all_sugestions()
                deleteOption = int(input('Digite o número da sugestão que deseja  '))
                sugestion.delete_especifc_sugestion(deleteOption)
        
        elif delete == 2:
            print('''
                TIPOS DE OCORRÊNCIAS
                
                [1] Reclamações 
                [2] Elogios
                [3] Sugestões
            ''')
            occorrenceDelete = int(input('Digite o número do tipo de ocorrência que deseja excluir todos os dados: '))
            
            if occorrenceDelete == 1:
                claims.delete_all_claims()

            elif occorrenceDelete == 2:
                compliment.delete_all_compliments()

            elif occorrenceDelete == 3:
                sugestion.delete_all_sugestions()

        elif delete == 3:
            deleteAll.delete_all_occurrences()
    
    elif menu == 4:
        claims.list_all_claims()
        idOption = input('Digite o número ID da reclamação que deseja alterar: ')
        register = input('Digite a sua nova reclamação: ')
        claims.uptade_especifc_claim(register, idOption)
    
    elif menu == 5:
        print('Obrigado por usar o programa!')
        break