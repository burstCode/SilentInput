import keyboard
import time
import pyperclip
import json

import encryption
import config


def load_config(filename: str):
    """ Загрузка конфигурации из JSON-файла """
    with open(filename, 'r') as file:
        return json.load(file)


config_data = load_config('config.json')

cfg = config.Config(config_data.get('LEVEL', 1), config_data.get('DEV_MODE', False))
encryptor = encryption.Encryptor(cfg)

last_press_time = 0
double_press_interval = 0.3


def print_ords(text: str, additional_info="") -> None:
    """ Вывод кодов символов для режима разработчика """
    print(additional_info)
    for sym in text:
        print(ord(sym), end=' ')


def copy_paste_encrypted() -> None:
    """ На двойное нажатие сочетания клавиш ctrl+c - шифрование
        текста против читаемости его системами фильтрации  """

    global last_press_time
    current_time = time.time()

    if current_time - last_press_time <= double_press_interval:
        # Копируем и вставляем зашифрованный текст при помощи либы pyperclip
        try:
            selected_text = pyperclip.paste()
            dev_mode = cfg.get_dev_mode()

            if dev_mode:
                print_ords(
                    selected_text,
                    f'Входной текст: {selected_text}\n'
                    f'\nКоды символов до шифрования: '
                )

            if selected_text:
                encrypted_text = encryptor.encrypt(selected_text)
                pyperclip.copy(encrypted_text)
                keyboard.press_and_release('ctrl+v')

                if dev_mode:
                    print_ords(
                        encrypted_text,
                        f'\n\nВыходной текст: {encrypted_text}\n'
                        f'\nКоды символов после шифрования: '
                    )
            else:
                print('Буфер обмена пуст.')
        except Exception as e:
            print(f'Непредвиденная ошибка: {e}')

    last_press_time = current_time


def setup_hotkeys():
    """ Установка сочетаний клавиш """
    keyboard.add_hotkey('ctrl+c', copy_paste_encrypted)


def main() -> None:
    if cfg.get_dev_mode():
        print('Приложение запущено в режиме разработчика.')
    else:
        print('Приложение запущено в обычном режиме.')

    setup_hotkeys()
    keyboard.wait()


if __name__ == '__main__':
    main()
