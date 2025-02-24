from typing import Optional
from dataclasses import dataclass
from openai import AsyncOpenAI

@dataclass
class AIResponse:
    text: str
    confidence: float
    category: str
    impact_score: float
    difficulty: str
    savings: dict
    tags: list[str]

class OpenAIEcoService:
    def __init__(self, api_key: str):
        self.client = AsyncOpenAI(api_key=api_key)

    async def generate_eco_advice(self, question: str) -> AIResponse:
        messages = [
            {"role": "system", "content": "You are an expert environmental consultant providing practical and effective eco-friendly advice. Analyze the user's question and provide detailed, actionable advice with environmental impact assessment."},
            {"role": "user", "content": f"Please provide eco-friendly advice for the following question, including category, impact score (1-10), difficulty level, and potential resource savings: {question}"}
        ]

        response = await self.client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            temperature=0.7,
            max_tokens=500
        )

        # Process the response and extract structured information
        response_text = response.choices[0].message.content
        
        # Parse the response to extract metadata
        # This is a simplified parsing logic - in production, you'd want more robust parsing
        lines = response_text.split('\n')
        advice = lines[0]  # First line is the main advice
        
        # Extract metadata from the response
        category = "general"  # default value
        impact_score = 5.0   # default value
        difficulty = "medium" # default value
        savings = {}
        tags = []
        
        for line in lines[1:]:
            if "Category:" in line:
                category = line.split("Category:")[1].strip()
            elif "Impact Score:" in line:
                try:
                    impact_score = float(line.split("Impact Score:")[1].strip().split('/')[0])
                except:
                    pass
            elif "Difficulty:" in line:
                difficulty = line.split("Difficulty:")[1].strip().lower()
            elif "Savings:" in line:
                savings_text = line.split("Savings:")[1].strip()
                savings = {"estimated": savings_text}
            elif "Tags:" in line:
                tags = [tag.strip() for tag in line.split("Tags:")[1].strip().split(',')]
        
        return AIResponse(
            text=advice,
            confidence=0.9,
            category=category,
            impact_score=impact_score,
            difficulty=difficulty,
            savings=savings,
            tags=tags
        )