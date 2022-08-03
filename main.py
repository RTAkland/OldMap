#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/8/4
# @File Name: main.py

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get('/')
async def index():
    """
    Index page
    :return:
    """
    return RedirectResponse(url="https://s4.s100.vip:8123", status_code=302)

