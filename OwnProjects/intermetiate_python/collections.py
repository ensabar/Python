# Collections: counter, namedtuple, orederdDict, defaultdict, deque
from collections import Counter

a = 'aaaaaaaabbbbccccdddd'

my_counter = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())

print(my_counter.most_common(1))
print(my_counter.most_common(1)[0]) 
print(my_counter.most_common(1)[0][0]) 

print(list(my_counter.elements()))

# namedtuples
from collections import namedtuple
Point = namedtuple('Point', 'x,y')
pt = Point(1,-4)
print(pt)
print(pt.x)
print(pt.y)

# orderedDict
from collections import OrderedDict

ordered_dict = OrderedDict()

ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)

ordered_dict = {}

ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)

# defaultDict
from collections import defaultdict
d = defaultdict(list)
d['a'] = 2
d['b'] = 5
print(d['c'])

# deque
from collections import deque
d = deque()

d.append(2)
d.append(3)
print(d)

d.appendleft(9)
print(d)

d.popleft()
print(d)

d.extend([4, 5, 6])
print(d)
d.extendleft([9, 85, 56])
print(d)

d.rotate(1)
print(d)

d.rotate(2)
print(d)

d.rotate(-2)
print(d)