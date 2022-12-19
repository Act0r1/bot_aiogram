from aiogram import Dispatcher, types


async def admins(msg: types.Message):
    await msg.reply("Hello admin")


def reg_admin(dp: Dispatcher):
    """
    Register admins handlers.
    :param: dp -> Dispatcher
    """
    dp.register_message_handler(admins)
