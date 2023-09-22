# 1․ Գրել ֆունկցիա, որը․
#    - որպես արգումենտ կընդունի շրջանագծի շառավիղը (r) և սեկտորի անկյունը (alpha) ռադիաններով արտահայտված,
#    - կհաշվի և կտպի համապատասխան շառավղով և անկյունով շրջանի մակերեսը,
#    - բանաձևը՝ S = (pi * r ** 2) * alpha / 360, բանաձևի մեջ alpha-ն արտահայտված է աստիճաններով։

# import math
# def radius_circle(r, a):
#     return (math.pi * r ** 2) * a / 360
# print(radius_circle(2, 90))


# 2․ Գրել ծրագիր, որը․
#    - կստանա 3 արգումենտ՝ տարի, ամիս, օր,
#    - կտպի թե նշված օրն շաբաթվա որ օրն է։

# import datetime
# def day_of_week(year, month, day):
#     week_days = {0: 'Monday', 
#                  1: 'Tuesday', 
#                  2: 'Wednesday', 
#                  3: 'Thursday', 
#                  4: 'Friday', 
#                  5: 'Saturday',
#                  6: 'Sunday'}
#     day_int = datetime.date(year, month, day).weekday()
#     return week_days[day_int]
# print(day_of_week(2023, 9, 22))


# 3․ Գրել ֆունկցիա, որը․
#    - կստանա արգումենտ արաբական բնական թիվ (0-ից մեծ),
#    - կվերադրձնի այդ թիվը հռոմեական տեսքով,
#    հռոմեական թվերի համարժեքները՝ I-1, V-5, X-10, L-50, C-100, D-500, M-1000,
#    օրինակ՝ 15 -> XV,
#            72 -> LXXII,
#            9 -> IX:

def arabic_num(n: int):
    def default_logic(i, a):
        r_number = ''
        default_num = {1: 'I',
                       5: 'V',
                       10: 'X',
                       50: 'L',
                       100: 'C', 
                       500: 'D', 
                       1000: 'M'}
        if i < 4:
            r_number += i * default_num[1 * a]
        elif i == 4:
            r_number += default_num[1 * a] + default_num[5 * a]
        elif i == 5:
            r_number += default_num[5 * a]
        elif i <= 8:
            r_number += default_num[5 * a] + (i - 5 * a) * default_num[1 * a]
        elif i == 9:
            r_number += default_num[10 * a] + default_num[1 * a]
        return r_number
    
    roman_num = ''
    c = (n - 1000 * (n // 1000)) // 100
    d = (n - (n // 100) * 100) // 10
    j = n % 10
    if n <= 3999:
        if n // 1000 >= 1:
            roman_num += n // 1000 * 'M'
        if c >= 1:
            roman_num += default_logic(c, 100)
        if d >= 1:
            roman_num += default_logic(d, 10)
        if j >= 1:
            roman_num += default_logic(j, 1)
        return roman_num
    else:
        raise ValueError
print(arabic_num(400)) 

