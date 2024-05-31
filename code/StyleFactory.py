from Leaf import *
from Container import *


# 定义一个抽象基类 StyleFactory
class StyleFactory(ABC):
    # 定义抽象方法，用于创建容器对象
    @abstractmethod
    def create_container(self, name, level):
        pass

    # 定义抽象方法，用于创建叶子对象
    @abstractmethod
    def create_leaf(self, name, value):
        pass


# 继承 StyleFactory 抽象基类的子类 TreeStyleFactory
class TreeStyleFactory(StyleFactory):
    # 实现创建容器对象的方法
    def create_container(self, name, level):
        return TreeContainer(name, level)

    # 实现创建叶子对象的方法
    def create_leaf(self, name, value):
        return TreeLeaf(name, value)


# 继承 StyleFactory 抽象基类的子类 RectangleStyleFactory
class RectangleStyleFactory(StyleFactory):
    # 实现创建容器对象的方法
    def create_container(self, name, level):
        return RectangleContainer(name, level)

    # 实现创建叶子对象的方法
    def create_leaf(self, name, value):
        return RectangleLeaf(name, value)
