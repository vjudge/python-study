# coding = utf-8

from app import create_app


if __name__ == '__main__':
    app = create_app()
    app.run(host='127.0.0.1', debug=True, port=8080)
