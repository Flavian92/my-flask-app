# app.py
import psutil
from flask import Flask
app = Flask()
@app.route('/')
def index():
    cpu_percent = psutil.cpu_percent
    mem_percent = psutil.virtual_memory().percent
    Message = None
    if cpu_percent > 80 or mem_percent > 80:
        Message = "High uttilization, please scale up"
        return f"CPU uttilization: {cpu_percent} ADN mEMEORY uTTILIZATION: {mem_percent}"


if __name__ == '__main__':
    app.run(debug=TRUE, host='0.0.0.0')