from sanic import Sanic
from sanic.response import text

# Criar uma instância do aplicativo Sanic
app = Sanic(__name__)

# Definir uma rota que responde a solicitações GET na raiz ("/") com "Hello, World!"
@app.route("/")
async def hello(request):
    return text("Hello, World!")

# Verificar se o script está sendo executado diretamente e iniciar o servidor
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)