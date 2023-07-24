import requests
from telethon import events
from ..helpers.functions import edit_or_reply
from SHRU import l313l
plugin_category = "utils"

@l313l.ar_cmd(
    pattern=f"حسابات(?:\s|$)([\s\S]*)",
    command=("حسابات", plugin_category),
    info={
        "header": "Search for accounts related to the name.",
        "usage": "{tr}حسابات (name)",
    },
)
async def search_accounts(event):
    name = event.pattern_match.group(1).strip()
    if not name:
        return await edit_or_reply(event, "⌔∮ يرجى تحديد الاسم الذي تبحث عنه.")
    
    headers = {
        'authority': 'api.hexomate.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://discoverprofile.com',
        'referer': 'https://discoverprofile.com/',
        'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 12; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    }

    json_data = {
        'source': name,
        'type': 'name',
        'rescan': False,
    }

    try:
        response = requests.post('https://api.hexomate.com/discoverProfile', headers=headers, json=json_data).json()
        profiles = "\n".join(profile["url"] for profile in response.get("profile", []))
        if not profiles:
            return await edit_or_reply(event, "⌔∮ لم يتم العثور على حسابات متعلقة بهذا الاسم.")
        
        await edit_or_reply(event, f"⌔∮ الحسابات المتعلقة بالاسم {name}:\n{profiles}")
    except requests.exceptions.RequestException as e:
        await edit_or_reply(event, f"⌔∮ حدث خطأ أثناء الاستعلام عن البحث: {e}")
