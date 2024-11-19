class Config:
    def __init__(self, level: int, dev_mode: bool):
        """ Уровень шифрования.
            1 - замена идентичных по виду символов кириллицы на символы латиницы
            2 - замена некоторых букв на цифра/знаки (с расчетом на читаемость человеком) """
        self._LEVEL: int = level

        """ Режим разработчика.
            При совершении шифрования отображает в консоли коды символов,
            чтобы убедиться в корректности шифрования """
        self._DEV_MODE: bool = dev_mode

        # Ключ - буква на кириллице. Значение - аналогичная буква на латинице.
        self._level_one_letters_dict: dict = {
            'А': 'A',
            'В': 'B',
            'Е': 'E',
            'К': 'K',
            'М': 'M',
            'Н': 'H',
            'О': 'O',
            'Р': 'P',
            'С': 'C',
            'Т': 'T',
            'Х': 'X',
            'а': 'a',
            'е': 'e',
            'о': 'o',
            'р': 'p',
            'с': 'c',
            'у': 'y',
            'х': 'x'
        }

    # Так называемые геттеры
    def get_level(self) -> int:
        return self._LEVEL

    def get_dev_mode(self) -> bool:
        return self._DEV_MODE

    def get_level_one_letters_dict(self) -> dict:
        return self._level_one_letters_dict
