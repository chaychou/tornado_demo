# -*- coding: utf-8 -*-
# @Time    : 2019/6/9 17:26
# @Author  : zhouchunyuan
# @Email   : zhouchunyuan@sina.cn
# @File    : app.py
# @Software: PyCharm

import tornado.httpserver
import tornado.ioloop
import tornado.web

from handlers import user as user_handlers

HANDLERS = [
    (r'/api/users', user_handlers.UserListHandler)
]


def run():
    app = tornado.web.Application(
        HANDLERS,
        debug=True,
    )
    http_server = tornado.httpserver.HTTPServer(app)
    port = 8888
    http_server.listen(port)
    print('server start on port: {}'.format(port))
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    run()
