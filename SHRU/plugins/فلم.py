#SHRU ©
#By Reda telegram: @rd0r0

from telethon.tl.custom import Button
from cryptography.fernet import Fernet
import requests
from html_telegraph_poster.upload_images import upload_image
import random
from SHRU import Qrh9
import asyncio
from ..core.managers import edit_delete, edit_or_reply

valid_extensions = [".jpg", ".jpeg", ".png", ".gif"]

ek = "ayD8OiHzrmRxNWUlhbgXY__xzObPjLxd87kj2ipE9wk="
ea = "gAAAAABkkpU1sfechRmGwMJB3XPOylswN2TwCioE9-EBmNudPKr537aSI9Tf_tVyB39nv1p_5Oro1ZGIG2cNduPbF-fhk4onPBmDOJSP3fwaSznl1Mu8FFsEzKPh4qXeWT8TgUF4nma2"

@Qrh9.ar_cmd(pattern="فلم")
async def rfilm(event):
    await event.edit("يرجى الانتظار جاري البحث عن فيلم...")
    dk = ek.encode()
    nk = ea.encode()
    cipher_suite = Fernet(dk)
    api_key = cipher_suite.decrypt(nk).decode()
    url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}"
    response = requests.get(url)
    top_movies = response.json()["results"]
    random_movie = random.choice(top_movies)
    movie_id = random_movie["id"]
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=ar"
    response = requests.get(url)
    movie = response.json()
    movied = movie["overview"]
    movien = random_movie["title"]
    rating = movie["vote_average"]
    year = movie["release_date"][:4]
    poster_path = movie["poster_path"]
    moviep = f"https://image.tmdb.org/t/p/w500{poster_path}"
    if movied is None:
        movied = "-"
    if any(moviep.endswith(ext) for ext in valid_extensions):
        try:
            moviep = upload_image(moviep)
        except BaseException:
            moviep = None
    else:
        moviep = "https://telegra.ph/file/15480332b663adae49205.jpg"

    moviet = f"الاسم: {movien}\nالسنة: {year}\nالتقييم: {rating}\nالقصة:\n{movied}"
    
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={api_key}"
    response = requests.get(url)
    movie_data = response.json()
    buttons = []
    if 'results' in movie_data:
        for video in movie_data["results"]:
            url = "https://www.youtube.com/watch?v={}".format(video["key"])
            x = [Button.url("مشاهدة الفيديو",url)]
            
            buttons.append(x)

    await event.delete()
    try:
        await Qrh9.tgbot.send_message(
            event.chat_id,
            moviet,
            buttons=buttons,
            file=moviep,
            force_document=False,
            link_preview=False,
        )
    except ValueError:
        await Qrh9.send_message(
            event.chat_id,
            moviet,
            file=moviep,
            force_document=False,
            link_preview=False,
        )


    
#Reda

@Qrh9.ar_cmd(pattern="مسلسل")
async def rfilm(event):
    await event.edit("يرجى الانتضار جاري البحث على مسلسل...")
    dk = ek.encode()
    nk = ea.encode()
    cipher_suite = Fernet(dk)
    api_key = cipher_suite.decrypt(nk).decode()
    url = f"https://api.themoviedb.org/3/tv/top_rated?api_key={api_key}"
    response = requests.get(url)
    top_series = response.json()["results"]
    random_series = random.choice(top_series)
    series_id = random_series["id"]
    url = f"https://api.themoviedb.org/3/tv/{series_id}?api_key={api_key}&language=ar"
    response = requests.get(url)
    series = response.json()
    sern = random_series["name"]
    serr = series["vote_average"]
    sers = series["overview"]
    sersn = series["number_of_seasons"]
    poster_path = random_series["poster_path"]
    serp = f"https://image.tmdb.org/t/p/w500{poster_path}"
    if any(serp.endswith(ext) for ext in valid_extensions):
        try:
            serp = upload_image(serp) 
        except BaseException:
            serp = None
    else:
        serp = "https://telegra.ph/file/15480332b663adae49205.jpg"
    if serp is None:
        serp = "https://telegra.ph/file/15480332b663adae49205.jpg"
    sm = f"الاسم: {sern}\nالتقييم: {serr}\nعدد المواسم: {sersn}\nالقصة:\n{sers}"
    url = f"https://api.themoviedb.org/3/tv/{series_id}/videos?api_key={api_key}"
    response = requests.get(url)
    series_data = response.json()
    buttons = []
    if 'results' in series_data:
        for video in series_data["results"]:
            url = "https://www.youtube.com/watch?v={}".format(video["key"])
            x = [Button.url("مشاهدة الفيديو",url)]
            buttons.append(x)
    await event.delete()
    try:
        await Qrh9.tgbot.send_message(
            event.chat_id,
            sm,
            buttons=buttons,
            file=serp,
            force_document=False,
            link_preview=False,
        )
    except ValueError:
        await Qrh9.send_message(
            event.chat_id,
            sm,
            file=serp,
            force_document=False,
            link_preview=False,
        )