# conda

### 查看版本
```buildoutcfg
conda --version
```


### 更新升级conda版本
```buildoutcfg
conda update conda
```


### 查看环境管理的全部命令帮助
```buildoutcfg
conda env -h
```


### 查看当前系统下的环境
```buildoutcfg
conda info -e
conda info --envs
conda env list
```


### 创建环境
```buildoutcfg
conda create --name [env_name]
# 创建指定Python版本的环境
conda create -n [env_name] [python=3.6]
# 创建包含某些包的环境 
conda create [env_name] [numpy] [scipy=0.15.0]
# 添加环境变量后需要激活命令行
conda init zsh
```


### 激活（进入）某个环境
```buildoutcfg
# Mac
source activate myenv
```


### 退出某个环境
```buildoutcfg
source deactivate [env_name]
```


### 复制某个环境
```buildoutcfg
conda create --name myclone --clone myenv
# 查看是否复制成功
conda info --envs
```


### 删除某个环境
```buildoutcfg
conda remove --name [env_name] --all
```


### 查看已安装的包
```buildoutcfg
conda list
# 查看指定环境下的包
conda list -n [env_name]
```


### 安装包
```buildoutcfg
conda install [pkg_name]
# 指定安装包时的安装环境
conda install -n env_name [pkg_name]
# 安装anaconda发行版中所有的包
conda install anaconda
```


### 卸载包
```buildoutcfg
conda remove [pkg_name]
```


### 查找包
```buildoutcfg
conda search [pkg_name]
```


### 更新包
```buildoutcfg
conda update [pkg_name]
```


### 分享环境
```buildoutcfg
# 通过 activate env_name 进入要分享的环境 env_name，执行下边命令生成文件
conda env export > environment.yml
# 将生成的文件放在工作目录下，通过以下命令从该文件创建环境
conda env create -f environment.yml
```













