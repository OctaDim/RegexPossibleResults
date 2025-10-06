from utilities.regexp_check_with_query import check_regexp_with_queries


QUESTIONS = [
    (r"(мед\w*)? ?(\w*реаб\w*|пом\w*|сан\w*кур\w*|сан\w* кур\w*|леч\w*|услуг\w*) (участн\w*)? ?(спец\w* воен\w* опер\w*|сво|эсвэо|эс вэ о|эсвео|эс ве о|эс вэо)", "77"),]


test_phrases = [
    "реабилитация СВО",
    "медицинская реабилитация участника специальной военной операции",
    "медицинская помощь СВО",
    "мед.реабилитация",
    "лечение участника СВО",
    "санкур участнику СВО",
    "сан кур участнику СВО",
    "медицинские услуги участнику СВО"
]


test_phrases_additional = [

]

test_phrases.extend(test_phrases_additional)

check_regexp_with_queries(regular_expressions=QUESTIONS,
                          queries=test_phrases)
