# coding:utf-8
# Flask などの必要なライブラリをインポートする
from flask import Flask, render_template, request, redirect, url_for
import numpy as np

app = Flask(__name__)


@app.route('/')

def index():
    title = "ベンチャー検定"
    return render_template('index.html',title=title)

@app.route('/questions', methods=['GET', 'POST'])

def questions():
    title = "ベンチャー検定"
    if request.method == 'POST':
        name = request.form['name']
        i = int(request.form['i'])

        venture_point = 0
        v = int(request.form['venture_point'])
        venture_point += v

        i += 1
        if i == 13:
            return render_template('result.html', title=title,name=name, venture_point=venture_point)

        question=generate_questions(i-1)
        answers=generate_answers(i-1)
        return render_template('questions.html',
                               name=name , title=title, question=question, answers=answers, venture_point=venture_point,i=i)

    else:
        return redirect(url_for('index'))

def generate_questions(i):
    questions = [
        "あなたはどのポケモンが好き?",
        "大手よりベンチャーがいい?",
        "来週もまた見てくれるかな?",
        "hogehoge",
        "問題ですe",
        "問題ですf",
        "問題ですg",
        "問題ですh",
        "問題ですi",
        "問題ですj",
        "問題ですk",
        "問題ですl",
    ]
    return questions[i]

def generate_answers(i):
    answers = [
         [["キャタピー",1],["ピカチュウ",2],["ミュウツー",3],["ジバニャン",4]],
         [["とてもそう思う",1],["まあまあ思う",2],["いやネームバリュー大事だから",3],["悲しみ",4]],
         [["いいとも!",1],["いいとも!",2],["いいとも!",3],["いいとも!",4]],
         [["hogehoge",1],["hagehage",2],["higehige",3],["hugehuge",4]],
         [["答えです1",1],["答えです2",2],["答えです3",3],["答えです4",4]],
         [["答えです5",1],["答えです6",2],["答えです7",3],["答えです8",4]],
         [["答えです1",1],["答えです2",2],["答えです3",3],["答えです4",4]],
         [["答えです5",1],["答えです6",2],["答えです7",3],["答えです8",4]],
         [["答えです1",1],["答えです2",2],["答えです3",3],["答えです4",4]],
         [["答えです5",1],["答えです6",2],["答えです7",3],["答えです8",4]],
         [["答えです1",1],["答えです2",2],["答えです3",3],["答えです4",4]],
         [["答えです5",1],["答えです6",2],["答えです7",3],["答えです8",4]],
    ]
    return answers[i]



if __name__ == '__main__':
    app.debug = True
    app.run()