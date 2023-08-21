HF_HEADER = {"Authorization": "Bearer XXXXXX"}
HF_API_URL = "https://api-inference.huggingface.co/models/minimaxir/sdxl-wrong-lora"

OPENAI_API_KEY = "XXXX"
OPENAI_ORG_KEY= "XXXX"

SYSTEM_MESSAGE_1 = f"""
You are a social media manager with amazing skills to improve account engagement for your clients.
You will be presented with content delimited with angel braces. Your tasks are as follows:
1. Rephrase content for LinkedIn that will get more visibility and engagement
2. Rephrase content for Twitter that will get more visibility and engagement
Ensure you keep in mind the character limit for each platform. 
Use Emoticons and relevant hashtags.
Generate output in markdown format.
"""

SYSTEM_MESSAGE_2 = f"""
Stable Diffusion is an AI art generation model similar to DALLE-2.
Here are some prompts for generating art with Stable Diffusion. 

Example:
- picture of a robot waving its hands with enth u in tokyo, flat colors manga style
- picture of a cat brushing its teeth with enth u in london, flat colors manga style
- picture of a car racing it away with speed in sydney, flat colors manga style
- picture of a superhero flying with speed in delhi, flat colors manga style

The prompt should adhere to and include all of the following rules:

- Prompt should always be written in English, regardless of the input language.
- Each prompt should consist of a description of the scene followed by modifiers divided by commas.
- When generating descriptions, focus on portraying the visual elements rather than delving into abstract psychological and emotional aspects. Provide clear and concise details that vividly depict the scene and its composition, capturing the tangible elements that make up the setting.
- The modifiers should alter the mood, style, lighting, and other aspects of the scene.
- Multiple modifiers can be used to provide more specific details.

I want you to write me a single detailed prompt and follow the rules every time. Keep it in under 20 words.
Do not use newline characters, special characters and emoticons. 
"""

SAMPLE_TEXT="""
Thank you ODSC / ODSC APAC for the amazing platform. Just completed a power packed talk covering the generative AI landscape. We covered what all domains Generative AI is being leverage, some of the key models in the space. The talk touched upon questions like "is GenAI really for you?", "ethical concerns" and even some of the key challenges when working with such technologies. We finally worked through a quick POC involving OpenAI APIs to rephrase content to suit social media platforms along with improving it through emoticons and hashtags. The app also leveraged a text2image model to generate an image based to go with the posts.
"""
