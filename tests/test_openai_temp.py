import os
import pytest
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    pytest.skip("OPEN_API_KEY not set", allow_module_level=True)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

TEST_STRING = "Suggest test cases for a login page."


def test_open_ai_temp_02():
    response = create_open_ai_response(0.2)
    assert response.output_text


def create_open_ai_response(temp, inputString = TEST_STRING):
    return client.responses.create(
        model="gpt-4.1",
        input=input_string,
        temperature=temp
    )