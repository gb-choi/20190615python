from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')
'''
@app.route('/formresult', methods=['POST'])
def form_result():
    username1 = request.form['username']
    Joblist=request.form.getlist('Job')
    return render_template('formresult.html' ,username=username, Joblist=Joblist)

@app.route('/cakes/')
def cakes():
    return 'My cakes'



@app.route('/user/<username>/<int:age>')
def user(username,age):
    # return 'user %s, 나이 %d' %(username,age)
    return render_template('index2.html',username=username,age=age)

@app.route('/forminput/')
def forminput():
    return render_template('forminput.html')

@app.route('/method/',methods=['GET','POST'])
def method():
    if request.method == 'POST':
        return "POST"
    else:
        return "GET"

@app.route('/login/')
def login():
    username=request.args.get('name')
    return render_template('index2.html',username=username)

@app.route('/forminput1/')
def forminput1():
    return render_template('forminput1.html')

@app.route('/login/',methods=['POST'])
def login_post():
    username=request.form['username']
    password=request.form['password']
    return render_template('index2.html',username=username,password=password)
'''
@app.route('/form_input/')
def form_input():
    return render_template('form_input.html')

@app.route('/login_input/', methods=['POST'])
def login_input():
    '''
    if request.method == 'POST':
    '''
    result = request.form
    return render_template('form_result.html', result=result)



if __name__ == '__main__':
    app.run(debug=True)

