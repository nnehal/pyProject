strs = ["flower", "flow", "flight"]

pref = "flower"
pref_len = len(pref)

for p in strs[1:pref_len]:
    while pref != p[0:pref_len]:
        pref_len -=1
        if pref_len == 0:
            pref = "fudge"
            break 
            