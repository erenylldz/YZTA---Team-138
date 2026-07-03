from .schemas import MOCK_ANALYSIS_RESPONSE


def call_llm(prompt, idea_text):
    response = MOCK_ANALYSIS_RESPONSE.copy()
    response["idea_summary"] = idea_text
    return response