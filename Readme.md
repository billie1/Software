## Readme



### 文件架构

+ code：存放软件实现的源代码
  + `fje.py`：main文件，通过运行该代码可以运行该软件
  + `Component.py`: 定义Component 类，定义组合中所有对象的通用接口
  + `Container.py`: 定义Container 类，表示复合节点对象，TreeContainer 和 RectangleContainer具体实现了绘制树形和矩形风格容器的方法
  + `Leaf.py`：定义Leaf 类，表示叶子节点对象，TreeLeaf 和 RectangleLeaf具体实现了绘制树形和矩形风格叶节点的方法
  + `Icon.py`: 定义IconFamily 类，定义了获取容器和叶子节点图标的方法，BlaceSpaceIcon 和 PokerFaceIcon具体实现了获取容器和叶子节点图标的方法
  + `StyleFactory.py`：定义StyleFactory类，定义了创建风格（容器，叶节点）的方法，TreeStyleFactory、RectangleStyleFactory分别实现了不同风格的创建方法
  + `FunnyJsonExplorer.py`: 定义FunnyJsonExplorer 类，为客户端类，通过组件接口与组合结构进行交互
+ result：运行结果截图
+ Funny JSON Explorer 设计文档.pdf: 设计文档
+ 设计类图.png: 设计类图


### 运行方法

+ 运行指令：(以树形结构扑克图标为例)

  ```shell
  cd code 
  python .\fje.py -f .\test.json -s tree -i poker
  ```

+ 所有指令如下：

  ```shell
  usage: fje.py [-h] [-f FILE] [-s STYLE] [-i ICON] [-l]
  
  Funny JSON Explorer
  
  optional arguments:
    -h, --help            show this help message and exit
    -f FILE, --file FILE  Path to the JSON file
    -s STYLE, --style STYLE
                          Style of visualization
    -i ICON, --icon ICON  Icon family to use
    -l, --list            List available styles and icon families
  ```

  

  

  
