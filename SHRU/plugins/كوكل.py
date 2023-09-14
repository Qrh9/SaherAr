#========================#
#       SHRU  - ll1ilt   #  
# =======================#

import io
import os
import re
import urllib
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from PIL import Image
from search_engine_parser import BingSearch, GoogleSearch, YahooSearch
from search_engine_parser.core.exceptions import NoResultsOrTrafficError

from SHRU import Qrh9

from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.functions import deEmojify
from ..helpers.utils import reply_id
from . import BOTLOG, BOTLOG_CHATID

opener = urllib.request.build_opener()
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
opener.addheaders = [("User-agent", useragent)]

plugin_category = "tools"


async def ParseSauce(googleurl):
    """Parse/Scrape the HTML code for the info we want."""
    source = opener.open(googleurl).read()
    soup = BeautifulSoup(source, "html.parser")
    results = {"similar_images": "", "best_guess": ""}
    try:
        for similar_image in soup.findAll("input", {"class": "gLFyf"}):
            url = "https://www.google.com/search?tbm=isch&q=" + urllib.parse.quote_plus(
                similar_image.get("value")
            )
            results["similar_images"] = url
    except BaseException:
        pass
    for best_guess in soup.findAll("div", attrs={"class": "r5a77d"}):
        results["best_guess"] = best_guess.get_text()
    return results


async def scam(results, lim):
    single = opener.open(results["similar_images"]).read()
    decoded = single.decode("utf-8")
    imglinks = []
    counter = 0
    pattern = r"^,\[\"(.*[.png|.jpg|.jpeg])\",[0-9]+,[0-9]+\]$"
    oboi = re.findall(pattern, decoded, re.I | re.M)
    for imglink in oboi:
        counter += 1
        if counter <= int(lim):
            imglinks.append(imglink)
        else:
            break
    return imglinks


@Qrh9.ar_cmd(
    pattern="كوكل بحث ([\s\S]*)",
    command=("كوكل بحث", plugin_category),
    info={
        "header": "Google search command.",
        "flags": {
            "-l": "for number of search results.",
            "-p": "for choosing which page results should be showed.",
        },
        "usage": [
            "{tr}gs <flags> <query>",
            "{tr}gs <query>",
        ],
        "examples": [
            "{tr}gs catuserbot",
            "{tr}gs -l6 catuserbot",
            "{tr}gs -p2 catuserbot",
            "{tr}gs -p2 -l7 catuserbot",
        ],
    },
)
async def gsearch(q_event):
    "Google search command."
    catevent = await edit_or_reply(q_event, "**᯽︙ جـاري البحـث انتـظر**")
    match = q_event.pattern_match.group(1)
    page = re.findall(r"-p\d+", match)
    lim = re.findall(r"-l\d+", match)
    try:
        page = page[0]
        page = page.replace("-p", "")
        match = match.replace("-p" + page, "")
    except IndexError:
        page = 1
    try:
        lim = lim[0]
        lim = lim.replace("-l", "")
        match = match.replace("-l" + lim, "")
        lim = int(lim)
        if lim <= 0:
            lim = int(5)
    except IndexError:
        lim = 5
    #     smatch = urllib.parse.quote_plus(match)
    smatch = match.replace(" ", "+")
    search_args = (str(smatch), int(page))
    gsearch = GoogleSearch()
    bsearch = BingSearch()
    ysearch = YahooSearch()
    try:
        gresults = await gsearch.async_search(*search_args)
    except NoResultsOrTrafficError:
        try:
            gresults = await bsearch.async_search(*search_args)
        except NoResultsOrTrafficError:
            try:
                gresults = await ysearch.async_search(*search_args)
            except Exception as e:
                return await edit_delete(catevent, f"**᯽︙ خطـأ  :**\n`{str(e)}`", time=10)
    msg = ""
    for i in range(lim):
        if i > len(gresults["links"]):
            break
        try:
            title = gresults["titles"][i]
            link = gresults["links"][i]
            desc = gresults["descriptions"][i]
            msg += f"👉[{title}]({link})\n`{desc}`\n\n"
        except IndexError:
            break
    await edit_or_reply(
        catevent,
        "**᯽︙ نتـائج البحـث :**\n`" + match + "`\n\n**᯽︙ النتائـج  :**\n" + msg,
        link_preview=False,
        aslink=True,
        linktext=f"**᯽︙ نتائـج البحـث ** `{match}` :",
    )
    if BOTLOG:
        await q_event.client.send_message(
            BOTLOG_CHATID,
            "**᯽︙ نتـائج بحـث جـوجـل  **" + match + "**تم تنـفيذهـا بنجـاح **",
        )


@Qrh9.ar_cmd(
    pattern="البحث عن$",
    command=("البحث عن", plugin_category),
    info={
        "header": "Google reverse search command.",
        "description": "reverse search replied image or sticker in google and shows results.",
        "usage": "{tr}grs",
    },
)
async def _(event):
    "Google Reverse Search"
    start = datetime.now()
    OUTPUT_STR = "**᯽︙ يجـب الـرد على صـورة للـبحث عـنها **"
    if event.reply_to_msg_id:
        catevent = await edit_or_reply(event, "**᯽︙ يـتم الـبحث عـن الـصورة انتـظر** ⏱")
        previous_message = await event.get_reply_message()
        previous_message_text = previous_message.message
        BASE_URL = "http://www.google.com"
        if previous_message.media:
            downloaded_file_name = await event.client.download_media(
                previous_message, Config.TMP_DOWNLOAD_DIRECTORY
            )
            SEARCH_URL = "{}/searchbyimage/upload".format(BASE_URL)
            multipart = {
                "encoded_image": (
                    downloaded_file_name,
                    open(downloaded_file_name, "rb"),
                ),
                "image_content": "",
            }
            # https://stackoverflow.com/a/28792943/4723940
            google_rs_response = requests.post(
                SEARCH_URL, files=multipart, allow_redirects=False
            )
            the_location = google_rs_response.headers.get("Location")
            os.remove(downloaded_file_name)
        else:
            previous_message_text = previous_message.message
            SEARCH_URL = "{}/searchbyimage?image_url={}"
            request_url = SEARCH_URL.format(BASE_URL, previous_message_text)
            google_rs_response = requests.get(request_url, allow_redirects=False)
            the_location = google_rs_response.headers.get("Location")
        await catevent.edit("**᯽︙ تم العثـور على نتيجـة بحـث جـوجـل **")
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0"
        }
        response = requests.get(the_location, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        # document.getElementsByClassName("r5a77d"): PRS
        try:
            prs_div = soup.find_all("div", {"class": "r5a77d"})[0]
            prs_anchor_element = prs_div.find("a")
            prs_url = BASE_URL + prs_anchor_element.get("href")
            prs_text = prs_anchor_element.text
            # document.getElementById("jHnbRc")
            img_size_div = soup.find(id="jHnbRc")
            img_size = img_size_div.find_all("div")
        except Exception:
            return await edit_delete(
                catevent, "**᯽︙ غيـر قـادر على إيجـاد صـور مـشابهـة **"
            )
        end = datetime.now()
        ms = (end - start).seconds
        OUTPUT_STR = """{img_size}
<b>᯽︙ امـكانيـة البـحث ذات الـصلة  : </b> <a href="{prs_url}">{prs_text}</a> 
<b>᯽︙ مزيـد من المعلومـات  : </b> إفتـح هـذا  <a href="{the_location}">Link</a> 
<i>᯽︙ تم الـتعـرف في {ms} من الـثواني ⏱</i>""".format(
            **locals()
        )
    else:
        catevent = event
    await edit_or_reply(catevent, OUTPUT_STR, parse_mode="HTML", link_preview=False)




@Qrh9.ar_cmd(
    pattern="كوكل(?:\s|$)([\s\S]*)",
    command=("كوكل", plugin_category),
    info={
        "header": "To get link for google search",
        "description": "Will show google search link as button instead of google search results try {tr}gs for google search results.",
        "usage": [
            "{tr}كوكل",
        ],
    },
)
async def google_search(event):
    "Will show you google search link of the given query."
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if not input_str:
        return await edit_delete(
            event, "**᯽︙ يجـب إعطـاء معلومـات عن البحـث **"
        )
    input_str = deEmojify(input_str).strip()
    if len(input_str) > 195 or len(input_str) < 1:
        return await edit_delete(
            event,
            "**᯽︙ لقـد تجـاوز اسطر البحـث عـن 200 حـرف أو أن حروف البحـث فـارغه ️**",
        )
    query = "#12" + input_str
    results = await event.client.inline_query("@StickerizerBot", query)
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    await event.delete()
