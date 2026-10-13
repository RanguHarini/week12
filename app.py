
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('registration.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    course = request.form['course']

    return render_template(
        'success.html',
        name=name,
        email=email,
        phone=phone,
        course=course
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
