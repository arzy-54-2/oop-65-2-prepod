from colorama import Fore, Back, Style

print(Fore.BLUE + "qwert" + Style.RESET_ALL)
print(Fore.YELLOW + Back.BLUE + "asdfg." + Style.RESET_ALL)
print(Style.BRIGHT + Fore.MAGENTA + "zxcvb" + Style.RESET_ALL)
# Эта библиотека нужна для изменения цвета текста и фона в консоли.
# Используется для того чтобы выделить важную информацию
# в первом примере изменяем только цвет текста (Fore)
# во втором цвет текста (Fore) и фон вокруг текста (Back)
# в третьем используем стиль (делаем текст светлее) и меняем цвет текста