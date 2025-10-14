from flask import Flask
import webbrowser

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    # Abre el navegador automáticamente en la URL
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=True)
