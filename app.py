# coding:utf-8
from flask import Flask, render_template, request, redirect, url_for
import random
app = Flask(__name__)


@app.route('/')

def index():
    title = "ビンゴやるお"
    f = open('bingo.txt', 'a')
    f.write('=-=-=-=-=-=-=-=-=-=-=-\n')
    f.close()
    return render_template('index.html',title=title)

@app.route('/bingo', methods=['POST'])

def bingo():
    title = "ビンゴだお"
    random_list=[x for x in range(1,76)]
    appear_list=[]

    if request.method == 'POST':

        i = int(request.form['i'])      
        # 終了
        if i == 75:
            return render_template('result.html', title=title, random_list=random_list, appear_list=appear_list, i=i)
        
        if i > 0:
            random_list = request.form['random_list'].replace("[", "").replace("]", "").replace(" ", "").replace("\'", "")
            random_list = random_list.split(",")

            appear_list = request.form['appear_list'].replace("[", "").replace("]", "").replace(" ", "").replace("\'", "")
            appear_list = appear_list.split(",")
        
            random_key=random.randint(0,74-i)
        else:
            random_key=random.randint(0,74)


        i += 1
        #print(random_list[random_key])
        
        
        appear_list.append(random_list[random_key])

        f = open('bingo.txt', 'a')
        f.write(str(random_list[random_key])+'\n')
        f.close()

        random_list.pop(random_key)




        return render_template('bingo.html',
                               title=title, random_list=random_list, random_key=random_key, appear_list=appear_list, i=i)

    else:
        return redirect(url_for('index'))
    


if __name__ == '__main__':
    app.debug = True
    app.run()