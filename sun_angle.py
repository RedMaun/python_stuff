def sun_angle(time):
    time = list(time)
    time.pop(2)
    hour = time[0] + time[1]
    minute = time[2] + time[3]
    hour = int(hour)
    minute = int(minute)
    if hour < 6:
        return "I don't see the sun!"
    if hour == 18:
        if minute > 0:
            return "I don't see the sun!"
        else:
            return 180
    time_now = hour*60 + minute - 360
    return time_now * 0.25

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("16:00"))