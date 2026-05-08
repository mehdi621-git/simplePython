from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "message": "Python Pipeline is working successfully!",
        "version": "1.0.0"
    })

if __name__ == '__main__':
    # Running on 0.0.0.0 makes it accessible on a network/server
    app.run(host='0.0.0.0', port=5000)