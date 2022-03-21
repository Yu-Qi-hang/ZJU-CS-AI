import numpy as np           # 提供维度数组与矩阵运算
import copy                  # 从copy模块导入深度拷贝方法
from board import Chessboard

def perm(q, n ,begin , end):#使用递归进行全排列
    if begin >= end:#判断是否排序到最后一个数
        q += n
    else:
        i = begin
        for num in range(begin , end):
            n[num], n[i] = n[i], n[num]
            perm(q, n, begin + 1, end)
            n[num], n[i] = n[i], n[num]
# 基于棋盘类，设计搜索策略
class Game:
    def __init__(self, show = True):
        """
        初始化游戏状态.
        """
        
        self.chessBoard = Chessboard(show)
        self.solves = []
        self.gameInit()
        
    # 重置游戏
    def gameInit(self, show = True):
        """
        重置棋盘.
        """
        
        self.Queen_setRow = [-1] * 8
        self.chessBoard.boardInit(False)
        
    ##############################################################################
    ####                请在以下区域中作答(可自由添加自定义函数)                 #### 
    ####              输出：self.solves = 八皇后所有序列解的list                ####
    ####             如:[[0,6,4,7,1,3,5,2],]代表八皇后的一个解为                ####
    ####           (0,0),(1,6),(2,4),(3,7),(4,1),(5,3),(6,5),(7,2)            ####
    ##############################################################################
    #                                                                            #
    
    def run(self, row=0):
        q = []
        a = []
        b = []
        for i in range(0,8):#获取1~n的列表
            a.append(i)
        perm(q, a , 0 , 8)#得到所有行列不相等的组合
        temp = 1
        for w in range(1 , 8+1):#获得输出行数
            temp *= w
        for j in range(0 , temp):#将perm中q所得的列表进行拆分
            b.append(q[j*8:j*8+8])
        b=sorted(b)
        couple={(1,0)}
        for i in range(1,8):
            for j in range(0,i):
                couple.add((i,j))
        for item in b:
            for (i,j) in couple:
                if i-j==item[i]-item[j]:
                    b.remove(item)#移除对角线遇到的元素
                    break
                elif j-i==item[i]-item[j]:
                    b.remove(item)#移除副对角线遇到的元素
                    break

        for item in b:
            cb = Chessboard(False)
            cb.boardInit(False)
            for k in range(0,8):
                if cb.setLegal(k,item[k]):
                    cb.queenMatrix[k][item[k]] =1                                       #落子位置
                    for i in range(8):
                        cb.unableMatrix[k][i] =-1                                 #本行无法落子
                        cb.unableMatrix[i][item[k]] =-1                                 #本列无法落子
                    for i in range(-7,8):
                        if cb.isOnChessboard(k+i,item[k]+i):
                            cb.unableMatrix[k+i][item[k]+i] =-1                         #正对角线无法落子
                        if cb.isOnChessboard(k+i,item[k]-i):
                            cb.unableMatrix[k+i][item[k]-i] =-1                         #反对角线无法落子
                    cb.chessboardMatrix = cb.unableMatrix +2*cb.queenMatrix   #更新棋盘
                    cb.printMatrix[1:9,1:9] = cb.chessboardMatrix
                else:
                    break
            if(cb.isWin()):
                self.solves.append(item)
        

    #                                                                            #
    ##############################################################################
    #################             完成后请记得提交作业             ################# 
    ##############################################################################
    
    def showResults(self, result):
        """
        结果展示.
        """
        
        self.chessBoard.boardInit(False)
        for i,item in enumerate(result):
            if item >= 0:
                self.chessBoard.setQueen(i,item,False)
        
        self.chessBoard.printChessboard(False)
    
    def get_results(self):
        """
        输出结果(请勿修改此函数).
        return: 八皇后的序列解的list.
        """
        
        self.run()
        return self.solves

game = Game()
solutions = game.get_results()
print('There are {} results.'.format(len(solutions)))
game.showResults(solutions[0])
