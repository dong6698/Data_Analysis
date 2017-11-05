def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

# with open('testDuplicate.txt','r') as f:
#     for line in dedupe(f):
#         print(line)

with open('testDuplicate.txt','r') as f:
    print(set(f))

