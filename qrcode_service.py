# coding=utf8

import qrcode

import StringIO
from nameko.rpc import rpc
import qiniu
import tempfile



ACCESS_KEY = "abc"
SECRET_KEY = "def"

q = qiniu.Auth(ACCESS_KEY, SECRET_KEY)

class QRCodeService(object):
    name = "qrcode_service"

    @rpc
    def serve(self, data):
        img = qrcode.make(data)
        token = q.upload_token('daixm-app')
        buff = StringIO.StringIO()
        img.save(buff)
        buff.seek(0)
        ret, error = qiniu.put_data(token,
            '/microservice/qrcode_service/test1.png', buff)
        buff.close()
        if ret:
            return ret['key']
        else:
            return error


if __name__ == "__main__":
    test('http://www.douban.com')
