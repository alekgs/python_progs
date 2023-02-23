class Foo:
    text = 'Hello, world !'

    def __init__(self):
        print(f'init: {self.text}')

    def print_out(self, text='Hi !'):
        self.text = text
        print(f'print_out: {self.text}')

    # def __del__(self):
    #     print('destructor')


obj = Foo()
obj.print_out()
obj.print_out('Hello, Python !')
