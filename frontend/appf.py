from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

HTML_FORM = """
<!doctype html>
<title>Calcular Factorial</title>
<h1>Ingrese un número</h1>
<form method=post>
  <input type=number name=numero min=0 required>
  <input type=submit value=Calcular>
</form>
{% if resultado %}
  <h2>El factorial de {{ resultado.numero }} es {{ resultado.factorial }}</h2>
{% endif %}
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    resultado = None
    if request.method == 'POST':
        numero = int(request.form['numero'])
        try:
            response = requests.post('http://localhost:5001/api/factorial', json={'numero': numero})
            resultado = response.json()
        except Exception as e:
            resultado = {'numero': numero, 'factorial': 'ERROR'}
    return render_template_string(HTML_FORM, resultado=resultado)

if __name__ == '__main__':
    app.run(port=5000)
