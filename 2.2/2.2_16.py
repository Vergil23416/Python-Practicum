p1, p2, p3 = int(input()), int(input()), int(input())
if max(p1, p2, p3) == p1 and min(p1, p2, p3) == p3:
    print('          Петя')
    print('  Вася')
    print('                  Толя')
    print('   II      I      III')
elif max(p1, p2, p3) == p1 and min(p1, p2, p3) == p2:
    print('          Петя')
    print('  Толя')
    print('                  Вася')
    print('   II      I      III')
elif max(p1, p2, p3) == p2 and min(p1, p2, p3) == p1:
    print('          Вася')
    print('  Толя')
    print('                  Петя')
    print('   II      I      III')
elif max(p1, p2, p3) == p2 and min(p1, p2, p3) == p3:
    print('          Вася')
    print('  Петя')
    print('                  Толя')
    print('   II      I      III')
elif max(p1, p2, p3) == p3 and min(p1, p2, p3) == p1:
    print('          Толя')
    print('  Вася')
    print('                  Петя')
    print('   II      I      III')
else:
    print('          Толя')
    print('  Петя')
    print('                  Вася')
    print('   II      I      III')
