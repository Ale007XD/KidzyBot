import openai
from config import OPENAI_API_KEY

class AIHelper:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("API-ключ для OpenAI не предоставлен.")
        openai.api_key = api_key

    def get_idea_for_child(self, category):
        ideas = {
            "творчество": "Нарисуй свой собственный волшебный мир!",
            "учёба": "Узнай 5 интересных фактов о динозаврах.",
            "спорт": "Сделай 10 приседаний и 5 отжиманий. Ты сможешь!",
        }
        return ideas.get(category, "Просто улыбнись этому дню!")

    def analyze_mood_data(self, mood_history):
        if not mood_history:
            return "Недостаточно данных для анализа."
        
        avg_mood = sum(item[0] for item in mood_history) / len(mood_history)
        if avg_mood < 2.5:
            return "Замечено частое плохое настроение. Рекомендую поговорить с ребенком о его чувствах."
        return "Настроение ребенка в целом стабильное. Продолжайте в том же духе!"

ai_helper = AIHelper(OPENAI_API_KEY) if OPENAI_API_KEY else None
