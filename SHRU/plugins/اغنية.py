import asyncio
import base64
import io
import urllib.parse
import os
import mutagen
import requests
from bs4 import BeautifulSoup
from pathlib import Path
import telethon
from pydub import AudioSegment
from ShazamAPI import Shazam
from telethon import types
from telethon.errors.rpcerrorlist import YouBlockedUserError, ChatSendMediaForbiddenError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from validators.url import url
from telethon import types
from moviepy.editor import VideoFileClip
from shazamio import Shazam
from telethon import events
from telethon.tl.types import Message, InputMediaAudio, InputMediaVideo
from pytube import YouTube
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.functions import delete_conv, name_dl, song_dl, video_dl, yt_search
from ..helpers.tools import media_type
from ..helpers.utils import _catutils, reply_id
from . import Qrh9

plugin_category = "utils"
LOGS = logging.getLogger(__name__)

# =========================================================== #
#                           STRINGS                           #
# =========================================================== #
SONG_SEARCH_STRING = "<code>يجؤة الانتظار قليلا يتم البحث على المطلوب</code>"
SONG_NOT_FOUND = "<code>عذرا لا يمكنني ايجاد اي اغنيه مثل هذه</code>"
SONG_SENDING_STRING = "<code>جارِ الارسال انتظر قليلا...</code>"
# =========================================================== #
#                                                             #
# =========================================================== #

# =========================================================== #1


class SongPlugin(telethon.plugin.BasePlugin):
    """Plugin for downloading songs from YouTube and sending them to users."""

    @Qrh9.ar_cmd(
        pattern="بحث(320)?(?:\s|$)([\s\S]*)",
        command=("بحث", plugin_category),
        info={
            "header": "To get songs from youtube.",
            "description": "Basically this command searches youtube and send the first video as audio file.",
            "flags": {
                "320": "if you use song320 then you get 320k quality else 128k quality",
            },
            "usage": "{tr}song <song name>",
            "examples": "{tr}song memories song",
        },
    )
    async def song(self, event: events.NewMessage, progress_bar: bool = False):
        """Downloads a song from YouTube and sends it to the user."""

        # Get the song name from the command.
        song_name = event.pattern_match.group(1)

        # Search for the song on YouTube.
        youtube = YouTube(song_name)

        # Get the highest quality stream.
        stream = youtube.streams.get_highest_resolution()

        # Download the stream.
        try:
            stream.download(progress_bar=progress_bar)
        except Exception as e:
            await event.reply(f'Sorry, an error occurred while downloading the song: {e}')
            return

        # Get the file name of the downloaded file.
        file_name = stream.default_filename

        # Check if the file is an audio file.
        if file_name.endswith('.mp3'):
            # Send the audio file to the user.
            await event.client.send_file(
                event.chat_id,
                file_name,
                force_document=False,
                caption=f'**Song:** {song_name}',
                supports_streaming=True,
                reply_to=event.message.id,
            )

            # Delete the original message.
            await event.client.delete_messages(event.chat_id, event.message.id)

        # Check if the file is a video file.
        elif file_name.endswith('.mp4'):
            # Send the video file to the user.
            await event.client.send_file(
                event.chat_id,
                file_name,
                force_document=False,
                caption=f'**Song:** {song_name}',
                supports_streaming=True,
                reply_to=event.message.id,
            )

            # Delete the original message.
            await event.client.delete_messages(event.chat_id, event.message.id)

        # If the file is not an audio or video file, send a message to the user.
        else:
            await event.reply('Sorry, I can only download audio and video files.')

        # Delete the downloaded file.
        finally:
            os.remove(file_name)

# =========================================================== #2
@Qrh9.ar_cmd(pattern="اسم الاغنية$")
async def shazamcmd(event):
    reply = await event.get_reply_message()
    mediatype = media_type(reply)
    if not reply or not mediatype or mediatype not in ["Voice", "Audio"]:
        return await edit_delete(
            event, "⌔∮ يرجى الرد على مقطع صوتي او بصمه للبحث عنها"
        )
    catevent = await edit_or_reply(event, "**⌔∮ يتم معالجه المقطع الصوتي  .**")
    try:
        for attr in getattr(reply.document, "attributes", []):
            if isinstance(attr, types.DocumentAttributeFilename):
                name = attr.file_name
        dl = io.FileIO(name, "a")
        await event.client.fast_download_file(
            location=reply.document,
            out=dl,
        )
        dl.close()
        mp3_fileto_recognize = open(name, "rb").read()
        shazam = Shazam(mp3_fileto_recognize)
        recognize_generator = shazam.recognizeSong()
        track = next(recognize_generator)[1]["track"]
    except Exception as e:
        LOGS.error(e)
        return await edit_delete(
            catevent, f"**⌔∮ لقد حدث خطأ ما اثناء البحث عن اسم الاغنيه:**\n__{e}__"
        )

    image = track["images"]["background"]
    song = track["share"]["subject"].replace(track["subtitle"], "Rio time's")
    await event.client.send_file(
        event.chat_id, image, caption=f"**الاغنية:** `{song}`", reply_to=reply
    )
    await catevent.delete


@Qrh9.ar_cmd(
    pattern="بحث2(?:\s|$)([\s\S]*)",
    command=("بحث2", plugin_category),
    info={
        "header": "To search songs and upload to telegram",
        "description": "Searches the song you entered in query and sends it quality of it is 320k",
        "usage": "{tr}song2 <song name>",
        "examples": "{tr}song2 memories song",
    },
)
async def _(event):
    "To search songs"
    song = event.pattern_match.group(1)
    chat = "@songdl_bot"
    reply_id_ = await reply_id(event)
    catevent = await edit_or_reply(event, SONG_SEARCH_STRING, parse_mode="html")
    async with event.client.conversation(chat) as conv:
        try:
            purgeflag = await conv.send_message("/start")
        except YouBlockedUserError:
            await edit_or_reply(
                catevent, "**Error:** Trying to unblock & retry, wait a sec..."
            )
            await catub(unblock("songdl_bot"))
            purgeflag = await conv.send_message("/start")
        await conv.get_response()
        await conv.send_message(song)
        hmm = await conv.get_response()
        while hmm.edit_hide is not True:
            await asyncio.sleep(0.1)
            hmm = await event.client.get_messages(chat, ids=hmm.id)
        baka = await event.client.get_messages(chat)
        if baka[0].message.startswith(
            ("I don't like to say this but I failed to find any such song.")
        ):
            await delete_conv(event, chat, purgeflag)
            return await edit_delete(
                catevent, SONG_NOT_FOUND, parse_mode="html", time=5
            )
        await catevent.edit(SONG_SENDING_STRING, parse_mode="html")
        await baka[0].click(0)
        await conv.get_response()
        await conv.get_response()
        music = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_file(
            event.chat_id,
            music,
            caption=f"<b>Title :- <code>{song}</code></b>",
            parse_mode="html",
            reply_to=reply_id_,
        )
        await catevent.delete()
        await delete_conv(event, chat, purgeflag)
