from . import calc
from flask import render_template, request
import re


@calc.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# 返回计算结果的API
@calc.route('/api/getresult', methods=['POST'])
def get_calc_result():
    data = request.get_json()
    expr_val = data['expr']
    return str(eval(expr_val))

