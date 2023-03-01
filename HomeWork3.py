from aiogram import Bot, types, Dispatcher, executor
from dotenv import load_dotenv
import logging
import os

from keybords import button

load_dotenv('bot.py')

bot = Bot(os.environ.get('token'))
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=["start"])
async def start(message:types.Message):
    await message.answer("Здравствуйте! Я чат-бот, который может помочь вам получить информацию об IT-курсах Geeks.")
    await message.answer('Доступны 5 направлений в IT-курсах. Для получения дополнительной информации о каждом направлении, пожалуйста, выберите соответствующую кнопку.', reply_markup=button)

@dp.callback_query_handler(lambda call:call)
async def inline(call):

    if call.data == 'backend':
        await back(call.message)
    elif call.data == 'frontend':
        await front(call.message)
    elif call.data == 'uxui':
        await uxui(call.message)
    elif call.data == 'android':
        await android(call.message)
    elif call.data == 'ios':
        await ios(call.message)
    elif call.data == "contact":
        await helper(call.message)


@dp.message_handler(commands=['backend'])
async def back(message: types.Message):
    await message.answer('Backend разработка - это создание программной части веб-приложения, которая работает на сервере и обрабатывает запросы от клиентской (frontend) части. Backend разработчики работают с базами данных, серверными языками программирования, API и другими инструментами для создания и поддержки функциональности веб-приложений.')
    await message.answer('Стоимость обучения: 10.000 сом в месяц.')
    await message.answer('Срок обучения: 5 месяцев.')


@dp.message_handler(commands=['frontend'])
async def front(message: types.Message):
    await message.answer('Frontend разработка - это процесс создания веб-приложений и веб-сайтов, который включает в себя разработку клиентской части сайта, с которой взаимодействуют пользователи. Frontend разработка включает в себя использование языков программирования, таких как HTML, CSS и JavaScript, а также различных фреймворков и библиотек, таких как React, Vue и Angular.')
    await message.answer('Стоимость обучения: 10.000 сом в месяц.')
    await message.answer('Срок обучения: 5 месяцев.')


@dp.message_handler(commands=['uxui'])
async def uxui(message: types.Message):
    await message.answer('UX/UI-дизайнер — это специалист, который проектирует пользовательские интерфейсы. Один человек может специализироваться на обоих направлениях, но иногда профессии разделяют. Если коротко, в UX-дизайне важны аналитические навыки, нужно изучать аудиторию и ее поведение, а в UI-дизайне берут за основу аналитику UX-специалистов и создают максимально удобный интерфейс.')
    await message.answer('Стоимость обучения: 10.000 сом в месяц.')
    await message.answer('Срок обучения: 3 месяцев.')


@dp.message_handler(commands=['android'])
async def android(message: types.Message):
    await message.answer('Андроид разработчик — это IT-специалист, который создает, поддерживает и совершенствует программное обеспечение для мобильных устройств, использующих популярную ОС Android. Вместе с этим он задействован в процессах поддержки, улучшения и обновления разрабатываемых продуктов.')
    await message.answer('Стоимость обучения: 10.000 сом в месяц.')
    await message.answer('Срок обучения: 7 месяцев.')


@dp.message_handler(commands=['ios'])
async def ios(message: types.Message):
    await message.answer('Разработка iOS-приложений – перспективное направление в сфере IT. Если вы уже программируете какое-то время, то наверняка задумывались над тем, чтобы попробовать себя в создании мобильной программы для iPhone, но, возможно, что-то вас останавливало. А ведь вы уже давно могли бы освоить эту нишу и начать зарабатывать хорошие деньги.')
    await message.answer('Стоимость обучения: 10.000 сом в месяц.')
    await message.answer('Срок обучения: 7 месяцев.')


@dp.message_handler(commands=['contact'])
async def helper(message: types.Message):
    await message.answer('Номера: \n+996 557 052 018\n+996 777 052 018\n+996 507 052 018')
    await message.answer('Email: geeks.kg@gmail.com')
    await message.answer('Адрес: Город Ош\nул. Мырзалы Аматова 1Б, БЦ Томирис, цокольный этаж (здание Визион)')


@dp.message_handler()
async def nothing(message: types.Message):
    await message.answer('')


executor.start_polling(dp)