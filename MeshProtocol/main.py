from app import create_app, socketio
from platform import system as st
import Socket


def main():

    app = create_app(True)
    socketio.run(app, host='0.0.0.0', port=8080 if st() == 'Darwin' else 80, debug=True)


if __name__ == '__main__':
    main()
