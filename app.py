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
    "MAIL_USERNAME": 'mailto:westafricanfeeds@gmail.com',
    "MAIL_PASSWORD":'mllxfdbcdihrpsvm'
}
app.config.update(mail_settings)
mail = Mail(app)

#get home 
@app.route("/", methods=["GET"])
def home():
    return url_for('static', filename="logo-footer.png", _external=True)

#service email test
@app.route('/api/contact-us', methods=["POST"])
@cross_origin(origin = '*', headers=['Content- Type', 'Authorization'])
def sendContactUs():
    try:
        _email = request.json['email']
        _firstname = request.json['firstname']
        _lastname = request.json['lastname']
        _phone = request.json['phone']
        _message = request.json['message']

        msg = Message(subject="Contact Us Information", 
                    sender=app.config.get("MAIL_USERNAME"),
                    recipients=["info@westafricanfeeds.co", "mailto:westafricanfeeds@gmail.com"],
                    body="Testing",
                    html=render_template('message.html', firstname=_firstname, lastname=_lastname, phone=_phone, email=_email, message=_message))
        mail.send(msg)
        return jsonify({'message':"Message sent", 'status':200})

    except Exception as e:
        return jsonify({'message':'Not sent', 'status':400, 'error':str(e)})


#become an outgrower email test 
@app.route('/api/become-an-outgrower', methods=["POST"])
@cross_origin(origin = '*', headers=['Content- Type', 'Authorization'])
def sendBecomeAnOutgrower():
    try:
        _email = request.json['email']
        _name = request.json['name']
        _phone = request.json['phone']
        _company_name = request.json['company_name']
        _nature_of_business = request.json['nature_of_business']

        msg = Message(subject="New outgrower request", 
                    sender=app.config.get("MAIL_USERNAME"),
                    recipients=["info@westafricanfeeds.com", "westafricanfeeds@gmail.com"],
                    body="Testing",
                    html=render_template('outgrower.html',name=_name, email=_email, company_name=_company_name, phone=_phone, nature_of_business=_nature_of_business))
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
    
    