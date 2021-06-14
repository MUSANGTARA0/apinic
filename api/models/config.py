import psycopg2
from string import printable
def decode(string):
    abc = [r for r in printable]
    num = [i for i in range(len(abc))]

    def char_split(string):
        return [char for char in string]

    def reverse(string):
        return string[::-1]
    result = string
    result = char_split(result)
    for i in range(len(result)):
        for j in range(len(abc)):
            for k in range(len(num)):
                if result[i] == num[j]:
                    result[i] = abc[j]
    return reverse("".join("{0}".format(n) for n in result))

config = {
    "DB": [12, 18, 23, 18, 25, 10],
    "USER": [28, 14, 27, 16, 29, 28, 24, 25],
    "PASS": [64, 1, 2, 3, 14, 22, 34, 27, 29],
    "HOST": [1, 75, 0, 75, 0, 75, 7, 2, 1],
    "PORT": [0, 4, 0, 4],
}
conn=psycopg2.connect(
    database=decode(config["DB"]),
    user=decode(config["USER"]),
    password=decode(config["PASS"]),
    host=decode(config["HOST"]),
    port=decode(config["PORT"])
)

conn.close()