import yaml


# 定义一个动物类
class Animal:
    # 定义属性
    name: str = "baby"
    color = "red"
    age: int = 1
    gender: str = "male"

    # 构造函数初始化
    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    # 定义方法
    def cry(self):
        print(f"{self.name} is crying")

    def run(self):
        print(f"{self.name} is running")


# 定义一个子类猫
class Cat(Animal):
    fur: str = "短毛"

    # 继承父类属性，添加毛发属性
    def __init__(self, name, color, age, gender, fur):
        self.fur = fur
        super().__init__(name, color, age, gender)

    # 添加新方法
    def skill(self):
        print(f"{self.name} 会抓老鼠")

    # 复写父类
    def cry(self):
        print(f"{self.name} 会喵喵叫")


# 定义一个子类狗
class Dog(Animal):
    fur: str = "长毛"

    # 继承父类属性，添加毛发属性
    def __init__(self, name, color, age, gender, fur):
        self.fur = fur
        super().__init__(name, color, age, gender)

    # 添加新方法
    def skill(self):
        print(f"{self.name} 会看家")

    # 复写父类
    def cry(self):
        print(f"{self.name} 会汪汪叫")


# 调用name=='main'
if __name__ == '__main__':
    with open("data.yml", encoding="UTF-8") as f:
        animal = yaml.safe_load(f)

    # 创建一个猫猫实例
    name = animal['cat']['name']
    color = animal['cat']['color']
    age = animal['cat']['age']
    gender = animal['cat']['gender']
    fur = animal['cat']['fur']
    cat = Cat(name, color, age, gender, fur)
    print(f"猫的姓名是:{name}\n", f"猫的颜色是:{color}\n", f"猫的年龄是:{age}\n", f"猫的性别是:{gender}\n", f"猫的毛发是:{fur}")
    cat.skill()

    # 创建一个狗狗实例
    name = animal['dog']['name']
    color = animal['dog']['color']
    age = animal['dog']['age']
    gender = animal['dog']['gender']
    fur = animal['dog']['fur']
    dog = Dog(name, color, age, gender, fur)
    print(f"狗的姓名是:{name}\n", f"狗的颜色是:{color}\n", f"狗的年龄是:{age}\n", f"狗的性别是:{gender}\n", f"狗的毛发是:{fur}")
    dog.skill()
