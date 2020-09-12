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
    print('\033[1;33;44mpath      :\033[0m', request.path)
    print('\033[1;33;44mfull_path :\033[0m', request.full_path)
    print('\033[1;33;44mhost      :\033[0m', request.host)
    print('\033[1;33;44mhost_url  :\033[0m', request.host_url)
    print('\033[1;33;44mbase_url  :\033[0m', request.base_url)
    print('\033[1;33;44murl       :\033[0m', request.url)
    print('\033[1;33;44murl_root  :\033[0m', request.url_root)
    print('\033[1;33;44margs      :\033[0m', request.args)
    print('\033[1;33;44mblueprint :\033[0m', request.blueprint)
    print('\033[1;33;44mcookies   :\033[0m', request.cookies)
    print('\033[1;33;44mdata      :\033[0m', request.data)
    print('\033[1;33;44mendpoint  :\033[0m', request.endpoint)
    print('\033[1;33;44mfiles     :\033[0m', request.files)
    print('\033[1;33;44mform      :\033[0m', request.form)
    print('\033[1;33;44mvalues    :\033[0m', request.values)
    print('\033[1;33;44mget_data  :\033[0m', request.get_data(cache=True, as_text=False, parse_form_data=False))
    print('\033[1;33;44mget_json  :\033[0m', request.get_json(force=False, silent=False, cache=True))
    print('\033[1;33;44mheaders   :\033[0m', request.headers)
    print('\033[1;33;44mis_json   :\033[0m', request.is_json)
    print('\033[1;33;44mjson      :\033[0m', request.json)
    print('\033[1;33;44mmethod    :\033[0m', request.method)
    print('\033[1;33;44mreferrer  :\033[0m', request.referrer)
    print('\033[1;33;44mscheme    :\033[0m', request.scheme)
    print('\033[1;33;44muser_agent:\033[0m', request.user_agent)
    return 'ok'