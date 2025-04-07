from llm_call import call_llm
from prompt import text_prompt
def classify_text(text):
    proompt=text_prompt(text)
    answer=call_llm(proompt)
    print(answer)