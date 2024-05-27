# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Dummy Test in DevOps in 'features' branch"

# La siguiente línea comprueba si el archivo app.py está siendo ejecutado directamente
# (es decir, no está siendo importado como un módulo en otro script).
if __name__ == "__main__":
    # Si el archivo se está ejecutando directamente, Flask inicia un servidor web local
    # que escucha en todas las interfaces de red ('0.0.0.0') en el puerto 5000.
    app.run(host='0.0.0.0', port=5000)
