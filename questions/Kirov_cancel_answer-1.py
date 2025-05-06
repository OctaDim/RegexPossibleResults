from utilities.regexp_check_with_query import check_regexp_with_queries


QUESTIONS = [
    (r'(?<!\bне)\s?\bотказ|\bне приду', "11111111"),

]


test_phrases = [
    "отказываюсь",
    "отказ",
    "отбой",
    # "ка бэ",
    # "кэ бэ",
    # "КБ",
    # "Оформление карты болельщика",
    # "Получить карту болельщика",
]


test_phrases_additional = [

]

test_phrases.extend(test_phrases_additional)

check_regexp_with_queries(regular_expressions=QUESTIONS,
                          queries=test_phrases)
