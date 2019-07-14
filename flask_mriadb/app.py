from flask import Flask,render_template,request
import db

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/insert', methods=['POST'])
def login_post():
    result = request.form.to_dict()
    print(result)
    return "입력성공"

if __name__ == '__main__':
    app.run(debug=True)
