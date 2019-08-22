from flask import Flask, request, render_template, redirect


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/noticias")
@app.route("/noticias/<pais>")
@app.route("/noticias/<pais>/<estado>")
def lista_de_noticias(pais=None, estado=None):
    retorno = ''
    if pais:
        retorno = f"\nVoce digitou o pais: {pais}"
    if estado:
        retorno += f"\nVoce digitou o estado: {estado}"
    return retorno


@app.route('/loteria/<int:numero>')
def loteria(numero):
    if numero:
        return f"<br/><b>Voce escolheu o numero:<br> {numero}"
    else:
        redirect()


@app.route('/argumentos')
def argumentos():
    argumentos = request.args.to_dict()
    return argumentos




app.run(debug=True, use_reloader=True)


