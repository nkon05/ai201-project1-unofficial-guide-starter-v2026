def judge(question, expects, answer, results) -> bool:
    q = question
    e = " ".join((expects or "").lower().split())
    a = " ".join((answer or "").lower().split())
    r = [str(x.source) for x in results]

    if not e:
        print(q + ": FAILED - no expects phrase set - sources: " + ", ".join(r))
        return False

    if e in a:
        print(q + ": PASSED - sources: " + ", ".join(r))
        return True
    else:
        print(q + ": FAILED - sources: " + ", ".join(r))
        return False