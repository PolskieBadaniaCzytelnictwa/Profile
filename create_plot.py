import polars as pl
import matplotlib.pyplot as plt
import os
os.chdir(os.path.dirname(__file__))


my_colors = [
    '#00AADB',
    '#981923',
    '#193441',
    '#E0404B',
    '#00F0F0',
    '#0070C0',
    '#006683',
    '#5B0F15',
    '#0F1F27',
    '#951821',
    '#009090',
    '#004373',
    '#16CBE1',
    '#D12230',
    '#30797E']


def format_ticks(list):
    for i, x in enumerate(list):
        if len(x) > 10:
            if len(x.split(' '))==3:
                first_margin = ' '*(15-len(x.split(' ', maxsplit=1)[0])//2)
                second_margin = ' '*(15-len(x.split(' ', maxsplit=1)[1])//2)
                list[i] =  first_margin+x.split(' ', maxsplit=1)[0]+first_margin+'\n'+second_margin+x.split(' ', maxsplit=1)[1]+second_margin
            else:
                first_part = x.split(' ')[0]+' '+x.split(' ')[1]
                second_part = x.split(' ')[2]+' '+x.split(' ')[3]

                first_margin = ' '*(15-len(first_part)//2)
                second_margin = ' '*(15-len(second_part)//2)
                list[i] =  first_margin+first_part+first_margin+'\n'+second_margin+second_part+second_margin
        else :
            list[i] = ' '*(12-len(x)) + x
    return list


df = pl.read_excel('./profile.xlsx')

kategorie_pionowe = df.select(['kat', 'zmienna']).rows()
kategorie_poziome = df.columns[2:]
kategorie_kombinacje = [(pozioma, pionowa) for pozioma in kategorie_poziome for pionowa in kategorie_pionowe]

wartosci = df.select(pl.col(pl.Float64)).melt()['value'].to_list()

colors = my_colors[:len(kategorie_pionowe)]*len(kategorie_poziome)

size_reference = 430
font_lato = {'fontname': 'Lato'}

fig, ax = plt.subplots(figsize=(7, 7))

for i, k in enumerate(kategorie_kombinacje):
    size = size_reference * (wartosci[i] / wartosci[i % 11]) * (wartosci[i] / wartosci[i % 11])
    size = max(size, 200)
    plt.scatter(kategorie_poziome.index(k[0]), 10 - kategorie_pionowe.index(k[1]),
                s=size, c=colors[i], zorder=2, edgecolors='none')

    txt = round(wartosci[i], 2)
    percent_value = f"{int(txt * 100)}"
    plt.annotate(percent_value, (kategorie_poziome.index(k[0]), 10 - kategorie_pionowe.index(k[1])),
                color='white', weight='bold', ha='center', va='center', fontsize=7.8)

# tutaj są 
plt.xticks(range(len(kategorie_poziome)), ['' for x in kategorie_poziome], rotation=90, ha="left", fontsize=8)
for i, x in enumerate(format_ticks(kategorie_poziome)):
    ax.text(i, 12.2, x, ha='center', va='center', fontsize=8, rotation=90)

plt.yticks(range(len(kategorie_pionowe)),
            [x[1] for x in kategorie_pionowe[::-1]],
            fontsize=8)

ax.xaxis.set_ticks_position('top')
ax.set_frame_on(False)

# Add grid lines
ax.grid(True, linestyle='-', linewidth=0.8, alpha=1, color='black')

ax.text(-3.7, 3.5, '-'*50, ha='left', va='center', fontsize=8)
ax.text(-3.7, 8.5, '-'*50, ha='left', va='center', fontsize=8)
ax.text(-3.7, 0.3, 'Wykształcenie', ha='left', va='bottom', fontsize=8, rotation=90)
ax.text(-3.7, 5.6, 'Wiek', ha='center', va='bottom', fontsize=8, rotation=90)
ax.text(-3.7, 9.2, 'Płeć', ha='left', va='bottom', fontsize=8, rotation=90)

plt.savefig('bubble_web.png', bbox_inches='tight')