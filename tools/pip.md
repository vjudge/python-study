# pip

pip 是Python包管理工具，该工具提供了对Python包的查找、下载、安装、卸载的功能。

```buildoutcfg
# 查看版本
pip --version
# 列出所有选项和命令
pip --help
```


### 安装
```buildoutcfg
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py # 下载安装脚本
sudo python get-pip.py # 运行安装脚本
```


### 升级版本
```buildoutcfg
pip install -U pip
pip install --upgrade pip
# 临时使用清华大学开源软件镜像站来升级 pip
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U
```


### 安装包
```buildoutcfg
pip install SomePackage          # 最新版本
pip install SomePackage==1.0.4   # 指定版本
pip install 'SomePackage>=1.0.4' # 最小版本
```


### 卸载包
```buildoutcfg
pip uninstall SomePackage
```


### 升级包
```buildoutcfg
pip install --upgrade SomePackage
```


### 搜索包
```buildoutcfg
pip search SomePackage
```


### 列出已安装的包
```buildoutcfg
pip list
# 查看可升级的包
pip list -o
```


### 显示安装包信息
```buildoutcfg
pip show
# 查看指定包的详细信息
pip show -f SomePackage
```


### 临时使用清华大学开源软件镜像站
```buildoutcfg
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
```


### 如果python2和python3环境都有，需要
```buildoutcfg
python2 -m pip install XXX
python3 -m pip install XXX
```


