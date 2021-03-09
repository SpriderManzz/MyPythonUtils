# 设计思路
* 采用Python3+Requests+Excel(demo是自己Mock的接口)  
* 该框架分为：显示层、用例层、逻辑层、工具层、配置层  
显示层：测试报告  
用例层：存放测试用例  
逻辑层：进行取数和写入的封装  
工具层：含各种封装的方法,可简化代码的书写  
配置层：用于配置基础数据



# 运行
* IDE工具直接执行main包下的go_on_run方法即可
* 命令执行需要在run_main模块下手动添加项目路径

# 测试报告
可在配置文件ismail字段设置是否需要发送测试报告


# base包
* run_method.py       基础Get和Post请求的封装类

# cases文件夹
用于存放测试用例Excel

# data包
* data_config.py      存放Excel测试用例的列号  
* get_data.py         获取Excel单元格方法的封装类(里面有含写入Excel的方法)

# 工具包
* get_path.py         获取路径工具类
* opera_excel.py      操作Excel工具类
* opera_json.py       操作json工具类
* send_email.py       发送邮箱工具类
* read_config.py      读取配置文件工具类
* config_data.py      config配置的信息
* common_util.py      存放一些公共方法的工具类
* log.py              日志工具类
* connect_db.py       数据库工具类

# config.ini配置文件
* 1、配置一些常量,例如Excel表格的列、接口、邮件、数据库的相关信息
* 2、在测试过程中发现有些项目的有公共的path，所以写一个配置来读取公共path，减少测试用例中url地址的长度(为了美观)  
    (Excel测试用例想要完整的URL展示，在run_main()方法下注释url = base_url+url即可)
* isemail邮件开关--True代表开启邮件功能,False代表关闭邮箱功能

# 环境模块说明
* python==3.8.1,解释器环境
* requests==2.25.1,模拟用户发送http协议get或者post类型请求
* xlrd==2.0.1,读取excel表格数据
* json,对服务器返回的字符串转换为字典，方便做断言
* os,获取路径
* sys,设置环境变量
* pymysql==1.2.3,操作数据库
* smtplib,操作邮箱

# 函数助手
* assert_dict(expected,result):预期结果与实际结果字典的比较
* bm_get_int(n):生成长度为n的随机整数
* bm_get_str(n):生成长度为n的随机字符串

# 后续优化点
* 解决测试数据依赖
* demo的接口用SpringBoot或者Django实现，方便逻辑判断  
* 考虑是否需要预期结果与数据库进行对比
* 预期结果的写法后续优化成dict，进行键值对的比较(原本为字符串比较)--已优化
* 实现各种方法供测试数据准备用，如：生成随机数，随机字符串等--已实现
* 找一套或者开发自己开源的web项目，实用文本进行测试脚本的编写，及把日志呈现出来，
* 后续使用jenkins集合rancher进行打包及升级--jenkins已实现

# 更新日志
* 新增配置文件
* 新增日志类
* 新增数据库工具类
* 202103/08 调整请求封装类
* 202103/08 调整预期结果与实际结果的判断逻辑
* 202103/09 新增请求参数的value可调用函数随机生成
