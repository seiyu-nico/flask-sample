from flask import Flask
from apis.views.hoge import hoge_module
from apis.views.foo import foo_module

app = Flask(__name__)

app.register_blueprint(hoge_module)
app.register_blueprint(foo_module)


print(f'__name__: {__name__}')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
