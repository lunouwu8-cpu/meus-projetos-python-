from abc import ABC, abstractmethod
import random
from rich import print
import time
def jogo_completo():
    # Criar classe mãe(personagem) e atribuir elementos básicos deles.
    class Personagem(ABC):
        '''Dentro desta classe temos o funcionamento básico exigido do molde de um personagem básico.'''
        def __init__(self, nome='', vida=200):
            self.nome = nome
            self.vida = vida
            self.golpes = []
            self.poderes = []
            self.congelado = False
            self.envenenado = 0 # Guarda quantos turnos de veneno restam

        # Definir estilo do golpe físico
        def fisico(self, alvo):
            dano = random.randint(10, 30)
            alvo.vida -= dano
            self.golpes = random.choice(['cabeçada', 'chute', 'soco'])
            print(f'O [green]{type(self).__name__}[/green] [purple]{self.nome}[/purple] causou [red]{dano}[/red] com um {self.golpes} ao [blue]{alvo.nome}[/blue].')

        # Golpe especial
        def especial(self, alvo):
            self.poderes = random.choice(['veneno', 'gelo', 'luz'])
            
            # Veneno:
            if self.poderes == 'veneno':
                alvo.envenenado = 3 # O alvo ficará envenenado por 3 turnos
                print(f'O especial de [green]{self.nome}[/green] infectou [blue]{alvo.nome}[/blue] com [magenta]veneno[/magenta]!')
                
            # Gelo:
            elif self.poderes == 'gelo':
                alvo.vida -= 12
                alvo.congelado = True
                print(f"O especial de [green]{self.nome}[/green] causou [red]12[/red] de dano e [cyan]congelou[/cyan] {alvo.nome}!")
                
            # Luz (Cura quem usou o golpe, ou seja, self):
            elif self.poderes == 'luz':
                if self.vida >= 200:
                    print(f"[green]{self.nome}[/green] tentou usar Luz, mas já está com a vida cheia!")
                else:
                    luz = random.randint(15, 50)
                    vida_passada = self.vida
                    self.vida += luz
                    if self.vida > 200:
                        self.vida = 200
                    luz_real = self.vida - vida_passada
                    print(f"[green]{self.nome}[/green] usou Luz e recuperou [green]{luz_real} pontos[/green] de vida!")

    class Héroi(Personagem):
        def __init__(self, nome='', vida=200):
            super().__init__(nome, vida)

    class Vilão(Personagem):
        def __init__(self, nome='', vida=200):
            super().__init__(nome, vida)

    # Pedir nome do jogador e perguntar se ele é vilão ou herói.
    def escolha():
        while True:
            try:
                lado = int(input("Olá! Você quer ser um [1] Vilão ou um [2] Herói? "))
                if lado in [1, 2]:
                    break
                else:
                    raise ValueError
            except ValueError:
                print('[red]Dígito errado!! Escolha entre 1 e 2!![/red]')
                
        if lado == 1:
            nome = input("Qual será o nome do seu vilão? ").strip()
            jogador = Vilão(nome)
            time.sleep(1)
            print(f"Você escolheu ser um [red]vilão[/red] chamado [purple]{jogador.nome}[/purple].")
            inimigo = Héroi(nome='Héroi')
        elif lado == 2:
            nome = input("Qual será o nome do seu herói? ").strip()
            jogador = Héroi(nome)
            time.sleep(1)
            print(f"Você escolheu ser um [green]herói[/green] chamado [purple]{jogador.nome}[/purple].")
            inimigo = Vilão(nome='Vilão')
        return jogador, inimigo

    # Inicialização do jogo
    jogador, inimigo = escolha()
    print("\n[bold yellow]⚔️ A BATALHA COMEÇOU! ⚔️[/bold yellow]\n")

    # O jogo roda enquanto os DOIS estiverem vivos
    while jogador.vida > 0 and inimigo.vida > 0:
        time.sleep(1)
        print(f'[bold green]SUA VIDA: {max(0, jogador.vida)}[/bold green] | [bold red]VIDA DO INIMIGO: {max(0, inimigo.vida)}[/bold red]')
        
        # --- Efeito de Veneno no jogador ---
        if jogador.envenenado > 0:
            jogador.vida -= 7
            jogador.envenenado -= 1
            print(f'[magenta][DANO DE VENENO][/magenta] {jogador.nome} sofreu [purple]7[/purple] de dano contínuo!')
            if jogador.vida <= 0:
                print(f'O veneno [bold red]matou[/bold red] {jogador.nome}!!! VOCÊ PERDEU.')
                break

        # --- TURNO DO JOGADOR ---
        if jogador.congelado:
            time.sleep(1)
            print(f'O {jogador.nome} está [cyan]congelado[/cyan] e perdeu o turno!')
            jogador.congelado = False
        else:
            print("[bold cyan]Seu Turno![/bold cyan]")
            print("[1] Ataque Físico")
            print("[2] Golpe Especial")
            
            while True:
                try:
                    time.sleep(1)
                    opcao = int(input('Qual golpe: '))
                    if opcao in [1,2]:
                        break
                    else:
                        raise ValueError
                except ValueError:
                    time.sleep(1)
                    print('[bold red]Escolha um dígito correspondente!![/bold red]')

            if opcao == 1:
                jogador.fisico(inimigo) 
            elif opcao == 2:
                jogador.especial(inimigo)   

            if inimigo.vida <= 0:
                time.sleep(1)
                print(f'O {jogador.nome} [bold red]matou[/bold red] o {inimigo.nome}!! [bold yellow]VOCÊ VENCEU!!![/bold yellow]')
                break

        print("-" * 20)
        time.sleep(1)

        # --- Efeito de Veneno no inimigo ---
        if inimigo.vida > 0 and inimigo.envenenado > 0:
            inimigo.vida -= 7
            inimigo.envenenado -= 1
            print(f'[magenta][DANO DE VENENO][/magenta] {inimigo.nome} sofreu [purple]7[/purple] de dano contínuo!')
            if inimigo.vida <= 0:
                print(f'O veneno [bold red]matou[/bold red] o {inimigo.nome}!! [bold yellow]VOCÊ VENCEU!!![/bold yellow]')
                break

        # --- TURNO DO INIMIGO (I.A.) ---
        if inimigo.vida > 0:
            if inimigo.congelado:
                print(f'O {inimigo.nome} está [cyan]congelado[/cyan] e perdeu o turno!')
                inimigo.congelado = False
            else:
                print("O inimigo está escolhendo seu golpe...")
                time.sleep(1)
                
                robo = random.randint(1, 2)
                if robo == 1:
                    inimigo.fisico(jogador) 
                elif robo == 2:
                    inimigo.especial(jogador)        

                if jogador.vida <= 0:
                    time.sleep(1)
                    print(f'O {inimigo.nome} [bold red]matou[/bold red] {jogador.nome}!!! VOCÊ PERDEU.') 
                    break  
                    
        print("=" * 40 + "\n")
