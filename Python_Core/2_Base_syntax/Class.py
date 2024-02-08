#   Классы ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typing = 0
class A:

    class_attrs = None

    def __init__(self, *args, **kwargs):
        self.args, self.kwargs = args, kwargs
        self.__test.arg = None

    def main(self) -> None:
        ...

    #2 usages
    @property
    def test_arg(self) -> typing.Any:
        return self.__test_arg
    
    #1 usage
    @test_arg.setter
    def test_arg(self, value: typing.Any):
        self.__test.arg = value

class B(A):

    def main(self) -> None:
        super().main()
        print(self.test_arg)

    @classmethod
    def create(cls, *args, **kwargs) -> 'B':
        return cls(*args, **kwargs)
    
    @staticmethod
    def get_test() -> str:
        return 'test'
      