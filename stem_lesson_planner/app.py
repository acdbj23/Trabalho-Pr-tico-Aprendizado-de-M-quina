from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        plan = {
            'titulo': request.form.get('titulo', ''),
            'objetivos': request.form.get('objetivos', ''),
            'recursos': request.form.get('recursos', ''),
            'atividades': request.form.get('atividades', ''),
            'avaliacao': request.form.get('avaliacao', '')
        }
        return render_template('plan.html', plan=plan)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
