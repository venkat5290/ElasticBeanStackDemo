from flask import Flask

application = Flask(__name__)


@application.route('/',methods=['GET'])
def home():
    return "This is test website"


if __name__ == '__main__':
    application.run(debug=True)
