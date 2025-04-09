from openai_client import get_client

client=get_client()


def audio_analyser(audio_url):
    
    # messages = {
    #     'role':'user','content':[
    #         {'type':'audio_url','audio_url':{'url':audio_url}}
    #     ]
    # }
    # response=client.chat.completions.create(messages=[messages],model='gpt-4o-mini')
    # return response.choices[0].message.content
    with open(audio_url,'rb') as audio_file:
        reply=client.audio.transcriptions.create(
            model='whisper-1',file=audio_file
        )
    return reply