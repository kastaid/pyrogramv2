#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from uuid import uuid4

import pyrogramv2
from pyrogramv2 import types
from ..object import Object


class InlineQueryResult(Object):
    """One result of an inline query.

    - :obj:`~pyrogramv2.types.InlineQueryResultCachedAudio`
    - :obj:`~pyrogramv2.types.InlineQueryResultCachedDocument`
    - :obj:`~pyrogramv2.types.InlineQueryResultCachedAnimation`
    - :obj:`~pyrogramv2.types.InlineQueryResultCachedPhoto`
    - :obj:`~pyrogramv2.types.InlineQueryResultCachedSticker`
    - :obj:`~pyrogramv2.types.InlineQueryResultCachedVideo`
    - :obj:`~pyrogramv2.types.InlineQueryResultCachedVoice`
    - :obj:`~pyrogramv2.types.InlineQueryResultArticle`
    - :obj:`~pyrogramv2.types.InlineQueryResultAudio`
    - :obj:`~pyrogramv2.types.InlineQueryResultContact`
    - :obj:`~pyrogramv2.types.InlineQueryResultDocument`
    - :obj:`~pyrogramv2.types.InlineQueryResultAnimation`
    - :obj:`~pyrogramv2.types.InlineQueryResultLocation`
    - :obj:`~pyrogramv2.types.InlineQueryResultPhoto`
    - :obj:`~pyrogramv2.types.InlineQueryResultVenue`
    - :obj:`~pyrogramv2.types.InlineQueryResultVideo`
    - :obj:`~pyrogramv2.types.InlineQueryResultVoice`
    """

    def __init__(
        self,
        type: str,
        id: str,
        input_message_content: "types.InputMessageContent",
        reply_markup: "types.InlineKeyboardMarkup"
    ):
        super().__init__()

        self.type = type
        self.id = str(uuid4()) if id is None else str(id)
        self.input_message_content = input_message_content
        self.reply_markup = reply_markup

    async def write(self, client: "pyrogramv2.Client"):
        pass
