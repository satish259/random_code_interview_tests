# coding=utf-8

def generate_sentences(subject, predicate, obj):
    """
    Generates a string of lists subject, predicate and obj to form sentences.
    Each list is iterated to form a sentence.
    Note: itertools.zip_longest would provide the same response.
    """
    out = ["{i} {j} {k}.".format(i=i, j=j, k=k) for i in subject
           for j in predicate
           for k in obj]
    return " ".join(out)
