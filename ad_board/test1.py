# import psycopg2

# conn = psycopg2.connect("dbname=postgres user=postgres")

# cur = conn.cursor()

# # Выполнить команду напрямую.
# cur.execute(
#     "CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);"
# )

# cur.execute(
#     "INSERT INTO test (num, data) VALUES (%s, %s)",
#     (100, "abc'def")
# )

# # Выполнить команду
# cur.execute("SELECT * FROM test;")
# # Но как получить результат её выполнения?..

# # А вот так. fetchone — «принести» одну строчку результата,
# # fetchall — все строчки.
# cur.fetchone()

# # Завершить транзакцию
# conn.commit()
# Закрыть курсор
# cur.close()
# # Закрыть подключение
# conn.close()

    dislikes = models.ManyToManyField(CustomUser)
    responses = models.ManyToManyField(CustomUser)
    accepted_responses = models.ManyToManyField(CustomUser)