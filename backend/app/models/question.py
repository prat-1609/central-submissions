"""
app/models/question.py — backward-compatibility shim.
Question models moved to question_model.py.
"""
from app.models.question_model import Subject, Question, question_subjects  # noqa: F401
