class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def show_status(self):
        print("-----")
        print("角色：", self.name)
        print("血量：", self.hp)
        print("攻擊力：", self.attack_power)

    def attack(self, enemy):
        print(self.name, "攻擊了", enemy.name)
        enemy.hp -= self.attack_power

        if enemy.hp < 0:
            enemy.hp = 0

        print(enemy.name, "受到了", self.attack_power, "點傷害")

    def is_alive(self):
        return self.hp > 0


player = Character("勇者", 100, 20)
monster = Character("史萊姆", 60, 15)

player.show_status()
monster.show_status()

print("戰鬥開始！")

while player.is_alive() and monster.is_alive():
    player.attack(monster)
    monster.show_status()

    if not monster.is_alive():
        print(monster.name, "被打倒了！")
        break

    monster.attack(player)
    player.show_status()

    if not player.is_alive():
        print(player.name, "被打倒了！")
        break

print("戰鬥結束！")

# 看懂他，下禮拜解釋一下這個 class
# __init__ 做了什麼事情？
# attribute、method 有哪些？