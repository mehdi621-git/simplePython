from flask import Flask, render_template_string, request

app = Flask(__name__)

# Simple modern UI template using HTML + CSS
TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>My Simple Web App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            background: linear-gradient(135deg, #6a11cb, #2575fc);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .card {
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            width: 350px;
            text-align: center;
        }
        h1 {
            color: #333;
        }
        input {
            width: 90%;
            padding: 10px;
            margin-top: 10px;
            border-radius: 8px;
            border: 1px solid #ccc;
        }
        button {
            margin-top: 15px;
            padding: 10px 20px;
            border: none;
            border-radius: 8px;
            background: #2575fc;
            color: white;
            cursor: pointer;
        }
        button:hover {
            background: #1a5edb;
        }
        .result {
            margin-top: 20px;
            font-size: 18px;
            color: #444;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>Welcome 👋</h1>
        <form method="POST">
            <input type="text" name="name" placeholder="Enter your name" required>
            <button type="submit">Subsmit</button>
        </form>
        {% if name %}
        <div class="result">Hello, <b>{{ name }}</b> 🚀</div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    name = None
    if request.method == 'POST':
        name = request.form.get('name')
    return render_template_string(TEMPLATE, name=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
