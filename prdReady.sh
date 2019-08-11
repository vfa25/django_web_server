#!/bin/bash

set -e

static_root="STATIC_ROOT = os.path.join(BASE_DIR, 'static')"

# 修改生产环境配置
sed -i "/STATIC_ROOT/c ${static_root}" djangoServer/settings.py
sed -i "s/DEBUG[ ]*=.*/DEBUG = False/g" djangoServer/settings.py

# 导入个人信息
file="djangoServer/myconfig.py"
if [ ! -f "$file" ]; then
  cp ../conf/django/myconfig.py ./djangoServer/
fi
# 静态文件归并
if [ ! -d "static" ]; then
 mkdir -p static
 python manage.py collectstatic
fi
