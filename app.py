from flask import Flask,render_template,request
import random
app = Flask(__name__, static_folder='.', static_url_path='')
@app.route('/', methods=["GET"])
def index():
    return render_template('RPS.html')

@app.route('/', methods=["POST"])
def action():
    #アイコンデータ
    data = ["fa-hand-rock","fa-hand-scissors","fa-hand-paper"]
    #プレイヤー
    player = int(request.form["player"])
    player_hand = data[player]
    #コンピューター
    computer = random.randint(0,2)
    computer_hand = data[computer]
    #勝敗
    judge_data=["ドロー","Computerの勝利","Playerの勝利"]
    judge = (player - computer + 3) % 3

    return render_template('RPS_Result.html',player_hand=player_hand,computer_hand=computer_hand,judgement=judge_data[judge])
if __name__ == "__main__":
    app.run(port=8000, debug=True)