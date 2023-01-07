from sanic import Sanic
from sanic.response import json, text
from model import global_token

import os
import importlib

app = Sanic(__name__)

@app.route('/')
async def index(request):
    return text('CallBack Gateway 0.1')


ret = {
    'code': 0,
    'msg': '',
    'triggered': {
        'bash': 0,
        'python': 0
    }
}

@app.post('/<api>')
async def call(request, api):
    bash_fn = f'./plugin/{api}/main.sh'
    py_fn = f'./plugin/{api}/main.py'
    res = ret.copy()
    fd = False
    if os.path.exists(bash_fn):
        print('Call => ' + bash_fn)
        os.system('bash ' + bash_fn)
        res['triggered']['bash'] = 1
        fd = True
    if os.path.exists(py_fn):
        try:
            print('Call => ' + py_fn)
            pyf = __import__(f'plugin.{api}.main', fromlist=[None])
            importlib.reload(pyf)
            res['msg'] = pyf.Plugin(global_token).execute(request.json)
        except Exception as e:
            res['msg'] = str(e)
        res['triggered']['python'] = 1
        fd = True
    
    if not fd:
        res['code'] = -1
        res['msg'] = 'Module not found'
    return json(res)
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)