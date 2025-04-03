import re


def check_regexp_with_queries(
        regular_expressions: list[tuple[str]] | list[tuple[str, str]],
        queries: list[str]) -> None:
    QUESTIONS = regular_expressions
    test_phrases = queries

    for test_phrase in test_phrases:
        test_phrase = test_phrase.lower()
        found_flag = False
        for q in QUESTIONS:
            subquestions = None
            subsubquestions = None

            if re.search(q[0], test_phrase, flags=re.U):
                found_flag = True
                print(f"Test Phrase: {test_phrase}\n"
                      f"Regular Expression: {q}\n"
                      f"Result: Base Question - OK ✅ \n"
                      f"len(q): {len(q)}\n"
                      f"Action: Playback q[1]: '{q[1]}' \n\n")
                # continue
            # else:
            #     print(f"Test Phrase: {test_phrase}\n"
            #           f"Regular Expression: {q}\n"
            #           f"len(q): {len(q)}\n"
            #           f"Result: NOT FOUND IN QUESTION!!! 🚫\n\n")

            if len(q) == 3:
                subquestions = q[2]
                # print(f"Regular Sub Expression: {subquestions}")

            if subquestions:
                for subq in subquestions:  # Sub questions in q[2]
                    if re.search(subq[0], test_phrase, flags=re.U):
                        found_flag = True
                        print(f"Test Phrase: {test_phrase}\n"
                              f"Regular Sub Expression: {subq}\n"
                              f"Result: Sub Question - OK ✅✅ \n"
                              f"len(subq): {len(subq)}\n"
                              f"Action: Play sub_q[1]: '{subq[1]}' \n\n")
                        # continue
                    # else:
                    #     print(f"Test Phrase: {test_phrase}\n"
                    #           f"Regular Sub Expression: {subq}\n"
                    #           f"len(subq): {len(subq)}\n"
                    #           f"Result: NOT FOUND IN SUB QUESTION!!! 🚫🚫\n\n")

                    if len(subq) == 3:
                        subsubquestions = subq[2]
                        # print(f"Regular Sub Sub Expression: {subsubquestions}")

                    if subsubquestions:
                        for subsubq in subsubquestions:  # Sub sub questions in q[2]
                            if re.search(subsubq[0], test_phrase, flags=re.U):
                                found_flag = True
                                print(f"Test Phrase: {test_phrase}\n"
                                      f"Regular Expression: {q}\n"
                                      f"Result: Sub Sub Question - OK ✅✅✅ \n"
                                      f"len(subsubq): {len(subsubq)}\n"
                                      f"Action: Play sub_sub_q[1]: '{subsubq[1]}' \n\n")
                                # continue
                            # else:
                            #     print(f"Test Phrase: {test_phrase}\n"
                            #           f"Regular Sub Sub Expression: {subq}\n"
                            #           f"len(subsubq): {len(subsubq)}\n"
                            #           f"Result: NOT FOUND IN SUB SUB QUESTION!!! 🚫🚫🚫\n\n")

        if not found_flag:
            print(f"Test Phrase: {test_phrase}\n"
                  f"Result: NOT FOUND !!! ❌❌❌❌❌ \n\n")
