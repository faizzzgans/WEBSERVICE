from flask import Flask

app = Flask(__name__)

@app.route('/entry1')
def entry():
    return "Hello, You entry!"


@app.route('/entry2')
def entrys():
      return "Hai, Anda entrys!"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
