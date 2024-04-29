# Декоратор для додавання коду який не можна змінювати але треба =)

class Greting:
    def __init__(self, username) -> None:
        self.username = username

    def say(self):
        return f'Hello {self.username}'
    
class DecoratorDreting:
    def __init__(self, wrapper:Greting) -> None:
        self.wraper = wrapper

    def say(self):
        base_grett = self.wraper.say()
        return base_grett.upper()


user = DecoratorDreting(Greting('Serhii'))
print(user.say())