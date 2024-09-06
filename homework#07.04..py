team1_name = 'Мастера кода'
team2_name = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды "Волшебники данных"!'

print('В команде "%s" участников: %s!' % (team1_name, team1_num))
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))
print('Команда "{}" решила задач:{}!'.format(team2_name, score_2))
print('"{}" решили задачи за {} с!'.format(team2_name, team2_time))
print(f'Команды решили {score_1} и {score_2} задачи.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задачи, в среднем по {time_avg} секунды на задачу!')
