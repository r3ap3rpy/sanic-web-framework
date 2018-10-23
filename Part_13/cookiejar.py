import sanic

app = sanic.Sanic()

@app.route("/expose")
async def expose(request):
	return sanic.response.text(request.cookies.get('testcookie'))


@app.route("/set")
async def set_cookie(request):
	response = sanic.response.text("It is working!")
	response.cookies['test'] = 'Its the test cookie'
	response.cookies['test']['domain'] = 'localhost'
	response.cookies['test']['httponly'] = True
	return response

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 8080)
	