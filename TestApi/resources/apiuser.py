import json
from flask import Flask, Response, jsonify
from database.model import Users
from flask_restful import Resource, Api, reqparse, request



parser = reqparse.RequestParser()


class UsersList(Resource):
    def get(self):
        offset = request.args.get('offset', default=None, type=int)
        limit = request.args.get('limit', default=None, type=int)
        order_by = request.args.get('order_by', default=None, type=str)
        id = request.args.get('id', default=True, type=str)
        email = request.args.get('email', default=True, type=str)
        name_substr = request.args.get('name_substr', default=True, type=str)
        args = parser.parse_args()
        #filter
        userslist = Users.objects()
        if id is not True: userslist = userslist.filter(id__icontains=id)
        if email is not True: userslist = userslist.filter(email__icontains=email)
        if name_substr is not True: userslist = userslist.filter(name__icontains=name_substr)
        # order_by - можно поставить перед словом "-" и будет наоборот
        newuserslist = userslist.order_by(order_by).skip(offset).limit(limit).to_json()
        total_count = userslist.count()

        List = json.loads(newuserslist)
        return {"total counts": total_count, "items": List}

    def post(self):
        body = request.get_json()
        user = Users(**body).save()
        id = user.id
        return {'id': str(id)}, 200

    # def post(self):
    #     fill_data = request.args.get('fill_data', default=None, type=int)
    #     for i in range(fill_data):
    #         body = {
    #             'name': 'name_' + str(i),
    #             'last_name': 'last_name' + str(i),
    #             'email': 'abra@'+str(i)+'.com',
    #             'balance': i
    #         }
    #         Users(**body).save()
    #
    # def delete(self):
    #     Users.objects.delete()
