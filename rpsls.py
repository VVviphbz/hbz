#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-spock
���ߣ�����֦
���ڣ�2020.4.12
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
		print("��Ӯ��")
	elif player_number==4 and (computer_number==2 or computer_number==3):
		print("��Ӯ��")
	elif player_number==2 and (computer_number==0 or computer_number==1):
		print("��Ӯ��")
	elif player_number==3 and (computer_number==1 or computer_number==2):
		print("��Ӯ��")
	elif player_number==1 and (computer_number==0 or computer_number==4):
		print("��Ӯ��")
	elif player_number==computer_number:
		print("���ͼ�����µ�һ��")
	else:
		print("�����Ӯ��")
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)


