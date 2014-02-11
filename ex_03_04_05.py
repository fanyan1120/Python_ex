#coding=utf-8

print "2 x (3 + 6) / 5 = ", 2 * (3 + 6) / 5
print "5%3 = ", 5%3
print "? 7 >  12%13", 7 >  12%13

# lili, qiang和papa有一个腐败专用小金库，每人都往这个小金库里存钱
# 这回腐败需要算个账
lili = 50 # lili的余额
qiang = 73.5 # qiang的余额
papa = 10.4 # papa的余额
meal_cost = 104.00
if (meal_cost > lili + qiang + papa):
    owe_total = meal_cost - (lili + qiang + papa)
    avg_cost= meal_cost/3
    print "本次消费", meal_cost, "元, 平均每人消费", avg_cost, "元"
    print "如果不想留下来刷盘子还要付", owe_total, "元"
    print "\tlili还要付", avg_cost - lili, "元"
    print "\tqiang还要付", avg_cost - qiang, "元"
    print "\tpapa还要付", avg_cost - papa, "元"
if (meal_cost < lili + qiang + papa):
    owe_total = lili + qiang + papa - meal_cost
    avg_cost= meal_cost/3
    print "本次消费", meal_cost, "元, 平均每人消费", avg_cost, "元"
    print "小金库还剩", owe_total, "元"
    print "\tlili还剩", lili - avg_cost, "元"
    print "\tqiang还剩", qiang - avg_cost, "元"
    print "\tpapa还剩", papa - avg_cost, "元"
    print "lili上次剩余 %f 元，这次剩余 %f 元 qiang上次剩余 %f 元，这次剩余 %f 元 papa上次剩余 %f 元，这次剩余 %f 元 " % (lili, lili - avg_cost, qiang, qiang - avg_cost, papa, papa - avg_cost)
