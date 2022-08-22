class morpion:
    def __init__(self):
        self.plateau=[[0 for i in range(3)] for i in range(3)]
        self.x=0
        self.y=0
        self.c=0
    def afficher(self):
        for e in self.plateau:
            print(e)
    def placer(self,number):
        self.x,self.y=map(int,input('ligne colonne\n').split())
        #gere les exeptions
        while self.x>3 or self.y>3 or self.x<1 or self.y<1 or self.plateau[self.x-1][self.y-1]!=0:
            self.x,self.y=map(int,input('ligne colonne\n').split())
        self.plateau[self.x-1][self.y-1]=number
     #differente case of who win
    #horizontal case
    def check_horizon(self, number,x):
        if self.plateau[x][0]==number and self.plateau[x][1]==number and self.plateau[x][2]==number:
            return True
      #vertical case      
    def check_verti(self,number,y):
         if self.plateau[0][y]==number and self.plateau[1][y]==number and self.plateau[2][y]==number:
             return True
     #diagonal case left to right
    def check_diago1(self,number):
         if self.plateau[0][0]==number and self.plateau[1][1]==number and self.plateau[2][2]==number:
             return True
     #diagonal case right to left
    def check_diago2(self,number):
        if self.plateau[0][2]==number and self.plateau[1][1]==number and self.plateau[2][0]==number:
             return True
    def who_win(self,number):
        for j in range(3):
            bool=self.check_horizon(number,j)
            if bool== True:
                return True
        for k in range(3):
            bool2=self.check_verti(number,k)
            if bool2== True:
                return True
        bool3=self.check_diago1(number)==True
        bool4=self.check_diago2(number)==True
        if bool3 or bool4:
             return True
def game():
    m=morpion()
    m.afficher()
    player=1
    check=None
    for i in range(9):
        player=1
        m.placer(player) 
        check=m.who_win(player)
        print(check)
        if check==True:
            print(f'Joueur {player} gagne!')
            break
        m.afficher()
        player=2
        m.placer(player)
        check=m.who_win(player)
        print(check)
        if check==True:
            print(f'Joueur {player} gagne!')
            break
        m.afficher()
game()