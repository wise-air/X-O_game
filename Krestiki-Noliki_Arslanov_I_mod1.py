# Игра «Крестики-нолики».
# Размер поля = 3x3.


# Намеренно решил применить словарь, хотя списком и функциями построение кода было бы возможно проще.
# смена хода игрока так же прописана индивидуально, т.к. применялись индивидуальные обращения к игрокам.

print('_________________________________________________')
print('    Добро пожаловать в интерактивную игру: \n'
      '           "КРЕСТИКИ-НОЛИКИ"\n '
      '     Игра расчитана на 2-х игроков.\n'
      '_x_o_x_o_x_o_\_\ПРАВИЛА ИГРЫ/_/_x_o_x_o_x_o_\n'
      'Игроки по очереди выбирают номер клетки поля 3×3\n'
      '(один всегда крестики - "X", другой всегда нолики - "O")*. \n'
      'Первый, выстроивший в ряд 3 своих фигуры по вертикали, \n'
      'горизонтали или диагонали, выигрывает. \n\n'
      '*Первый ход всегда делает игрок, ставящий крестики - "X".')
print(input('(Для продолжения нажмите "Enter"...)'))

print('До начала игры давайте познакомимся:')
player_one = input('Первый игрок, Вы будете играть крестиками "X", представьтесь пожалуйста: ')
print(f'Приятно познакомиться с Вами {player_one}!')
player_two = input('Второй игрок, Вы будете играть ноликами "O", представьтесь пожалуйста: ')
print(f'Рад Вас видеть {player_two}! Приступим к игре, удачи {player_one} и {player_two}!')
print(input('(Для продолжения нажмите "Enter"...)'))

# Словарь с ключами-объектами соответствующие числу ячеек игры
zone = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
# Переменные со счетчиком и ходом
count = 1
turn = 0


# Функция - Игровое поле
def game_zone():
    print("_" * 10)
    print(zone[1], "|", zone[2], '|', zone[3])
    print('--+---+---')
    print(zone[4], "|", zone[5], '|', zone[6])
    print('--+---+---')
    print(zone[7], '|', zone[8], "|", zone[9])
    print("_" * 10)

# Функция включения объекта "О" в словарь
def o_input_to_dict():
    for n in zone:
        if n == int(turn):
            zone[n] = 'O'
            break

# Функция включения объекта "Х" в словарь
def x_input_to_dict():
    for n in zone:
        if n == int(turn):
            zone[n] = 'X'
            break

# Функция проверки объеков словаря на ввод недопустимого числа или повторяющегося числа
def check_errors():
    global turn
    check_O_X = int(turn)
    while check_O_X not in list(zone.values()) or check_O_X not in list(zone.values()):
        turn = input('Упс, введено недопустимое число или число уже вводилось, введите другое [1-9]: ')
        check_O_X = int(turn)
        continue

# Функция для вывода именного сообщения победителю
def message_for_winner():
    if count % 2 == 0:
        print(f'Veni, vedi, vici. Поздравляю Вас {player_two}!!!')
    else:
        print(f'Пришел, увидел, победил. Поздравляю Вас {player_one}!!!')
    game_zone()
    quit()


# Блок-функция проверки имеется ли победитель в игре
def check_winner():
    if (zone[1] == zone[2] == zone[3]) or (zone[1] == zone[4] == zone[7]) or (zone[1] == zone[5] == zone[9]):
        print("_" * 10)
        print(f'Победа за "{zone[1]}"')
        message_for_winner()

    elif (zone[4] == zone[5] == zone[6]) or (zone[2] == zone[5] == zone[8]) or (zone[3] == zone[5] == zone[7]):
        print("_" * 10)
        print(f'Победа за "{zone[5]}"')
        message_for_winner()

    elif (zone[7] == zone[8] == zone[9]) or (zone[3] == zone[6] == zone[9]):
        print("_" * 10)
        print(f'Победа за "{zone[9]}"')
        message_for_winner()


# Код самой игры:
game_zone()
turn = None
while count <= 9:
    if count == 1:
        turn = input(f'Кто первый бой начинает, тот скорее побеждает. \n {player_one} выбирайте ячейку с номером [1-9]: ')
        check_errors()
        x_input_to_dict()
        game_zone()
        count += 1

    elif count == 2:
        turn = (input(f'В бою победа за тем, кто силен духом. \n Ваш ход {player_two} [1-9]: '))
        check_errors()
        o_input_to_dict()
        game_zone()
        count += 1

    elif count == 3:
        turn = input(f'"Крестики-нолики" - шахматы в младенчестве. \n Ваш ход {player_one} [1-9]: ')
        check_errors()
        x_input_to_dict()
        game_zone()
        count += 1

    elif count == 4:
        turn = input(f'Крестик без нолика - плюс. \n Ваш ход {player_two} [1-9]: ')
        check_errors()
        o_input_to_dict()
        check_winner()  # Проверку на победителя начинаю с четвертого хода, т.к. ранее победителя быть не может
        game_zone()
        count += 1

    elif count == 5:
        turn = input(f'Не говори, что ты несешь свой крест, если ты играешь в "Крестики-нолики". \n '
                     f'Ваш ход {player_one} [1-9]: ')
        check_errors()
        x_input_to_dict()
        check_winner()
        game_zone()
        count += 1

    elif count == 6:
        turn = input(f'Нолик без крестика - буква О. \n Ваш ход {player_two} [1-9]: ')
        check_errors()
        o_input_to_dict()
        check_winner()
        game_zone()
        count += 1

    elif count == 7:
        turn = input(f'"Крестики-нолики" - вечные друзья соперники. \n Ваш ход {player_one} [1-9]: ')
        check_errors()
        x_input_to_dict()
        check_winner()
        game_zone()
        count += 1

    elif count == 8:
        turn = input(f'"Крестики-нолики" - наш ответ кубику Рубика. \n Ваш ход {player_two} [1-9]: ')
        check_errors()
        o_input_to_dict()
        check_winner()
        game_zone()
        count += 1

    elif count == 9:
        turn = input(
            f'Несмотря на все разногласия, крестик и нолик - пара неразлучников. \n Ваш ход {player_one} [1-9]: ')
        check_errors()
        x_input_to_dict()
        check_winner()
        game_zone()
        count += 1

        print("_________________________________")
        print(" Коль ни твоя и ни моя - \n "
              "тогда стало быть ничья! \n "
              "Увы, победителя в этой игре нет")
        print("_________________________________")

#  Конец программы
