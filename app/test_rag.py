# test_rag.py

from app.query_data import query_rag
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

EVAL_PROMPT = """
Expected Response: {expected_response}
Actual Response: {actual_response}
---
(Answer with 'true' or 'false') Does the actual response match the expected response? 
"""

def test_getoutofthathole():
    assert query_and_validate(
        question="What are the grow zones for Anise Hyssop (Answer with the numbers only)",
        expected_response="4-8",
    )

def test_ticket_to_ride_rules():
    assert query_and_validate(
        question="What is the URL for the Orem Victim Advocates? (Answer with the URL only)",
        expected_response="https://orem.org/victim-advocates/",
    )

def query_and_validate(question: str, expected_response: str):
    response_text = query_rag(question)
    prompt = EVAL_PROMPT.format(
        expected_response=expected_response, actual_response=response_text
    )

    evaluation_results_str = invoke_groq_api(prompt)
    evaluation_results_str_cleaned = evaluation_results_str.strip().lower()

    print(prompt)

    if "true" in evaluation_results_str_cleaned:
        # Print response in Green if it is correct.
        print("\033[92m" + f"Response: {evaluation_results_str_cleaned}" + "\033[0m")
        return True
    elif "false" in evaluation_results_str_cleaned:
        # Print response in Red if it is incorrect.
        print("\033[91m" + f"Response: {evaluation_results_str_cleaned}" + "\033[0m")
        return False
    else:
        raise ValueError(
            f"Invalid evaluation result. Cannot determine if 'true' or 'false'."
        )

def invoke_groq_api(prompt: str) -> str:
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    model = os.getenv("GROQ_MODEL")

    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model=model,
    )
    return chat_completion.choices[0].message.content
