# src/ai_module.py
import google.generativeai as genai
from config import GOOGLE_GEMINI_API_KEY
import random
import logging

# Настройка логирования
logger = logging.getLogger(__name__)

class AIHelper:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("API-ключ для Google Gemini не предоставлен.")
        genai.configure(api_key=api_key)
        # Настройка модели. Вы можете выбрать другую модель, например 'gemini-1.0-pro'
        self.model = genai.GenerativeModel('gemini-1.5-flash') # Используем более быструю модель для экономии квот

    def get_idea_for_child(self, category):
        """Генерирует идею для ребенка по заданной категории."""
        try:
            # TODO: Реализовать реальный вызов к API Google Gemini
            # Это заглушка с улучшенной логикой
            ideas = {
                "творчество": ["Нарисуй свой собственный волшебный мир!", "Создай комикс о своих друзьях!", "Слепи из пластилина любимого персонажа."],
                "учёба": ["Узнай 5 интересных фактов о динозаврах.", "Почитай одну главу из интересной книги.", "Сделай карточку с новым английским словом."],
                "дом": ["Помоги накрыть на стол.", "Разбери свою одежду в шкафу.", "Полей цветы на подоконнике."],
                "спорт": ["Сделай 10 приседаний и 5 отжиманий. Ты сможешь!", "Потанцуй любимую песню в течение 2 минут.", "Сделай упражнение 'берпи' 3 раза."],
                "досуг": ["Сыграй в настольную игру с семьей.", "Посмотри короткий познавательный ролик.", "Составь список фильмов, которые хочешь посмотреть."]
            }
            category_ideas = ideas.get(category, ["Просто улыбнись этому дню!", "Поделись добрым словом с кем-то сегодня!"])
            return random.choice(category_ideas)
        except Exception as e:
            logger.error(f"Ошибка при генерации идеи для категории '{category}': {e}")
            return "У меня пока нет идей для этой категории. Попробуй другую!"

    def analyze_mood_data(self, mood_history):
        """Анализирует историю настроений и дает совет родителю."""
        try:
            # TODO: Реализовать аналитику и вызов к API Google Gemini
            # Это заглушка с улучшенной логикой
            if not mood_history:
                return "Недостаточно данных для анализа."
            # mood_history это список кортежей (mood_score, tracked_at)
            scores = [item[0] for item in mood_history]
            avg_mood = sum(scores) / len(scores)
            if avg_mood < 2.5:
                return "Замечено частое плохое настроение. Рекомендую поговорить с ребенком о его чувствах."
            elif avg_mood > 4:
                 return "У ребенка очень хорошее настроение! Продолжайте в том же духе!"
            return "Настроение ребенка в целом стабильное. Продолжайте поддерживать его!"
        except Exception as e:
            logger.error(f"Ошибка при анализе настроения: {e}")
            return "Произошла ошибка при анализе настроения. Попробуйте позже."

    def suggest_daily_challenge(self):
        """Предлагает ежедневный челлендж."""
        try:
            # TODO: Реализовать вызов к API Google Gemini
            # Это заглушка
            challenges = [
                "Сделай доброе дело для кого-то.",
                "Выучи 3 новых слова на иностранном языке.",
                "Потренируйся в течение 15 минут.",
                "Прочитай 10 страниц книги.",
                "Нарисуй что-нибудь новое."
            ]
            return random.choice(challenges)
        except Exception as e:
            logger.error(f"Ошибка при генерации челленджа: {e}")
            return "Попробуй придумать свой интересный челлендж на сегодня!"

    def give_parent_advice(self, child_name, activity_summary):
        """Дает совет родителю на основе активности ребенка."""
        try:
             # TODO: Реализовать вызов к API Google Gemini
            # Это заглушка с улучшенной логикой
            advice_templates = [
                f"{child_name} был(а) очень активен(а) сегодня! Похвалите его(её) за старания.",
                f"Похоже, {child_name} мог(ла) бы больше заниматься спортом. Предложите веселую активность!",
                f"{child_name} хорошо справляется с задачами. Поддержите его(её) и предложите новую цель!",
                f"У {child_name} был продуктивный день. Расспросите о его(её) успехах!"
            ]
            return random.choice(advice_templates)
        except Exception as e:
            logger.error(f"Ошибка при генерации совета для родителя: {e}")
            return "Попробуйте сами пообщаться с ребенком о его днях!"

# Инициализация помощника с ключом из config.py
# В GitHub Actions ключ будет браться из environment variable
ai_helper = AIHelper(GOOGLE_GEMINI_API_KEY) if GOOGLE_GEMINI_API_KEY else None
