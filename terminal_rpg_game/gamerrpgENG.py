from abc import ABC, abstractmethod
import random
from rich import print
import time

# Create mother class (Character) and assign their basic elements.
class Character(ABC):
    '''Within this class we have the basic functioning required for a basic character template.'''
    def __init__(self, name='', hp=200):
        self.name = name
        self.hp = hp
        self.moves = []
        self.powers = []
        self.frozen = False
        self.poisoned = 0 # Stores how many turns of poison are left

    # Define physical attack style
    def physical_attack(self, target):
        damage = random.randint(10, 30)
        target.hp -= damage
        self.moves = random.choice(['headbutt', 'kick', 'punch'])
        print(f'The [green]{type(self).__name__}[/green] [purple]{self.name}[/purple] caused [red]{damage}[/red] damage with a {self.moves} to [blue]{target.name}[/blue].')

    # Special move
    def special_attack(self, target):
        self.powers = random.choice(['poison', 'ice', 'light'])
        
        # Poison:
        if self.powers == 'poison':
            target.poisoned = 3 # Target will be poisoned for 3 turns
            print(f'[green]{self.name}[/green]\'s special infected [blue]{target.name}[/blue] with [magenta]poison[/magenta]!')
            
        # Ice:
        elif self.powers == 'ice':
            target.hp -= 12
            target.frozen = True
            print(f"[green]{self.name}[/green]\'s special caused [red]12[/red] damage and [cyan]froze[/cyan] {target.name}!")
            
        # Light (Heals whoever used the skill, which is self):
        elif self.powers == 'light':
            if self.hp >= 200:
                print(f"[green]{self.name}[/green] tried to use Light, but is already at full health!")
            else:
                heal = random.randint(15, 50)
                previous_hp = self.hp
                self.hp += heal
                if self.hp > 200:
                    self.hp = 200
                real_heal = self.hp - previous_hp
                print(f"[green]{self.name}[/green] used Light and recovered [green]{real_heal} health points[/green]!")

class Hero(Character):
    def __init__(self, name='', hp=200):
        super().__init__(name, hp)

class Villain(Character):
    def __init__(self, name='', hp=200):
        super().__init__(name, hp)

# Ask for the player's name and faction.
def choose_character():
    while True:
        try:
            side = int(input("Hello! Do you want to be a [1] Villain or a [2] Hero? "))
            if side in [1,2]:
                break
            else:
                raise ValueError
        except ValueError:
            print('[red]Wrong digit!! Choose between 1 and 2!![/red]')
            
    if side == 1:
        name = input("What will be the name of your villain? ").strip()
        player = Villain(name)
        time.sleep(1)
        print(f"You chose to be a [red]villain[/red] named [purple]{player.name}[/purple].")
        enemy = Hero(name='Super')
    elif side == 2:
        name = input("What will be the name of your hero? ").strip()
        player = Hero(name)
        time.sleep(1)
        print(f"You chose to be a [green]hero[/green] named [purple]{player.name}[/purple].")
        enemy = Villain(name='Super')
    return player, enemy

# Game initialization
player, enemy = choose_character()
print("\n[bold yellow]⚔️ THE BATTLE HAS BEGUN! ⚔️[/bold yellow]\n")

# The game runs while BOTH are alive
while player.hp > 0 and enemy.hp > 0:
    time.sleep(1)
    print(f'[bold green]YOUR HP: {max(0, player.hp)}[/bold green] | [bold red]ENEMY HP: {max(0, enemy.hp)}[/bold red]')
    
    # --- Poison effect on player ---
    if player.poisoned > 0:
        player.hp -= 7
        player.poisoned -= 1
        print(f'[magenta][POISON DAMAGE][/magenta] {player.name} suffered [purple]7[/purple] continuous damage!')
        if player.hp <= 0:
            print(f'The poison [bold red]killed[/bold red] {player.name}!!! YOU LOST.')
            break

    # --- PLAYER'S TURN ---
    if player.frozen:
        time.sleep(1)
        print(f'{player.name} is [cyan]frozen[/cyan] and skipped the turn!')
        player.frozen = False
    else:
        print("[bold cyan]Your Turn![/bold cyan]")
        print("[1] Physical Attack")
        print("[2] Special Attack")
        
        while True:
            try:
                time.sleep(1)
                choice = int(input('Choose your move: '))
                if choice in[1,2]:
                    break
                else:
                    raise ValueError
            except ValueError:
                time.sleep(1)
                print('[bold red]Choose a corresponding digit!![/bold red]')

        if choice == 1:
            player.physical_attack(enemy) 
        elif choice == 2:
            player.special_attack(enemy)   

        if enemy.hp <= 0:
            time.sleep(1)
            print(f'{player.name} [bold red]killed[/bold red] {enemy.name}!! [bold yellow]YOU WON!!![/bold yellow]')
            break

    print("-" * 20)
    time.sleep(1)

    # --- Poison effect on enemy ---
    if enemy.hp > 0 and enemy.poisoned > 0:
        enemy.hp -= 7
        enemy.poisoned -= 1
        print(f'[magenta][POISON DAMAGE][/magenta] {enemy.name} suffered [purple]7[/purple] continuous damage!')
        if enemy.hp <= 0:
            print(f'The poison [bold red]killed[/bold red] {enemy.name}!! [bold yellow]YOU WON!!![/bold yellow]')
            break

    # --- ENEMY'S TURN (AI) ---
    if enemy.hp > 0:
        if enemy.frozen:
            print(f'{enemy.name} is [cyan]frozen[/cyan] and skipped the turn!')
            enemy.frozen = False
        else:
            print("The enemy is choosing a move...")
            time.sleep(1)
            
            ai_choice = random.randint(1, 2)
            if ai_choice == 1:
                enemy.physical_attack(player) 
            elif ai_choice == 2:
                enemy.special_attack(player)        

            if player.hp <= 0:
                time.sleep(1)
                print(f'{enemy.name} [bold red]killed[/bold red] {player.name}!!! YOU LOST.') 
                break  
                
    print("=" * 40 + "\n")
