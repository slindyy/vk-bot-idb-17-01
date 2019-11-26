import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from time_schedule_and_item_schedule import TimeAndTimetable


def write_message(user_id, message):
    print(user_id, message)
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': 0})
    print("All OK" + '\n')


token = "7d29aeab4a857db2093b2f7e0421f9caa021bb4ba92c2066c19c937b725d4ebb344aa1b479aa53513542e"
vk = vk_api.VkApi(token = token)
longpoll = VkLongPoll(vk)
print("Server started" + '\n')


def sending_message(request):
    if request == "Привет" or request == "привет":
        write_message(event.user_id, "Здравствуй, товарищ! Для вызова списка команд напиши ключевое слово 'Команды'")
    elif request == "Расписание на сегодня" or request == "расписание на сегодня":
        answer = TimeAndTimetable()
        write_message(event.user_id, answer.timetable_for_today())
        del answer
    elif request == "Расписание на завтра" or request == "расписание на завтра":
        answer = TimeAndTimetable()
        write_message(event.user_id, answer.timetable_for_tomorrow())
        del answer
    elif request == "Время" or request == "время":
        answer = TimeAndTimetable()
        write_message(event.user_id, answer.get_time_for_end_occupation())
        del answer
    elif request.find('Расписание на', 0, len(request)) != -1 or request.find('расписание на', 0, len(request)) != -1:
        answer = TimeAndTimetable()
        write_message(event.user_id, answer.timetable_for_a_specific_date(request[14:20]))
        del answer
    elif request == 'Команды' or request == 'команды':
        commands = "Привет" + '\n' + 'Расписание на сегодня' + '\n' + 'Расписание на завтра' + '\n' + 'Время' + '\n'\
                   + 'Команды' + '\n' + 'Расписание на 01.01(ваша дата)' + '\n' + '(на это пока что все)'
        write_message(event.user_id, commands)
    else:
        write_message(event.user_id, "Не понятно. Для вызова списка команд напиши 'Команды'.")


for event in longpoll.listen():
    try:
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                request = event.text
                print("Сообщение: " + event.text + '\n')
                sending_message(request)
    except:
        longpoll = VkLongPoll(vk)
        print(VkLongPoll(vk))
        sending_message(request)

