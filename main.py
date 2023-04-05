from module import *
csincsillak:list[Csincsilla] = []
file = open(file='chi.txt', mode='r', encoding='utf-8')
for sor in file: csincsillak.append(Csincsilla(sor))

print(f'osszesen {len(csincsillak)} db kiasallat adatai vannak az allomanyban')

szereti_db:int = 0
for cs in csincsillak:
    if cs.simi:
        szereti_db += 1
p:float = round(szereti_db / len(csincsillak) * 100, 2)
print(f'a csincsillag {p}%-a szereti, ha simogatjak')

for cs in csincsillak:
    if cs.kor >= 8 and cs.suly < 360:
        print(f'{cs.nev} oreg ({cs.kor} ev) es sovany ({cs.suly} g)')
        break
else: print(f'nincs oreg es sovany csincsilla')

# 'b' bebűvel kezdődő nevű kisállatok listája <kivalogatas>
# legnagyobb sulyu kisallat neve <maximum hely megh.>
# átlagéletkor <osszegzés => avg>
# a legfiatalabb neve és súlya <minimum hm.>
# input év -> ebben az évben szül. nevek listája <kiválogatás>
# 4 évesnél fiatalabbak száma