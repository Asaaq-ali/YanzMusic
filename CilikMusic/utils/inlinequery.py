#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="إيقاف مؤقــتاً",
            description=f" لإيقاف التشــغيل مؤقتاً.",
            thumb_url="https://telegra.ph/file/c0a1c789def7b93f13745.png",
            input_message_content=InputTextMessageContent("قف"),
        ),
        InlineQueryResultArticle(
            title="إستــئناف",
            description=f" للأستمرار ومواصلة تشغيل الاغنيه .",
            thumb_url="https://telegra.ph/file/02d1b7f967ca11404455a.png",
            input_message_content=InputTextMessageContent("واصل"),
        ),
        InlineQueryResultArticle(
            title="كتم",
            description=f"لكتم صوت البوت في المكالمه .",
            thumb_url="https://telegra.ph/file/66516f2976cb6d87e20f9.png",
            input_message_content=InputTextMessageContent("اسكت"),
        ),
        InlineQueryResultArticle(
            title="الغاء كتم",
            description=f"لالغاء كـــتم البوت في المكالمه .",
            thumb_url="https://telegra.ph/file/3078794f9341ffd582e18.png",
            input_message_content=InputTextMessageContent("تكلم"),
        ),
        InlineQueryResultArticle(
            title="تخطي",
            description=f"لتخطي الاغنــية او الانتقال الى الاغنيه التاليه بقائمة التشغيل ",
            thumb_url="https://telegra.ph/file/98b88e52bc625903c7a2f.png",
            input_message_content=InputTextMessageContent("تخطي"),
        ),
        InlineQueryResultArticle(
            title="لايقاف التشغيل",
            description="لإيقاف التشــغيل في المكالمه وانهاء الاغنيه.",
            thumb_url="https://telegra.ph/file/d2eb03211baaba8838cc4.png",
            input_message_content=InputTextMessageContent("توقف"),
        ),
        InlineQueryResultArticle(
            title="عشوائي",
            description="لتشغيل عشوائي.",
            thumb_url="https://telegra.ph/file/7f6aac5c6e27d41a4a269.png",
            input_message_content=InputTextMessageContent("عشوائي"),
        ),
        InlineQueryResultArticle(
            title="لتقدم",
            description="لتقدم الاغنيه ١٠ ثواني.",
            thumb_url="https://telegra.ph/file/cd25ec6f046aa8003cfee.png",
            input_message_content=InputTextMessageContent("/seek 10"),
        ),
        InlineQueryResultArticle(
            title="تكرار",
            description="لتكرار الاغنيه مرة اخرى ",
            thumb_url="https://telegra.ph/file/081c20ce2074ea3e9b952.png",
            input_message_content=InputTextMessageContent("تكرار 1"),
        ),
    ]
)
