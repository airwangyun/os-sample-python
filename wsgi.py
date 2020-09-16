from flask import Flask
import urllib3
application = Flask(__name__)


@application.route("/")
def hello():
    http = urllib3.PoolManager()
    request = http.request("GET", "http://common1.iinthecloud.com:10258/web/services/fromCity")
    # request = http.request("GET", "http://www.baidu.com")
    # print(request.data.decode())

    return request.data.decode()


@application.route("/test/test/")
def hello2():
    return "test"


if __name__ == "__main__":
    application.run()
