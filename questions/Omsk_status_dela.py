from utilities.regexp_check_with_query import check_regexp_with_queries


QUESTIONS = [
    (r"(получ\w*|узн\w*|как\w*)? ?(готов\w*|статус\w*|состоян\w*|этап\w*) (дел\w*|докум\w*|заявл\w*)", "111"),

]


test_phrases = [
    "статус дела",
    "узнать статус документа",
    # "Присвоение адреса",
    # "Присвоение адреса земельному участку",

]


test_phrases_additional = [

]

test_phrases.extend(test_phrases_additional)

check_regexp_with_queries(regular_expressions=QUESTIONS,
                          queries=test_phrases)
