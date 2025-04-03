from utilities.regexp_check_with_query import check_regexp_with_queries


QUESTIONS = [
    (r"(оформл\w*|получ\w*) карт\w* болельщ\w*||кэ бэ|ка бэ|карта болельщика|\bк ?б\b", "64"),

]


test_phrases = [
    "Карта болельщика",
    "ка бэ",
    "кэ бэ",
    "КБ",
    "Оформление карты болельщика",
    "Получить карту болельщика",
]


test_phrases_additional = [

]

test_phrases.extend(test_phrases_additional)

check_regexp_with_queries(regular_expressions=QUESTIONS,
                          queries=test_phrases)
