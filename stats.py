import sys
import collections

inputNum = [int(params) for params in sys.argv[1:]]
inputNum.sort()
'''
Python 的 del 只是減少該物件的 Reference counting，除非該記憶體位址已沒有任何物件參照，才有機會被 garbage collection

實務上的角度，del 指令能帶給你的效能提升有限，但容易造成可讀性與維護性上的負擔

故除非測過 benchmark 確定效能瓶頸真的發生在 del 與否、或「商業邏輯」真的需要你做這一步才能完成，才去使用

另外，在實務上也很少對一個 list 做 in-line 刪除元素的行為，因為很容易在後面的 routine 誤會了 list 的內容其實不一樣了
'''

print('your input (in ascending order):'+ str(inputNum))

# 宣告為有排序的dict
result = collections.OrderedDict()
'''
Good! 找了個除了原始的 dict、實務上最有可能接觸到的 collection data type 來用
'''

# 數量
numLen = len(inputNum)
# 總和
result['sum'] = sum(inputNum)
# 平均
result['mean'] = result['sum'] / numLen
# 中位數
if (numLen % 2 == 0):
    key = numLen // 2
    result['med'] = (inputNum[key] + inputNum[key+1]) / 2
else:
    key = numLen // 2
    result['med'] = (inputNum[key])
# 最小值
result['min'] = min(inputNum)
# 最大值
result['max'] = max(inputNum)

# 樣本標準差 & 眾數 處理
numMode = []
tmpNum = 0
for num in inputNum:
    tmpNum += (num - result['mean']) ** 2
    if (inputNum.count(num) >= 2 and numMode.count(num) == 0):
        numMode.append(num)
# '''
# inputNum.count() 在這裡會造成複雜度為 O(N**2)

# Try Again: 試著用 dict 的資料結構來做「用 key 查找、然後 counting 的行為」
# '''

# '''
# 另外，實務上，不太會像寫 C 一樣盡量節省 loops (i.e. 不太會做 O(3N) -> O(2N) 的事)

# 通常優先考慮可讀性與維護性 (因為若效能會是商業模型中的基礎，通常就直接選擇 C/C++ 或 Go 這類編譯式語言來編寫那些商業邏輯)

# 所以我們會選擇一個 loop 只做一件事，「樣本標準差」與「眾數」就會有各自的 routine (function) 各自 loop 處理各自要的內容

# Try Again: 試著將「樣本標準差」與「眾數」的 routine 拆開來做
# '''

# 樣本標準差
result['std'] = (tmpNum / numLen) ** 0.5

# 無眾數時處理
if(len(numMode) == 0):
    numMode = list(set(inputNum))

# 眾數
numMode.sort()

for k in result:
    v = result[k]
    print("{key:>4s}: {num:->15.2f}".format(key=k, num=v))
# '''
# 補充上課沒講的：實務上 dict.itemts() 從來不用，因為 items() 會多 copy 一份 result 出來
# '''

#為了眾數排序 單獨印
print("{key:>4s}: {num}".format(key='mode', num=numMode))
# '''
# 「,」後記得空白唷，比較好看
# '''
