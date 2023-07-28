try:
    from app import app
except Exception as e:
    print('Ошибка при попытке импорта из app.py: {}'.format(e))

if __name__ == '__main__':
    app.run()
