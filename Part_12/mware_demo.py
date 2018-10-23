import sanic

app = sanic.Sanic()

@app.route("/")
async def index(request):
	return sanic.response.text('Damn this middleware is cool!')

@app.middleware('request')
async def mwreqhandler(request):
	print('I got a new request to process!!!!')

@app.middleware('response')
async def mwresphandler(request, response):
	print('I got a new response to provide!')

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 8080)
	