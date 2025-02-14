# TG04 TG Buttons
### Задание 1: Создание простого меню с кнопками
При отправке команды /start бот будет показывать меню с кнопками "Привет" и "Пока". При нажатии на кнопку "Привет" бот должен отвечать "Привет, {имя пользователя}!", а при нажатии на кнопку "Пока" бот должен отвечать "До свидания, {имя пользователя}!".

### Задание 2: Кнопки с URL-ссылками
При отправке команды /links бот будет показывать инлайн-кнопки с URL-ссылками. Создайте три кнопки с ссылками на новости/музыку/видео

### Задание 3: Динамическое изменение клавиатуры
При отправке команды /dynamic бот будет показывать инлайн-кнопку "Показать больше". При нажатии на эту кнопку бот должен заменять её на две новые кнопки "Опция 1" и "Опция 2". При нажатии на любую из этих кнопок бот должен отправлять сообщение с текстом выбранной опции.

### Ход выполнения
Кнопки "Привет!" и "Пока!" выполнены в виде Reply-клавиатуры, и появляются после команды \start.

Inline-клавиатура со ссылками выполнена также как было показано в уроке, вызывается командой \links.

Команда \dynamic вызовет Inline-клавиатуру с одной кнопкой, которая поменяет её на клавиатуру, построенную с помощью билдера. Параметрам text и callback_data присвоены одинаковые значения. В качестве аргумента для декоратора обработчика callback-запросов применён метод F.data.in_(kbrd.options), где kbrd.options - список кнопок, таким образом для обоих кнопок используется универсальный обработчик, что весьма удобно. В сообщениях от бота используется атрибут callback.data, указывающий нажатую кнопку.