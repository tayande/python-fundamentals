def passing_scores(scores):
    result = []
    for one in range(len(scores)):
        if scores[one] >= 50:
            result.append(scores[one])
    return result
print(passing_scores([49, 50, 80, 65]))


# part c. Assertions

assert passing_scores([49, 50]) == [50]
assert passing_scores([55]) == [55]
assert passing_scores([]) == []