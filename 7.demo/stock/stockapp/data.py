#!/usr/bin/env python3
#coding=utf-8

import tushare as ts

def stock_A():
    df = ts.get_realtime_quotes('sh')
    return df


def stock_company(code):
    code = str(code)
    df = ts.get_realtime_quotes(code)
    return df
