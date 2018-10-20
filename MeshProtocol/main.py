from app import create_app, socketio
import Socket

def main():
	app = create_app()
	socketio.run(app, host='0.0.0.0', port='8080')

if __name__ == '__main__':
	main()