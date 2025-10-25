from flask import Flask,jsonify
import requests,os
from itertools import cycle


app=Flask(__name__)

servers=['http://127.0.0.1:5001', 'http://127.0.0.1:5002','http://127.0.0.1:8000']
server=cycle(servers)


@app.route('/')
def loadbalancer():
    server_data=next(server)
    copy=server_data
    try:
        return requests.get(server_data).text
    except:
        server_data=next(server)
        try:
            res=requests.get(server_data).text
            res+="  --   "+copy +" :     -- this server have error"
            return res
        except:
            return "server {server_data} have error"
        

port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)
