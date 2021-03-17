# coding:utf-8
import re
import json
import random
from random import randint
#from data.get_data import GetData
import inspect


class CommonUtil:
	def __init__(self):
		#self.getData = GetData()
		pass
	def is_contain(self, expectValue, resultValue):
		'''
		判断一个字符串是否再另外一个字符串中
		'''
		flag = None
		# 判断是否为字符串，如果不是就变成是
		if isinstance(resultValue, dict):
			resultValue = json.dumps(resultValue).replace(" ", "") # 将字典变成json，然后再去掉空格
		if expectValue.replace(" ", "") in resultValue:
			flag = True
		else:
			flag = False
		return flag

	# 预期结果校验
	def assert_dict(self, expected, result):
		"""
		需要传递预期结果和实际结果的字典值，
		判断之后会返回True或者false
		"""
		#result = json.loads(result)  # 转成字典转成
		flag = None
		for key in expected:
			if (key in result):
				if result[key] == expected[key]:
					flag = True
				elif expected[key] == 'bm_exist()':
					flag = True
				else:
					flag = False
					break
			else:
				print('预期结果字段与响应结果不匹配,请检查！')
				break
		return flag

	# 生成指定长度随机整数
	def bm_get_int(self, n):
		range_start = 10 ** (n - 1)
		range_end = (10 ** n) - 1
		return randint(range_start, range_end)

	# 生成指定长度的随机字符串
	def bm_get_str(self, randomlength, str_name=None):
		random_str = ''
		base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
		length = len(base_str) - 1
		for i in range(randomlength):
			random_str += base_str[random.randint(0, length)]

		#str_dic = {str_name: random_str}
		#print(str_dic)
		#print(type(CommonUtil.str_dic))

		#print(locals())
		return random_str
	# def bm_get_name(self):
	# 	"""
	# 	该方法实现返回用户调用自定义方法时设置的变量
	# 	"""
	# def bm_get(self,row,var_name):
	# 	"""
	# 	获取用户前面指定参数的名的值，会返回出去
	# 	应该要拿到字典，拿到key=用户定义的变量名，然后对应的value是那个函数生成的值
	# 	"""
	# 	data = self.getData.getDataValue(row)




	def get_method_num(self,str):
		"""
		获取字符串中第一个出现的数字
		:return:第一次出现的数字
		"""
		content = str.replace(" ", "")
		model = re.compile("[0-9]+")
		if model.search(content) is not None:
			pos = model.search(content).span()
			num = int(content[pos[0]:pos[1]])
		return num

	# def is_equal_dict(self,dict_one,dict_two):
	# 	'''
	# 	判断两个字典是否相等
	# 	'''
	# 	if isinstance(dict_one,str):
	# 		dict_one = json.loads(dict_one)
	# 	if isinstance(dict_two,str):
	# 		dict_two = json.loads(dict_two)
	# 	return cmp(dict_one,dict_two)



if __name__ == '__main__':
	cu = CommonUtil()
	print(cu.bm_get_str(7))
	print(cu.bm_get_int(55))
	print(cu.get_method_num('qwe234,21111'))
	#print(88888888)

	# 只获取调用函数的随机值
	#print(cu.bm_get_str(8, "zhangsan").keys()) 	#获取所有key也就是获取用户指定的变量名
	#print(cu.bm_get_str(8, "zhangsan").values()) #获取所有values也就是获取用户希望生成的字符串


	# resultValue = '"oderId":"OT123"'
	# expectValue = '{"name": "zhangsan", "oderId": "OT123"}'
	# print(cu.is_contain(expectValue, resultValue))
	#
	# # 预期结果
	# expected = {'username': 'kaishui',
	# 			"token": "bm_exist()"}
	# # 实际结果
	# result = {
	# 	'code': 1,
	# 	'username': 'kaishui',
	# 	'token': 'ihbedvbwejhvkjvberkjvbkjgkesjvbbje'
	# }
	# res = cu.assert_dict(expected, result)
	# if res:
	# 	print("测试通过")
	# else:
	# 	print("测试不通过")
