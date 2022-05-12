import random
def name_to_number(name):
    if name=="石头":
        return 0
    if name=="史洛克":
        return 1
    if name == "纸":
        return 2
    if name == "蜥蜴":
        return 3
    if name == "剪刀":
        return 4
    else:
        return 6
    pass
def number_to_name(number):
    if number==0:
        return "石头"
    if number==1:
        return "史洛克"
    if number==2:
        return "纸"
    if number==3:
        return "蜥蜴"
    if number==4:
        return "剪刀"
    else:
        return "Error: No Correct Name"
    pass
def rpsls(player_choice):
    print("您的选择为 :" + player_choice)
    player_number = name_to_number(player_choice)
    if player_number==6:
        print ("Error: No Correct Name")
        round
    computer_number = random.randrange(0, 4)
    computer_choice = number_to_name(computer_number)
    print("计算机的选择为 :" + computer_choice)
    diff = (player_number - computer_number) % 5
    if diff == 1 or diff == 2:
        print("您赢了！")
    elif diff == 3 or diff == 4:
        print("机器赢了")
    elif diff==0:
        print("平手")
    else:
      print("Error: No Correct Name")
    pass
while True:
    print("欢迎使用RPSLS游戏")
    print("----------------")
    player_choice = input("请输入您的选择: ")
    rpsls(player_choice)
