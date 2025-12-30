#Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Анна', color="#dbc8ff")
define y = Character('Мысли', color="#1771d860")
define x = Character('AO', color="#555555")
define q = Character("???", color="#1d1b1b6b")
define r = Character("Асака", color="#1d1b1b6b")

define open_book = False 



# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

transform left2:
    xalign 0.2
    yalign 1.0

transform right2:
    xalign 0.8
    yalign 1.0


transform micro_shake:
    linear 0.02 xoffset -15
    linear 0.02 xoffset 15
    linear 0.02 xoffset 0


transform micro_shake1:
    linear 0.02 xoffset -15
    linear 0.02 xoffset 15
    linear 0.02 xoffset 5


init python:
    # Словарь сопоставления: БУКВА (КЛЮЧ) : СИМВОЛ (ЗНАЧЕНИЕ)
    cipher_map = {
        'А': '∇', 'Б': '¤', 'В': '⋔', 'Г': 'Δ', 'Д': 'Ξ', 'Е': 'λ',
        'Ж': '', 'З': 'Ω', 'И': 'x', 'К': '⊗', 'Л': '§', 'М': 'Σ',
        'Н': 'о', 'О': '◯', 'П': '▱', 'Р': '₽', 'С': '∞', 'Т': '◬',
        'У': '⏚', 'Ф': 'φ', 'Х': '⨂', 'Ц': 'ζ', 'Ч': '⋏', 'Ш': '≡',
        'Щ': '≢',
        # Дополнительные символы и цифры
        ' ': ' ', # Сохраняем пробелы
        '.': '.',
        '!': '!',
        '?': '?',
        '1': '①',
        '2': '②',
        '3': '③',
        '4': '④',
        '5': '⑤'
    }

    def encrypt_text(text):
        """Функция для шифрования текста."""
        encrypted_text = ""
        # Проходим по всем символам в исходном тексте
        for char in text.upper():
            # Если символ есть в словаре, берем его символ-замену, иначе оставляем как есть
            encrypted_text += cipher_map.get(char, char) 
        return encrypted_text

default quick_menu = True

screen author_contract_screen():
    # Заставляет экран блокировать игру, пока не будет принято решение
    modal True 
    
    # Фон (черный или ваш фирменный темный фон)
    add "bg darklibrary"
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 800
        ysize 600
        background "#1A1A1ACC" # Темный, полупрозрачный фон для текста
        padding (50, 50)
        
        vbox:
            spacing 20
            
            # --- ЗАГОЛОВОК И ПРАВИЛА ---
            text "КОНТРАКТ С АВТОРОМ: ПРАВИЛА БИБЛИОТЕКИ ГРЕХОВ" size 36 color "#FFD700"
            
            # Поле для прокручиваемого текста
            viewport:
                yfill True
                mousewheel True
                scrollbars "vertical"
                
                vbox:
                    spacing 15
                    
                    text "§1. ПРАВИЛО НЕ-ВМЕШАТЕЛЬСТВА: Игрок признает, что сущность, известная как АННА, является основой Вселенной. АВТОР не может напрямую изменить ее память или судьбу. Только Выбор Игрока может повлиять на Анну." size 22
                    
                    text "§2. ПРАВИЛО ПОИСКА: Игрок обязуется искать истину, а не получать ее. Каждое решение должно быть осознанным." size 22
                    
                    text "§3. ВОЗМОЖНЫЕ ПОСЛЕДСТВИЯ: Игрок соглашается с тем, что нарушение логики сюжета или вмешательство в код может привести к непредсказуемым и необратимым последствиям для Вселенной." size 22
            
            # --- КНОПКИ ---
            hbox:
                spacing 50
                xalign 0.5
                
                # Кнопка "Принять"
                textbutton "ПРИНЯТЬ УСЛОВИЯ КОНТРАКТА":
                    text_idle_color "#FFFFFF"
                    text_hover_color "#652988c0"
                    text_size 28
                    # Действие: Скрывает экран и возвращает "True"
                    action Return(True) 
                
                # Кнопка "Отказаться" (Отказ равносилен выходу)
                textbutton "ОТКАЗАТЬСЯ":
                    text_idle_color "#909090"
                    text_hover_color "#FF5050"
                    text_size 28
                    action Quit() # Выход из игры

# Начальные переменные
default fear = 0      # уровень страха Анны

default code = "A51C"  # стартовый код

#вверху файла (глобальные переменные)
default correct_password = "8Я8Р"
default user_input = ""

screen password_screen():

    frame:
        #xalign 0.5
        #yalign 0.5
        #padding (10, 10, 10, 10)


        vbox:
            spacing 10

            text "Введите пароль:" size 30

            input value user_input length 4  # length работает только так!

            textbutton "Подтвердить":
                action [SetVariable("result", user_input), Return()]






# --- Успешный конец ---

label password_correct:
    "..."
    "Вы успешно прошли проверку!"
    return

# --- Пример вызова в игре ---
# label start:
#     "Персонаж" "Нужно ввести код, чтобы продолжить."
#     call start_password_challenge
#     "Персонаж" "Продолжение истории..."
#     return