#GPT-4 Turbo integration with optimized token usage


from openai import OpenAI

client = OpenAI(
    api_key=api_key
)

def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # ✅ Use faster model
        messages=[
            {"role": "system", "content": "You are a helpful and concise AI assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=80,   # ✅ Short reply
        temperature=0.7
    )
    return response.choices[0].message.content
