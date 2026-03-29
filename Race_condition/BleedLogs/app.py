import os
import time
from flask import Flask, request, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

LOGS_DIR = os.path.abspath("./logs/")
FLAG_FILE = os.path.abspath("./flag.txt")

shared_data = {
    "current_path": ""
}


@app.route('/')
def landing():
    return render_template('landing.html')
    
@app.route("/console")
def pab_console():
    return render_template("lab.html")

@app.route('/view')
def view_log():
    global shared_data
    filename = request.args.get('file')

    if not filename:
        return "Error: No file specified", 400
        

    target_path = os.path.abspath(os.path.join(LOGS_DIR, filename))
    shared_data["current_path"] = target_path
    
    print(f"\n[+] Processing: {target_path}")

    if not target_path.startswith(LOGS_DIR):
        return "Access Denied: Invalid Path", 403

    if not os.path.exists(target_path):
        return "File not found", 404

    final_path = shared_data["current_path"]
    
    try:
        with open(final_path, 'r') as f:
            content = f.read()
        return content
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=False)
