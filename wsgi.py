from flask import Flask
import urllib2
application = Flask(__name__)


@application.route("/<string:test>/")
def hello(test):
    request = urllib2.Request("http://{}/web/services/students".format(test))
    request.add_header('content-TYPE', 'application/x-www-form-urlencoded')
    response = urllib2.urlopen(request)
    return response.read()


if __name__ == "__main__":
    application.run()
