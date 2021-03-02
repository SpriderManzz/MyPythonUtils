import os
import sys

class  PathUtil(object):
  """
    路径处理工具类
  """
  def __init__(self):
    # 判断调试模式
    debug_vars = dict((a, b) for a, b in os.environ.items()
             if a.find('IPYTHONENABLE') >= 0)
    # 根据不同场景获取根目录
    if len(debug_vars) > 0:
      """当前为debug运行时"""
      self.rootPath = sys.path[2]
    elif getattr(sys, 'frozen', False):
      """当前为exe运行时"""
      self.rootPath = os.getcwd()
    else:
      """正常执行"""
      self.rootPath = sys.path[1]
    # 替换斜杠
    #self.rootPath = self.rootPath.replace("\\", "/")


  def getPathFromResources(self, fileName):
    """按照文件名拼接资源文件路径"""
    filePath = "%s/resources/%s" % (self.rootPath, fileName)
    return filePath



def get_current_path():
    """
    获取当前模块路径
    :return: 当前模块当前路径
    """
    currentPath = os.path.split(os.path.realpath(__file__))[0]
    return currentPath


def get_absolute_path():
    """
    获取项目所在位置  F:\
    :return: 项目所在位置
    """
    absolutePath = os.path.abspath(os.path.dirname(__file__)).split('MyPythonUtils')[0]
    return absolutePath


if __name__ == '__main__':
    PathUtil = PathUtil()
    print('当前路径为:', get_current_path())
    print('项目所在位置:', get_absolute_path())
    print("项目绝对路径为:"+PathUtil.rootPath)


