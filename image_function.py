from openai_client import get_client

client=get_client()


def image_analyser_function(image_url,image_url_2,question):
    
    messages = {
        'role':'user','content':[
            {'type':'text','text':question},
            {'type':'image_url','image_url':{'url':image_url}},
            {'type':'image_url_2','image_url':{'url':image_url_2}}
        ]
    }
    response=client.chat.completions.create(messages=[messages],model='gpt-4o-mini')
    return response.choices[0].message.content