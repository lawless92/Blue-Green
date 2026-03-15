import os
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        color = os.getenv('APP_COLOR', 'blue')
        html = f"<html><body style='background-color: {color}; color: white; text-align: center; font-family: sans-serif; margin-top: 50px;'>" \
               f"<h1>¡Hola desde el entorno {color.upper()}!</h1>" \
               f"<p>Esta es mi simple app en Python para la tarea Blue-Green.</p>" \
               f"</body></html>"
        self.wfile.write(html.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=SimpleHandler, port=80):
    server_address = ('0.0.0.0', port)
    httpd = server_class(server_address, handler_class)
    print(f"Iniciando servidor en el puerto {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
