
class Mama:
    def says(self):
        print('do your homewok')

class Sister(Mama): # 旧事写法
    def says(self):
        Mama.says(self)
        print('and clean your bedroom')

class Sister1(Mama): # 新式写法
    def says(self):
        super().says()
        print('and clean your bedroom')

