from collections import deque

food = [int(n) for n in input().split(', ')]
stamina = deque(int(n) for n in input().split(', '))
peaks_difficulty = [[70, 'Kamenitza'], [60, 'Polezhan'], [100, 'Banski Suhodol'], [90, 'Kutelo'], [80, 'Vihren']]
conquered_peaks = []

for _ in range(7):
    if food.pop() + stamina.popleft() >= peaks_difficulty[-1][0]:
        conquered_peaks.append(peaks_difficulty[-1][1])
        peaks_difficulty.pop()
    if len(conquered_peaks) == 5:
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
        break

else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print("Conquered peaks:")
    [print(p) for p in conquered_peaks]
