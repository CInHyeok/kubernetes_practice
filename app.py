from flask import Flask
import socket 


app = Flask(__name__)
hostname = socket.gethostname()
ip_address = (socket.gethostbyname(hostname))

@app.route("/whoareyou")
def hello():
    return "최인혁 : " + hostname + " : " + ip_address


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
    
    
    