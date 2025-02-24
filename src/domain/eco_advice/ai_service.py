from typing import List
import torch
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

class AIService:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")
        self.model = AutoModelForQuestionAnswering.from_pretrained("bert-base-multilingual-cased")
        self.eco_knowledge_base = {
            "енергозбереження": {
                "context": """
                Енергозбереження є ключовим аспектом екологічної відповідальності. 
                Використання LED-ламп, сонячних панелей та енергоефективних приладів 
                може значно зменшити споживання електроенергії.
                """,
                "impact_score": 9,
                "difficulty": "середня",
                "savings": "до 40% енергії"
            },
            "відходи": {
                "context": """
                Правильна утилізація відходів та їх сортування є важливими для 
                збереження довкілля. Компостування органічних відходів та переробка 
                пластику, паперу і скла значно зменшують навантаження на полігони.
                """,
                "impact_score": 8,
                "difficulty": "легка",
                "savings": "зменшення сміття на 70%"
            },
            # Add more categories...
        }

    async def generate_eco_advice(self, question: str) -> dict:
        best_answer = ""
        max_score = 0
        category = ""
        
        for cat, data in self.eco_knowledge_base.items():
            inputs = self.tokenizer(
                question,
                data["context"],
                return_tensors="pt",
                padding=True,
                truncation=True
            )
            
            outputs = self.model(**inputs)
            score = torch.max(outputs.start_logits).item()
            
            if score > max_score:
                max_score = score
                category = cat
                best_answer = self._extract_answer(
                    inputs, outputs, data["context"]
                )

        return {
            "text": best_answer,
            "confidence": max_score,
            "category": category,
            "impact_score": self.eco_knowledge_base[category]["impact_score"],
            "difficulty": self.eco_knowledge_base[category]["difficulty"],
            "savings": self.eco_knowledge_base[category]["savings"],
            "tags": [category]
        }

    def _extract_answer(self, inputs, outputs, context):
        # Answer extraction logic here
        return context  # Simplified for example