"""Temel Python Project

### Flatten
 Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]

Çözüm :"""

karisik = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
karisik_bos = []

def flatten(x]:
  for i in x:
    if isinstance(i, list):
      flatten(i)
    else:
      karisik_bos.append(i)
flatten(karisik)
print(karisik_bos)
