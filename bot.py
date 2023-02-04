import config
import texts
import openai
import aiogram
import asyncio
from aiogram.dispatcher import Dispatcher
from aiogram.types import Message
from aiogram import types


openai.api_key = config.OPENAITOKEN

bot = aiogram.Bot(token=config.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: Message):
    # response = openai.Completion.create(
    # engine="text-davinci-002",
    # prompt='How can i help you?',
    # temperature=0.5,
    # max_tokens=150
    # )
    # if message.chat.type == "group" or message.chat.type == "supergroup": 
    #     await bot.send_message(chat_id=message.chat.id, text=response.choices[0].text)
    # else:
    #     await bot.send_message(chat_id=message.from_user.id,text=response.choices[0].text )
    await message.answer(text=texts.welcomeText)

async def get_response_from_ai(prompt: str):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=150
    )
    return response.choices[0].text


@dp.message_handler(commands=['ai'])
async def group_chat(message: types.Message):
        ai_response = await get_response_from_ai(message.text)
        await bot.send_message(chat_id=message.chat.id, text=ai_response)  

@dp.message_handler()
async def private_chat(message: types.Message):
        ai_response = await get_response_from_ai(message.text)
        await bot.send_message(chat_id=message.from_user.id, text=ai_response)
            

   
if __name__ == '__main__':
    async def main():
         await dp.start_polling()
    asyncio.run(main())
