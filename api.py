from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/users/', methods=['GET'])
def returnUser():
    id = request.args.get("id")
    users = {
        1: {
            "name": "Alex",
            "age": 25
        },
        2: {
            "name": "Max",
            "age": 28
        },
        3: {
            "name": "Egor",
            "age": 15
        }
    }
    return jsonify(users[int(id)])

if __name__ == "__main__":
    app.run(debug=True)