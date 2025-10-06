from utilities.regexp_check_with_query import check_regexp_with_queries


QUESTIONS = [
    (r"(пересч\w*|перерасч\w*) (пенси\w*|w*\плат\w*) (по|за)? ?уход\w* (по|за)? ?(ребенком|дет\w*)? ?инвал\w*", "75"),


]

test_phrases = [
    "пересчет пенсии по уходу за инвалидами",
    "перерасчет пенсии по уходу за ребенком инвалидом"
]


test_phrases_additional = [

]

test_phrases.extend(test_phrases_additional)

check_regexp_with_queries(regular_expressions=QUESTIONS,
                          queries=test_phrases)
