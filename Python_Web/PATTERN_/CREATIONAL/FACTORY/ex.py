from abc import ABC, abstractmethod
'/////////////////////////////////////////////////////////////////////   Фабричний метод (Factory Method)     ///////////////////////////////////////////////////////////////////////////////////////////////////'
class Creator(ABC):
    @abstractmethod
    def create(self):
        pass

    def send_messages(self):
        product = self.create()
        result = product.sending()
        return result

class SendingMessages(ABC):
    @abstractmethod
    def sending(self):
        pass

class CreatorPush(Creator):
    def create(self):
        return SendingPushMassages()
    
class CreatorSMS(Creator):
    def create(self):
        return SendingSMShMassages()

class SendingPushMassages(SendingMessages):
    def sending(self):
        return 'Push mailing has been complet'
    
class SendingSMShMassages(SendingMessages):
    def sending(self):
        return 'SMS mailing has been complet'

def client_code(creator:Creator):
    print('We know noting about the creator code that works')
    result = creator.send_messages()
    # print(f'Result: {result}')

if __name__ == "__main__":
    print("The application performs Push mailing lists.")
    client_code(CreatorPush())
    # print("\n")

    print("The application performs SMS mailing.")
    client_code(CreatorSMS())

'........................................................................................................................................................................................................'

class Sum:
    def __init__(self, num_1, num_2) -> None:
        self.num_1 = num_1
        self.num_2 = num_2

    def say(self):
        return self.num_1 + self.num_2

class Mul:
    def __init__(self, num_1, num_2) -> None:
        self.num_1 = num_1
        self.num_2 = num_2

    def say(self):
        return self.num_1 - self.num_2

def create_class(a, b, obj = 'sum'):
    mul_sum = dict(sum = Sum(a, b), mul = Mul(a, b))
    return mul_sum.get(obj)

if __name__ == "__main__":
    result = create_class(10, 5, 'mul')
    print(result.say())

