from flask import Flask, render_template
# from dotenv import
app=Flask(__name__)

posts=[
    {
        'author':'Corey Schafer',
        'title':'Blog Post  1',
        'content':'First post content',
        'date posted': 'April 20, 2025'
    },

    {
        'author':'Jane Doe',
        'title':'Blog Post  2',
        'content':'second post content',
        'date posted': 'April 21, 2025'
    },
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html',posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')
if __name__=='__main__':
    app.run(debug=True)