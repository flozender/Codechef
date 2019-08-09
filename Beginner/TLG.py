#  Starting leads = 0
p1_lead, p2_lead = 0, 0

lead = []
leader = []

for t in range(int(input())):
    x, y = map(int, input().split())
    p1_lead += x
    p2_lead += y
    #  P1 has the lead
    if p1_lead - p2_lead > 0:
        leader.append(1)
    # P2 has the lead
    else:
        leader.append(2)
    # store the lead
    lead.append(abs(p1_lead - p2_lead))

# Find the leader who has the max lead
ind = lead.index(max(lead))
# print leader and his max lead
print(leader[ind],max(lead))
