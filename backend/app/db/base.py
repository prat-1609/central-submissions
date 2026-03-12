# app/db/base.py

# 1. Import the foundation (The Concrete Slab)
from app.db.base_class import Base  # noqa

# 2. Import every model (The Blueprints) to register them with the Metadata
from app.models.user_model import User  # noqa
from app.models.question_model import Subject, Question, question_subjects  # noqa
from app.models.interview_model import InterviewSession, InterviewQuestion, Answer  # noqa

# After these imports, Base.metadata now contains the
# definitions for all 7 of your tables.