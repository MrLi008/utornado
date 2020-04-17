# coding=utf-8
"""
:func
:author MrLi008
:data: 

"""
import sys, os, json, io

bsdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(bsdir)

# tornado
import tornado.web as tweb
import tornado.ioloop as tIO

from tornado.httpserver import HTTPServer

from requesthandle import webhttp,websocket


urls_index = list()
port = 8000
host = '0.0.0.0'


class IndexHandle(tweb.RequestHandler):
    def get(self):
        self.render('index.html', urls=urls_index)


def loadurl():
    """
    根据制定的规则,自动加载满足条件的handle
    """
    
    def loadurl_(pkgname, modelname_, classname_):
        urllist = set()
        urlvisit = set()
        hlist = __import__(pkgname).__dict__.get('__all__')
        if not hlist:
            return []
        for h in hlist:
            for modelname, val in __import__('.'.join([pkgname, h])).__dict__.items():
                if modelname_ in modelname:
                    for classname, v in val.__dict__.items():
                        
                        if classname_ not in classname:
                            continue
                        name = '{modelname}_{classname}'.format(classname=classname, modelname=modelname)
                        if name in urlvisit:
                            continue
                        
                        if issubclass(v, (webhttp, websocket)):
                            tip = v.tip
                        else:
                            tip = "default.html"
                        urlvisit.add(name)
                        url = ''.join([r'/', classname.lower()])
                        urllist.add(tweb.url(url, v, name=name))
                        urls_index.append([url, name, tip])
        return [url for url in urllist]
    
    urllist = loadurl_('handle', 'handle', 'Handle')
    urllist.append((r'/', IndexHandle))
    # [print('http://localhost:{port}{url}'.format(port=port, url=url))
    #  for url, _h in urllist]
    print('http://{host}:{port}/'.format(host=host, port=port))
    print('http://localhost:{port}/'.format(port=port))
    
    return urllist


urls = loadurl()


def config():
    configuration = {
        'template_path'    : '/'.join([bsdir, 'templates']),
        'static_path'      : '/'.join([bsdir, 'static']),
        'autoreload'       : False,
        'static_hash_cache': False,
        'max_body_size'    : 1024 ** 3 * 5
    }
    
    return tweb.Application(urls, **configuration)


def main():
    app = config()
    app.listen(port=port, address=host)
    tIO.IOLoop.instance().start()


if __name__ == '__main__':
    main()
