""" Reverse
Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın.
Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]

Çözüm: """

liste =[[1, 2], [3, 4], [5, 6, 7]]
liste = liste[::-1]

for i in range(len(liste)):
    (liste[i])=(liste[i])[::-1]
print(liste)
