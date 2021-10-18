import os
from importlib import util


class Base:
    """Basic resource class. Concrete resources will inherit from this one
    """
    plugins = []

    # For every class that inherits from the current,
    # the class name will be added to plugins
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.plugins.append(cls)


# Small utility to automatically load modules
def load_module(path):
    name = os.path.split(path)[-1]
    spec = util.spec_from_file_location(name, path)
    module = util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def find_file(self, filepath, filename, find_depth=1, ignore_path=['.git', 'node_modules']):
    """查找文件"""
    # print blue("当前查找目录：{}，递归层级：{}".format(filepath, find_depth))
    # 递归深度控制
    find_depth -= 1
    for file_ in os.listdir(filepath):
        # print cyan("file: {}".format(file_))
        if os.path.isfile(os.path.join(filepath, file_)):
            # print "当前文件：{}".format(file_)
            if file_ == filename:
                return True, filepath
        elif find_depth <= 0:  # 递归深度控制, 为0时退出
            # print yellow("超出递归深度，忽略!")
            continue
        elif file_ in ignore_path:  # 忽略指定目录
            # print yellow("此目录在忽略列表中，跳过！")
            continue
        else:
            result, abs_path = self.find_file(filepath=os.path.join(filepath, file_),
                                              filename=filename,
                                              find_depth=find_depth)
            if result:
                print("找到{}文件，所在路径{}".format(filename, abs_path))
                return result, abs_path
    return False, filepath

def get_all_submodule():
    
    all_mod = {}
    # Get current path
    path = os.path.abspath(__file__)
    dirpath = os.path.dirname(path)

    for fname in os.listdir(dirpath):
        # Load only "real modules"

        cpath = os.path.join(dirpath, fname)
        if os.path.isdir(cpath) and os.path.isfile(os.path.join(cpath, 'index.py')):
            mod = load_module(os.path.join(cpath, 'index.py'))
            all_mod[fname] = mod
    
    return all_mod
            
