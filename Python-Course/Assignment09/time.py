class Time():
    def __init__(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s
    def sum(self, mehman):
        result = Time(None, None, None)
        result.second = t1.second + t2.second
        result.minute = t1.minute + t2.minute
        result.hour = t1.hour + t2.hour
        if result.second >= 60 :
            result.second -= 60
            result.minute +=1
        if result.minute >= 60 :
            result.minute -= 60
            result.hour +=1
        return result
        return result
    def abs(self, mehman):
        result = Time(None, None, None)
        result.second = t1.second - t2.second
        result.minute = t1.minute - t2.minute
        result.hour = t1.hour - t2.hour
        if result.second <= -1:
            result.second +=60
            result.minute -= 1
        if result.minute <= -1:
            result.minute += 60
            result.hour -= 1
        if result.hour <= -1:
            result.hour = None
            result.minute = None
            result.second = None
            print('Time1 is less than Time2')
        return result

    def show(self):
        print(self.hour, ':', self.minute, ':', self.second)


t1 = Time(2,30,45)
t2 = Time(3,17,40)
t1.show()
t2.show()
t3 = t1.abs(t2)
t3.show()
