# Разность времен
h1, m1, s1 = (int(input()) for _ in '123')
h2, m2, s2 = (int(input()) for _ in '123')

h_res = h2 - h1
m_res = m2 - m1
s_res = s2 - s1

print(h_res * 60 * 60 + m_res * 60 + s_res)
