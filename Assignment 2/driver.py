from flask import Flask, render_template
import bfs

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    bfs.shuffler()
    initialState = bfs.initial_state
    bfs.bfs(initialState)
    moves = bfs.backtrace()
    return render_template('index.html', initial=initialState, moves=moves)

if __name__ == '__main__':
    app.run(debug=True)
