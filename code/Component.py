from abc import ABC, abstractmethod


# 抽象基类：Component
# Component 是一个抽象基类，为组合模式中的叶子节点和复合节点提供统一的接口。
class Component(ABC):
    @abstractmethod
    def draw(self, prefix):
        """
        抽象方法：绘制组件。
        每个具体组件（叶子或容器）必须实现此方法，以特定的格式绘制自己。

        :param prefix: 用于绘制时的前缀字符串，表示层级关系
        """
        pass

    @abstractmethod
    def add(self, component):
        """
        抽象方法：添加子组件。
        只有容器类组件会实现此方法，叶子节点不需要实现。

        :param component: 要添加的子组件
        """
        pass

    @abstractmethod
    def get_children(self):
        """
        抽象方法：获取子组件列表。
        只有容器类组件会实现此方法，叶子节点通常返回空列表。

        :return: 子组件列表
        """
        return []
