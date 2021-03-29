from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask import jsonify

db_connect = create_engine('sqlite:///sample_test.db')
app = Flask(__name__)
api = Api(app)


@app.route('/api/v1/location/', methods=['GET'])
def Location():
    conn = db_connect.connect()
    query = conn.execute("select location from meta_data")
    return {'locations': [i[0] for i in query.cursor.fetchall()]}


@app.route('/api/v1/location/<location_id>/department/', methods=['GET'])
def Location2(location_id):
    conn = db_connect.connect()
    query = conn.execute("select department from meta_data where location='{0}'".format(location_id))
    return {'department': [i[0] for i in query.cursor.fetchall()]}


@app.route('/api/v1/location/<location_id>/department/<department_id>/category/', methods=['GET'])
def Location3(location_id, department_id):
    conn = db_connect.connect()
    query = conn.execute("select category from meta_data where location='{0}' and department='{1}' ".format(location_id, department_id))
    return {'category': [i[0] for i in query.cursor.fetchall()]}


@app.route('/api/v1/location/<location_id>/department/<department_id>/category/<category_id>/subcategory/', methods=['GET'])
def Location4(location_id, department_id, category_id):
    conn = db_connect.connect()
    query = conn.execute("select subcategory from meta_data where location='{0}' and department='{1}' and category='{2}'".format(location_id, department_id, category_id))
    return {'category': [i[0] for i in query.cursor.fetchall()]}

@app.route('/api/v1/location/<location_id>/department/<department_id>/category/<category_id>/subcategory/<subcategory_id>', methods=['GET'])
def Location5(location_id, department_id, category_id, subcategory_id):
    conn = db_connect.connect()
    print("select * from meta_data where location='{0}' and department='{1}' and category='{2}' and subcategory='{3}'".format(location_id, department_id, category_id, subcategory_id))
    query = conn.execute("select * from meta_data where location='{0}' and department='{1}' and category='{2}' and subcategory='{3}'".format(location_id, department_id, category_id, subcategory_id))
    return {'all': [i for i in query.cursor.fetchall()]}


@app.route('/api/v1/location/<location_id>/department/<department_id>/category/<category_id>/subcategory/<subcategory_id>/sku', methods=['GET'])
def Location6(location_id, department_id, category_id, subcategory_id):
    conn = db_connect.connect()
    print("select * from sku_data where location='{0}' and department='{1}' and category='{2}' and subcategory='{3}'".format(location_id, department_id, category_id, subcategory_id))
    query = conn.execute("select * from sku_data where location='{0}' and department='{1}' and category='{2}' and subcategory='{3}'".format(location_id, department_id, category_id, subcategory_id))
    return {'all': [i for i in query.cursor.fetchall()]}


if __name__ == '__main__':
    app.run(port='5002')
