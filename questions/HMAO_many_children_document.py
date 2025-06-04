# -*-coding=utf-8-*-


from utilities.regexp_check_with_query import check_regexp_with_queries


QUESTIONS = [
    (r"(как? ?(можно|нужно|мне)?|какое|что (\w*делать|нужно)? ?(для|чтобы)?)? ?(оформ\w*|\w*делать||получ\w*|заказ\w*|\w*готов\w*)? ?(удостов\w* многод\w* семь\w*)", "204"),

]


test_phrases = [
    "как оформить удостовероение многодетной семьи",
    "оформить удостовероение многодетной семьи",
    "удостовероение многодетной семьи",
    "",
    "",

]


test_phrases_additional = [

]

test_phrases.extend(test_phrases_additional)

check_regexp_with_queries(regular_expressions=QUESTIONS,
                          queries=test_phrases)
