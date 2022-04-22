from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle
class Question():
    def __init__(self, question, right_answer, wrong_1, wrong_2, wrong_3):
        self.question = question
        self.right_answer = right_answer
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3
question_list=[]
question_list.append(Question('Государственный язык Бразилии:', 'Португальский' , 'Испанский' , 'Итальянский' , 'Бразильский'))
question_list.append(Question('Сколько лет нашей планете?','4.5 миллиарда', '2021', '1 миллион','3 года'))
question_list.append(Question('Столица Канады?', 'Оттава', 'Москва','Торонто','Онтарио'))
question_list.append(Question('Когда каникулы в школе?', 'Летом', 'Зимой', 'Осенью', 'Весной'))
question_list.append(Question('2+2', '4', '245875734384', '2^-1', 'холодильник'))
app = QApplication([])
main_win=QWidget()
main_win.resize(1000,500)
main_win.setWindowTitle('Memory Card')
question = QLabel('Какой национальности не существует?')
rbth_1 = QRadioButton('Энцы')
rbth_2 = QRadioButton('Смурфы')
rbth_3 = QRadioButton('Чульмцы')
rbth_4 = QRadioButton('Алеуты')
RadioGroupBox=QGroupBox('Варианты ответов')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbth_1)
layout_ans2.addWidget(rbth_2)
layout_ans3.addWidget(rbth_3)
layout_ans3.addWidget(rbth_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
main_layout = QVBoxLayout()
AnswerGroupBox= QGroupBox('Результат теста')
layout_ans11 = QHBoxLayout()
layout_ans22 = QHBoxLayout()
layout_ans33 = QVBoxLayout()
r_w = QLabel('Правильно/Неправильно')
r = QLabel('Правильно')
layout_ans11.addWidget(r_w)
layout_ans22.addWidget(r, alignment=Qt.AlignHCenter)
layout_ans33.addLayout(layout_ans11)
layout_ans33.addLayout(layout_ans22)
AnswerGroupBox.setLayout(layout_ans33)
AnswerGroupBox.hide()
answer=QPushButton('Ответить')
def show_question():
    AnswerGroupBox.hide()
    RadioGroupBox.show()
    answer.setText('Ответить')
    rbth_1.setChecked(False)
    rbth_2.setChecked(False)
    rbth_3.setChecked(False)
    rbth_4.setChecked(False)
def show_result():
    RadioGroupBox.hide()
    AnswerGroupBox.show()
    answer.setText('Следующий вопрос')
def show_start():
    if answer.text() == 'Ответить':
        show_result()
    else:
        show_question()
main_win.score = 0
answers = [rbth_1, rbth_2, rbth_3, rbth_4]
main_win.number_question = -1
shuffle(question_list)
def next_question():
    main_win.number_question += 1
    if main_win.number_question >= len(question_list):
        shuffle(question_list)
        main_win.number_question = 0
        print('Вы прошли тест на:', (main_win.score / 5) * 100, '%')
        exit()
    q = question_list[main_win.number_question]
    ask(q)

def click_OK():
    if answer.text() == 'Ответить':
        check_answer()
    else:
        next_question()

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong_1)
    answers[2].setText(q.wrong_2)
    answers[3].setText(q.wrong_3)
    question.setText(q.question)
    r.setText(q.right_answer)
    show_question()
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
    elif answers[1].isChecked():
        show_correct('Неправильно!')
    elif answers[2].isChecked():
        show_correct('Неправильно!')
    elif answers[3].isChecked():
        show_correct('Неправильно!')
def show_correct(res):
    r_w.setText(res)
    show_result()

ask_1 = Question('Государственный язык Бразилии:', 'Португальский', 'Испанский', 'Итальянский', 'Бразильский')
ask(ask_1)
answer.clicked.connect(click_OK)
main_layout.addWidget(question, alignment = Qt.AlignHCenter)
main_layout.addWidget(RadioGroupBox, alignment = Qt.AlignHCenter)
main_layout.addWidget(AnswerGroupBox, alignment=Qt.AlignHCenter)
main_layout.addWidget(answer, alignment = Qt.AlignHCenter)
main_win.setLayout(main_layout)
main_win.show()
app.exec_()