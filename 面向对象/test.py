class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __del__(self):
        print(self.__name)
        print("-----------del---------------")


if __name__ == "__main__":
    laowang = Person("老王", 30)