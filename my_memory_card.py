#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from random import randint, shuffle
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout,QRadioButton,QGroupBox,QButtonGroup)
#импортирование модулей и их элементов
app=QApplication([])#создание оконного приложения
class Question():# создание класса, который содержит вопрос, 1 правильный ответ и 3 неправильных ответа
    def __init__(self,questions,rightanswer,wrong1,wrong2,wrong3):
        self.questions=questions#вопрос
        self.rightanswer=rightanswer#1 правильный ответ
        self.wrong1=wrong1#неправильный ответ
        self.wrong2=wrong2#неправильный ответ
        self.wrong3=wrong3#неправильный ответ
questions_list=[]#создание списка  с вопросами и ответами на них
#сами вопросы
questions_list.append(Question('Какая страна первой встречает Новый год?','Кирибати','Новая Зеландия','Австралия','Россия'))
questions_list.append(Question('По какому календарю Новый год наступает 1 января?', 'По григорианскому календарю','По юлианскому календарю','По еврейскому календарю','По лунному календарю'))
questions_list.append(Question('Сколько лучей у снежинки?','6','7','8', '5'))
questions_list.append(Question('С какого года Новый год в России стали отмечать 1 января?','1700','2001','988','1861'))
questions_list.append(Question('Чем была украшена первая елка во Франции в 1600 году?','Бумажными розами','Стеклянными шариками','Фруктами','Шёлковыми бантами'))
questions_list.append(Question('Герой какой сказки сражался с Мышиным королем как раз накануне Нового года? ', 'Щелкунчик', 'Снежная королева', 'Снегурочка','Жила-была девочка'))
main_win = QWidget()#создание окна приложения
main_win.resize(400, 300)

main_win.cur_question=-1#счётчик вопросов
main_win.setWindowTitle('Новогодняя викторина')#название окна
button = QPushButton('Ответить')#виджет-кнопка для ответа
question=QLabel('Вопрос')#текст вопроса

RadioGroupBox=QGroupBox('Варианты ответов')# группа для переключателей с ответами
rbtn1=QRadioButton('Вариант 1')#сами переключатели
rbtn2=QRadioButton('Вариант 2')
rbtn3=QRadioButton('Вариант 3')
rbtn4=QRadioButton('Вариант 4')

RadioGroup=QButtonGroup()#группировка переключателей для регуляции их поведения
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)
layout_ans1=QHBoxLayout()#горизонтальная направляющая
layout_ans2=QVBoxLayout()#вертикальная направляющая
layout_ans3=QVBoxLayout()#вертикальная направляющая
layout_ans2.addWidget(rbtn1)#добавление ответа в первую часть
layout_ans2.addWidget(rbtn2)#добавление ответа в первую часть
layout_ans3.addWidget(rbtn3)#добавление ответа во вторую часть
layout_ans3.addWidget(rbtn4)#добавление ответа во вторую часть

layout_ans1.addLayout(layout_ans2)#добавление  столбцов одну строку
layout_ans1.addLayout(layout_ans3)#добавление  столбцов одну строку

RadioGroupBox.setLayout(layout_ans1)#добавление вариантов ответа на лэйаут,создание панели с ними

AnsGroupBox= QGroupBox('Рeзультат теста')#создание группы с результатом теста
result = QLabel('правильно/неправильно')#виджет-результат правильно или неправильно
correct=QLabel('Правильный ответ')#виджет для правильного ответа

layout_res= QVBoxLayout()#создание вертикального лэйаута
layout_res.addWidget(result, alignment=(Qt.AlignLeft | Qt.AlignTop))#добавление на этот лэйаут виджет результата, выравнивание  по левому краю
layout_res.addWidget(correct, alignment=Qt.AlignHCenter,stretch=2)#добавление на этот лэйаут виджет правильного ответа,выравнивание по центру
AnsGroupBox.setLayout(layout_res)#группа вопросов по лэйаутам

layout_line1= QHBoxLayout()#лэйаут вопроса
layout_line2=QHBoxLayout()#лэйаут вариантов ответа или результат теста
layout_line3=QHBoxLayout()#лэйаут для кнопки ответить

layout_line1.addWidget(question,alignment=(Qt.AlignHCenter | Qt.AlignVCenter))#добавление на лэйаут вопроса и выравнивание по центру по горизонтали и по вертикали
layout_line2.addWidget(RadioGroupBox)#добавление на лэйаут варианты ответов или результат теста
layout_line2.addWidget(AnsGroupBox)#добавление на лэйаут кнопки ответить
AnsGroupBox.hide()#скрытие панели ответов

layout_line3.addStretch(1)#растягиваю виджет
layout_line3.addWidget(button, stretch=2)#растягиваю кнопку ответить
layout_line3.addStretch(1)#растягиваю

layout_card=QVBoxLayout()#лэйаут 

layout_card.addLayout(layout_line1,stretch=2)#добавление лэйаута на лэйаут,его растягивание
layout_card.addLayout(layout_line2,stretch=8)#добавление лэйаута на лэйаут,его растягивание
layout_card.addStretch(1)#растягивание
layout_card.addLayout(layout_line3,stretch=1)#добавление лэйаута на лэйаут,его растягивание
layout_card.addStretch(1)#растягиваю
layout_card.addSpacing(5)#создание пробелов

def show_result():#функция,обрабатывающая нажатие на кнопку «ответить»
    RadioGroupBox.hide()#скрываю форму вопроса
    AnsGroupBox.show()#отображаю форму правильного ответа
    button.setText('Следующий вопрос')#меняю надпись на кнопке на «следующий вопрос».
def show_question():#функция,обрабатывающая нажатие на  кнопке «следующий вопрос»
    RadioGroupBox.show()#скрываю форму ответа
    AnsGroupBox.hide()#показываю форму вопроса
    button.setText('Ответить')#меняю надпись «следующий вопрос» на «ответить»;
    RadioGroup.setExclusive(False)#сбрасываю все переключатели
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)

answer=[rbtn1,rbtn2,rbtn3,rbtn4]#список с вариантами ответов

def ask(q: Question):#функция работает со свойствами класса Question
    shuffle(answer)#перемешивает варианты ответов
    answer[0].setText(q.rightanswer)#размещает заранее правильный ответ
    answer[1].setText(q.wrong1)#
    answer[2].setText(q.wrong2)#
    answer[3].setText(q.wrong3)#
    question.setText(q.questions)#отображает форму вопроса
    correct.setText(q.rightanswer)#отображает правильный ответ
    show_question()#обработка нажатия на кнопку
def check_answer():#функция проверяет правильность ответа при нажатии на кнопку «ответить»
    if answer[0].isChecked():#если выбран переключатель answers[0], то вызывает функцию show_correct с аргументом «правильно»;
        show_correct('Правильно!')#печатает результат
        main_win.score+=1#увеличивает счетчик для подсчета правильный ответов
    else:#функция вызывает функцию show_correct с аргументом «неверно» при выборе других вариантов ответа
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Неверно!')#результат
    print('Статистика\n-Всего вопросов:',main_win.total,'\n-Правильных ответов:',main_win.score)#печатаю статистику
    print('Рейтинг:', (main_win.score/main_win.total)*100, '%')#печатаю рейтинг
def next_question():#последовательный переход между вопросами
    main_win.total+=1#счетчик вопросов
    print('Статистика\n-Всего вопросов:',main_win.total,'\n-Правильных ответов:',main_win.score)#снова статистика
    cur_question=randint(0,len(questions_list)-1)#номер текущего вопроса делаю как случайное число в пределе количества вопросов
    q=questions_list[cur_question]
    ask(q)#
def click_ok():#функция для переключателя между вопросами и ответами
    if button.text()=='Ответить':#если сейчас ответить
        check_answer()
    else:
        next_question()
    
def show_correct(res):#
    result.setText(res)#устанавливает текст-результат в форме ответа
    show_result()#отображает форму ответа
main_win.setLayout(layout_card)
main_win.cur_question=-1#счетчик
button.clicked.connect(click_ok)#нажимая на кнопку выбираем, что происходит
main_win.score=0#счетчик
main_win.total=0#счетчик
next_question()
main_win.resize(400,300)#размеры окна
main_win.show()#отображаю 
app.exec()#оставляю открытым окно пока его не закроют