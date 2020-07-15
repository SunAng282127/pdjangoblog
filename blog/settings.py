import django_heroku
import os

django_heroku.settings(locals())

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 设置静态路径STATIC_ROOT
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# 修改ALLOWED_HOSTS
ALLOWED_HOSTS = ['pdjangoblog.herokuapp.com']
