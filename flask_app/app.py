from flask import Flask, request
 
app = Flask(__name__)
 
@app.route('/', methods=['GET'])
def home():
    return "Hello KanchiLUG!"
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)  # Run the app on port 5000