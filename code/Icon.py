from abc import ABC, abstractmethod


# 抽象产品：IconFamily
# IconFamily 是一个抽象基类，定义了两个抽象方法，用于获取容器和叶子节点的图标。
class IconFamily(ABC):
    @abstractmethod
    def get_icon_for_Container(self):
        """
        返回容器图标的抽象方法，必须由子类实现。
        :return: 容器图标
        """
        pass

    @abstractmethod
    def get_icon_for_leaf(self):
        """
        返回叶子节点图标的抽象方法，必须由子类实现。
        :return: 叶子节点图标
        """
        pass


# 具体产品：BlackSpace Icon
# BlackSpaceIcon 类实现了 IconFamily 接口，提供了空白字符作为容器和叶子节点的图标。
class BlackSpaceIcon(IconFamily):
    def get_icon_for_Container(self):
        """
        返回用于容器的空白图标。
        :return: 空白字符 " "
        """
        return " "

    def get_icon_for_leaf(self):
        """
        返回用于叶子节点的空白图标。
        :return: 空白字符 " "
        """
        return " "


# 具体产品：PokerFace Icon
# PokerFaceIcon 类实现了 IconFamily 接口，提供了扑克字符作为容器和叶子节点的图标。
class PokerFaceIcon(IconFamily):
    def get_icon_for_Container(self):
        """
        返回用于容器的扑克图标。
        :return: 扑克容器字符 "♢"
        """
        return "♢"

    def get_icon_for_leaf(self):
        """
        返回用于叶子节点的扑克图标。
        :return: 扑克叶子字符 "♤"
        """
        return "♤"
