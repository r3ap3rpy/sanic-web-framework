import sanic

app = sanic.Sanic()

@app.route("/", name = "index")
async def index(request):
	return sanic.response.text("Everything was OK!")

@app.route("/test")
async def test(request):
	return sanic.response.redirect(app.url_for('index'))

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 8080)