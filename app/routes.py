from flask import Blueprint, request, jsonify
from .ocr import extract_ingredients
from .gpt import analyze_ingredients

main = Blueprint('main', __name__)

@main.route('/upload', methods=['POST'])
def upload():
    try:
        # Get files and age bracket from request
        files = request.files.getlist('productImage')
        age_bracket = request.form['ageBracket']
        
        if not files:
            return jsonify({'error': 'No files uploaded'}), 400
        
        ingredients = []

        for file in files:
            text = extract_ingredients(file.stream)
            ingredients.extend(text.split('\n'))
        
        # Clean up extracted ingredients
        ingredients = [ingredient.strip() for ingredient in ingredients if ingredient.strip()]
        
        # Analyze ingredients with GPT
        analysis = analyze_ingredients(ingredients, age_bracket)
        
        response = {
            'age_bracket': age_bracket,
            'ingredients': ingredients,
            'analysis': analysis,
            'message': 'Ingredients analyzed successfully'
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)}), 500
