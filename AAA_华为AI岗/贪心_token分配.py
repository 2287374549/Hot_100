# ACM 输入
line = input()
prior = [int(x) for x in line.split(',')]    # 中间是拿逗号分隔的

# 第一次遍历 —— 找到优先级小于 0 的，进行分割处理，被分割的有效段之间互不影响
cur = []                    # 存取当前优先级有效的连续的段
segments = []               # 存取被分割好的多个有效连续的段

for p in prior:
    if p > 0:
        cur.append(p)                   # 有效就存起来
    else:
        if cur:                         # 如果 cur 中有数值的话
            segments.append(cur)        # 存的是有效的段
            cur = []                    # cur 再去接受下一个有效的段

# 下面是一个双层嵌套的循环
total = 0                               # 最终的返回的数值，先置零
for seg in segments:                    # 依次处理其中每个 互不影响 的有效的段
    n = len(seg)
    tokens = [1] * n                    # 先都初始化分配 1 千个 tokens
    # 先从左到右遍历
    for i in range(1, n):                # 左闭右开 [1,n-1] —— 从 1 开始因为下面要 i-1
        if seg[i] > seg[i-1]:
            tokens[i] = tokens[i-1] + 1
    # 再从右到左遍历
    for i in range(n-2, -1, -1):        # 第一个 -1 是结束值，[n-2,0]，第二个是每次 -1 的意思
        if seg[i] > seg[i+1]:           # 为了不破坏开始从左到右的结果，因此取 max
            tokens[i] = max(tokens[i], tokens[i-1])
    total += sum(tokens)

print(total)