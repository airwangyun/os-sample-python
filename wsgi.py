from flask import Flask
import urllib3
application = Flask(__name__)


@application.route("/<string:test>/")
def hello(test):
    http = urllib3.PoolManager()
    request = http.request("GET", "http://{}/web/services/students".format(test))
    # print(request.data.decode())

    return request.data.decode()


if __name__ == "__main__":
    application.run()
