from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route to serve the frontend
@app.route('/')
def index():
    return render_template('index.html')

# API route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')
    
    response = {
        'status': 'success',
        'message': f'Thank you {name}, we have received your message.'
    }
    print(f"Received Data - Name: {name}, Email: {email}, Message: {message}")
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
