import sanic
from sanic import response
app = sanic.Sanic()

@app.route("/")
async def streamer(request):
	async def stream_response(response):
		for i in range(10):
			await response.write(str(i) + ' ')
	return response.stream(stream_response,content_type = "text/plain")

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 8080)