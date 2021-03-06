from flask import Flask, flash, request, render_template, session,redirect,url_for
from flask_mysqldb import MySQL
import MySQLdb
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from werkzeug.utils import secure_filename
import docx2txt
import re
import nltk
stop_words = set(nltk.corpus.stopwords.words('english'))
import string
from collections import defaultdict 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import spacy

nlp = spacy.load("en_core_web_sm")

app = Flask(__name__, template_folder = 'template')    
app.secret_key="1234353234"
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="Bindu@2801"
app.config["MYSQL_DB"]="login"
db=MySQL(app)

app.config.from_pyfile('config.py')
mail = Mail(app)
s = URLSafeTimedSerializer('Thisisasecret!')

# user registration
@app.route('/new',methods=['GET','POST'])
def new_user():
    if request.method=="POST":
        if "name" in request.form and "username" in request.form and "password" in request.form:
            name =request.form ['name']
            email=request.form['username']
            password=request.form ['password']
            cur=db.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("SELECT * FROM logininfo WHERE email = %s",(email,))
            info = cur.fetchone()
            if(info == None):
                cur.execute("INSERT INTO login.logininfo(name,email,password)VALUES(%s,%s,%s)",(name,email,password))
                db.connection.commit()
            else:
                result = "You already had an account with ---->"+email+", please register with other email-id or login"
                flash(result)
                return render_template("register.html")
    return render_template("register.html")

#Welcome Page
@app.route('/')
def welcome():
    return render_template("welcome.html")

# user login
@app.route('/login',methods =['GET','POST'])
def index():
    if request.method=='POST':
        if 'username' in request.form and 'password' in request.form:
            username=request.form['username']
            password =request.form['password']
            cursor=db.connection.cursor(MySQLdb.cursors.DictCursor)   #1
            cursor.execute("SELECT * FROM logininfo WHERE email=%s AND password =%s",(username,password))
            info=cursor.fetchone()
            print(info)
        if info is not None:
            if info['email']==username and info['password']==password:
                return render_template("upload.html")
                session['loginsuccess']=True
        
        else:
            msg = "Invalid Credentials"
            flash(msg,"error")
    return render_template("login.html")

# uploading CV
@app.route('/upload', methods = ['POST']) 
def upload():
    if session['loginsuccess']==True:
        return render_template("upload.html")

# Extracting input
@app.route('/success',methods = ['POST'])
def success():
    if(request.method == 'POST'):
        company_links = {'Google': "C:\\Users\\BINDU SRI NAGAVALLI\\RateMyResume_B05\\Google.txt", 'Amazon':"C:\\Users\\BINDU SRI NAGAVALLI\\RateMyResume_B05\\Amazon.txt",'TCS':"C:\\Users\\BINDU SRI NAGAVALLI\\RateMyResume_B05\\TCS.txt",'IBM':"C:\\Users\\BINDU SRI NAGAVALLI\\RateMyResume_B05\\IBM.txt",'Infosys':"C:\\Users\\BINDU SRI NAGAVALLI\\RateMyResume_B05\\Infosys.txt",'Flipkart':"C:\\Users\\BINDU SRI NAGAVALLI\\RateMyResume_B05\\flipkart.txt"}

        checked = request.form.getlist('mycheckbox')
        f = request.files['file']
        txt = docx2txt.process(f)
        
        # processing CV
        if txt:
            resume = txt.replace('\t', ' ')
        else:
            resume = " "
        companys_req = {}
        j = 0
        # match resume with these requirements 
        word_tokens = nltk.tokenize.word_tokenize(resume)

        # remove the stop words
        filtered_tokens = [w for w in word_tokens if w not in stop_words]

        # remove the punctuation
        filtered_tokens = [w.lower() for w in word_tokens if w.isalpha()]

        # generate bigrams and trigrams (such as artificial intelligence)
        bigrams_trigrams = list(map(' '.join, nltk.everygrams(filtered_tokens, 2, 3)))

        # Finding whether projects/interns/achievements done by the user.
        other_perct = others(filtered_tokens)
        tech_perct = []
        skill_perct = []
        edu_perct = []
        # companys_req = {"company1":{"technical skills":[values],"skills":[values]}, "company2":{}}
        for i in checked:
            d = defaultdict(list)
            company = company_links[i]
            with open(company) as file:
                for line in file:
                    if ":" in line:
                        k,v = line.rstrip().split(":")
                        d[k].extend(map(str.strip,v.split("\n")) if v.strip() else []) 
               	    else:
                    	d[k].append(line.rstrip()) 
                companys_req[i] = dict(d)

            found_skills = []
            SKILLS_DB = companys_req[i]['Skills']
            SKILLS_DB = [string.lower() for string in SKILLS_DB]
        
            # we search for each token in our skills database
            for token in list(set(filtered_tokens)):
                if token in SKILLS_DB:
                    found_skills.append(token)
                    
            # we search for each bigram and trigram in our skills database
            for ngram in list(set(bigrams_trigrams)):
                if ngram in SKILLS_DB:
                    found_skills.append(ngram)
                   
        
            #  calculate percentage of matched skills
            perct = (int)(len(found_skills)/len(SKILLS_DB)*100)
            skill_perct.append(perct)          


            found_tech_skills = []
            TECH_SKILLS_DB = companys_req[i]['Technical Qualifications']
            TECH_SKILLS_DB = [string.lower() for string in TECH_SKILLS_DB]
        
            # we search for each token in our skills database
            for token in list(set(filtered_tokens)):
                if token in TECH_SKILLS_DB:
                    found_tech_skills.append(token)

            # we search for each bigram and trigram in our technical skills database
            for ngram in list(set(bigrams_trigrams)):
                if ngram in TECH_SKILLS_DB:
                    found_tech_skills.append(ngram)
        
            # print skills matched and calculate percentage of match
            print(found_tech_skills)
            perct = (int)(len(found_tech_skills)/len(TECH_SKILLS_DB) * 100)
            print(f"Percentage of technical skills match for company {i}",perct)
            tech_perct.append(perct)            
            
            education = extract_education(txt) #education = {'Btech': value, 'SSC':values,...}
            score = score_of_edu(i,education)
            if(score/len(education) == 100):
                edu_perct.append(100)
            else:
                edu_perct.append(0)
        print(edu_perct)
        msg = {}
        check = 0
       
        for x in edu_perct:
            if(x != 100):
                msg[checked[check]] = [0] 
            else:
                msg[checked[check]] = [1] 
            check += 1  
            

        check = 0
        for x in tech_perct:
            if(x < 50):
                msg[checked[check]].append(0)
            else:
                msg[checked[check]].append(1)
            check+= 1
        
        
        check = 0
        for x in skill_perct:
            if(x < 50):
                msg[checked[check]].append(0)
            else:
                msg[checked[check]].append(1)
            check += 1
        success = "Eligible for "
        eligible = []
        for i in checked:
            if(msg[i] == [1,1,1]):
                success += i+" "
                eligible.append(i)
                
        if(len(eligible) != len(checked) and len(eligible) > 0):
            comp = ""
            for i in eligible:
                comp += i
                comp += ","
            flash("You are just few steps away from perfecting your resume. Check out the detailed reviews to improve the score. Score more to improve your chances of short listing"+"\n"+"-------->"+ "You are eligible for only "+comp)
        
        elif(len(eligible) == 0):
            flash("Your resume score is too low...You are not eligible for companies you have selected. It has room for lot of improvements!! Improve your resume and come back to check your score!!!")
        
        else:
            flash("Great Job!! You are eligible for all the companies you have selected.")


        plt = bar_graph(tech_perct,skill_perct,other_perct,checked)    
        plt.show()
        return render_template('message.html')
        
@app.route('/new/logout')
def logout():
    session.Pop('logoutsuccess',None)
    return redirect(url_for('index'))

def others(filtered_tokens):
    other_perct = 0
    if(("project" in filtered_tokens) or ("projects" in filtered_tokens)):
        other_perct += 25
    if(("intern" in filtered_tokens) or ("interns" in filtered_tokens) or ("internship" in filtered_tokens) or ("internships" in filtered_tokens)):
        other_perct += 25
    if(("achievements" in filtered_tokens) or ("achievements" in filtered_tokens)):
        other_perct += 25
    if(("strength" in filtered_tokens) or ("strengths" in filtered_tokens)):
        other_perct += 25
    return other_perct
    
def extract_education(text):
    EDUCATION = [
            'BE','B.E.', 'B.E', 'BS', 'B.S', 
            'ME', 'M.E', 'M.E.', 'MS', 'M.S', 
            'BTECH', 'B.TECH', 'M.TECH', 'MTECH', 
            'SSC', 'HSC', 'CBSE', 'ICSE', 'X', 'XII','INTER','INTERMEDIATE','POLYTECHNIC','DIPLOMA'
        ]
    nlp_text = nlp(text)
    # Sentence Tokenizer
    nlp_text = [str(sent).strip() for sent in nlp_text.sents]
    edu = {}
    # Extract education degree
    for index, text in enumerate(nlp_text):
        for tex in text.split():
            # Replace all special symbols
            tex = re.sub(r'[?|$|.|!|,]', r'', tex)
            if tex.upper() in EDUCATION:
                edu[tex] = text + nlp_text[index + 1]
    # Extract year
    education = {}
    index = 0
    for key in edu.keys():
        num_list = re.findall(r'\d{1,10}', edu[key][index:])
        i = 0
        if(num_list):
            for i in num_list:
                if(len(i) <= 3):
                    index = edu[key].index(i) + len(i)
                    education[key] = i
                    break
    return (education)


def score_of_edu(company, education):
    test_dict2 = {'Google':{'Btech' : 65, 'Inter' : 65, 'SSC' : 65, 'DIPLOMA':65},
                    'Amazon':{'Btech' : 65, 'Inter' : 65, 'SSC' : 65, 'DIPLOMA':65},
                     'Flipkart':{'Btech' : 60, 'Inter' : 60, 'SSC' : 60, 'DIPLOMA':65},
                      'TCS':{'Btech' : 60, 'Inter' : 60, 'SSC' : 60, 'DIPLOMA':65},
                      'Infosys':{'Btech' : 68, 'Inter' : 60, 'SSC' : 60, 'DIPLOMA':65},
	     'IBM':{'Btech' : 70, 'Inter' : 65, 'SSC' : 65, 'DIPLOMA':65}}

    total=0
    for key in education:
        if(int(education[key])>=test_dict2[company][key]):
            score=100
        else:
            score=0
        total=total+score
    return total
   
def bar_graph(tech_perct,skill_perct,other_perct,company_list):
    N = len(company_list)
    techskills = tech_perct
    techskills_std = []
    for i in range(N):
        techskills_std.append(0)

    ind = np.arange(N)  # the x locations for the groups
    width = 0.25       # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, techskills, width, color='#36648B', yerr=techskills_std)

    skills = skill_perct
    skills_std = []
    for i in range(N):
        skills_std.append(0)

    rects2 = ax.bar(ind+width, skills, width, color='#7D9EC0', yerr=skills_std)

    others = other_perct
    others_std = []
    for i in range(N):
        others_std.append(0)

    rects3 = ax.bar(ind+width+width, others, width, color='#A4D3EE', yerr=others_std)
    ax.set_ylabel('Percentages')
    ax.set_title('Bar Graph by rating Resume')
    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels(company_list)
    ax.legend((rects1[0], rects2[0], rects3[0]), ('Technical Skills', 'Skills','others'), prop = {'size': 6})
    autolabel(ax,rects1)
    autolabel(ax,rects2)
    autolabel(ax,rects3)
    return plt

def autolabel(ax,rects):
    #Attach a text label above each bar displaying its height
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1*height,
                '%d' % int(height),
                ha='center', va='bottom')


if __name__=='__main__':
   app.run(debug=True)


"""
@app.route("/verification/<cur>/<name>/<email>/<password>")
def verify(cur,name,email,password):
    token = s.dumps (email, salt='email-confirm')
    msg = Message('Confirm Email', sender= 'resumerating123@gmail.com', recipients= [email])
    my_list.append(token)
    link= url_for('confirm_email', token=token,cur=cur,name=name,email=email,password=password, _external=True)
    msg.body = 'Your link is {}. This will expire within 360seconds. If time expired verify again.'.format(link)
    mail.send(msg)
    return "<h2>Verification link is sent to your mail...please check!!!</h2>"

@app.route('/confirm_email/<token>/<cur>/<name>/<email>/<password>')
def confirm_email(token,cur,name,email,password):
    try:
        email = s.loads (token, salt='email-confirm', max_age=360)
    except SignatureExpired:
        return '<h1>The token is expired.</h1></br></br><form action = "/new"><input type="submit" value="Go to Register page" class="btn btn-primary"/></form>'
    cur.execute("INSERT INTO login.logininfo(name,email,password)VALUES(%s,%s,%s)",(name,email,password))
    db.connection.commit()
    return render_template("verify.html")
"""

