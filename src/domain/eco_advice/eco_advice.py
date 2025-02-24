class EcoAdvice:
    def __init__(self):
        self.tips_database = {
            "energy": [
                "Install LED bulbs to reduce energy consumption by up to 80%",
                "Use natural light when possible and turn off lights in empty rooms",
                "Set your thermostat a few degrees lower in winter and higher in summer"
            ],
            "water": [
                "Install water-efficient fixtures in your bathroom and kitchen",
                "Collect rainwater for watering plants",
                "Fix leaky faucets and pipes promptly"
            ],
            "waste": [
                "Start composting kitchen scraps and yard waste",
                "Use reusable bags, containers, and water bottles",
                "Practice proper recycling and learn local recycling guidelines"
            ],
            "transport": [
                "Consider using public transportation or carpooling",
                "Maintain proper tire pressure for better fuel efficiency",
                "Consider switching to an electric or hybrid vehicle"
            ]
        }

    def get_advice(self, user_input):
        user_input = user_input.lower()
        response = []
        
        # Simple keyword matching
        if "energy" in user_input or "electricity" in user_input:
            response.extend(self.tips_database["energy"])
        if "water" in user_input:
            response.extend(self.tips_database["water"])
        if "waste" in user_input or "trash" in user_input or "garbage" in user_input:
            response.extend(self.tips_database["waste"])
        if "transport" in user_input or "car" in user_input or "travel" in user_input:
            response.extend(self.tips_database["transport"])
            
        # If no specific matches, provide general advice
        if not response:
            from random import sample
            all_tips = [tip for tips in self.tips_database.values() for tip in tips]
            response = sample(all_tips, 2)
            
        return "\n\n".join(response)