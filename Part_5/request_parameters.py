import sanic

app = sanic.Sanic()

#'app', 'args', 'body', 'clear', 'content_type', 'cookies', 'copy', 'files', 'form', 'fromkeys', 'get', 'headers', 'host', 'ip', 'items', 'json', 'keys', 'load_json', 'match_info', 'method', 'parsed_args', 'parsed_files', 'parsed_form', 'parsed_json', 'path', 'pop', 'popitem', 'port', 'query_string', 'raw_args', 'raw_url', 'remote_addr', 'scheme', 'setdefault', 'socket', 'stream', 'token', 'transport', 'update', 'uri_template', 'url', 'values', 'version'

@app.route("/")
async def index(request):
	print(dir(request))
	return sanic.response.text("OK")

@app.route("/url")
async def index_url(request):
	return sanic.response.text("The url was: {}".format(request.url))

@app.route("/qstring")
async def index_qstring(request):
	return sanic.response.text("The query string was: {}".format(request.query_string))


if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 8080)