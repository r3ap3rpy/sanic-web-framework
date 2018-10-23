import sanic

app = sanic.Sanic()

@app.route("/get", methods = ['GET'])
async def get_context(request):
	return sanic.response.text("Hit was with GET!")

@app.route("/post", methods = ['POST'])
async def pot_context(request):
	return sanic.response.text("Hit was with POST!")

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 8080)
