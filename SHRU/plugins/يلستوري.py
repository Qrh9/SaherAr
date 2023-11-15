from telethon import types
from telethon.tl.functions.stories import UploadMedia, UploadStory, GetStories
from telethon.tl.types import InputMessagesFilterDocument, InputMessagesFilterPhoto
import asyncio
import os
from SHRU import Qrh9
# Function to upload a story
async def upload_story(client, reply_to_message, caption=None):
    try:
        # Edit the reply message to indicate story uploading
        uploading_msg = await reply_to_message.edit(f"**Uploading story...**\n\n______________________")

        # Check if the replied message is a photo or a video
        if reply_to_message.photo:
            media = types.InputPhoto(
                id=reply_to_message.photo.id,
                access_hash=reply_to_message.photo.access_hash,
                file_reference=reply_to_message.photo.file_reference,
                thumb=types.InputDocument(
                    id=reply_to_message.photo.thumbs[0].id,
                    access_hash=reply_to_message.photo.thumbs[0].access_hash,
                    file_reference=reply_to_message.photo.thumbs[0].file_reference,
                    file_size=reply_to_message.photo.thumbs[0].file_size,
                    location=reply_to_message.photo.thumbs[0].location,
                    type=reply_to_message.photo.thumbs[0].type,
                ),
                size=reply_to_message.photo.size,
            )
        elif reply_to_message.video:
            media = types.InputDocument(
                id=reply_to_message.video.id,
                access_hash=reply_to_message.video.access_hash,
                file_reference=reply_to_message.video.file_reference,
                date=reply_to_message.video.date,
                mime_type=reply_to_message.video.mime_type,
                size=reply_to_message.video.size,
                dc_id=reply_to_message.video.dc_id,
                version=reply_to_message.video.version,
                attributes=reply_to_message.video.attributes,
            )
        else:
            return await uploading_msg.edit("Error: Only photos and videos are supported for stories.")

        # Upload the media to the user's story
        media_id = await client(UploadMedia(
            file=media,
            stickers=[],
            ttl_seconds=86400,  # Story lasts for 24 hours
        ))

        # Set the caption as the story description
        story_caption = caption or "**none**"

        # Upload the story
        await client(UploadStory(
            media=types.InputStoryMediaPhoto(
                id=media_id,
                lat=0.0,
                long=0.0,
                reply_markup=None,
                random_id=0,
            ),
            stickers=[],
            ttl_seconds=86400,
            geo_point=types.InputGeoPointEmpty(),
            reply_to=types.InputStoryReply(
                random_id=0,
                user_id=0,
            ),
            multiple=False,
            attached_sticker=None,
            poll=None,
            question=None,
            answer=None,
            viewer_id=0,
            story_id=0,
            # Add the story caption as the story text
            text=story_caption,
        ))

        # Get the newly uploaded story details
        uploaded_story = await client(GetStories(
            id=None,
            limit=1,
            offset_id=0,
            hash=0,
            emojis="",
            filter=InputMessagesFilterPhoto() if reply_to_message.photo else InputMessagesFilterDocument(),
        ))
        uploaded_story = uploaded_story.chats[0].messages[0]

        # Edit the reply message to indicate successful story upload
        await uploading_msg.edit(
            f"**New story uploaded!!**\n\n"
            f"```\n"
            f"Story length: {uploaded_story.media.duration} seconds\n"
            f"Story id: {uploaded_story.id}\n"
            f"Story description: {story_caption}\n"
            f"```\n"
            f"______________________"
        )

    except Exception as e:
        print(f"Error uploading story: {e}")
        await uploading_msg.edit("Error: Failed to upload story.")

# Command handler
@Qrh9.on(events.NewMessage(pattern=r"\.مرر", incoming=True))
async def story_upload_handler(event):
    if event.is_reply and event.reply_to_msg_id:
        await upload_story(Qrh9, await event.get_reply_message(), caption=event.text[len(".مرر"):].strip())
    else:
        await event.reply("Reply to a photo or video to upload it as a story with an optional caption.")