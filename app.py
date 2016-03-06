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
            if venture_point > 46:
                point_result = "お前のようなやつが世界を変えていくんやで!"
            elif venture_point > 45:
                point_result = "すさまじい殺気だ...ベンチャー10段."
            elif venture_point > 43:
                point_result = "惜しかったな. ベンチャー9段."
            elif venture_point > 41:
                point_result = "ベンチャー8段."
            elif venture_point > 39:
                point_result = "ベンチャー7段."
            elif venture_point > 37:
                point_result = "ベンチャー6段."
            elif venture_point > 36:
                point_result = "ベンチャー5段."
            elif venture_point > 34:
                point_result = "ベンチャー4段."
            elif venture_point > 32:
                point_result = "ベンチャー3級."
            elif venture_point > 30:
                point_result = "ベンチャー2段."
            elif venture_point > 28:
                point_result = "ベンチャー初段."
            elif venture_point > 25:
                point_result = "ベンチャー1級."
            elif venture_point > 22:
                point_result = "ベンチャー2級."
            elif venture_point > 19:
                point_result = "ベンチャー3級."
            elif venture_point > 17:
                point_result = "ベンチャー4級."
            elif venture_point > 14:
                point_result = "ベンチャー5級."
            elif venture_point > 11:
                point_result = "ベンチャー6級."
            elif venture_point > 5:
                point_result = "ベンチャー入門."
            elif venture_point > 0:
                point_result = "人間のクズ."
            else:
                point_result = "なんだおまえは."
            return render_template('result.html', title=title,name=name, venture_point=venture_point, point_result=point_result)

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
        "あなたは何派? 1",
        "あ:なたは何派? 2",
        "あなたは何派? 3",
        "あなたは何派? 4",
        "あなたは何派? 5",
        "あなたは何派? 6",
        "あなたは何派? 7",
        "あなたは何派? 8",
        "あなたは何派? LAST",
        "来週:もまたやってくれるかな?",
    ]
    return questions[i]

def generate_answers(i):
    answers = [
         [["キ:ャタピー",4],["ピカチュウ",1],["ミュウツー",2],["ジバニャン",0]],
         [["とてもそう思う",1],["まあまあ思う",4],["いやネームバリュー大事だから",3],["悲しみ",0]],
         [["atom",2],["sublimetext",0],["emacs",3],["vim",4]],
         [["穀物",3],["パン",1],["麺",0],["豆腐",4]],
         [["甘党",4],["辛党",2],["苦党",0],["酸味党",1]],
         [["空",4],["山",0],["海",2],["森",3]],
         [["git",4],["subversion",0],["mercurial",1],["veracity",2]],
         [["A",4],["B",0],["C",1],["それ以上",2]],
         [["Java",1],["PHP",0],["C",2],["JavaScript",2]],
         [["おパンツ",4],["黒タイツ",4],["スク水",4],["ブラジャー",0]],
         [["Ruby",3],["Python",3],["Go",4],["Brainfxxk",6]],
         [["やらないとも!",4],["いいとも",0],["いいとも!",1],["いいとも!!!!!!!!",2]],
    ]
    return answers[i]



if __name__ == '__main__':
    app.debug = True
    app.run()