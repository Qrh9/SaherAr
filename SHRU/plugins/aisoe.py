import os
import requests
import openai  # You need to install the OpenAI Python library: pip install openai
from telethon import events, utils
from SHRU import l313l
# Set your OpenAI API key here
openai.api_key = "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"

# Set your clarifai API key here
clarifai_api_key = "a5987016426644ef81de76dee40ff5f0"

plugin_category = "utils"

@l313l.ar_cmd(
    pattern="شنوهاي(?:\s|$)([\s\S]*)",
    command=("شنوهاي", plugin_category),
    info={
        "header": "AI-based image recognition bot.",
        "usage": "{tr}شنوهاي <image description>",
        "examples": "{tr}شنوهاي A wolf standing on the moon",
    },
)
async def image_recognition(event):
    reply = await event.get_reply_message()
    if not reply or not reply.file:
        return await event.edit("⌔∮ يرجى الرد على صورة لتوصيلها لخدمه التعرف")
    
    # Download the image
    image_path = await event.client.download_media(reply)
    
    # Use the "clarifai" API to analyze the content of the image
    try:
        response = requests.post(
            "https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs",
            headers={
                "Authorization": f"Key {clarifai_api_key}",
                "Content-Type": "application/json",
            },
            json={"inputs": [{"data": {"image": {"url": utils.get_display_name(reply.media)}}}]},
        ).json()
        concepts = response.get("outputs", [])[0].get("data", {}).get("concepts", [])
        tags = [concept["name"] for concept in concepts]
    except Exception as e:
        return await event.edit(f"⌔∮ حدث خطأ أثناء تحليل الصورة: {str(e)}")
    
    if not tags:
        return await event.edit("⌔∮ لم أتمكن من تحليل محتوى الصورة.")
    
    # Generate the AI text based on the user's description using GPT-3.5
    description = event.pattern_match.group(1)
    prompt = f"An AI-based image recognition bot.\nPlease generate an image of: {description}"
    try:
        ai_response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            temperature=0.7,
            max_tokens=200,
        )
        ai_text = ai_response.choices[0].text.strip()
    except Exception as e:
        return await event.edit(f"⌔∮ حدث خطأ أثناء توليد النص: {str(e)}")
    
    # Sending the AI-generated text as a message
    await event.edit(f"⌔∮ {ai_text}")
    
    # Sending the AI-generated image as a message
    await event.client.send_file(event.chat_id, image_path, caption=ai_text)

    # Delete the downloaded image
    os.remove(image_path)