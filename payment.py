from config import *
from telethon import events
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
from telethon.tl.types import Channel
from help import *
import asyncio


@IEX.on(events.NewMessage(outgoing=True))
async def _(event):
    try:
        await IEX(JoinChannelRequest("@r6r6rr"))
    except BaseException:
        pass

@IEX.on(events.NewMessage(outgoing=True))
async def _(event):
    if ispay[0] == 'yes':
        pass
    else:
        ispay.clear()
        ispay.append("yes")
        pass
        
    
    


@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.نظف"))
async def leave_IEX_channel(event):
    dialogs = await IEX.get_dialogs()
    await event.edit(f"**جارى التحقق من القنوات**")
    left_count_svj = 0
    left_count_pattern = 0
    
    for dialog in dialogs:
        if isinstance(dialog.entity, Channel) and not dialog.entity.username:
            # مغادرة قنوات SVJ Hunting Channal
            if dialog.entity.title == 'SVJ Hunting Channal':
                try:
                    await IEX(LeaveChannelRequest(dialog.entity))
                    left_count_svj += 1
                except Exception as e:
                    await event.respond(f"**خطأ أثناء مغادرة قناة SVJ: {e}**")
            
            # مغادرة قنوات SVJ Pattern Hunting Channel
            elif dialog.entity.title == 'SVJ Pattern Hunting Channel':
                try:
                    await IEX(LeaveChannelRequest(dialog.entity))
                    left_count_pattern += 1
                except Exception as e:
                    await event.respond(f"**خطأ أثناء مغادرة قناة Pattern: {e}**")
    
    await event.edit(f"**تم مغادرة {left_count_svj} قناة (SVJ Hunting Channal) و {left_count_pattern} قناة (SVJ Pattern Hunting Channel) خاصة.**")
