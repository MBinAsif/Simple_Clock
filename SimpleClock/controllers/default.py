# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------
import datetime

def index():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return dict(current_time=current_time)

def get_time():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return response.json(dict(current_time=current_time))
