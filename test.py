s = "abcd"
longest_substr = 0
for n in range(len(s)):
    freq_list = [0] * 256
    for m in (range(n, len(s))):
        freq_list[ord(s[m])] += 1

sub_str = s[n:m]
print(sub_str)
