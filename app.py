from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ""
    input_text = ""
    direction = "en-hi"

    if request.method == 'POST':
        input_text = request.form['input_text']
        direction = request.form['direction']

        if input_text.strip() != "":
            src, dest = direction.split('-')
            try:
                translated = translator.translate(input_text, src=src, dest=dest)
                translated_text = translated.text
            except Exception as e:
                translated_text = f"Error: {str(e)}"

    return render_template('index.html', translated_text=translated_text, input_text=input_text, direction=direction)

if __name__ == '__main__':
    app.run(debug=True,port=5050)
