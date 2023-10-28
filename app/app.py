from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from mysql_model import Person

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:p%40ssw0rd1@mysqldb/test_mysql?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'Response Data'

@app.route('/another')
def another():
    return 'Another Response'

@app.route('/test_request')
def test_request():
    return f'test_request:{request.args.get("dummy")}'

@app.route("/users/<user_name>")
def users(user_name):
    return user_name

@app.route('/show_html')
def show_html():
    return render_template('test.html')

@app.route('/exercise')
def show2_html():
    return f'exercise:{request.args.get("my_name")}'

@app.route('/try_rest', methods=['POST'])
def try_rest():
    # リクエストデータをJSONとして受け取る
    request_json = request.get_json()
    print(request_json)
    print(type(request_json))
    name = request_json['name']
    print(name)
    response_json = {"response_json": request_json}
    return jsonify(response_json)

@app.route('/person_search')
def show_try_html():
    return render_template('person_search.html')

@app.route('/show_try_html')
def show_try_html2():
    return render_template('try_html.html')

@app.route('/show_data')
def show2_try_html():
    return f'show_data:{request.args.get("text")}'

@app.route('/person_result')
def person_result():
    search_size = request.args.get("search_size")
    persons = db.session.query(Person).filter(Person.size > search_size)
    return render_template('./person_result.html', persons=persons, search_size=search_size)

