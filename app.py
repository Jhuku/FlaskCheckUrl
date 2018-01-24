from flask import Flask, render_template,request,flash,make_response
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email


app = Flask(__name__)
app.secret_key = 'hoxter'

class UrlForm(FlaskForm):
    url = StringField('URL',validators=[DataRequired()])

@app.route('/',methods=['GET','POST'])
def index():
    form = UrlForm(request.form)
    if form.url.data == None:
        return render_template('entry_page.html',form=form)
    if cookieExists(form.url.data) == False:
        urlStatus = checkInFiles(form.url.data)
        resp = make_response(render_template('result.html',x=urlStatus))
        resp.set_cookie(form.url.data,urlStatus)
    else:
        resp = make_response(render_template('result.html',x=getCookie(form.url.data)))
    return resp

def getCookie(data):
    print "Now i dont Check in the file"
    return request.cookies.get(data.encode('utf-8'))

def cookieExists(url):
    if request.cookies.get(url.encode('utf-8')) == None:
        return False
    else:
        return True

def checkInFiles(enteredUrl):
    print "Now i Check in the file"
    search = enteredUrl.encode('utf-8')+'\n'
    with open("SafeUrls.txt") as file:
        if any(line == search for line in file):
            return 'Safe'

    with open("UnsafeUrls.txt") as file:
        if any(line == search for line in file):
            return 'UnSafe'

if __name__ == "__main__":
    app.run(debug=True)
