from langchain.tools import BaseTool
from typing import Optional, Type
from pydantic import BaseModel, Field

class SummarizationInput(BaseModel):
    """Input for text summarization tool."""
    text: str = Field(description="The text to summarize in the format: 'TEXT: <text to summarize> LENGTH: <length description> STYLE: <style description>'")

class SummarizationTool(BaseTool):
    name: str = "text_summarization"
    description: str = """Summarizes text based on specified length and style preferences. 
    Input should be in the format: 'TEXT: <text to summarize> LENGTH: <length description> STYLE: <style description>'"""
    args_schema: Type[BaseModel] = SummarizationInput
    
    def _run(self, text: str) -> str:
        """Summarize the text according to specified parameters."""
        try:
            # Parse the input text to extract components
            text_parts = text.split(" LENGTH: ")
            main_text = text_parts[0].replace("TEXT: ", "").strip()
            remaining = text_parts[1].split(" STYLE: ")
            length_desc = remaining[0].strip()
            style_desc = remaining[1].strip()
            
            prompt = f"""Please summarize the following text {length_desc} and {style_desc}.
            Focus on the most important information and main points.
            
            TEXT TO SUMMARIZE:
            {main_text}
            """
            
            return prompt
        except Exception as e:
            return f"Error parsing input: {str(e)}. Please ensure input is in the format: 'TEXT: <text> LENGTH: <length> STYLE: <style>'"
    
    def _arun(self, text: str):
        """Async implementation of text summarization."""
        raise NotImplementedError("Async not implemented for this tool")

class TextAnalysisTool(BaseTool):
    name: str = "text_analysis"
    description: str = "Analyzes text for key metrics such as word count, sentiment, etc."
    
    def _run(self, text: str) -> str:
        """Analyze the text and return metrics."""
        word_count = len(text.split())
        sentence_count = text.count('.') + text.count('!') + text.count('?')
        
        return f"Analysis: {word_count} words, approximately {sentence_count} sentences."
    
    def _arun(self, text: str):
        """Async implementation of text analysis."""
        raise NotImplementedError("Async not implemented for this tool")

# Create a list of tools to pass to the agent
tools = [
    SummarizationTool(),
    TextAnalysisTool(),
]

# You can add more tools here as needed