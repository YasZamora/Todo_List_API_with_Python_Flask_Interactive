from flask import Flask, jsonify, request, json
app = Flask(__name__)

todos = [{ "label": "My first task", "done": False }]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    print(request.data)
    decoded_object = json.loads(request.data)
    list = todos
    list.append(decoded_object)
    return jsonify(list)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):    
    print("This is the position to delete: ",position)
    list= todos
    list.remove(list[0])
    return jsonify(list)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)