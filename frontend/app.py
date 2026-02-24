from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hello CloudNexus</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            margin: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1e3c72, #2a5298);
            color: #ffffff;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }

        .card {
            background: rgba(255, 255, 255, 0.12);
            backdrop-filter: blur(10px);
            border-radius: 16px;
            padding: 50px 40px;
            text-align: center;
            max-width: 500px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        }

        h1 {
            font-size: 2.8rem;
            margin-bottom: 10px;
            color: #ffd369;
        }

        h2 {
            font-weight: 400;
            margin-bottom: 25px;
        }

        p {
            font-size: 1.05rem;
            line-height: 1.6;
            color: #e6e6e6;
        }

        .badge {
            display: inline-block;
            margin-top: 30px;
            padding: 10px 22px;
            background: #00c6ff;
            background: linear-gradient(135deg, #00c6ff, #0072ff);
            border-radius: 30px;
            font-weight: 600;
            letter-spacing: 0.5px;
        }

        footer {
            margin-top: 35px;
            font-size: 0.85rem;
            opacity: 0.85;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>Hello 👋</h1>
        <h2>Welcome to <strong>CloudNexus</strong></h2>

        <p>
            The application is successfully deployed and running in the cloud.
            This setup is designed to be scalable, secure, and production-ready.
        </p>

        <div class="badge">🚀 Powered by Flask</div>

        <footer>
            © 2026 CloudNexus | Cloud Innovation Hub
        </footer>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

