from service.services import Services

class UI:

    def __init__(self, services):
        self.services = services

    def show_principal_menu(self):
       while True:

           print("=====MENU======")
           print("CADASTRAR -> 1")
           print("LISTAR -> 2")
           print("BUSCARPORID -> 3")
           print("ATUALIZAR -> 4")
           print("DELETAR -> 5")
           print("SAIR -> 6")

           escolha = input(" O que deseja fazer? ")

           if escolha == "1":
               nome = input("Nome do Bolo: ")
               sabor = input("Sabor do Bolo:")

               try:
                   bolo = self.services.create(nome, sabor)
                   print(f"Bolo cadastrado com sucesso! ID: {bolo.id}")
               except ValueError as error:
                   print(f"Erro: {erro}")
           
           elif escolha == "2":
               try:
                   lista = self.services.find_all()
                   if not lista:
                       print("Sem registro")
                   print("lista de registros:")
                   for i in lista:
                       if i.closed:
                           feito = "Produzido"
                       else:
                           feito = "Não Produzido"
                       print(f"nome : {bolo.nome}// sabor: {bolo.sabor}// feito: {bolo.feito}")
               except ValueError as error:
                   print(f"Erro: {error}")       
           
           elif escolha == "3":
               resposta = int(input("Digite o ID:"))
               try:
                   resultado = self.services.get(resposta)
                   if not resultado:
                       print("Não encontrado")
                   print(f"id: {resultado.id}// nome: {resultado.nome}// sabor: {resultado.sabor} // feito: {resultado.feito}")
               except ValueError as erro:
                   print(f"Erro: {erro}")
           
           elif escolha == "4":
               nome_novo = input("Digite o novo nome: ")    
               sabor_novo = input("Digite o novo sabor: ") 
               try:
                   self.services.update(bolo_id, nome_novo, sabor_novo)
                   print("Atualizado com sucesso")
               except ValueError as erro:
                   print(f"Erro: {erro}")
          
           elif escolha == "5" :
               resposta = int(input("Digite o Id:"))
               try:
                   resultado = self.services.get(resposta)
                   if not resultado:
                       print("Não encontrado")
                   self.services.delete(resposta)
                   print(f"Deletado, id = {resultado}")
               except ValueError as error:
                   print(f"Erro: {erro}")
           elif escolha == "6":
               print("encerrando programa....")
                   
                    
                      
                   
                     
        
        
