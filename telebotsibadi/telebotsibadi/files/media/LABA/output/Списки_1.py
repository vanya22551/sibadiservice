footballTeam = ['Neuer', 'Ramos', 'Kroos', 'Messi', 'Ronaldo']
reserve = []
goalkeepers = []
defenders = []
halfbacks = []
forwards = []

for f in footballTeam:
    print("Вот такую команду я хотел бы видеть в минифутболе,которая состоит из", len(footballTeam), 'игроков:', footballTeam)
    reserve.append('Ter Stegen')
    reserve.append('Humels')
    reserve.append('Coutinho')
    reserve.append('Lewandowski')
    reserve.append('Bale')
    print('В запасе у меня будет тоже', len(reserve), 'игроков.')
    print('Мои запасные игроки:', reserve)
    goalkeepers.append(footballTeam[:1])
    goalkeepers.append(reserve[:1])
    defenders.append(footballTeam[1:2])
    defenders.append(reserve[1:2])
    halfbacks.append(footballTeam[2:3])
    halfbacks.append(reserve[2:3])
    forwards.append(footballTeam[3:4])
    forwards.append(footballTeam[4:5])
    forwards.append(reserve[3:4])
    forwards.append(reserve[4:5])
    print('Моя заявка на игры:')
    print('Вратари:', goalkeepers)
    print('Защитники:', defenders)
    print('Полузащитники:', halfbacks)
    print('Нападющие:', forwards)
    break
