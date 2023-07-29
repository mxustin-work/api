try:
    from flask import Flask
    from flask_restful import Api as API, Resource
except Exception as e:
    print('Ошибка при попытке импорта библиотек: {}'.format(e))

app = Flask('REST API Application')
api = API(app)


class Hello(Resource):

    def __int__(self):
        # Добавить реальный функционал
        pass

    def get(self):  # noqa
        return {
            'message': '👋 Hello there! 🔋 Everything works fine! ',
            'code': 200
        }


api.add_resource(Hello, 'bank/api/v1/usns/cifra-ibsmb-gw/hello')

if __name__ == '__main__':
    app.run(debug=True)
