import csv
import os

class ReservatorioPetroleo:
    def __init__(self, nome, capacidade, pressao, localizacao):
        self._nome = nome
        self._capacidade = capacidade
        self._pressao = pressao
        self._localizacao = localizacao
        if len(self._valida()) > 0:
            raise ValueError(f"Valores inválidos: {self._valida()}")

    def _valida(self):
        parametros_invalidos = []
        if not (isinstance(self.nome, str) and self.nome):
            parametros_invalidos.append("O nome deve ser uma string válida.")
        if not (isinstance(self.capacidade, (int, float)) and self.capacidade > 0):
            parametros_invalidos.append("A capacidade deve ser um número positivo.")
        if not (isinstance(self.pressao, (int, float)) and self.pressao > 0):
            parametros_invalidos.append("A pressão deve ser um número positivo.")
        if not (isinstance(self.localizacao, str) and self.localizacao):
            parametros_invalidos.append("A localização deve ser uma string válida.")
        return parametros_invalidos
    
    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if isinstance(valor, str) and valor:
            self._nome = valor
        else:
            raise ValueError("O nome deve ser uma string válida.")

    @property
    def capacidade(self):
        return self._capacidade

    @capacidade.setter
    def capacidade(self, valor):
        if isinstance(valor, (int, float)) and valor > 0:
            self._capacidade = valor
        else:
            raise ValueError("A capacidade deve ser um número positivo.")

    @property
    def pressao(self):
        return self._pressao

    @pressao.setter
    def pressao(self, valor):
        if isinstance(valor, (int, float)) and valor > 0:
            self._pressao = valor
        else:
            raise ValueError("A pressão deve ser um número positivo.")

    @property
    def localizacao(self):
        return self._localizacao

    @localizacao.setter
    def localizacao(self, valor):
        if isinstance(valor, str) and valor:
            self._localizacao = valor
        else:
            raise ValueError("A localização deve ser uma string válida.")

    def __str__(self):
        return (f"Reservatório {self.nome}, Capacidade: {self.capacidade} barris, "
                f"Pressão: {self.pressao} PSI, Localização: {self.localizacao}")


def desenhar_plataforma(func):
    def wrapper(*args, **kwargs):
        print(r"""
                                                                                                       
                                                                                                                                                                                                 
                                                                 .                                     
                                                                %%%                                    
                                                                %%%                                    
                                                                %%%                                    
                                                           %%%%%%%%%%%%%                               
                                                          %%%%%%%%%%%%%%%                              
                                                          %%    %%%    %%                              
                           %%%%%%%%%%%%%%*                %%    %%%    %%%                             
                           %%%%%%%%%%%%%%*               #%%    %%%     %%                             
                            %%=:::::::+%%                %%     %%%     %%                             
                            %%=:::::::+%%                %%%%%%%%%%%%%%%%%                             
                            %%=:::::::+%%                %%%%%%%%%%%%%%%%%                             
                            %%%%%%%%%%%%%%%%%%%%%%%      %%     %%%     %%-                            
                     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    :%%     %%%     #%%                            
                     %%%%%%%%%=::::::::::::::::::=%%    %%-     %%%      %%                            
                       %%   %%=: =%%%%%%%%%%%%= :=%%    %%      %%%      %%                            
                        -%%-%%=: =%%%%%%%%%%%%= :=%%    %%%%%%%%%%%%%%%%%%%                            
                          %%%%=::::::::::::::::::=%%    %%%%%%%%%%%%%%%%%%%                            
                           %%%=::::::::::::::::::=%%    %%      %%%      %%%                           
                            %%=::::::::::::::::::=%%   %%%      %%%       %%                           
                            %%=::::::::::::::::::=%%   %%       %%%       %%                           
                        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%:                        
                       %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                       
                       %%#==================================================+%%%                       
                     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*                     
                     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*                     
                       %%#==================================================+%%%                       
                       %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                       
                        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%:                        
                            %%#**#%%     %%*               %%     %%%***%%%                            
                            %%#**#%%    %%                  *%%   %%%***%%%                            
                            %%#**#%%  %%                      %%  %%%***%%%                            
                            %%#**#%%%%%                         %%%%%***%%%                            
                            %%#**#%%%                            %%%%***%%%                            
             -              %%#*-:%%%=*                        +-%%%* **%%%              +             
             %%%%%          %%: -%%%%%%%%%%%              *%%%%%%%%%%*  %%%         %%%%%*             
                  %%-       %%%%%          -%%          %%%          %%%%%%       %%-                  
                    %%%%%%%%%%%               %%%%%%%%%%%              %%%%%%%%%%%                     
                         *                        .+                        +.                         
             -                        *                        ==                        +             
             %%%%%               %%%%%%%%%%%              +%%%%%%%%%%+              %%%%%*             
                  %%-          %%          -%%          %%%          %%%          %%-                  
                    %%%%%%%%%%%               %%%%%%%%%%%              %%%%%%%%%%%                     
                         *                        .+                        +.                         
             -                        *                        ==                        +             
             %%%%%               %%%%%%%%%%%              +%%%%%%%%%%+              %%%%%*             
                  %%-          %%          -%%          %%%          %%%          %%-                  
                    %%%%%%%%%%%               %%%%%%%%%%%              %%%%%%%%%%%                     
                         *                        .+                        +.                         
                                                                                                       
                                                                                                       
                                                                                              
        """)
        print("Operação em andamento...\n")
        
        resultado = func(*args, **kwargs)
        
        print("\nOperação concluída.")
        print(r"""                                                       
                                                                                                       
                                                                 .                                     
                                                                %%%                                    
                                                                %%%                                    
                                                                %%%                                    
                                                           %%%%%%%%%%%%%                               
                                                          %%%%%%%%%%%%%%%                              
                                                          %%    %%%    %%                              
                           %%%%%%%%%%%%%%*                %%    %%%    %%%                             
                           %%%%%%%%%%%%%%*               #%%    %%%     %%                             
                            %%=:::::::+%%                %%     %%%     %%                             
                            %%=:::::::+%%                %%%%%%%%%%%%%%%%%                             
                            %%=:::::::+%%                %%%%%%%%%%%%%%%%%                             
                            %%%%%%%%%%%%%%%%%%%%%%%      %%     %%%     %%-                            
                     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    :%%     %%%     #%%                            
                     %%%%%%%%%=::::::::::::::::::=%%    %%-     %%%      %%                            
                       %%   %%=: =%%%%%%%%%%%%= :=%%    %%      %%%      %%                            
                        -%%-%%=: =%%%%%%%%%%%%= :=%%    %%%%%%%%%%%%%%%%%%%                            
                          %%%%=::::::::::::::::::=%%    %%%%%%%%%%%%%%%%%%%                            
                           %%%=::::::::::::::::::=%%    %%      %%%      %%%                           
                            %%=::::::::::::::::::=%%   %%%      %%%       %%                           
                            %%=::::::::::::::::::=%%   %%       %%%       %%                           
                        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%:                        
                       %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                       
                       %%#==================================================+%%%                       
                     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*                     
                     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*                     
                       %%#==================================================+%%%                       
                       %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                       
                        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%:                        
                            %%#**#%%     %%*               %%     %%%***%%%                            
                            %%#**#%%    %%                  *%%   %%%***%%%                            
                            %%#**#%%  %%                      %%  %%%***%%%                            
                            %%#**#%%%%%                         %%%%%***%%%                            
                            %%#**#%%%                            %%%%***%%%                            
             -              %%#*-:%%%=*                        +-%%%* **%%%              +             
             %%%%%          %%: -%%%%%%%%%%%              *%%%%%%%%%%*  %%%         %%%%%*             
                  %%-       %%%%%          -%%          %%%          %%%%%%       %%-                  
                    %%%%%%%%%%%               %%%%%%%%%%%              %%%%%%%%%%%                     
                         *                        .+                        +.                         
             -                        *                        ==                        +             
             %%%%%               %%%%%%%%%%%              +%%%%%%%%%%+              %%%%%*             
                  %%-          %%          -%%          %%%          %%%          %%-                  
                    %%%%%%%%%%%               %%%%%%%%%%%              %%%%%%%%%%%                     
                         *                        .+                        +.                         
             -                        *                        ==                        +             
             %%%%%               %%%%%%%%%%%              +%%%%%%%%%%+              %%%%%*             
                  %%-          %%          -%%          %%%          %%%          %%-                  
                    %%%%%%%%%%%               %%%%%%%%%%%              %%%%%%%%%%%                     
                         *                        .+                        +.                         
                                                                                                       
                                                                                           
                                                                                                       
        """)
        
        return resultado
    return wrapper


class GerenciadorReservatorios:
    def __init__(self):
        diretorio = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')
        self.arquivo_csv = os.path.join(diretorio, 'Reservatorio_Petroleo.csv')

        try:
            with open(self.arquivo_csv, 'x', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Nome", "Capacidade (bbl)", "Pressão (psi)", "Localização"])
        except FileExistsError:
            pass

    def adicionar_reservatorio(self):
        nome = input("Digite o nome do reservatório: ")
        capacidade = float(input("Digite a capacidade do reservatório (bbl): "))
        pressao = float(input("Digite a pressão do reservatório (psi): "))
        localizacao = input("Digite a localização do reservatório (Lat/Long): ")
        reservatorio = ReservatorioPetroleo(nome, capacidade, pressao, localizacao)
        with open(self.arquivo_csv, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([reservatorio.nome, reservatorio.capacidade, reservatorio.pressao, reservatorio.localizacao])
        print(f"Reservatório {reservatorio.nome} adicionado com sucesso!")

    def listar_reservatorios(self):
        try:
            reservatorios = self.leitor()

            if not reservatorios:
                print("Nenhum reservatório cadastrado.")
            else:
                print("Reservatórios cadastrados:")
                for idx, reservatorio in enumerate(reservatorios, 1):
                    print(f"{idx} - Nome: {reservatorio.nome}, Capacidade: {reservatorio.capacidade} bbl, Pressão: {reservatorio.pressao} psi, Localização: {reservatorio.localizacao}")
        except FileNotFoundError:
            print(f"Erro: O arquivo '{self.arquivo_csv}' não foi encontrado.")

    def leitor(self):
        reservatorios = []
        with open(self.arquivo_csv, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            
            for linha in reader:
                nome, capacidade, pressao, localizacao = linha
                reservatorio = ReservatorioPetroleo(
                    nome=nome,
                    capacidade=float(capacidade),
                    pressao=float(pressao),
                    localizacao=localizacao
                )
                reservatorios.append(reservatorio)
        
        return reservatorios

    def atualizar_reservatorio(self, indice):
        reservatorios = self.leitor()
        
        if 0 <= indice < len(reservatorios):
            reservatorio = reservatorios[indice]
            nome_atual = reservatorio.nome
            capacidade_atual = reservatorio.capacidade
            pressao_atual = reservatorio.pressao
            
            nome = input(f"Digite o novo nome do reservatório (atual: {nome_atual}) ou pressione Enter para manter o nome atual: ")
            capacidade = input(f"Digite a nova capacidade do reservatório (bbl) (atual: {capacidade_atual}) ou pressione Enter para manter a capacidade atual: ")
            pressao = input(f"Digite a nova pressão do reservatório (psi) (atual: {pressao_atual}) ou pressione Enter para manter a pressão atual: ")
            if not nome and not capacidade and not pressao:
                print(f"Reservatório {nome_atual} não foi atualizado.")
            else:
                if nome:
                    reservatorio.nome = nome
                if capacidade:
                    reservatorio.capacidade = float(capacidade)
                if pressao:
                    reservatorio.pressao = float(pressao)

                with open(self.arquivo_csv, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Nome", "Capacidade (bbl)", "Pressão (psi)", "Localização"])
                    for r in reservatorios:
                        writer.writerow([r.nome, r.capacidade, r.pressao, r.localizacao])
                
                print(f"Reservatório '{reservatorio.nome}' atualizado com sucesso!")
        else:
            print("Índice inválido.")

    def remover_reservatorio(self, indice):
        reservatorios = self.leitor()
        
        if 0 <= indice < len(reservatorios):
            reservatorio = reservatorios.pop(indice)

            with open(self.arquivo_csv, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Nome", "Capacidade (bbl)", "Pressão (psi)", "Localização"])
                for r in reservatorios:
                    writer.writerow([r.nome, r.capacidade, r.pressao, r.localizacao])
            print(f"Reservatório '{reservatorio.nome}' removido com sucesso!")
        else:
            print("Índice inválido.")

@desenhar_plataforma   
def main():
    gerenciador = GerenciadorReservatorios()
    while True:
        opcao = int(input("\n=== Menu de Gerenciamento Reservatório de Petróleo Offshore ==="
        "\n1 - Cadastrar reservatório"
        "\n2 - Visualizar reservatórios cadastrados"
        "\n3 - Atualizar dados já cadastrados"
        "\n4 - Excluir reservatório"
        "\n5 - Sair do sistema"
        "\nEscolha uma opção: "))
        
        match opcao:
            case 1:
                gerenciador.adicionar_reservatorio()
            case 2:
                gerenciador.listar_reservatorios()
            case 3:
                gerenciador.atualizar_reservatorio(int(input("Digite o índice do reservatório que deseja atualizar:"))-1)
            case 4:
                gerenciador.remover_reservatorio(int(input("Digite o índice do reservatório que deseja excluir:"))-1)
            case 5:
                print("\nSaindo do sistema...")
                break
            case _:
                print("Opção inválida. Escolha outra opção.")     
        
main()

