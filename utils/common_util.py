# coding:utf-8
import json
import random
from random import randint


class CommonUtil:
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
				print('响应结果中无该字段,请检查！')
		return flag

	# 生成指定长度随机整数
	def bm_get_int(self, n):
		range_start = 10 ** (n - 1)
		range_end = (10 ** n) - 1
		return randint(range_start, range_end)

	# 生成指定长度的随机字符串
	def bm_get_str(self, randomlength):
		random_str = ''
		base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
		length = len(base_str) - 1
		for i in range(randomlength):
			random_str += base_str[random.randint(0, length)]
		return random_str

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
	resultValue = '"oderId":"OT123"'
	expectValue = '{"name": "zhangsan", "oderId": "OT123"}'
	print(cu.is_contain(expectValue, resultValue))

	# 预期结果
	expected = {'username': 'kaishui',
				"token": "bm_exist()"}
	# 实际结果
	result = {
		'code': 1,
		'username': 'kaishui',
		'token': 'ihbedvbwejhvkjvberkjvbkjgkesjvbbje'
	}
	res = cu.assert_dict(expected, result)
	if res:
		print("测试通过")
	else:
		print("测试不通过")