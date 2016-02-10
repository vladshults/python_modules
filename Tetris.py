import sys
# from random import randint
from PyQt4 import QtCore, QtGui


class Tetris(QtGui.QMainWindow):
    def __init__(self):
        super(Tetris, self).__init__()
        # self.tboard = Board(self)
        # self.setCentralWidget(self.tboard)
        self.statusbar = self.statusBar()
        self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)
        self.tboard.start()
        self.resize(180, 380)
        self.center()
        self.setWindowTitle('Tetris')
        self.show()

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) // 2, (screen.height() - size.height()) // 2)

'''
class Board(QtGui.QFrame):
    msg2Statusbar = QtCore.pyqtSignal(str)
    BoardWidth, BoardHeight, Speed = 10, 22, 300
    EmptyLine = [0] * BoardWidth
    geometry = (None,
                (((0, 0), (-1, -1), (0, -1), (-1, -2)), ((-1, 0), (0, 0), (0, -1), (1, -1)),
                 ((0, 0), (-1, -1), (0, -1), (-1, -2)), ((-1, 0), (0, 0), (0, -1), (1, -1))),
                (((-1, 0), (-1, -1), (0, -1), (0, -2)), ((0, 0), (1, 0), (-1, -1), (0, -1)),
                 ((-1, 0), (-1, -1), (0, -1), (0, -2)), ((0, 0), (1, 0), (-1, -1), (0, -1))),
                (((0, 0), (0, -1), (0, -2), (0, -3)), ((-2, -1), (-1, -1), (0, -1), (1, -1)),
                 ((0, 0), (0, -1), (0, -2), (0, -3)), ((-2, -1), (-1, -1), (0, -1), (1, -1))),
                (((-1, 0), (0, 0), (1, 0), (0, -1)), ((1, 0), (0, -1), (1, -1), (1, -2)),
                 ((0, 0), (-1, -1), (0, -1), (1, -1)), ((-1, 0), (-1, -1), (0, -1), (-1, -2))),
                (((-1, 0), (0, 0), (-1, -1), (0, -1)), ((-1, 0), (0, 0), (-1, -1), (0, -1)),
                 ((-1, 0), (0, 0), (-1, -1), (0, -1)), ((-1, 0), (0, 0), (-1, -1), (0, -1))),
                (((0, 0), (1, 0), (0, -1), (0, -2)), ((-1, 0), (0, 0), (1, 0), (1, -1)),
                 ((0, 0), (0, -1), (-1, -2), (0, -2)), ((-1, 0), (-1, -1), (0, -1), (1, -1))),
                (((-1, 0), (0, 0), (0, -1), (0, -2)), ((1, 0), (-1, -1), (0, -1), (1, -1)),
                 ((0, 0), (0, -1), (0, -2), (1, -2)), ((-1, 0), (0, 0), (1, 0), (-1, -1))))

    def __init__(self, parent):
        super(Board, self).__init__(parent)
        self.timer = QtCore.QBasicTimer()
        self.isWaitingAfterLine = self.isStarted = self.isPaused = False
        self.numLinesRemoved = 0
        self.setFocusPolicy(QtCore.Qt.StrongFocus)

    def start(self):
        if self.isPaused:
            return
        self.isStarted = True
        self.isWaitingAfterLine = False
        self.numLinesRemoved = 0
        self.board = [Board.EmptyLine.copy() for _ in range(Board.BoardHeight)]
        self.msg2Statusbar.emit(str(self.numLinesRemoved))
        self.newPiece()
        self.timer.start(Board.Speed, self)

    def paintEvent(self, event):
        glass = [l.copy() for l in self.board]
        if self.shape:
            s, a, X, Y = self.shape
            for x, y in self.geometry[s][a]:
                glass[y + Y][x + X] = s
        h, w = self.contentsRect().height() // Board.BoardHeight, self.contentsRect().width() // Board.BoardWidth
        painter = QtGui.QPainter(self)
        for y, l in enumerate(glass):
            y = self.contentsRect().bottom() - (y + 1) * h
            for x, s in enumerate(l):
                if s:
                    x *= w
                    color = QtGui.QColor(
                        (None, 0xCC6666, 0x66CC66, 0x6666CC, 0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00)[s])
                    painter.fillRect(x + 1, y + 1, w - 2, h - 2, color)
                    painter.setPen(color.light())
                    painter.drawLine(x, y + h - 1, x, y)
                    painter.drawLine(x, y, x + w - 1, y)
                    painter.setPen(color.dark())
                    painter.drawLine(x + 1, y + h - 1, x + w - 1, y + h - 1)
                    painter.drawLine(x + w - 1, y + h - 1, x + w - 1, y + 1)


    def keyPressEvent(self, event):
        if not (self.isStarted and self.shape):
            super(Board, self).keyPressEvent(event)
            return
        key = event.key()
        if key == QtCore.Qt.Key_P:
            self.isPaused ^= True
            if self.isPaused:
                self.timer.stop()
                self.msg2Statusbar.emit('paused')
            else:
                self.timer.start(Board.Speed, self)
                self.msg2Statusbar.emit(str(self.numLinesRemoved))
        elif key == QtCore.Qt.Key_Left:
            self.nextshape[2] -= 1
            self.tryMove()
        elif key == QtCore.Qt.Key_Right:
            self.nextshape[2] += 1
            self.tryMove()
        elif key == QtCore.Qt.Key_Down:
            self.nextshape[1] = (self.shape[1] + 1) % 4
            self.tryMove()
        elif key == QtCore.Qt.Key_Up:
            self.nextshape[1] = (self.shape[1] + 3) % 4
            self.tryMove()
        elif key == QtCore.Qt.Key_Space:
            self.dropDown()
        elif key == QtCore.Qt.Key_D:
            self.oneLineDown()
        else:
            super(Board, self).keyPressEvent(event)

    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            if self.isWaitingAfterLine:
                self.isWaitingAfterLine = False
                self.newPiece()
            else:
                self.oneLineDown()
        else:
            super(Board, self).timerEvent(event)

    def dropDown(self):
        while self.tryMove():
            self.nextshape[3] -= 1
        self.pieceDropped()

    def oneLineDown(self):
        self.nextshape[3] -= 1
        if not self.tryMove():
            self.pieceDropped()

    def pieceDropped(self):
        s, a, X, Y = self.shape
        for x, y in self.geometry[s][a]:
            self.board[y + Y][x + X] = s
        self.board = [l for l in self.board if not all(l)]
        numFullLines = Board.BoardHeight - len(self.board)
        if numFullLines:
            for i in range(numFullLines):
                self.board.append(Board.EmptyLine.copy())
            self.numLinesRemoved += numFullLines
            self.msg2Statusbar.emit(str(self.numLinesRemoved))
            self.isWaitingAfterLine = True
            self.shape = None
            self.update()
        if not self.isWaitingAfterLine:
            self.newPiece()

    def newPiece(self):
        self.nextshape = [randint(1, 7), 0, Board.BoardWidth // 2, Board.BoardHeight - 1]
        if not self.tryMove():
            self.shape = None
            self.timer.stop()
            self.isStarted = False
            self.msg2Statusbar.emit("Game over")

    def tryMove(self):
        s, a, X, Y = self.nextshape
        for x, y in self.geometry[s][a]:
            x += X
            y += Y
            if not (0 <= x < Board.BoardWidth and 0 <= y) or self.board[y][x]:
                self.nextshape = self.shape.copy()
                return False
        self.shape = self.nextshape.copy()
        self.update()
        return True
'''

if __name__ == '__main__':
    app = QtGui.QApplication([])
    tetris = Tetris()
    sys.exit(app.exec_())
