from flask import Flask, render_template
import astar
import time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():

    astar.shuffler()
    initialState = astar.initial_state
    sec = time.time()
    a, b = astar.astar_state(initialState)
    sec_astar = round(time.time()-sec, 6)
    moves = astar.backtrace2()
    sec2 = time.time()
    c, d = astar.bfs(initialState)
    sec_bfs = round(time.time()-sec2, 6)
    moves2 = astar.backtrace()


    return render_template('index.html', initial=initialState, moves=moves, moves2=moves2, astar=b, bfs=d, sec_astar=sec_astar, sec_bfs=sec_bfs)

app.run(debug=True)