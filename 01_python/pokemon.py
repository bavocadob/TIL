from library import Pokemon

# 상속 받는다.
class Pikachu(Pokemon):
    no = 25
    type = '전기'

    def __init__(self, name, lv=5):
        # super -> 부모 클래스의 메서드를 호출하고자 할 때 사용
        super().__init__()
        # 부모 클래스의 메서드를 직접 호출 -> self 인자로 넘겨야함
        # Pokemon.__init__(self)
        self.name = name
        self.lv = lv

        # 최초의 피카츄가 태어났을 때만, 종 정보를 기록한다.
        # first_child
        # if Pikachu.first_child is None:
        #     Pikachu.first_child = self
        #     super().increase_spcies('피카츄')

class Metamon(Pokemon):
    no = 132
    type = '노말'

    def __init__(self, name, lv=5):
        super().__init__()
        self.name = name
        self.lv = lv

        # if Metamon.first_child is None:
        #     Metamon.first_child = self
        #     super().increase_spcies('메타몽')

        self.skill_1 = '변신'

    def attack(self, target):
        self.type = target.type
        return f'{self.name}이 {target.name}으로 변신했다.'
        


p1 = Pikachu('피카츄')
m1 = Metamon('메타몽')

print(m1.type)
# 노말
print(m1.attack(p1))
# 메타몽이 피카츄로 변신했다.
print(m1.type)
# 전기



# 다중 상속, 여러 클래스를 동시에 상속 받을 수 있음.
# mro
# class Child(Pikachu, Metamon):
    
#     def __init__(self, name, lv=5):
#         super().__init__(name, lv)

# c1 = Child('피카츄 메타몽')
# print(c1.type)
# print(c1.no)
# print(c1.skill_1)
# print(c1.attack())