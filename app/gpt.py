import openai

# Set your OpenAI API key
openai.api_key = 'api_key'

def analyze_ingredients(ingredients, age_bracket):
    prompt = f"Analyze the following ingredients for a toddler in the age bracket {age_bracket}. Provide a detailed report on their suitability and suggest alternatives for any unsuitable ingredients:\n\n" + "\n".join(ingredients)
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )
    
    return response['choices'][0]['message']['content'].strip()
