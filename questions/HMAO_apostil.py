# -*-coding=utf-8-*-


from utilities.regexp_check_with_query import check_regexp_with_queries


QUESTIONS = [
    (r"(как? ?(можно|нужно|мне)?|какое|что (\w*делать|нужно)? ?(для|чтобы)?)? ?(оформ\w*|\w*делать||получ\w*|заказ\w*|\w*готов\w*)? ?(апост\w*)", "201"),

]


test_phrases = [
    "как оформить апостиль",
    "какое оформление апостиля",
    "апостиль",
    "",
    "",

]


test_phrases_additional = [

]

test_phrases.extend(test_phrases_additional)

check_regexp_with_queries(regular_expressions=QUESTIONS,
                          queries=test_phrases)
