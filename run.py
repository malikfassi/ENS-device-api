from App import App
import os

app = App()


def run():
    app.run('127.0.0.1', 5000)


if __name__ == '__main__':
    os.environ['WERKZEUG_RUN_MAIN'] = 'true'
    run()

