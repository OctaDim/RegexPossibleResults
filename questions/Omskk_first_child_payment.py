from utilities.regexp_check_with_query import check_regexp_with_queries


QUESTIONS = [
    (r'(выплат\w*)? ?(с)? ?(рожден\w*)? ?перв\w* реб[её]н\w*|усынов\w* перв\w* реб[её]н\w*|выпл\w* (на|для)? ?перв\w* реб[её]н\w*', '45'),
]


test_phrases = [
    "выплата на первого ребенка",
    "выплата первого ребенка",
    "усыновление первого ребенка",

]


test_phrases_additional = [

]

test_phrases.extend(test_phrases_additional)

check_regexp_with_queries(regular_expressions=QUESTIONS,
                          queries=test_phrases)
