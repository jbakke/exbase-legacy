#!/usr/bin/env python

import tornado

tornado.options.define("port", default=8888, help="run on the given port", type=int)

class ExbaseLegacy(tornado.web.Application):
    pass

class BaseHandler(tornado.web.RequestHandler):
    pass

class ArticleHandler(BaseHandler):
    def get(self, id):
        self.write('you requested article %s' % id)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = ExbaseLegacy([
        (r"/", RootHandler),
        (r"/article/(.*)+", ArticleHandler)
    ])
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()