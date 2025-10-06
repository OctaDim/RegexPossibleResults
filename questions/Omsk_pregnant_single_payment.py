from utilities.regexp_check_with_query import check_regexp_with_queries


QUESTIONS = [
    (r"декретные|(пособ\w*|деньги|ежемес\w*) (по уходу|за ребенка до полутора лет|за декретный ?(отпуск)?|по уходу за ребенком|не работающим для детей)", "73"),]


test_phrases = [
    "пособие по уходу",
    "деньги за ребенка до полутора лет",
    "пособие не работающим для детей",
    "ежемесячное по уходу за ребенком",
    "декретные",
    "деньги за декретный отпуск"
]


test_phrases_additional = [

]

test_phrases.extend(test_phrases_additional)

check_regexp_with_queries(regular_expressions=QUESTIONS,
                          queries=test_phrases)
