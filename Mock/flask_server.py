import json
import operator
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # 防止乱码jsonify


"""
    1、本接口服务默认约定所有接口返回都是dict(json格式数据)
    2、本服务默认接口的Response Headers为：Content-Type: application/json
"""


# 无需携带headers的get请求-----------------------------------------未优化完成
@app.route('/get/without/headers', methods=['get'])
def gwh1():
    errmsg = {}
    get_args = dict(request.args)
    if not get_args:
        return {"errcode": -1, "errmsg": "id missing"}

    #         for i in request.args.keys()):
    #         print(i)
    #         if i is None:
    #             print(333)
    #             return {"errcode": -1, "errmsg": "id missing"}
    if request.args.get('id') is not None:
        id = int(request.args.get('id'))
    if request.args.get('sex') is not None:
        sex = request.args.get('sex')
    #res = {"msg": "success", "statues": 0, "id": id, "sex": sex}
    # res = '{"msg": "success", "statues": 0}'   这种方式也可以
    # res = json.loads(res)  # 字符串反序列化转成字典

    res = {'msg': 'success', 'statues': 0}
    return res


# 无需携带headers的post请求
@app.route('/post/without/headers', methods=['post'])
def add_stu():
    res1 = '{"msg": "success", "statues": 144}'
    res2 = {"msg": "success", "statues": 144}
    res3 = {'msg': 'success', 'statues': 144}
    return res2 # 框架暂未处理这里



# 需要请求头的get请求 ------------------------------勿动
@app.route('/get/with/headers', methods=["get"])
def index2():

    # 定义接口需要的请求头
    headers = {"Authorization": "test_token",
               "Content-Type": "application/json"}

    # 校验用户请求头是否等于定义接口定义的请求头
    req_headers = dict(request.headers)  # 将用户请求转成字典

    for key in headers:
        if (key in req_headers) & (req_headers[key] == headers[key]):
            falg = True
            continue
        else:
            return {"errcode": 4001, "errmsg:": "请求头有误！请检查"}
    if falg:
        if request.args.get('id') is not None:
            id = int(request.args.get('id'))
        if request.args.get('sex') is not None:
            sex = request.args.get('sex')
        msg = {"code": 1, "id": id, "sex": sex}
        return msg


# 需要请求头的post请求 ------------------------------勿动
@app.route('/post/with/headers', methods=["post"])
def index3():
    if not request.data:  # 检测是否有数据
        return {"errcode": -1, "msg:": "请求数据不存在！"}

    # 定义接口需要的请求头
    result_headers = {"Authorization": "test_token",
                      "Content-Type": "application/json"}

    # 校验用户请求头是否等于定义接口定义的请求头
    req_headers = dict(request.headers)  # 将用户请求转成字典
    for key in result_headers:
        if (key in req_headers) & (req_headers[key] == result_headers[key]):
            return {"code": 1, "msg:": "你已经携带了所需要的请求头！"}
        else:
            return {"errcode": 4001, "errmsg:": "请求头有误！请检查"}



# 测试依赖
@app.route("/yilai", methods=["post"])
def ryj():
    if not request.data:  # 检测是否有数据
        return {"errcode": -1, "msg:": "请求数据不存在！"}
    res = {"msg": "success", "statues": 144}
    print(request.values)
    return res




# 测试返回的接口
@app.route('/test/response', methods=['get'])
def t1():
    res1 = '{"msg": "success", "statues": 144}'   # 返回类型为str;Response Headers的Content-Type为text/html; charset=utf-8
    res2 = {"msg": "success", "statues": 144}  # 返回类型为str;Response Headers的Content-Type为application/json; charset=utf-8
    res3 = {'msg': 'success', 'statues': 144} # 返回类型为str;Response Headers的Content-Type为application/json; charset=utf-8
    res4 = jsonify(res2) # 返回类型为str;Response Headers的Content-Type为application/json; charset=utf-8

    return res4



if __name__ == "__main__":
    app.run(port=1234, debug=True)


    """
    # 随便定义个json字典
    dic={"a":1,"b":2,"c":"你好"}
    @app.route('/jsonify')
    def jsonifys():
        # Content-Type: application/json
        return jsonify(dic)
     
    @app.route('/jsondumps')
    def jsondumps():
        # Content-Type: text/html; charset=utf-8
        return json.dumps(dic,ensure_ascii=False)
    """