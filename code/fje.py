import argparse
from FunnyJsonExplorer import *

"""
软件功能描述：
该软件名为 Funny JSON Explorer，用于以不同风格和图标显示 JSON 数据的内容。用户可以通过命令行参数指定 JSON 文件路径、显示风格以及图标风格。
支持动态注册新风格和图标，使其具有高度的可扩展性。

注册新风格和新图标步骤：
1. 定义新的风格工厂类和图标类，并确保它们实现相应的接口。
2. 使用 register_style 和 register_icon 函数将新的风格工厂类和图标类注册到全局注册表中。
3. 使用命令行参数指定新注册的风格和图标，即可显示 JSON 数据。

以下代码实现了上述功能，并提供了默认的风格和图标注册。
"""

# 全局注册表
style_registry = {}
icon_registry = {}


# 注册新风格函数
def register_style(name, factory_class):
    """
    注册一个新的风格工厂类到全局注册表。

    :param name: 风格名称
    :param factory_class: 风格工厂类
    """
    style_registry[name] = factory_class


# 注册新图标函数
def register_icon(name, icon_family_class):
    """
    注册一个新的图标类到全局注册表。

    :param name: 图标名称
    :param icon_family_class: 图标类
    """
    icon_registry[name] = icon_family_class


# 注册默认风格和图标
register_style('tree', TreeStyleFactory)
register_style('rectangle', RectangleStyleFactory)
register_icon('blackspace', BlackSpaceIcon)
register_icon('poker', PokerFaceIcon)


# 命令行解析
def parse_args():
    """
    解析命令行参数，支持文件路径、风格、图标以及列出可用风格和图标的选项。

    :return: 解析后的命令行参数
    """
    parser = argparse.ArgumentParser(description='Funny JSON Explorer')
    parser.add_argument('-f', '--file', type=str, help='Path to the JSON file')
    parser.add_argument('-s', '--style', type=str, help='Style of visualization')
    parser.add_argument('-i', '--icon', type=str, help='Icon family to use')
    parser.add_argument('-l', '--list', action='store_true', help='List available styles and icon families')
    return parser.parse_args()


def list_options():
    """
    列出当前可用的风格和图标。
    """
    print("Available styles:")
    for style in style_registry:
        print(f" - {style}")
    print("Available icon families:")
    for icon in icon_registry:
        print(f" - {icon}")


def main():
    """
    程序主入口，根据命令行参数展示 JSON 数据。
    """
    args = parse_args()

    if args.list:
        list_options()
        return

    if not args.file or not args.style or not args.icon:
        print("Please provide all required arguments: -f <json file> -s <style> -i <icon family>")
        print("Input the following instruction to get help: fje --help")
        return

    with open(args.file, 'r') as f:
        json_data = json.load(f)

    # 检查提供的风格和图标
    style_key = f"{args.style}"
    if style_key in style_registry:
        style = style_registry[style_key]()
    else:
        raise ValueError(f"Unknown style: {args.style}")

    icon_key = f"{args.icon}"
    if icon_key in icon_registry:
        icon = icon_registry[icon_key]()
    else:
        raise ValueError(f"Unknown icon: {args.icon}")

    # 创建 explorer 并显示数据
    explorer = FunnyJsonExplorer(style, icon)
    explorer.show(json_data)


if __name__ == "__main__":
    main()
