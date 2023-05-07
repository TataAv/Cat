def add(a, b):
    return a+b

def mult(a, b):
    return a*b



# 5.1.Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов- как
# минимум один атрибут должен быть с уровнем доступа private.Соответственно, для получания значений этого
# атрибута нужно использовать методы get и set
# 5.2.Cоздайте репозиторий на Github и отправте файл сдомашним заданием в этот удаленный репозиторий
class Cat:
    clasificacion = 'Animales'
    def __init__(self, name, weight, color):
        self._name = name
        self.weight = weight
        self.color = color
    def run(self):
        return "i can run"
    def get_name(self):
        return f"hello. my name is {self.name}"
    def set_name(self, new_name):
        self._name=new_name
cat1 = Cat('Tom', 1, 'blanco')
# print(cat1.name)
# print(cat1.get_name())
#
cat2 = Cat('Murca', 2, 'gris')
# print(cat2.run())
# print(cat2.clasificacion)
#
cat3 = Cat('Ryzik', 6, 'narahja')
# print(cat3.clasificacion)
# print(cat3.name)

class Sfinks(Cat):
    def __init__(self,name, weight, color, gender):
        super().__init__(name, weight, color)
        self.gender = gender

    def myau(self):
        return 'Myau'
    def run(self):
        return 'i can run fast'

cat4 = Sfinks('Gloria', 4, 'pink', 'femenino')
# print(cat4.myau())
# print(cat4.name)
# # print(cat2.myau())
# print(cat1.run())
# print(cat4.run())
cat2.name = 'Murzik'
# print(cat2.get_name())
# print(cat2.__dict__)
# print(cat1._name)
print(cat2.set_name('Shkoda'))
print(cat2.get_name())





