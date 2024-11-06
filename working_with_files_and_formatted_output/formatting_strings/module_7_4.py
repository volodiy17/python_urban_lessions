# Использование %
team1_name = input("Введите название первой команды: ")
print(f"название первой команды: %s" % team1_name)
team2_name = input("Введите название второй команды: ")
print(f"название второй команды: %s" % team2_name)

team1_num = input("Введите количество участников первой команды: ")
print(f"В команде %s участников: %s !" % (team1_name, team1_num))
team2_num = input("Введите количество участников второй команды: ")
print(f"В команде %s участников: %s !" % (team2_name, team2_num))
print("Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num))

# Использование format()
score_1 = input("Введите количество задач решённых командой {}: ".format(team1_name))
print("Команда {} решила задач: {} !".format(team1_name, score_1))
score_2 = input("Введите количество задач решённых командой {}: ".format(team2_name))
print("Команда {} решила задач: {} !".format(team2_name, score_2))

team1_time = input("Введите время за которое команда {} решила задачи: ".format(team1_name))
print("{} решили задачи за {} с !".format(team1_name, team1_time))
team2_time = input("Введите время за которое команда {} решила задачи: ".format(team2_name))
print("{} решили задачи за {} с !".format(team2_name, team2_time))

print(f"Команды решили {score_1} и {score_2} задач.")

challenge_result = str()
if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
    print(f'Победа команды {team1_name}!')
elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
    print(f'Победа команды {team2_name}!')
else:
    print('Ничья!')

tasks_total = int(score_1) + int(score_2)
time_avg = (float(team1_time) + float(team2_time)) / tasks_total
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.2f} секунды на задачу!.")
