import json

with open(input(), encoding='UTF-8') as nums:
    d = [int(i) for i in nums.read().split()]
statistic = {
    'count': len(d),
    'positive_count': len([i for i in d if i > 0]),
    'min': min(d),
    'max': max(d),
    'sum': sum(d),
    'average': round(sum(d) / len(d), 2)
}
with open(input(), 'w', encoding='UTF-8') as i:
    json.dump(statistic, i, indent=4)
