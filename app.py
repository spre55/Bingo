# coding:utf-8
# Flask などの必要なライブラリをインポートする
from flask import Flask, render_template, request, redirect, url_for

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
        "あなたは何派? 1",
        "あなたは何派? 2",
        "あなたは何派? 3",
        "あなたは何派? 4",
        "あなたは何派? 5",
        "あなたは何派? 6",
        "あなたは何派? 7",
        "あなたは何派? 8",
        "あなたは何派? LAST",
    ]
    return questions[i]

def generate_answers(i):
    answers = [
         [["キャタピー",3],["ピカチュウ",1],["ミュウツー",1],["ジバニャン",4]],
         [["とてもそう思う",1],["まあまあ思う",2],["いやネームバリュー大事だから",3],["悲しみ",4]],
         [["いいとも!",3],["いいとも!",3],["いいとも!",3],["いいとも!",3]],
         [["vim",1],["vim",1],["vim",1],["vim",1]],
         [["穀物",3],["パン",1],["麺",1],["豆腐",4]],
         [["甘党",4],["辛党",2],["苦党",1],["酸味党",1]],
         [["空",4],["山",1],["海",1],["森",1]],
         [["git",3],["subversion",1],["mercurial",3],["veracity",3]],
         [["A",4],["B",1],["C",1],["それ以上",1]],
         [["Java",1],["PHP",1],["C",2],["JavaScript",2]],
         [["Ruby",2],["Python",4],["Go",4],["Brainfxxk",4]],
         [["bash",1],["zsh",4],["wsh",1],["csh",3]],
    ]
    return answers[i]



if __name__ == '__main__':
    app.debug = True
    app.run()