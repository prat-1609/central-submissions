"""
app/models/interview.py — backward-compatibility shim.
Interview models moved to interview_model.py.
"""
from app.models.interview_model import InterviewSession, InterviewQuestion, Answer  # noqa: F401