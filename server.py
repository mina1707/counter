from flask import Flask , render_template, redirect, request, session

app=Flask(__name__)
app.secret_key='secret'

@app.route('/') #-> this route will increment one for every visit to the main page.
def main_route():
#Display
    if 'count' in session:
        session['count']+=1
    return render_template("index.html", count= session['count'])
#Action
@app.route('/count_one') #--> this route will add one when we click/ this is the action in html.
def addone():
    session['count']
    return redirect('/') #--> this will redirect to the main page.
#Action
@app.route('/reset') # --> this route will reset the count.
def reset():
    session['count']=0 #-> this is 0, but we will see 1 in the screen because we are 1 session in.
    return redirect('/') #--> this will redirect to the main page.

@app.route('/count_two')
def addtwo():
    session['count'] += 4
    return redirect('/')

@app.route('/add_one')
def pokemon():
    session['count']+=1
    return redirect('/')

app.run(debug=True)