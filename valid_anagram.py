s = "xx"
t = "x"

# Anagrams must have the same length
if len(s) != len(t):
    print(False)
else:
    latter_occur = [0] * 26
    for i in range(len(s)):
        alpha_sindex = ord(s[i]) - ord("a")
        latter_occur[alpha_sindex] += 1
        alpha_tindex = ord(t[i]) - ord("a")
        latter_occur[alpha_tindex] -= 1

    if all(count == 0 for count in latter_occur):
        print(True)
    else:
        print(False)
