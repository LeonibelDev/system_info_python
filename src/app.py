from flask import Flask, render_template
from main import get_system_data

app = Flask(__name__, template_folder='views')

@app.route('/', methods=['GET'])

def home():
    system_info = get_system_data()
    
    return render_template('index.html', data=system_info)

if __name__ == '__main__':
    app.run(port=8080, debug=True)
