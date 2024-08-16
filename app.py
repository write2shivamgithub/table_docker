from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    multiplication_table = None
    number = None
    if request.method == 'POST':
        try:
            number = int(request.form['number'])
            multiplication_table = [(number, i, number * i) for i in range(1, 11)]
        except ValueError:
            multiplication_table = None

    return render_template('index.html', multiplication_table=multiplication_table, number=number)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
