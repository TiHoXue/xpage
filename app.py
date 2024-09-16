from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def homepage():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>xueth's homepage</title>
        <style>
            body {
                font-family: Cascadia Code, monospace;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: black;
            }
            .content {
                font-size: 24px;
                text-align: center;
                color: white;
            }
        </style>
    </head>
    <body>
        <div class="content">
            <h1>xueth's homepage</h1>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
