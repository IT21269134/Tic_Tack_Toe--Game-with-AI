# main code
def main():
  choice=input("Enter 1 for Single 2 for Multiple:");
  choice =int(choice);
  board =[0, 0, 0, 0, 0, 0, 0, 0, 0];
  if(choice==1):
    print("Computer:0 Vs. You:X :")
    player=input("Enter to play 1(st) or 2(nd)");
    player =int(player);
    for i in range(0,9):
      if(analyseBoard(board)!=0):
        break;
      if((i+player)%2==0):
        compTurn(board);
      else:
        constBoard(board);
        user1Turn(board);
  else:
    for i in range(0,9):
      if(analyseBoard(board)!=0):
        break;
      if(i%2==0):
        constBoard(board);
        user1Turn(board);
      else:
        constBoard(board);
        user2Turn(board);

# create constBoard Function
def constBoard(board):
  print("Current state of the board: \n\n");
  for i in range(0,9):
    if((i>0) and (i%3==0)):
      print("\n");
    if(board[i]==0):
      print("_ ", end =" ");
    if(board[i]==-1):
      print("X ", end =" ");
    if(board[i]==1):
      print("O ", end =" ");
  print("\n\n");

# create user1Turn function
def user1Turn(board):
  pos =input("Enter X's position from [1,2,3,4,...9]: ");
  pos =int(pos);
  if(board[pos-1]!=0):
    print("Wrong move");
    exit(0);
  board[pos-1]=-1;

# Create user2Turn function
def user2Turn(board):
  pos =input("Enter O's position from [1,2,3,4,...9]: ");
  pos =int(pos);
  if(board[pos-1]!=0):
    print("Wrong move");
    exit(0);
  board[pos-1]=1;

# Create compTurn function
def compTurn(board):
  pos =-1;
  value = -2;
  for i in range(0,9):
    if(board[i]==0):
      board[i]=1;
      score =-minmax(board, -1);
      board[i] =0;
      if(score >value):
        value= score;
        pos=i;
  board[pos] =1;


# create analyseBoard function
def analyseBoard(board):
  cb =[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
  for i in range(0,8):
    if(board[cb[i][0]]!=0 and board[cb[i][0]]==board[cb[i][1]] and board[cb[i][1]]==board[cb[i][2]] ):
      return board[cb[i][0]];
    return 0;

# create minmax function
def minmax(board,player):
  x =analyseBoard(board);
  if(x!=0):
    return (x*player);
  pos =-1;
  value = -2;
  for i in range(0,9):
    if(board[i]==0):
      board[i]=player;
      score =-minmax(board, player*-1);
      board[i] =0;
      if(score >value):
        value= score;
        pos=i;
  if(pos==-1):
    return 0;
  return value;

