"""
author : mealsOrder
last modified: 2020.07.01

"""

import wx
import random

## 클래스 선언 부분 ##

##테트리스 클래스 생성
class Tetris(wx.Frame):

    ##생성자
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,size=(180, 380),  ## 창크기를 180x380으로 설정 및 각종 설정
                          style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)
        self.initFrame() ## 프레임 생성 매서드 실행

    ##프레임 초기화 및 생성 매서드
    def initFrame():
        self.statusbar=self.CreateStatusBar()   ## 상태 표시줄 생성
        self.statusbar.SetStatusText('0')       ## 상태 표시줄에 나타날 텍스트
        self.board=Board(self)                  ## 보드 생성
        self.board.SetFocus()                   ## 
        self.board.start()                      ## 보드 시작?

        self.SetTitle("Tetris Game")            ## 프레임 제목 설정
        self.Centre()                           ## ??(뭔가 중심과 관련되어있을 것같음)
    
##보드 클래스 생성
class Board(wx.Panel):

    ##보드 기본설정(변수선언)
    BoardWidth=10                               
    BoardHeight=22
    Speed=300
    ID_TIMER=1

    ##생성자
    def __init__(self,*args,**kw):              ## 가변매개변수 사용
        super(Board,self).__init__(*args,**kw)

        self.initBoard()

    ##보드 초기화 및 생성 매서드
    def initBoard(self):

        self.timer=wx.Timer(self,Board.ID_TIMER)## 타이머 설정
        self.isWaitingAfterLine=False
        self.curPiece=Shape()
        self.nextPuece=Shape()
        self.curX=0
        self.curY=0
        self.numLinesRemoved=0
        self.board=[]

        self.isStarted=False
        self.isPaused=False

        self.Bind(wx.EVT_PAINT, self.OnPaint)                   ## 그림그리기 이벤트 묶기
        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)              ## 키를 눌렀을때 이벤트
        self.Bind(wx.EVT_TIMER, self.OnTimer, id=Board.ID_TIMER)## 타이머 묶기

    ## 모양의 좌표
    def shapeAt(self,x,y):
        return self.board[(y*Board.BoardWidth)+x]       ## y좌표 x 보드의 너비 + x좌표

    ## 모양설정 및 모양의 좌표 설정
    def setShapeAt(self,x,y,shape):
        self.board[(y*Board.BoardWidth)+x]=shape

    
    
        
## 함수 선언 부분 ##




## 변수 선언 부분 ##




## 메인 부분 ##
