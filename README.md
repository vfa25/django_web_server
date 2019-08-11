# django_web_server

```sh
# 依赖包安装（建议先创建虚拟环境）
pip3 install -r requirements.md
# 加入全局变量配置，见下文：
vi djangoServer/myconfig.py
# 本地启动
python3 manage.py runserver
```

- 个人敏感信息文件：

```md
# djangoServer/myconfig.py
my_config = {
    'MYSQL_HOST': '数据库host',
    'MYSQL_DBNAME': '数据库名',
    'MYSQL_USER': '数据库登录账号',
    'MYSQL_PASSWORD': '密码',
    'MYSQL_PORT': 3306
}

EMAIL_HOST_USER = '邮箱账号'
EMAIL_HOST_PASSWORD = '密码'

YUNPIAN_API_KEY = '云片网（第三方短信提供商）KEY'
```

- 线上环境预配置

```sh
sh prdReady.sh
```
