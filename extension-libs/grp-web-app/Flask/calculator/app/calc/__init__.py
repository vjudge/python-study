from flask import Blueprint

# 通过实例化一个 Blueprint 类对象，创建蓝本。
print('__name__')
calc = Blueprint('calc', __name__)

from . import views