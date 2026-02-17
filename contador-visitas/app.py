import os
from flask import Flask
import redis

app = Flask(__name__)

redis_client = redis.Redis(host='db', port=6379, db=0)

@app.route('/')
def hello():
 try:
 visits = redis_client.incr('counter')
 except redis.ConnectionError:
 return "ERROR: No puedo conectar con Redis. Revisa el nombre del host."

 html = f"<h3>¡Hola!</h3>" \
 f"<b>Visitas:</b> {visits} <br/>" \
 f"<b>Servidor:</b> {os.getenv('HOSTNAME')}"
 return html
if __name__ == "__main__":
 app.run(host="0.0.0.0", port=5000)