from flask import Flask, render_template, request, jsonify
import os
from llm import llm

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    """API endpoint to process summarization requests"""
    # Get data from the request
    data = request.json
    text = data.get('text', '')
    length_option = data.get('length', 'medium')
    style_option = data.get('style', 'concise')
    
    # Create descriptions based on user selections
    if length_option == 'short':
        length_desc = "very brief (about 10% of original length)"
    elif length_option == 'medium':
        length_desc = "moderately condensed (about 20% of original length)"
    else:  # long
        length_desc = "detailed but condensed (about 30% of original length)"
    
    if style_option == 'bullet':
        style_desc = "in bullet point format"
    elif style_option == 'detailed':
        style_desc = "with important details preserved"
    else:  # concise
        style_desc = "in a concise manner"
    
    # Construct the prompt for direct LLM use
    prompt = f"""Please summarize the following text {length_desc} and {style_desc}.
    Focus on the most important information and main points.
    
    TEXT TO SUMMARIZE:
    {text}
    
    SUMMARY:"""
    
    try:
        # Get summary directly from LLM
        summary = llm.invoke(prompt).strip()
        
        # Calculate word counts
        original_words = len(text.split())
        summary_words = len(summary.split())
        
        # Calculate reduction percentage
        if original_words > 0:
            reduction = round((1 - (summary_words / original_words)) * 100)
        else:
            reduction = 0
            
        return jsonify({
            'summary': summary,
            'original_length': original_words,
            'summary_length': summary_words,
            'reduction': reduction
        })
    
    except Exception as e:
        return jsonify({
            'error': str(e),
            'summary': "An error occurred while generating the summary."
        }), 500

if __name__ == '__main__':
    app.run(debug=True)