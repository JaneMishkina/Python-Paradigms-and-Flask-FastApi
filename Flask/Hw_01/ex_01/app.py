from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def shoes():
    return render_template('shoes.html')

@app.route('/clothes/')
def clothes():
    return render_template('clothes.html')

@app.route('/coat/')
def coat():
    return render_template('coat.html')



if __name__ == '__main__':
    app.run()
