from gevent import monkey;monkey.patch_all()
from app import create_app, socketio
from platform import system as st
import Socket
import Controller
import sys


def main():

    app = create_app(True)

    if not len(sys.argv) >= 2 or sys.argv[1] != 'server':
        print('running streamer')
        Controller.start_streamer()
    else:
        Controller.server = True

    socketio.run(app, host='0.0.0.0', port=8080 if st() == 'Darwin' else 80, debug=True, use_reloader=False)
if __name__ == '__main__':
    main()
