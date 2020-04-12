from functool import wraps
from flask import request, g, abort
from jwt import decode,exceptions
from ../settings import SECRET_KEY

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        token = request.headers.get("authorization", None)
        if not token:
            return jsonify({"error":"no authorization token provied"}), 401
        try:
            data = decode(token, SECRET_KEY, verify=False, algorithms=['HS256'])
        except:
            return jsonify({"msg":"Token is invalid"}), 401
        return f(*args, **kwargs)
    return wrap
