import config


class Encryptor:
    # Класс подтягивает конфиг и производит шифрование в соответствии с ним
    def __init__(self, cfg: config.Config):
        self.cfg = cfg

    def encrypt(self, text: str) -> str:
        """ Возвращает аналогичный для кириллицы символ
            из латинского алфавита или иной знак в соответствии
            с уровнем шифрования """

        level = self.cfg.get_level()
        output = ""

        if level == 1:
            letters_dict = self.cfg.get_level_one_letters_dict()

            for symbol in text:
                if symbol in letters_dict.keys():
                    output += letters_dict[symbol]
                else:
                    output += symbol

            return output

        elif level == 2:
            print('Уровень шифрования 2 находится в разработке!')
            return ""
        else:
            exit(1)
