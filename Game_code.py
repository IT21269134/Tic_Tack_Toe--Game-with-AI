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
