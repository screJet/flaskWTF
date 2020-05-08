from flask import Flask, render_template

app = Flask(__name__)


@app.route('/list_prof/<list>')
def index(list):
    professions = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач', 'инженер по терраформированию',
                   'климатолог', 'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
                   'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер', 'штурман',
                   'пилот дронов']
    return render_template('list_prof.html', list=list, professions=professions)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
