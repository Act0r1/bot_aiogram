from aiogram import Dispatcher, types


async def echo(msg:types.Message):
    await msg.answer(msg.text) 



def register_echo(dp:Dispatcher):
    dp.register_message_handler(echo)
