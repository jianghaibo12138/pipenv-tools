# pipenv-tools
The tool for pipenv to change source.

- 执行环境
    - macos

- 目的
    - 为[pipenv](https://github.com/pypa/pipenv)包管理工具换源(不清楚的同学, 百度一下 pip 换源)
   
- 安装
    - clone or download 代码到本地
    ```bash
      git clone https://github.com/jianghaibo12138/pipenv-tools.git
      
      wget https://github.com/jianghaibo12138/pipenv-tools/archive/master.zip
    ```
    - 进入文件目录, 然后执行
    ```bash
      sudo python install.py 
    ```
    (Ps: 默认会生成一个 piph 的可执行脚本, 并 move 至 */usr/local/bin* 路径下)
    
- 使用
    - 在已经执行过*pipenv --three* or *pipenv --two*的目录, 并且已经成功创建虚拟环境,生成*Pipeline*后执行
    ```bash
        # 默认替换为清华大学 pip 源(*https://pypi.tuna.tsinghua.edu.cn/simple*)
        piph
        
        # 通过 -r or --registry 参数更换至指定的源, 比如豆瓣源
        piph -r http://pypi.douban.com/simple/
    ```

- todo 兼容 window 和 linux
    
       
 
    