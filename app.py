from flask import Flask, render_template, request, jsonify
from agent import InternHubAgent
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.json
        
        student_profile = {
            "name": data.get('name', 'Student'),
            "skills": [s.strip() for s in data.get('skills', '').split(',')],
            "interests": [i.strip() for i in data.get('interests', '').split(',')],
            "experience": data.get('experience', 'Fresher')
        }
        
        internship_jd = {
            "role": data.get('role', 'Intern'),
            "requirements": data.get('requirements', ''),
            "description": data.get('description', '')
        }
        
        agent = InternHubAgent()
        results = agent.analyze_match(student_profile, internship_jd)
        
        return jsonify({
            "success": True,
            "results": results
        })
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

