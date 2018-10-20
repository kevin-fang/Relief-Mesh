from app import create_app, socketio
from platform import system as st
import Socket
import Controller


def main():

    app = create_app(True)
    Controller.start_streamer()
    socketio.run(app, host='0.0.0.0', port=8080 if st() == 'Darwin' else 80, debug=True, use_reloader=False)
if __name__ == '__main__':
    main()
