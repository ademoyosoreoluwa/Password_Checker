from translate import Translator

translator = Translator(to_lang = "ja")

try:
    with open('*.txt', mode='r or rw or r+ or a') as my_file:
        text = my_file.read()
        translation = translator.translate("This is a pen...")
        print(translation)
except FileNotFoundError as err:
    print('Check your file path')
    raise err
