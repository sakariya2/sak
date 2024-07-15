from flask import Flask, request, render_template, jsonify
import openai

app = Flask(__name__)

# Replace with your OpenAI API key
openai.api_key = 'sk-proj-ZzpvuTfrwDyEeeE6XYeZT3BlbkFJ1ovbHURz26DYuFLAV7S'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    title = data.get('title', '')
    description = data.get('description', '')

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Generate a patent draft based on the following title and description:\nTitle: {title}\nDescription: {description}"}
        ]
    )

    draft = response['choices'][0]['message']['content'].strip()
    return jsonify({'draft': draft})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
