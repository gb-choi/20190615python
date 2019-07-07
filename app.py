from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/formresult', methods=['POST'])
def form_result():
    username = request.form['username']
    Joblist=request.form.getlist('Job')
    return render_template('formresult.html' ,username=username, Joblist=Joblist)

if __name__ == '__main__':
    app.run(debug=True)
