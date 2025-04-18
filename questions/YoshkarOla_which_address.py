# -*-coding=utf-8-*-


from utilities.regexp_check_with_query import check_regexp_with_queries


QUESTIONS = [
    (r"какой адрес|какой", "0"),
]


test_phrases = [
    "какой",
    "какой какой",
    "адрес",
    "какой адрес",
    "не пон адрес",
    "не пон как адрес",
    "непон адрес",
    "непон как адрес",
]


test_phrases_additional = [

]

test_phrases.extend(test_phrases_additional)

check_regexp_with_queries(regular_expressions=QUESTIONS,
                          queries=test_phrases)
