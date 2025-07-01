from colormatrix import *

for key, value in colors.items():
    print(f'{key:10} {value}')

# YOUR CODE HERE
N = 12
atable = []
for row_index in range(N):
    arow = []
    for col_index in range(N):
        if row_index + col_index == N-1:
            arow.append('yellow')
        elif col_index < N-1-row_index:
            arow.append('green')
        else:
            arow.append('')
    atable.append(arow)
str_html = html_table(atable)
save_html(str_html, 'cmatrix03')