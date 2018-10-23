import sanic

app = sanic.Sanic()

@app.route("/serve_file/<file_name>")
async def serve_file_small(request, file_name):
	return await sanic.response.file(r'.\{}'.format(file_name))


@app.route("/stream_file/<file_name>")
async def stream_file_big(request, file_name):
	return await sanic.response.file_stream(r'.\{}'.format(file_name))


if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 8080)