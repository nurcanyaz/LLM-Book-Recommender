from flask import Flask, request, render_template,jsonify
# app
app = Flask(__name__)
# Store chats in memory (or use a database for persistence in production)
chats = [{'name': 'New Chat', 'id': 1, 'messages': []}]  # Default first chat
# Route to render the main page
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/get_chats",methods=['GET'])
def get_chats():
    return jsonify({'chats':chats})

@app.route("/get_chat_history",methods=['GET'])
def get_chat_history():
    chat_id = int(request.args.get('chat_id'))
    chat = next((chat for chat in chats if chat['id']==chat_id),None)
    if chat:
        return jsonify({'messages': chat['messages']})
    return jsonify({'messages':[]})


# python
if __name__=="__main":
    app.run(debug=True)