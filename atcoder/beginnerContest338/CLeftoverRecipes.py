n = int(input())
qList = list(map(int, input().split()))
aList = list(map(int, input().split()))
bList = list(map(int, input().split()))

result = 0


def judge(qListInput, aCount, bCount, oType):
    global aList
    global bList
    global result

    if oType == "a":
        # aを一個減らす
        qListA = []
        aSuccessFlag = True
        for i in range(n):
            newA = qListInput[i] - aList[i]
            if newA < 0:
                aSuccessFlag = False
                if aCount + bCount > result:
                    result = aCount + bCount
                return
            qListA.append(newA)
        if aSuccessFlag:
            judge(qListA, aCount + 1, bCount, "a")
            judge(qListA, aCount + 1, bCount, "b")

    if oType == "b":
        # bを一個減らす
        qListB = []
        bSuccessFlag = True
        for i in range(n):
            newB = qListInput[i] - bList[i]
            if newB < 0:
                bSuccessFlag = False
                if aCount + bCount > result:
                    result = aCount + bCount
                return
            qListB.append(newB)
        if bSuccessFlag:
            judge(qListB, aCount, bCount + 1, "a")
            judge(qListB, aCount, bCount + 1, "b")


judge(qList, 0, 0, "a")
judge(qList, 0, 0, "b")
print(result)
