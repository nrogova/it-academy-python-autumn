"""Task 4 В файле хранятся данные с сайта IMDB.
Скопированные данные хранятся в файле ./data6/ ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла  top250_movies.txt – названия файлов,
ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.
"""
# Unfortunately, I cannot create histograms.
try:
    f = open("ratings.list", encoding="ISO-8859-1")
    a = [line.strip() for line in f]
    x = a[28:278]
    b = [line.split() for line in x]

    for el in b:
        t = el[3:-1]
        top_str = ' '.join(t)
        print(top_str)
        with open('top250_movies.txt', 'a') as top:
            top.write(top_str + "\n")

    for el in b:
        y = el[-1].strip('()/I')
        with open('years.txt', 'a') as years:
            years.write(y + "\n")

    for el in b:
        r = el[2]
        with open('rank.txt', 'a') as rank:
            rank.write(r + "\n")

    f.close()

except FileNotFoundError:
    message = "File not found. Please save file to required directory"
    print(message)
