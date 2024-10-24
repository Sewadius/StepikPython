# Шифр Цезаря
shift, text = int(input()), input()

for ch in text:
    position = ord(ch) - shift          # Код символа после сдвига

    if position >= ord('a'):            # Не переходит через "a"
        print(chr(position), end='')
        continue

    diff = ord('a') - position          # Сдвиг после символа "a"
    symbol = chr(ord('z') - diff + 1)   # Новая позиция от "z"
    print(symbol, end='')
