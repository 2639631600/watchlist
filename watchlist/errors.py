# -*- coding: utf-8 -*-
from flask import render_template

from watchlist import app


@app.errorhandler(404)  # errorhandler翻译为“错误处理器” 传入要处理的错误代码
def page_not_found(e):  # e 接受异常对象作为参数
    return render_template('404.html'), 404  # 返回模板和状态码
