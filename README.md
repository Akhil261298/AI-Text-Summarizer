# AI Text Summarizer

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-3.0.2-green)
![LangChain](https://img.shields.io/badge/LangChain-0.1.9-orange)
![License](https://img.shields.io/badge/license-MIT-blue)

An advanced text summarization web application that leverages AI to generate concise, customizable summaries. Built with Flask, LangChain, and Ollama (Gemma model).

## 🌟 Features

- **Customizable Summarization**
  - Adjustable summary length (short, medium, long)
  - Multiple summary styles (concise, bullet points, detailed)
  - Real-time word count and reduction metrics

- **Modern UI/UX**
  - Clean, responsive design
  - Real-time feedback
  - Progress indicators
  - Error handling

- **Technical Features**
  - Optimized LLM configuration for fast processing
  - Multi-threaded text processing
  - RESTful API endpoints
  - Efficient text analysis

## 🚀 Live Demo

[Live Demo](your-deployment-url) - Coming soon

## 🛠️ Technology Stack

- **Frontend:**
  - HTML5
  - CSS3 (Modern design with Flexbox/Grid)
  - JavaScript (Vanilla JS for API interactions)

- **Backend:**
  - Python 3.8+
  - Flask 3.0.2
  - LangChain 0.1.9
  - Ollama (Gemma model)

- **Development Tools:**
  - Git for version control
  - Virtual Environment for dependency management
  - RESTful API design

## 📋 Prerequisites

- Python 3.8 or higher
- Ollama installed with the Gemma model
- pip (Python package manager)

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/text-summarizer.git
cd text-summarizer
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install and run Ollama with Gemma model:
```bash
ollama pull gemma
```

## 🚀 Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Enter your text, select summarization options, and click "Summarize"

## 📊 API Endpoints

### POST /summarize
Generates a summary of the provided text.

Request body:
```json
{
    "text": "Your text to summarize",
    "length": "medium",  // "short", "medium", or "long"
    "style": "concise"   // "concise", "bullet", or "detailed"
}
```

Response:
```json
{
    "summary": "Generated summary",
    "original_length": 100,
    "summary_length": 30,
    "reduction": 70
}
```

## 🎯 Key Features Explained

### Summary Options

- **Length Settings:**
  - Short: ~10% of original length
  - Medium: ~20% of original length
  - Long: ~30% of original length

- **Style Options:**
  - Concise: Clear and direct summary
  - Bullet Points: Key points in bullet format
  - Detailed: Comprehensive summary with important details

### Performance Optimizations

- Optimized LLM configuration
- Multi-threaded processing
- Efficient text analysis algorithms
- Responsive UI with loading states

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Contact

Your Name - [your-email@example.com](mailto:your-email@example.com)

Project Link: [https://github.com/your-username/text-summarizer](https://github.com/your-username/text-summarizer) 