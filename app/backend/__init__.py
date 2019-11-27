from flask import Flask

from config import config


# app工厂函数
def create_app(config_name):
    app = Flask(__name__,
                static_folder='../dist/static',
                template_folder='../dist')

    # load config
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # init flask module

    # register blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')

    return app
