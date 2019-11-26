from datetime import datetime
import datetime
import calendar
import time
import json
import requests


class TimeAndTimetable:
    def __init__(self):
        print()

    def get_time_for_end_occupation(self):
        time_now = datetime.datetime.today().strftime("%H:%M:%S")

        if (time_now > '08:30:00') and (time_now < '09:15:00'):
            result = TimeAndTimetable.time_difference('09:15:00', time_now) + " до начала перерыва 1 пары."
        elif (time_now > '09:15:00') and (time_now < '09:25:00'):
            result = TimeAndTimetable.time_difference('09:25:00', time_now) + " до конца перерыва 1 пары."
        elif (time_now > '09:25:00') and (time_now < '10:10:00'):
            result = TimeAndTimetable.time_difference('10:10:00', time_now) + " до конца 1 пары."
        elif (time_now > '10:10:00') and (time_now < '10:20:00'):
            result = TimeAndTimetable.time_difference('10:20:00', time_now) + " до начала 2 пары."
        elif (time_now > '10:20:00') and (time_now < '11:05:00'):
            result = TimeAndTimetable.time_difference('11:05:00', time_now) + " до начала перерыва 2 пары."
        elif (time_now > '11:05:00') and (time_now < '11:15:00'):
            result = TimeAndTimetable.time_difference('11:15:00', time_now) + " до конца перерыва 2 пары."
        elif (time_now > '11:15:00') and (time_now < '12:00:00'):
            result = TimeAndTimetable.time_difference('12:00:00', time_now) + " до конца 2 пары."
        elif (time_now > '12:00:00') and (time_now < '12:20:00'):
            result = TimeAndTimetable.time_difference('12:20:00', time_now) + " до начала 3 пары."
        elif (time_now > '12:20:00') and (time_now < '13:05:00'):
            result = TimeAndTimetable.time_difference('13:05:00', time_now) + " до начала перерыва 3 пары."
        elif (time_now > '13:05:00') and (time_now < '13:15:00'):
            result = TimeAndTimetable.time_difference('13:15:00', time_now) + " до конца перерыва 3 пары."
        elif (time_now > '13:15:00') and (time_now < '14:00:00'):
            result = TimeAndTimetable.time_difference('14:00:00', time_now) + " до конца 3 пары."
        elif (time_now > '14:00:00') and (time_now < '14:10:00'):
            result = TimeAndTimetable.time_difference('14:10:00', time_now) + " до начала 4 пары."
        elif (time_now > '14:10:00') and (time_now < '14:55:00'):
            result = TimeAndTimetable.time_difference('14:55:00', time_now) + " до начала перерыва 4 пары."
        elif (time_now > '14:55:00') and (time_now < '15:05:00'):
            result = TimeAndTimetable.time_difference('15:05:00', time_now) + " до конца перерыва 4 пары."
        elif (time_now > '15:05:00') and (time_now < '15:50:00'):
            result = TimeAndTimetable.time_difference('15:50:00', time_now) + " до конца 4 пары."
        else:
            if (time_now > '00:00:00') and (time_now < '08:30:00'):
                result = TimeAndTimetable.time_difference('08:30:00', time_now) + " до начала 1 пары."
            elif (time_now > '15:50:00') and (time_now < '24:00:00'):
                old_day = TimeAndTimetable.time_difference('24:00:00', time_now)
                new_day = TimeAndTimetable.time_difference('08:30:00', '00:00:00')
                result = TimeAndTimetable.time_conversion_to_standard_view(((TimeAndTimetable.conversion_in_seconds(old_day)) + (TimeAndTimetable.conversion_in_seconds(new_day)))) + " до начала 1 пары."

        return result

    @staticmethod
    def conversion_in_seconds(user_time):
        hours = int(user_time[0:2])
        minutes = int(user_time[3:5])
        seconds = int(user_time[6:8])
        user_time = hours * 3600 + minutes * 60 + seconds

        return user_time

    @staticmethod
    def time_conversion_to_standard_view(time):
        hour = time // 3600
        time -= (hour * 3600)
        minutes = time // 60
        time -= (minutes * 60)
        result_time = datetime.time(hour, minutes, time, 0000)
        result_time = result_time.strftime("%H:%M:%S")

        return result_time

    @staticmethod
    def time_difference(start, end):
        all_time_start = TimeAndTimetable.conversion_in_seconds(start)
        all_time_end = TimeAndTimetable.conversion_in_seconds(end)
        result_sec = all_time_start - all_time_end
        if (result_sec < 0):
            result_sec = abs(result_sec)
        result_time = TimeAndTimetable.time_conversion_to_standard_view(result_sec)

        return result_time

    @staticmethod
    def get_json_file(day_of_the_week):
        with open("timetable.json", encoding='utf-8') as json_file:
            json_data = json.load(json_file)
        name_day_in_week = TimeAndTimetable.get_name_the_day_in_week(day_of_the_week)

        return json_data[name_day_in_week]

    @staticmethod
    def get_name_the_day_in_week(day_of_the_week):
        if day_of_the_week == 0:
            return 'monday'
        elif day_of_the_week == 1:
            return 'tuesday'
        elif day_of_the_week == 2:
            return 'wednesday'
        elif day_of_the_week == 3:
            return 'thursday'
        elif day_of_the_week == 4:
            return 'friday'
        elif day_of_the_week == 5:
            return 'saturday'
        else:
            return 'Какая то ошибка.'

    def timetable_for_today(self):
        day_for_week = datetime.datetime.today().weekday()
        date_now = datetime.date.today().strftime("%m.%d")
        if day_for_week != 6:
            day_in_json_file = TimeAndTimetable.get_json_file(day_for_week)
            final_str = TimeAndTimetable.dictionary_partitioning(day_in_json_file, date_now)
            return final_str
        else:
            return 'Сегодня воскресенье, а значит пар нет товарищ!'

    def timetable_for_tomorrow(self):
        day_for_week = datetime.datetime.today().weekday()
        if day_for_week == 6:
            day_for_week = 0
        else:
            day_for_week += 1
        date_now = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%m.%d")
        if day_for_week != 6:
            day_in_json_file = TimeAndTimetable.get_json_file(day_for_week)
            final_str = TimeAndTimetable.dictionary_partitioning(day_in_json_file, date_now)
            return final_str
        else:
            return 'Завтра воскресенье - можно расслабиться и отдохнуть. МинЗдрав рекомендует!'

    def timetable_for_a_specific_date(self, user_date):
        flag = 0
        try:
            day_for_week = datetime.datetime(2019, int(user_date[3:5:]), int(user_date[0:2:]), 0, 0, 0, 0000).weekday()
            user_date = TimeAndTimetable.date_swap(user_date)
        except:
            flag = 1

        if flag == 1:
            return 'Неправильная дата.'
        elif day_for_week != 6:
            day_in_json_file = TimeAndTimetable.get_json_file(day_for_week)
            final_str = TimeAndTimetable.dictionary_partitioning(day_in_json_file, user_date)
            return final_str
        else:
            return 'В этот день воскресенье! Отдыхай!'

    @staticmethod
    def date_swap(date):
        try:
            date = date[3:5:] + '.' + date[0:2:]
        except:
            return 'Это некорректная дата.'

        return date

    @staticmethod
    def dictionary_partitioning(day_in_json_file, date):
        class_object_string = ''
        for value_day in day_in_json_file:
            class_object = day_in_json_file.get(value_day)
            if type(class_object) == dict:
                check_date = TimeAndTimetable.check_if_item_is_on(date, class_object.get('date_object'))
                if check_date == True:
                    class_object_string += 'Пара №{0}: '.format(value_day[0:1])
                    class_object_string += (TimeAndTimetable.extracting_information_object(class_object) + '\n')

            elif type(class_object) == list:
                class_object_string += 'Пара №{0}: \n'.format(value_day[0:1])
                for value_list in class_object:
                    check_date = TimeAndTimetable.check_if_item_is_on(date, value_list.get('date_object'))
                    if check_date == True:
                        class_object_string += (TimeAndTimetable.extracting_information_object(value_list) + '\n')
        if class_object_string != '':
            return class_object_string
        else:
            return 'Походу в этот день нет пар!'

    @staticmethod
    def check_if_item_is_on(date, user_date):
        if type(user_date) == list:
            for value_date in user_date:
                date_object = TimeAndTimetable.one_date_to_two_date(value_date)
                if type(date_object) == list:
                    if (date >= date_object[0]) and (date <= date_object[1]):
                        flag = True
                        break
                else:
                    if date == date_object:
                        flag = True
                        break
            if flag:
                return True
            else:
                return False
        else:
            date_object = TimeAndTimetable.one_date_to_two_date(user_date)
            if (date >= date_object[0]) and (date <= date_object[1]):
                return True
            else:
                return False

    @staticmethod
    def one_date_to_two_date(date):
        if date.find('-', 0) != -1:
            final_list_date = [date[0:5:], date[6:11]]
            final_list_date[0] = TimeAndTimetable.date_swap(final_list_date[0])
            final_list_date[1] = TimeAndTimetable.date_swap(final_list_date[1])
        else:
            final_list_date = TimeAndTimetable.date_swap(date)

        return final_list_date

    @staticmethod
    def extracting_information_object(class_object):
        class_object_string = class_object.get('name_object') + ", "
        class_object_string += class_object.get('name_teacher') + ", "
        class_object_string += class_object.get('classroom') + ", "
        class_object_string += class_object.get('type_of_object') + ". "

        return class_object_string


qwe = TimeAndTimetable()
#print(qwe.timetable_for_a_specific_date('01.01'))
print(qwe.get_time_for_end_occupation())
