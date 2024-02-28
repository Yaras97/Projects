from datetime import datetime, timedelta
class Lecture:
    def __init__(self, topic, start_time, duration):
        self.topic = topic
        self.start_time = datetime.strptime(start_time, '%H:%M')
        self.duration = duration

class Conference:
    def __init__(self):
         self.konf = []

    @staticmethod  # время окончания лекции
    def end(konf_):
        return konf_.start_time + timedelta(hours=int(konf_.duration[:2]),
                                                      minutes=int(konf_.duration[3:]))
    @staticmethod   # вывод 00:00
    def result(res):
        return str(res)[:-3] if len(str(res).split(':')[0]) == 2 else '0' + str(res)[:-3]

    def add(self, lecture: Lecture):
        for lec in self.konf:
            if (lec.start_time <= lecture.start_time < self.end(lec)) or (lec.start_time < self.end(lecture) < self.end(lec)) or (lecture.start_time < lec.start_time < self.end(lecture)):
                raise ValueError("Провести выступление в это время невозможно")
        self.konf.append(lecture)
        self.konf.sort(key=lambda x: x.start_time)

    def total(self):
        tot = timedelta(hours=0, minutes=0)
        for long in self.konf:
            tot += timedelta(hours=int(long.duration[:2]),
                                                      minutes=int(long.duration[3:]))
        return self.result(tot)

    def longest_lecture(self):
        longest = timedelta(hours=0, minutes=0)
        for long in self.konf:
            dura = timedelta(hours=int(long.duration[:2]),
                             minutes=int(long.duration[3:]))
            if dura > longest:
                longest = dura
        return self.result(longest)

    def longest_break(self):
        kofebreak = timedelta(hours=0, minutes=0)
        for long in range(1, len(self.konf)):
            kofe = self.konf[long].start_time - self.end(self.konf[long - 1])
            if kofe > kofebreak:
                kofebreak = kofe
        return self.result(kofebreak)

    def str(self):
        return f'{self.konf}'