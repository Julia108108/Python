# 15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, 
# а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, а для 
# тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему! Пользователь вводит одно число N
# – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое.
# Здесь каждое число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

count_wm = int(input('--> '))
min_wm = int(input('wm--> '))
max_wm = min_wm

min_wm_i = 0
max_wm_i = 0
for i in range(1, count_wm):
    wm = int(input('wm--> '))
    if wm > max_wm:
        max_wm = wm # перазписываем макисмум
        max_wm_i = i # и перезаписываем его индекс
    if wm < min_wm:
        min_wm = wm
        min_wm_i = i

print(max_wm, max_wm_i, min_wm, min_wm_i)
