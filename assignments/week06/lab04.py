""" เขียน function ชื่อ analyze_scores ที่มีคุณสมบัติดังนี้:

รับ list ของคะแนน (ตัวเลข)
return dictionary ที่มี:

total: ผลรวมของคะแนนทั้งหมด
average: คะแนนเฉลี่ย (ปัดเศษ 1 ตำแหน่งหลังจุดทศนิยม)
highest: คะแนนสูงสุด
lowest: คะแนนต่ำสุด
passed: จำนวนคะแนนที่ >= 70 """


def analyze_scores(score):
    total = sum(score)
    avg = total / len(score)
    highest = max(score)
    lowest = min(score)
    passed = 0
    for i in score:
        if i > 70:
            passed = i
    return  {
        "total":total,
        "average":avg,
        "highest":highest,
        "lowest": lowest,
        "passed": passed,
    }
test_scores = [95, 87, 73, 68, 45]
result = analyze_scores(test_scores)
print(result)