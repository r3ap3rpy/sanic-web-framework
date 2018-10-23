import sanic

app = sanic.Sanic()

app.config.from_envvar('MY_CONFIG')

# set MY_CONFIG=app.conf

@app.route("/<parameter>")
async def index(request,parameter):
	return sanic.response.text("The value of parameter: {}, is {}!".format(parameter, app.config.get(parameter,'N.A.')))

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 8080)