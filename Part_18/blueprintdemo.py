import sanic

bp = sanic.Blueprint('Blue Print demo')

@bp.route("/")
async def index(request):
	return sanic.response.text("Response from the blueprint!")


@bp.middleware('request')
async def mwprocessor(request):
	print("Processing request with blueprint middleware!")

@bp.listener('before_server_start')
async def befservstart(app, loop):
	print('Using the listener before_server_start from blueprint!')


app = sanic.Sanic()
app.blueprint(bp)

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 8080)