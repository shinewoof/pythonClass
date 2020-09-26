from flask import Flask
from flask import request
from flask import Response
import json

app = Flask(__name__)


@app.route("/")  # 就是一般而言的首頁
def hello():
    return "Hello, World!"


@app.route("/get", methods=["GET"])
def testGet():
    reqArgs = dict(request.args)
    reqHeader = dict(request.headers)

    response = {}
    response['args'] = reqArgs
    response['hears'] = reqHeader
    response['origin'] = request.headers.get(
        'X-Forwarded-For', request.remote_addr)
    response['url'] = request.url

    return Response(
        status=200,
        response=json.dumps(
            response,
            indent=4),
        mimetype="application/json"
    )


@app.route("/post", methods=["POST"])
def testPost():
    reqArgs = dict(request.args)
    reqHeader = dict(request.headers)

    response = {}
    response['args'] = reqArgs
    response['data'] = ''
    response['hears'] = reqHeader
    response['origin'] = request.headers.get(
        'X-Forwarded-For', request.remote_addr)
    response['url'] = request.url+'?'

    reqPostData = ''
    if(reqHeader['Content-Type']=='application/json'):
        reqPostData = request.get_json()
    elif(reqHeader['Content-Type']=='text/plain'):
        reqPostData = str(request.get_data())
    else:
        return "Content-Type error", 415

    response['data'] = reqPostData
    print(request.get_json())

    return Response(
        status=200,
        response=json.dumps(
            response,
            indent=4),
        mimetype="application/json"
    )





if __name__ == "__main__":
    print("Start server")

    host = "localhost"
    port = 3456

    app.run(host=host, port=port, debug=True)
    print("Server shutdonw")
