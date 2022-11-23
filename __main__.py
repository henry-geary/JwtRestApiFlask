from __init__ import create_app
from dotenv import load_dotenv

app = create_app()


if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True, port=4000, host="0.0.0.0")
