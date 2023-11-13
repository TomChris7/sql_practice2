from flask import Flask, render_template, request, redirect, url_for

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

all_books = []


@app.route('/')
def home():


    return render_template("index.html", books=all_books, len=len(all_books))


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == "POST":
        data = request.form
        all_books.append(data.to_dict())

    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

