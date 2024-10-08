from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def get_pod_info():
    pod_name = os.getenv('POD_NAME', 'Unknown')
    node_name = os.getenv('NODE_NAME', 'Unknown')
    namespace = os.getenv('POD_NAMESPACE', 'Unknown')
    
    return f"Container EDU | POD Working : {pod_name} | nodename : {node_name} | namespace : {namespace}\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
