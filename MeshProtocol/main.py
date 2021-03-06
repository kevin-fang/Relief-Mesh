from gevent import monkey;monkey.patch_all()
from app import create_app, socketio
from platform import system as st
import Socket
import PIController
import Controller
import sys


def main():

    app = create_app(True)

    option = sys.argv[1] if len(sys.argv) >= 2 else 'client'

    if option == 'server':
        Controller.server = True
    elif option == 'client':
        Controller.start_streamer()
    elif option == 'rpi':
        Controller.start_streamer()
        PIController.start()
    elif option == 'bridge':
        Controller.start_streamer()
        PIController.start()
        PIController.start_nrf()

    host = '0.0.0.0' if option != 'rpi' else '192.168.1.1'
    socketio.run(app, host=host, port=8080 if st() == 'Darwin' else 80, debug=True, use_reloader=False)

if __name__ == '__main__':
    main()
