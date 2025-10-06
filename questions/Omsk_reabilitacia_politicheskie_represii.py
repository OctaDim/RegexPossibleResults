from utilities.regexp_check_with_query import check_regexp_with_queries


QUESTIONS = [
    (r"(как)? ?(оформить)? ?(пособ\w*|деньги|\w*плат\w*|льгот\w*|лекарств\w*|таблет\w*|что положено)? ?реабилитированн\w*", "76"),]


test_phrases = [
    "льготы реабилитированным",
    "реабилитированные",
    "лекарства реабилитированным",
    "выплаты реабилитированным",
    "что положено реабилитированным",
    "как оформить выплату реабилитированным"
]


test_phrases_additional = [

]

test_phrases.extend(test_phrases_additional)

check_regexp_with_queries(regular_expressions=QUESTIONS,
                          queries=test_phrases)
