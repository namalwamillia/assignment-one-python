from flask import Flask

app=Flask(__name__)#creating an instance


@app.route('/')
def home():
    return " masterie flask"


if __name__ =="__main__":
    app.run(debug=True)