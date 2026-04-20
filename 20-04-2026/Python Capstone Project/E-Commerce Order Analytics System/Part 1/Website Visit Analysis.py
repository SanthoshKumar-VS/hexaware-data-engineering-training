with open("../website_visits.txt", "r") as sk:
    visits = [line.strip() for line in sk]
for s in visits:
    print(s)
print("total number of visits:", len(visits))

uniqe_visitors = set(visits)
print("unique visitors:", uniqe_visitors)

visit_count = {}
for s in visits:
    visit_count[s] = visit_count.get(s, 0) + 1
print("{")
for s in visit_count:
    print(f'  "{s}": {visit_count[s]},')

print("}")

most_visitor = max(visit_count, key=visit_count.get)
print("most frequent visitor:", most_visitor)