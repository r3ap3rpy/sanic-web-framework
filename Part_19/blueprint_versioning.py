import sanic

bp_version1 = sanic.Blueprint('version1', url_prefix = '/v1')
bp_version2 = sanic.Blueprint('version2', url_prefix = '/v2')

@bp_version1.route('/generate')
async def generate(request):
	return sanic.response.text('OK from version 1')


@bp_version2.route('/generate')
async def generate(request):
	return sanic.response.text('OK from version 2')

if __name__ == '__main__':
	app = sanic.Sanic()
	app.blueprint(bp_version1)
	app.blueprint(bp_version2)

	app.run(host = '0.0.0.0', port = 8080)
