#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : microfat
# @time   : 09/12/20 08:40:59
# @File   : app.py

'''
Test Request object's attributes and methods
'''

from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/<path:name>', methods=['GET', 'POST'])
def gen(name):
    print('------------------')
    print(name)
    print('path      :', request.path)
    print('full_path :', request.full_path)
    print('host      :', request.host)
    print('host_url  :', request.host_url)
    print('base_url  :', request.base_url)
    print('url       :', request.url)
    print('url_root  :', request.url_root)
    print('args      :', request.args)
    print('blueprint :', request.blueprint)
    print('cookies   :', request.cookies)
    print('data      :', request.data)
    print('endpoint  :', request.endpoint)
    print('files     :', request.files)
    print('form      :', request.form)
    print('values    :', request.values)
    print('get_data  :', request.get_data(cache=True, as_text=False, parse_form_data=False))
    print('get_json  :', request.get_json(force=False, silent=False, cache=True))
    print('headers   :', request.headers)
    print('is_json   :', request.is_json)
    print('json      :', request.json)
    print('method    :', request.method)
    print('referrer  :', request.referrer)
    print('scheme    :', request.scheme)
    print('user_agent:', request.user_agent)
    return 'ok'