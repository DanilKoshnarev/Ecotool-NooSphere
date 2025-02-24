class EcoAdviceRepository:
    def __init__(self):
        self.advice_store = {}

    async def save(self, advice):
        self.advice_store[advice.id] = advice
        return advice

    async def get(self, advice_id):
        return self.advice_store.get(advice_id)

    async def get_popular_questions(self):
        # Implement logic to return frequently asked questions
        return [
            {
                "question": "Як зменшити споживання електроенергії?",
                "answer": "Використовуйте LED-лампи, вимикайте прилади з режиму очікування, встановіть розумні термостати."
            },
            {
                "question": "Як правильно сортувати сміття?",
                "answer": "Розділяйте відходи на органічні, пластик, папір, скло та метал. Дізнайтеся про місцеві правила переробки."
            }
        ]