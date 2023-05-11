from flask import Flask, render_template
from apscheduler.schedulers.background import BackgroundScheduler
import os
import RecarregarBanco

app = Flask(__name__)

port = int(os.environ.get('PORT', 5000))



def my_task():
    # coloque o código que você deseja executar continuamente aqui
    RecarregarBanco.FilaTags()
    print('Executando tarefa...')

scheduler = BackgroundScheduler()
scheduler.add_job(func=my_task, trigger='interval', seconds=270)
scheduler.start()

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)

