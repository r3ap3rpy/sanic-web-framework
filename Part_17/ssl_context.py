import ssl
import sanic

app = sanic.Sanic()

context = ssl.create_default_context(purpose = ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(r"C:\Users\Cyber\Desktop\SanicWebFrameWork\Part_17\certificate.crt", keyfile = r"C:\Users\Cyber\Desktop\SanicWebFrameWork\Part_17\private.key")

@app.route("/")
async def index(request):
	return sanic.response.text("OK")

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 443, ssl = context)