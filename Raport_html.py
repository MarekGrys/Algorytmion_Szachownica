from string import Template
import os
import datetime

dane = []
ilosc_plikow = 0
dzisiaj = str(datetime.date.today())

for fname in os.listdir('in'):
    if fname.endswith('txt'):
        podejscie = {}
        try:
            with open(os.path.join('in', fname), 'r') as in_file:
                with open(os.path.join('out', fname), 'r') as out_file:
                    podejscie['name'] = fname
                    podejscie['in'] = in_file.read().replace('\n', '<br>')
                    podejscie['out'] = out_file.read().replace('\n', '<br>')
                    ilosc_plikow += 1

            dane.append(podejscie)

        except OSError:
            pass
tabela = ""
for zawartosc in dane:
    row = "<tr>"
    row += f'<td>{zawartosc["name"]}</td>'
    row += f'<td class="board">{zawartosc["in"]}</td>'
    row += f'<td class="false">{zawartosc["out"]}</td>'
    row += "</tr>"
    tabela += row
d = {
    'date': dzisiaj,
    'output': tabela,
    'no_files': str(ilosc_plikow),
}
nazwa, nazwa_sufiks = 'raport_' + dzisiaj, 1
if os.path.exists(nazwa + '.html'):
    while os.path.exists(nazwa + '_' + str(nazwa_sufiks) + '.html'):
        nazwa_sufiks += 1
    nazwa += '_' + str(nazwa_sufiks)
with open('wzor.html', 'r') as f:
    src = Template(f.read())
    result = src.substitute(d)
    with open(nazwa + '.html', 'w') as fout:
        fout.write(result)
    print(nazwa + '.html')
