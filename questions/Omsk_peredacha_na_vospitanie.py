from utilities.regexp_check_with_query import check_regexp_with_queries


QUESTIONS = [
    (r"(пособ\w*|деньги|ежемес\w*|выпл\w*) (за|при) (воспит\w*)? ?прием\w* (детей|ребенка)|(за|при) перед\w* (детей|ребенка) в (приемную)? ?семью", "74"),


]

test_phrases = [
    "деньги за приемных детей",
    "пособие за передачу детей в приемную семью",
    "выплаты при передаче ребенка в семью",
    "деньги за воспитание приемного ребенка"
]


test_phrases_additional = [

]

test_phrases.extend(test_phrases_additional)

check_regexp_with_queries(regular_expressions=QUESTIONS,
                          queries=test_phrases)
