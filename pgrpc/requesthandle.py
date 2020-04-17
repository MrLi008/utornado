# coding=utf-8
"""
MyRequestHandle
@author MrLi008
@data 
"""

import sys, os, codecs, json

bsdir = os.path.dirname(os.path.abspath(__file__))
if bsdir not in sys.path:
    sys.path.append(bsdir)
import tornado.web as tweb
import tornado.websocket as twebsocket
from tornado import gen
from tornado.concurrent import run_on_executor
from concurrent import futures

# 全局工具类加载


# 常量库
const = {
    'domain': 'localhost:8000'
}


class webhttp(tweb.RequestHandler):
    """
    基础类-http请求
    """
    # 实例化 工具类以及数据库
    
    # 全局共享变量
    executor = futures.ThreadPoolExecutor(max_workers=10)
    # 用户标记
    cookie_user_info = 'cookie_user_info'
    # get 请求默认需要渲染的数据 可通过self.context()
    _context = {
        'const': const
    }
    # 接口提示信息
    tip = 'webhttp'
    # get 请求访问页面
    defhtml = 'index.html'
    
    def _process(self, *args, **kwargs):
        # post 请求数据处理
        return ''
    
    def context(self):
        """
        get 请求数据渲染
        :return:
        """
        pass
    
    @run_on_executor
    def process(self):
        return self._process()
    
    @gen.coroutine
    def post(self, *args, **kwargs):
        res = yield self.process()
        if not res:
            print('in webhttp')
            return
        if isinstance(res, list):
            print('not support list')
            return
        
        self.write(res)
    
    def get(self, *args, **kwargs):
        self.context()
        self.render(self.defhtml, **self._context)


class websocket(twebsocket.WebSocketHandler):
    """
    基础类-websocket 请求
    """
    # 实例化 工具类以及数据库
    
    # 全局共享变量
    executor = futures.ThreadPoolExecutor(max_workers=10)

    # 用户标记
    cookie_user_info = 'cookie_user_info'
    # get 请求默认需要渲染的数据
    _context = {}
    
    def _on_message(self, message):
        # websocket 请求数据处理
        return ''
    
    def on_message(self, message):
        self.write_message(self._on_message(message))
    
    def on_close(self):
        print('close')
    
    def check_origin(self, origin):
        return True

