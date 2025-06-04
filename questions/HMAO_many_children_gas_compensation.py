# -*-coding=utf-8-*-


from utilities.regexp_check_with_query import check_regexp_with_queries


QUESTIONS = [
    (r"(как? ?(можно|нужно|мне)?|какое|что (\w*делать|нужно)? ?(для|чтобы)?)? ?(оформ\w*|\w*делать||получ\w*|заказ\w*|\w*готов\w*)? ?(выпл\w*|компен\w*) ?(для|на) (оплат\w*|расход\w*) газиф\w* ?(для)? многод\w* сем\w*", "209"),

]


test_phrases = [
    "как оформить компенсацию на оплату газификации для многодетной семьи",
    "оформить компенсацию на оплату газификации для многодетной семьи",
    "компенсацию на оплату газификации для многодетной семьи",
    "компенсация на оплату газификации для многодетной семьи",
    "компенсация на оплату газификации многодетной семьи",

]


test_phrases_additional = [

]

test_phrases.extend(test_phrases_additional)

check_regexp_with_queries(regular_expressions=QUESTIONS,
                          queries=test_phrases)
