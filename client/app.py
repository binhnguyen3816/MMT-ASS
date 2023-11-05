from flask import request
from flask import Flask, render_template, jsonify, get_template_attribute, make_response,redirect, jsonify, send_file
from flask import abort
from flask import session, url_for
import subprocess
# from werkzeug import secure_filename
# import numpy as np
import json
import time
# from python.client import Client
import copy
import os
def getpath(repath):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)),repath)

app = Flask(__name__)

def delete_line_from_file(line_to_delete):
    # Create a temporary file to store the modified content
    with open(getpath('list.txt'), 'r') as file, open(getpath('list.txt') + '.temp', 'w') as temp_file:
        for line in file:
            if line.strip() != line_to_delete.strip():
                temp_file.write(line)
    os.remove(getpath('list.txt'))
    os.rename(getpath('list.txt') + '.temp', getpath('list.txt'))


@app.route('/', methods=['GET','POST'])
def home():
    #open list.txt
    f = open(getpath("list.txt"), "r")
    res = []
    for x in f:
        bla= x.rsplit(" - ")
        for sub in bla:
            res.append(sub.replace("\n", ""))
    f.close()
    columns = 2
    rows = len(res)/2
    # Convert the 1D array to a 2D array
    result = [res[i:i+columns] for i in range(0, len(res), columns)]

    for x in result:
        x.append(url_for('static', filename=('MyFile/'+x[0])))

    # open hostname.txt
    h = open(getpath("hostname.txt"), "r")
    hostList = []
    for x in h:
        splitdata= x.rsplit(" - ")
        for subdata in splitdata:
            hostList.append(subdata.replace("\n", ""))
    h.close()
    columns = 2
    rows = len(hostList)/2
    # Convert the 1D array to a 2D array
    hostnames = [hostList[i:i+columns] for i in range(0, len(hostList), columns)]
    
    if request.method == 'POST':
        postData = request.form.to_dict()
        if postData["fname"]!='' and postData["lname"]!='':
            newline= postData['lname'] + ' - ' + postData['fname']
            with open(getpath("list.txt"), "a") as file:
                file.write('\n'+newline)
            file.close()
        else:
            del postData
    # Clear postData on every reload
    else:
        postData = {}


    return render_template('index.html', data=result, username='hoangdanh', hostnames=hostnames, delete_line_from_file=delete_line_from_file)




# @app.route('/signin', methods=['GET','POST'])

# @app.route('/signup', methods=['GET','POST'])
# def signup():
#     # print('sign_up')
    
#     # signuphtml = render_template('signup.html')
#     # print(render_template('index.html', signup = signup))
#     # return render_template('signup.html')
    
#     if request.method == 'POST':
#         print('post')
#         name=request.form['name']
#         un = request.form['username']
#         pw = request.form['password']
#         gender=request.form['gender']
#         print(name, un, pw, gender)
#         res=Client.request_signup(name,un,pw,gender)
#         print(res)
#         if(res):
#             Client.exist=True
#             return redirect("/signin", code=302)
#         else:
#             return render_template('signup.html', state=True)
#     else:         
#         print('sign_up_2')
#         return render_template('signup.html',state=False)
if __name__ == "__main__":
    # app.jinja_env.auto_reload = True
    # print(1000000)
    # app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host="localhost", port=5001, debug=True, use_reloader=False)