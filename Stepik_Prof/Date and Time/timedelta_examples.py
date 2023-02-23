from datetime import timedelta


def hours_minutes(td):
    """Функция перевода секунд в часы и минуты из timedelta"""
    return td.seconds // 3600, (td.seconds // 60) % 60


# Рабочая смена длится 7 часов 30 минут, сколько полных смен в 3-х сутках?

all_time = timedelta(days=3)

# продолжительность смены
sm = timedelta(hours=7, minutes=30)

sm_hm = hours_minutes(sm)
ost = hours_minutes(all_time % sm)
# res = hours_minutes((all_time % sm) // all_time)
res = hours_minutes((all_time % sm) // all_time.days)

print(f'В {all_time.days} сутках - {all_time//sm} смен по {sm_hm[0]} ч. {sm_hm[1]} мин')
print(f'Остается времени всего - {ost[0]} ч. {ost[1]} мин.')
print(f'Остается времени в 1 сут. - {res[0]} ч. {res[1]} мин.')
