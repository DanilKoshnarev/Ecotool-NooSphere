from flask import Flask, render_template, request, jsonify
from src.domain.eco_advice.services import EcoAdviceService
from src.domain.eco_advice.ai_service import AIService
from src.infrastructure.repository import EcoAdviceRepository

app = Flask(__name__)

# Initialize services
ai_service = AIService()
repository = EcoAdviceRepository()
eco_service = EcoAdviceService(ai_service, repository)

@app.route('/', methods=['GET', 'POST'])
async def index():
    advice = None
    metadata = None
    
    if request.method == 'POST':
        user_input = request.form.get('user_input', '')
        advice_response = await eco_service.generate_advice(user_input)
        advice = advice_response.content
        metadata = advice_response.metadata
        
    return render_template('index.html', advice=advice, metadata=metadata)

@app.route('/api/faq', methods=['GET'])
async def get_faq():
    # Return frequently asked questions
    faqs = await repository.get_popular_questions()
    return jsonify(faqs)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)