import os


def timeConversion(s):
    noon = s[8:10]
    hh = s[0:2]
    mm = s[3:5]
    ss = s[6:8]
    if noon == "PM":
        if int(hh) < 12:
            hh = str(int(hh) + 12)
    if noon == "AM":
        if int(hh) >= 12:
            hh = int(hh) - 12
            if hh < 10:
                hh = "0" + str(hh)
            else:
                hh = str(hh)
    return hh + ":" + mm + ":" + ss


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s_inp = input()
    result = timeConversion(s_inp)
    fptr.write(result + '\n')
    fptr.close()
