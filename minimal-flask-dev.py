from flask import Flask
import ssl

app = Flask(__name__)

@app.route('/ping')
def ping():
    return 'pongers'

if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.verify_mode = ssl.CERT_REQUIRED
    context.load_verify_locations('ca-crt.pem')
    context.load_cert_chain('server.crt', 'server.key')
    app.run('0.0.0.0', 8080, ssl_context=context)
