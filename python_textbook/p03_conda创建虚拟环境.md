# 列出当前环境中已安装的包

conda list



# 列出当前存在的所有环境

conda env list



# 为conda添加国内镜像源

conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/



# 移除指定的channel

conda config --remove channels [channel_name]



# 恢复默认源

conda config --remove-key channels



# 查看当前channels配置状态

conda config --show channels



# 搜索指定的包

conda search [package_name]



# 创建 Python 虚拟环境

conda create -n [your_env_name] python=x.x



# 激活指定的环境

conda activate [your_env_name]



# 退出当前环境

conda deactivate



# 在当前环境中安装包

conda install [package_name]=x.x



# 在指定环境中安装包

conda install -n [your_env_name] [package_name]=x.x



# 删除当前环境中的某个包

conda remove [package_name]



# 删除指定环境中的某个包

conda remove -n [your_env_name] [package_name]



# 删除指定的虚拟环境

conda remove -n [your_env_name] --all

