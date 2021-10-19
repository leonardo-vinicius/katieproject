class bancoDeDados(): #aqui há uma classe principal banco de dados que serve como uma especie de classe controle e vai armazenando os produtos numa lista
      def __init__(self):
            self.listaDeProdutos = [] #nessa lista os elementos são objetos produtosnovos if produto.nome == alvo -> listadeprodutos.remove(alvo)

class main():
      def __init__(self, bdd):
            while True:     #loop infinito para adicionar, alterar ou remover um produto.               

                  print('\nHá produtos das categorias: limpeza, bebidas e massas')
                  print('\nDigite um número:')
                  print('\n1 - para adicionar um produto')
                  print('\n2 - para alterar um produto')
                  print('\n3 - para remover um produto\n')
                  numero = input()

                  if(numero == '1'):      #se o numero digitado for 1 chama a funcao adicionar
                        adicionar(bdd)
                  elif(numero == '2'):    #se o numero digitado for 2 chama a funcao buscar2
                        buscar2(bdd)
                  elif(numero == '3'):    #se o numero digitado for 2 chama a funcao buscar2
                        buscar(bdd)
                  else:                   #se o numero digitado for diferente das opções anteriores
                        print('\nnumero inválido.')  

class produto(): #classe produto com os atributos validade e nome
      def __init__(self,data,nome): #construtor com ele mesmo(especie de ponteiro), data e nome
            self.validade = data
            self.nome = nome
#cada produto pertence a uma classe(limpeza, bebidas, massas), que, por herança pertencem a produto(classe pai/mãe)
class limpeza(produto): 
       def __init__(self, data, tipo,nome):
              super().__init__(data,nome)
              self.tipoLimpeza = tipo

class bebidas(produto):
       def __init__(self, data, tipo,nome):
              super().__init__(data,nome)
              self.tipoDaBebida = tipo

class massas(produto):
      def __init__(self, data, tipo,nome):
            super().__init__(data,nome)
            self.tipoDaMassa = tipo

class buscar(bancoDeDados): #aqui há a classe buscar, que é chamada quando o usuario seleciona a opção 3 - remover
      def __init__(self, alvo):
            self.alvo = input("digite o produto a ser removido\n")
            self.retorne = remover(bdd, self.alvo) #aqui é chamada a função remover com o alvo que é a string do objeto a ser removido

def remover(bdd, produtoaremover):
      for elemento in bdd.listaDeProdutos: #aqui há um loop que procura o objeto a ser removido
             if elemento.nome == produtoaremover: #condicional que encontra o objeto 
                    bdd.listaDeProdutos.remove(elemento) #aqui é um comando para remover o elemento na lista de produtos 
                    print(f"produto removido {produtoaremover}") #e aqui um print só para conferir e deixar o dono da mercearia vendo o produto que foi removido
                    
                    return elemento #retornar o elemento a função
             else:
                     return None    #se não achar retorne nada                           

class buscar2(bancoDeDados): #aqui há outra classe de busca, dessa vez para a alteração de um produto
      def __init__(self, alvo2):
              self.alvo2 = input("digite o produto a ser alterado\n")
              self.retorne3 = alterar(bdd,self.alvo2) #chamando a função de alterar
            
def alterar(bdd, produtoaalterar): 
       for elemento2 in bdd.listaDeProdutos: #a função de alterar também vai procurar o objeto desejado
             if elemento2.nome == produtoaalterar:
                     print("o que vai ser alterado do produto?\n")
                     print("1- para nome\n 2- para data de validade")
                     alterarp = input() #aqui é um comando do usuario para que ele selecione o que deseja remover
                     
                     if alterarp == '1':
                            print("Digite novo nome")
                            elemento2.nome = input() #aqui ele digita um novo nome, alterando assim o anterior.
              
                     elif alterarp == '2':
                            print("Digite nova data de validade")
                            elemento2.data = input() #aqui ele digita uma nova data de validade, alterando assim a anterior.
              
                     else:
                            print("numero invalido") #se o comando digitado for invalido
                     
                     return elemento2 #retorne elemento2
             else:
                     return None #retorne nada

def adicionar(objetoBancoDeDados): #criação de uma nova função
      print("Qual a categoria?\n 1-Limpeza\n 2-Bebidas\n 3-Massas\n")
      resposta = input()
      if resposta == '1': #se a pessoa escolhe limpeza
            print("Qual o nome do produto?")
            name = input()
            print("Qual a validade?")
            val = input()
            print("Qual a marca?")
            tipo = input()
            produtoNovo = limpeza(val,tipo,name) #objeto do classe limpeza
            objetoBancoDeDados.listaDeProdutos.append(produtoNovo)
      elif resposta == '2': #se escolhe bebidas
            print("Qual o nome do produto?")
            name = input()
            print("Qual a validade?")
            val = input()
            print("Qual a marca?")
            tipo = input()
            produtoNovo = bebidas(val,tipo,name) #objeto do classe bebidas
            objetoBancoDeDados.listaDeProdutos.append(produtoNovo)
      elif resposta == '3': #se escolhe massas
            print("Qual o nome do produto?")
            name = input()
            print("Qual a validade?")
            val = input()
            print("Qual a marca?")
            tipo = input()
            produtoNovo = massas(val,tipo,name) #objeto do classe massas
            objetoBancoDeDados.listaDeProdutos.append(produtoNovo)
      else:
            print("Digite 1 2 ou 3")
            adicionar(bdd) #recursao

bdd = bancoDeDados()
main(bdd)            
