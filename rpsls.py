#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-spock
作者：胡冰枝
日期：2020.4.12
"""
import random
def name_to_number(name):
	if name=="rock":
		return 0
	if name=="spock":
		return 1
	if name=="paper":
		return 2
	if name=="lizard":
		return 3
	if name=="scissors":
		return 4
	else:
		print("Error:No Correct Name")
def number_to_name(number):
	if number==0:
		return "rock"
	if number==1:
		return "spock"
	if number==2:
		return "paper"
	if number==3:
		return "lizard"
	if number==4:
		return "scissoes"
	else:
		print("Error:No Correct Name")
def rpsls(player_choice):
	player_number=name_to_number(player_choice)
	computer_number=random.randrange(0,4)
	computer_choice=number_to_name(computer_number)
	if player_number==0 and (computer_number==3 or computer_number==4):
		print("您赢了")
	elif player_number==4 and (computer_number==2 or computer_number==3):
		print("您赢了")
	elif player_number==2 and (computer_number==0 or computer_number==1):
		print("您赢了")
	elif player_number==3 and (computer_number==1 or computer_number==2):
		print("您赢了")
	elif player_number==1 and (computer_number==0 or computer_number==4):
		print("您赢了")
	elif player_number==computer_number:
		print("您和计算机猜的一样")
	else:
		print("计算机赢了")
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)


