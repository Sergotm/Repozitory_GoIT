import random
import time
def get_main():
    Playing = 'Да' 
    while Playing == 'Да' or 'да':
        word = ['Арбуз', 'Дыня', 'Собака', 'Радуга', 'Пылесос', 'Стол', 'Ноутбук', 'Сарафан', 'Футболка']
        print('Сейчас выведем список с будущих Анаграм')

        random_word = random.choice(word)
        new_list = list(random_word)

        for i in word:
            time.sleep(0.1)
            print('[',i,']')

        random.shuffle(new_list)
        shuffle_word = ' '.join(new_list)

        print('[ ' + shuffle_word + ' ]')
        count = 1   
        coling = 0
        while coling == 0:
            word_print = input('Введите разгаданное слово: ')

            if word_print == random_word:
                print('У вас Получилось: c ',count,'раза!')
                coling +=1 
                print('Хотите повторить? Да или Нет')
                Playing = input('Введите ответ: ')

                if Playing == 'Нет' or 'нет' or 'не':
                    Playing = 'Нет'
            
            else: 
                if word_print != random_word:
                    count +=1
                    print('Ответ не верный:')
                else:
                    pass
        return Playing
    

if __name__ == '__main__':
    get_main()

