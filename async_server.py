# -*- coding: utf-8 -*-
# @Time    : 2019/6/7 23:33
# @Author  : zhouchunyuan
# @Email   : zhouchunyuan@sina.cn
# @File    : async_server.py
# @Software: PyCharm
import datetime as dt

import tornado.gen
import tornado.httpserver
import tornado.ioloop
import tornado.web


class SleepHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        # time.sleep(5)
        # self.write("when i sleep")
        yield tornado.gen.sleep(5)
        self.write(str(dt.datetime.now()))


if __name__ == '__main__':
    app = tornado.web.Application(
        [
            (r'/sleep', SleepHandler)
        ],
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8080)
    print('server start on 8080')
    tornado.ioloop.IOLoop.instance().start()
