
def text_prompt(text):
    #takes a text to classify and returns a prompt for text classification
    instruction='is the underlying sentiment positive or negative'
    formatting='Positive or Negative'
    return f'Text:{text}\n Instruction: {instruction}\n Answer({formatting})'