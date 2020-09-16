from flask import Flask
from json2html import *
import urllib3

application = Flask(__name__)


@application.route("/")
def hello():
    http = urllib3.PoolManager()
    request = http.request("GET", "http://common1.iinthecloud.com:10258/web/services/fromCity")

    request2 = http.request("GET", "http://common1.iinthecloud.com:10258/web/services/ToCity")

    input = request.data.decode()

    input2 = request2.data.decode()

    outputhtml = "<br /><b>Flight information application running in OpenShift Container Platform " \
                 "with data retrieved from IBM i rest service.</b><br /><br />" \
                 "<table>" \
                 "<tr><th>From City</th><th>To City</th></tr>" \
                 "<tr><td>{}</td><td>{}</td></tr>" \
                 "</table>".format(json2html.convert(json=input), json2html.convert(json=input2))

    return outputhtml


@application.route("/test/test/")
def hello2():
    return "test"


if __name__ == "__main__":
    application.run()
