#Маршрутизатор нейросигналов (Обработка импульсов)/
#Буфер памяти нейросети обрабатывает потоки сигналов([P1,P2,…..]). /
#Сигналы могут резонировать или гасить друг друга.
data_stream = [3, 5, 10, 0, -2, 7, 9, -7, 12]
buffer = []
for p in data_stream:
    if p > 0:                                   # импульс
        buffer.append(p)
        while len(buffer) > 1 and buffer[-1] % 2 == buffer[-2] % 2:
            buffer.append(buffer.pop() + buffer.pop())   # слияние left + right
    elif p == 0:                                # фильтр шума
        for x in buffer:
            if x % 5 == 0:
                buffer.remove(x)
                break
    else:                                       # интерференция
        for i in range(len(buffer) - 1):
            if abs(buffer[i] - buffer[i + 1]) == abs(p):
                del buffer[i:i + 2]             # удаляем пару
                break
        else:                                   # пара не найдена
            buffer.insert(0, abs(p))
print(buffer)