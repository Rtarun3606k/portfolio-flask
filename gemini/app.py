from flask import render_template, request, Flask,redirect
# from gemini import GEMINI
from gemini.GEMINI import generate
from flask import Flask
 

app = Flask(__name__)
 


@app.route('/',methods=['POST','GET'])
@app.route('/home',methods=['POST','GET'])
def hello_world():
    s='trial'
    if request.method=='POST':
        query = request.form['query']
        query = str(query)
        # print(len(query),'query length')
        # print(,"hello")
        print(len(query),query)
        # string_without_spaces = query.replace(" ", "")
        for i in query:
            if i.isalnum():
                s= generate(query)
                response = s.process()
                response = str(response)
                return render_template('index.html',response=response)  
                return render_template('index.html',response=s)
                break

            # return redirect('/home') 
        else:
            s="length prob"
            return render_template('index.html',response=s)  

        return render_template('index.html',response=s)
 

if __name__ == '__main__':
 

    app.run(port=2000,debug=True)
    