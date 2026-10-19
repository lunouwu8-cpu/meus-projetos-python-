from abc import ABC, abstractmethod
import random
from rich import print
import time
# Criar classe mãe(personagem) e atribuir elementos básicos deles.
class Personagem(ABC):
    # Documentação
    '''Dentro desta classe temos o funcionamento básico exigido do molde de um personagem básico. 
    Isso foi criado por mim rsrsr, nela acabei utilizando as bibliotecas ABC, RICH, RANDOM e TIME
    (Elas são escritas em minúsculas, mas deixei assim para diferenciarem ela dos outros.)
    ABC => Utilizei para fazer herança.
    RICH => Cores e emotes(Não coloquei emotes kk, perdão.).
    RANDOM => escolha de golpes, ataques e habilidades do jogador e I.A.
    TIME => A leve demora entre as ações para evitar o travamento.
    Isso foi tudo!'''
    def __init__(self, nome='', vida=200):
    # Vida e nome:
        self.nome = nome
        self.vida = vida
    # Golpes e poderes:
        self.golpes = []
        self.poderes = []
    # Estado:
        self.congelado = False
    # Definir estilo do golpe(Cabeçada, perna...):
    def fisico(self, alvo):
        dano = random.randint(10, 30)
        alvo.vida -= dano
        #golpe = ['cabeçada', 'chute', 'soco']
        self.golpes = random.choice(['cabeçada', 'chute', 'soco'])
        return print(f'O [green]{type(self).__name__}[/green] [purple]{self.nome}[/purple] causou [red]{dano}[/red] com um {self.golpes} ao [blue]{alvo.nome}[/blue].')
    # Golpe especial
    def especial(self, alvo):
        # Definir elemento do golpe(Veneno, luz, escuridão etc...) 
        self.poderes = random.choice(['veneno', 'gelo', 'luz'])
        # Veneno:
        if self.poderes == 'veneno':
            # Dano contínuo 
            for c in range(0,4):
                alvo.vida -= 7
                print(f'[purple]-{7}[/purple]', end=" ", flush=True)
            print(f'O {alvo.nome} está sofrendo [magenta]envenenado[/magenta]. 7 dano.')
        # Gelo:
        elif self.poderes == 'gelo':
            alvo.vida -= 12
            alvo.congelado = True
            print(f"O {alvo.nome} foi [cyan]congelado[/cyan]!")
        # Luz:
        elif self.poderes == 'luz':
            if self.vida >= 200:
                print(f"{self.nome} já está com a vida cheia, não pode recuperar mais pontos de vida!")
            else:
                luz = random.randint(10,90)
                vida_passada = self.vida
                self.vida += luz
                if self.vida > 200:
                    self.vida = 200
                    luz = self.vida - vida_passada
                    print(f"{self.nome} recuperou [green]{luz} pontos[/green] de vida!")
                else:
                    print(f"{self.nome} recuperou [green]{luz} pontos[/green] de vida!")

class Héroi(Personagem):
      def __init__(self, nome='', vida=200):
          super().__init__(nome, vida)
class Vilão(Personagem):
    def __init__(self, nome='', vida=200):
        super().__init__(nome, vida)

#Pedir nome do jogador e perguntar se ele é vilão ou héroi.
def escolha():
    while True:
        try:
            lado=int(input("Olá iremos testar isso e queremos saber se você irá ser um [1]vilão ou um [2]héroi. Qual?"))
            if lado in [1,2]:
              break
            else:
              raise ValueError
        except ValueError:
            print('[red]Dígito errado!! escolha entre 1 e 2!![/red]')
    if lado == 1:
        nome = input("Qual será o nome do seu vilão? ").strip()
        jogador = Vilão(nome)
        time.sleep(1)
        print(f"Você escolheu ser um [red]vilão[/red] chamado [purple]{jogador.nome}[/purple].")
        alvo= Héroi(nome = 'Super')

    elif lado == 2:
        nome = input("Qual será o nome do seu héroi? ").strip()
        jogador = Héroi(nome)
        time.sleep(1)
        print(f"Você escolheu ser um [green]héroi[/green] chamado [purple]{jogador.nome}[/purple].")
        alvo= Vilão(nome = 'Super')
    return jogador, alvo

# Criar ás funções:

#Peguei da IA, mas irei refazer por mim mesmo, pois quero entender melhor o que está acontecendo.
# 1. Captura os personagens criados na sua função.
jogador, alvo = escolha()

print("\n[bold yellow]⚔️ A BATALHA COMEÇOU! ⚔️[/bold yellow]\n")

# 2. O jogo roda enquanto os DOIS estiverem vivos
while jogador.vida > 0 and alvo.vida > 0:
    # Mostra o status atual da rodada
    time.sleep(1)
    print(f'[bold green]SUA VIDA: {jogador.vida}[/bold green] | [bold red]VIDA DO INIMIGO:{alvo.vida}[/bold red]')
    if jogador.congelado == True:
        time.sleep(1)
        print(f'O {jogador.nome} está [cyan]congelado[/cyan] e não pode atacar!')
        jogador.congelado = False
    else:
    # --- TURNO DO JOGADOR ---
        print("[bold cyan]Seu Turno![/bold cyan]")
        print("[1] Ataque Físico")
        print("[2] Golpe Especial")
        
        # Escolha da opção do jogador com tratamento de erro
        while True:
            try:
                time.sleep(1)
                opcao = int(input('Qual golpe:'))
                if opcao in [1,2]:
                    break
                else:
                    raise ValueError
            except ValueError:
                time.sleep(1)
                print('[bold red]Escolha um dígito correspondente!![/bold red]')

        # Executa a ação escolhida pelo jogador
        if opcao == 1:
                jogador.fisico(alvo) 
        elif opcao == 2:
                jogador.especial(alvo)   
        # Verifica se o inimigo morreu após o seu ataque
        if alvo.vida <= 0:
            time.sleep(1)
            print(f' O {jogador.nome} [bold red]matou[/bold red] o {alvo.nome}!! [bold yellow]VOCÊ VENCEU!!![/bold yellow]')
            break
        else:
            pass
    time.sleep(1)
    if alvo.congelado == True:
        print(f'O {alvo.nome} está [cyan]congelado[/cyan] e não pode atacar!')
        alvo.congelado = False
    else:
    # --- TURNO DO INIMIGO (I.A. Simples) ---
        print("O inimigo está escolhendo seu golpe...")
    
        # O inimigo escolhe aleatoriamente entre atacar físico ou especial
        robo = random.randint(1,2)
        if robo == 1:
            alvo.fisico(alvo = jogador) 
        elif robo == 2:
            alvo.especial(alvo = jogador)        
        # Verifica se você morreu após o ataque do inimigo
        if jogador.vida <= 0:
            time.sleep(1)
            print(f'O {alvo.nome} [bold red] matou [/bold red] {jogador.nome}!!! VOCÊ PERDEU.') 
            break  
        else:
            pass 
    print("=" * 40 + "\n")
