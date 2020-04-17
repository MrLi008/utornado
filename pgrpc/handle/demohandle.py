# coding=utf-8
'''
:func 
:author: MrLi
:date: 

'''
import sys
import os
import codecs
import json
from requesthandle import webhttp, websocket


class DemoWebHttpHandle(webhttp):
    tip = '演示demo'
    defhtml = 'demo.html'
    
    # 表单
    formdict = [
        {
            'name'       : 'name',  # post 参数名
            'inputtype'  : 'text',  # input 类型
            'label'      : 'name-label',  # label 提示
            'default-val': ''  # 默认值
        }, {
            'name'       : 'val',
            'inputtype'  : 'number',
            'label'      : 'name-number',
            'default-val': 0
        }
    ]
    
    def _process(self, *args, **kwargs):
        form = self.formdict.copy()
        for v in form:
            v['default-val'] = self.get_argument(v.get('name'))
        return {'res': form}
    
    def context(self):
        self._context = {
            'msg'     : 'This is a demo',
            'formdict': self.formdict
        }


class DemoWebSocketIndexHandle(webhttp):
    defhtml = 'demowebsocket.html'
    tip = '演示 websocket'


class DemoWebSocketHandle(websocket):
    tip = 'websocket 数据接收接口'
    
    def _on_message(self, message):
        return 'receive: {}'.format(message)
