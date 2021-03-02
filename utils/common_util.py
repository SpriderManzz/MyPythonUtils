# coding:utf-8
import json

import simplejson as simplejson


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

	#
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
	resultValue='"oderId":"OT123"'
	expectValue='{"name": "zhangsan", "oderId": "OT123"}'
	print(cu.is_contain(expectValue,resultValue))