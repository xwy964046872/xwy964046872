# 初始状态下带宽每分钟可以完成 1 个插件的下载。假定每分钟选择以下两种策略之一:
#
# 使用当前带宽下载插件
# 将带宽加倍（下载插件数量随之加倍）
## 请返回小扣完成下载 n 个插件最少需要多少分钟。
#
# 注意：实际的下载的插件数量可以超过 n 个


n = 4
s = 1
t = 1

max = 1

while max < n:
    t += 1
    max = 2**(t-1)
#    print(max)
print(t)

# minimum download time

