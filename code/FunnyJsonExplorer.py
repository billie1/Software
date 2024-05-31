# 导入 StyleFactory 模块，该模块包含了风格工厂类
from StyleFactory import *
# 导入 Icon 模块，该模块包含了图标类
from Icon import *
# 导入 json 模块，用于处理 JSON 数据
import json


# 核心类 FunnyJsonExplorer
class FunnyJsonExplorer:
    def __init__(self, styleFactory, iconFamily):
        self.styleFactory = styleFactory  # 风格工厂对象
        self.iconFamily = iconFamily  # 图标族对象

    def show(self, json_data):
        root = self.styleFactory.create_container('root', 0)  # 创建根容器
        self._load(json_data, root)  # 加载 JSON 数据到容器
        root.find_first_last(root)  # 找到每个容器的第一个和最后一个子节点
        children = root.get_children()  # 获取根容器的子节点
        for i, child in enumerate(children):
            child.draw("")  # 绘制每个子节点的结构

    def _load(self, json_data, container):
        for key, value in json_data.items():
            if isinstance(value, dict):
                sub_container = self.styleFactory.create_container(key, container.level + 1)  # 创建子容器
                container_icon = self.iconFamily.get_icon_for_Container()  # 获取容器图标
                container.add(sub_container)  # 将子容器添加到父容器中
                sub_container.icon = container_icon  # 设置子容器的图标
                self._load(value, sub_container)  # 递归加载子容器中的数据
            else:
                leaf = self.styleFactory.create_leaf(key, value)  # 创建叶子节点
                leaf_icon = self.iconFamily.get_icon_for_leaf()  # 获取叶子节点图标
                container.add(leaf)  # 将叶子节点添加到父容器中
                leaf.icon = leaf_icon  # 设置叶子节点的图标


# 示例用法
if __name__ == "__main__":
    json_data = '''
    {
        "oranges": {
            "mandarin": {
                "clementine": null,
                "tangerine": "cheap & juicy!"
            }
        },
        "apples": {
            "gala": null,
            "pink lady": null
        }
    }
    '''

    data = json.loads(json_data)

    # 树形风格+空格图标
    print("树形风格:")
    fje_tree = FunnyJsonExplorer(TreeStyleFactory(), BlackSpaceIcon())
    fje_tree.show(data)

    print("矩形风格:")
    fje_rectangle = FunnyJsonExplorer(RectangleStyleFactory(), PokerFaceIcon())
    fje_rectangle.show(data)
