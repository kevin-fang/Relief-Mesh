from app import create_app, socketio


def main():

    app = create_app()
    socketio.run(app, host='0.0.0.0', port=8080, debug=True)


if __name__ == '__main__':
    main()
