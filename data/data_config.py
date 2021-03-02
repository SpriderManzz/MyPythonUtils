# coding:utf-8


class GlobalVar:
    # 测试用例字段值的编号，定义为常量
    isRun = '0'
    caseId = '1'
    modelName = '2'
    desc = '3'
    url = '4'
    requestMethod = '5'
    header = '6'
    caseDepend = '7'
    dataDepend = '8'
    fieldDepend = '9'
    requetsData = '10'
    expectData = '11'
    resultData = '12'


# ！！！！！！！！！！注意返回的str类型
# 获取【是否运行】
def getIsRunLine():
    return GlobalVar.isRun

# 获取【caseid】
def getCaseIdLine():
    return GlobalVar.caseId


# 获取【模块】
def getModelNameLine():
    return GlobalVar.modelName

# 获取【desc】
def getDescLine():
    return GlobalVar.desc


# 获取【url】
def getUrlLine():
    return GlobalVar.url


# 获取【请求类型】
def getRquestMethodLine():
    return GlobalVar.requestMethod


# 获取【是否携带header】
def getHeaderLine():
    return GlobalVar.header


# 获取【case依赖】
def getCaseDependLine():
    return GlobalVar.caseDepend


# 获取【依赖的返回数据】
def getDataDependLine():
    return GlobalVar.dataDepend


# 获取【数据依赖字段】
def getFieldDependLine():
    return GlobalVar.fieldDepend


# 获取【请求数据】
def getDataLine():
    return GlobalVar.requetsData


# 获取【预期结果】
def getExpectLine():
    return GlobalVar.expectData


# 获取【实际结果】
def getResultLine():
    return GlobalVar.resultData


def getHeaderValue():
    return GlobalVar.header



if __name__ == '__main__':
    print(type(GlobalVar.caseId))
    print("【是否运行】为第" + GlobalVar.isRun + "列")
    print("【caseId】为第" + GlobalVar.caseId + "列")
    print("【模块】为第" + GlobalVar.modelName + "列")
    print("【desc】为第" + GlobalVar.desc + "列")
    print("【url】为第" + GlobalVar.url + "列")
    print("【请求类型】为第" + GlobalVar.requestMethod + "列")
    print("【是否携带header】为第" + GlobalVar.header + "列")
    print("【case依赖】为第" + GlobalVar.caseDepend + "列")
    print("【依赖的返回数据】为第" + GlobalVar.dataDepend + "列")
    print("【数据依赖字段】为第" + GlobalVar.fieldDepend + "列")
    print("【请求数据】为第" + GlobalVar.requetsData + "列")
    print("【预期结果】为第" + GlobalVar.expectData + "列")
    print("【实际结果】为第" + GlobalVar.resultData + "列")
