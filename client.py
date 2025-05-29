from openai import OpenAI


# pip install OpenAI
# If you saved he key under the diffrent environments variable name,  you can do something like: 

client = OpenAI (api_key= "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" ) 


completion = client.chat.completions.create(
  model="gpt-4.1",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)