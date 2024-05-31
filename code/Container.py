from Component import *


# 容器基类：Container
# Container 是 Component 的具体实现类，表示组合模式中的复合节点，可以包含子节点。
class Container(Component):
    def __init__(self, name, level):
        self.name = name  # 容器名称
        self.level = level  # 容器层级
        self.children = []  # 子组件列表
        self.icon = ""  # 容器图标
        self.is_first = False  # 是否是第一个子节点
        self.is_last = False  # 是否是最后一个子节点

    def add(self, child):
        """
        添加子组件到容器中。

        :param child: 子组件
        """
        self.children.append(child)

    def get_children(self):
        """
        获取子组件列表。

        :return: 子组件列表
        """
        return self.children

    @abstractmethod
    def draw(self, prefix):
        """
        抽象方法：绘制容器。
        每个具体容器必须实现此方法，以特定的格式绘制自己及其子组件。

        :param prefix: 用于绘制前缀字符串
        """
        pass

    @abstractmethod
    def find_first_last(self, container, is_execute=False):
        """
        抽象方法：找到并设置容器的第一个和最后一个子节点。

        :param container: 容器
        :param is_execute: 是否执行标志
        """
        pass


# 树形风格容器：TreeContainer
# TreeContainer 是 Container 的具体实现类，按树形结构绘制容器及其子组件。
class TreeContainer(Container):
    def draw(self, prefix):
        """
        按树形结构绘制容器及其子组件。

        :param prefix: 用于绘制前缀字符串
        """
        print(prefix + ("└─" + self.icon if self.is_last else "├─" + self.icon) + self.name)
        new_prefix = prefix + ("    " if self.is_last else "│   ")
        for i, child in enumerate(self.children):
            child.is_last = i == len(self.children) - 1
            child.draw(new_prefix)

    def find_first_last(self, container, is_execute=False):
        """
        设置容器的第一个和最后一个子节点。

        :param container: 容器
        :param is_execute: 是否执行标志
        """
        for i, child in enumerate(container.children):
            child.is_last = i == len(container.children) - 1


# 矩形风格容器：RectangleContainer
# RectangleContainer 是 Container 的具体实现类，按矩形结构绘制容器及其子组件。
class RectangleContainer(Container):
    def draw(self, prefix):
        """
        按矩形结构绘制容器及其子组件。

        :param prefix: 用于绘制前缀字符串
        """
        if self.is_first:
            print(prefix + "┌─" + self.icon + self.name + "─" * (40 - len(prefix) - len(self.name)) + "┐")
        else:
            print(prefix + "├─" + self.icon + self.name + "─" * (40 - len(prefix) - len(self.name)) + "┤")

        for i, child in enumerate(self.children):
            new_prefix = prefix + "│  " if not child.is_last else prefix + "└──"
            child.draw(new_prefix)

    def find_first_last(self, container, is_execute=False):
        """
        设置容器的第一个和最后一个子节点。

        :param container: 容器
        :param is_execute: 是否执行标志
        """
        if not is_execute:
            container.children[0].is_first = True
            is_execute = False
        if container.children:
            if isinstance(container.children[-1], RectangleContainer):
                self.find_first_last(container.children[-1], is_execute)
            else:
                container.children[-1].is_last = True
                return
