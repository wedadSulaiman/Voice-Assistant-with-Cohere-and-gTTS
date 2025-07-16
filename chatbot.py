import cohere

co = cohere.Client("Your API key.")

def get_bot_reply(user_input):
    prompt = f"رد على هذا النص باللغة العربية فقط: {user_input}"
    response = co.chat(message=prompt, temperature=0.7)
    return response.text
