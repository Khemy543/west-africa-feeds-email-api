from flask import Flask, jsonify, request, session, render_template, url_for
from flask_mail import Mail, Message
from flask_cors import CORS ,cross_origin

#heroku
#https://salty-anchorage-79079.herokuapp.com/
app = Flask(__name__)

app.config['SECRET_KEY'] = 'shut the fuck up'
app.config['CORS_ALLOW_HEADERS'] = 'Content-Type'
#cors
cors = CORS(app, resource={r"/foo": {"origins": "*"}})


mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'gassafuah@gmail.com',
    "MAIL_PASSWORD":'bckxuddevfmovebr'
}
app.config.update(mail_settings)
mail = Mail(app)

#get home 
@app.route("/", methods=["GET"])
def home():
    return url_for('static', filename="logo-footer.png", _external=True)

#wainsight email test
@app.route('/api/v1/wainsight', methods=["POST"])
@cross_origin(origin = '*', headers=['Content- Type', 'Authorization'])
def sendWaInsightMail():
    try:
        _name = "Julia"

        msg = Message(subject="waInsight Test Mail", 
                    sender=app.config.get("MAIL_USERNAME"),
                    recipients=["gassafuah@gmail.com","gideon@walulel.com","julia@walulel.com"],
                    body="We are just testing Wa Insight mails",
                    html=render_template('waInsight.html',name=_name))
        mail.send(msg)
        return jsonify({'message':"Message sent", 'status':200})

    except Exception as e:
        return jsonify({'message':'Not sent', 'status':400, 'error':str(e)})


#waptron email test 
@app.route('/api/v1/wapatron', methods=["POST"])
@cross_origin(origin = '*', headers=['Content- Type', 'Authorization'])
def sendWaPatronMail():
    try:
        _name = "Julia"

        msg = Message(subject="WaPatron Test Mail", 
                    sender=app.config.get("MAIL_USERNAME"),
                    recipients=["gassafuah@gmail.com","gideon@walulel.com","julia@walulel.com"],
                    body="We are just testing Wa Patron mails",
                    html=render_template('waPatron.html',name=_name))
        mail.send(msg)
        return jsonify({'message':"Message sent", 'status':200})

    except Exception as e:
        return jsonify({'message':'Not sent', 'status':400, 'error':str(e)})

#wacommunicate email test
@app.route('/api/v1/wacommunicate', methods=["POST"])
@cross_origin(origin = '*', headers=['Content- Type', 'Authorization'])
def sendWaCommunicateMail():
    try:
        _name = "Derbie"

        msg = Message(subject="WaCommunicate Test Mail", 
                    sender=app.config.get("MAIL_USERNAME"),
                    recipients=["gassafuah@gmail.com","julia@walulel.com","deborah@walulel.com","gideon@walulel.com"],
                    body="We are just testing Wa Communicate mails",
                    html=render_template('waComm.html',name=_name))
        mail.send(msg)
        return jsonify({'message':"Message sent", 'status':200})

    except Exception as e:
        return jsonify({'message':'Not sent', 'status':400, 'error':str(e)})



#servie message
@app.route('/api/v1/post-message',  methods = ["POST"])
@cross_origin(origin = '*', headers=['Content- Type', 'Authorization'])
def  index():
    try:
        _email = request.json['email']
        _name = request.json['name']
        _message = request.json['message']

        msg = Message(subject="Information Request",
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=["gassafuah@gmail.com"], 
                      body= 'Hello',
                      html=render_template('message.html', name=_name, email=_email, message=_message, logo=url_for('static', filename="logo-footer.png", _external=True)) )
        mail.send(msg)
        return jsonify({"message":"Message sent successfully","status":200})

			
    except Exception as e:
        return jsonify({"message":"Not sent", "status":400, 'error':str(e)});


#admissionForm submission
@app.route('/api/v1/admission-form', methods=['POST'])
@cross_origin(origin= '*', headers=['Content- Type', 'Authorization'])
def formSubmission():
    try:
        firstname = request.json['firstname']
        lastname = request.json['lastname']
        nationality = request.json['nationality']
        age = request.json['age']
        sex = request.json['sex']
        program = request.json['program']
        guardfirstname= request.json['guardfirstname']
        guardlastname = request.json['guardlastname']
        occupation = request.json['occupation']
        address = request.json['address']
        phone = request.json['phone']
        email = request.json['email']

        msg = Message(
            subject='Admissions',
            sender=app.config.get('MAIL_USERNAME'),
            recipients=['gassafuah@gmail.com'],
            body="New Admission Received",
            html=render_template('admissionForm.html',
                firstname=firstname, 
                lastname=lastname, 
                nationality=nationality, 
                age=age, 
                sex=sex, 
                program=program,
                guardfirstname=guardfirstname,
                guardlastname=guardlastname,
                occupation=occupation,
                address=address,
                phone=phone,
                email=email
            ))
        mail.send(msg)
        return jsonify({"message":"Form submitted", "status":200})
    
    except Exception as e:
        return jsonify({"message":"Not sent", "error":str(e)});

#martekmail
@app.route('/api/v1/martek', methods=["POST"])
@cross_origin(origin = '*', headers=['Content- Type', 'Authorization'])
def sendMartekVerification():
    try:
        _name = "Kwakye"

        msg = Message(subject="Martek Email Verification", 
                    sender=app.config.get("MAIL_USERNAME"),
                    recipients=["kwakyekwabena123@gmail.com","ahadzi.airdem@gmail.com","gassafuah@gmail.com"],
                    body="Verify Email",
                    html=render_template('resetPassword.html',name=_name))
        mail.send(msg)
        return jsonify({'message':"Message sent", 'status':200})

    except Exception as e:
        return jsonify({'message':'Not sent', 'status':400, 'error':str(e)})


@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  response.headers.add('Access-Control-Allow-Credentials', 'true')
  return response;
   
if  __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)
    
    