import openai

openai.api_key = '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'

response = openai.Completion.create(
    engine="davinci",
    prompt="What color are strawberries?\n\nStrawberries are",
    temperature=0.9,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\n"]
    )
