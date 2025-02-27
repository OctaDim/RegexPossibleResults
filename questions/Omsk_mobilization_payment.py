from utilities.regexp_check_with_query import check_regexp_with_queries


QUESTIONS = [
    (r'предоставление единовременной денежной выплаты|выплаты участникам сво|выплаты участникам специальной военной операции|выплата губернатора как участнику сво|выплата участнику сво|единовременная выплата участнику сво', '28'),
    (r'(один)? ?миллион за участника сво|(один)? ?миллион членам погибшего участника сво', '28'),
]


test_phrases = [
    "миллион за участника сво",
    "миллион членам погибшего участника сво",
]


test_phrases_additional = [

]

test_phrases.extend(test_phrases_additional)

check_regexp_with_queries(regular_expressions=QUESTIONS,
                          queries=test_phrases)
