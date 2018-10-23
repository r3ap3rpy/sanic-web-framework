import sanic

app = sanic.Sanic()

@app.listener('before_server_start')
async def bst(app, loop):
	print('This is the before server start listener!')

@app.listener('after_server_start')
async def ast(app, loop):
	print('This is the after server start listener!')

@app.listener('before_server_stop')
async def bsst(app, loop):
	print('This is the before server stop listener!')

@app.listener('after_server_stop')
async def asst(app, loop):
	print('This is the after server stop listener!')

@app.route("/")
async def index(request):
	return sanic.response.text("OK")


if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 8080)