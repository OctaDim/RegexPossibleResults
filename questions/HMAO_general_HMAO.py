# -*-coding=utf-8-*-


from utilities.regexp_check_with_query import check_regexp_with_queries


QUESTIONS = [
    (r"добровольному переселению|проживающих за рубежом|прибывшим в ХМАО|югр\w*|ханты\w* ?(автоном\w*)? ?(област\w*|округ\w*|регион\w*|район\w*|югр\w*)?|соотечественники|подъемное пособие соотечественникам|компенсация по договору найма соотечественникам|единовременная выплата соотечественникам", "35"),
    (r'ХМАО|югр\w*|ханты\w* ?(автоном\w*)? ?(област\w*|округ\w*|регион\w*|район\w*|югр\w*)?', '66'),

]


test_phrases = [
    "ХМАО",
    "хантыманс",
    "хантыманс окр",
    "хантыманс авт окр",
    "югр",

]


test_phrases_additional = [

]

test_phrases.extend(test_phrases_additional)

check_regexp_with_queries(regular_expressions=QUESTIONS,
                          queries=test_phrases)
