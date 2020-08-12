# coding=utf-8
from generate_sentences import generate_sentences


def test_generate_sentences():
    """
    This is the perfect case!
    """
    assert generate_sentences(["Mark", "Mary"], ["hates", "loves"], ["apples",
                                                                     "bananas"]) == "Mark hates apples. Mark hates bananas. Mark loves apples. Mark loves bananas. Mary hates apples. Mary hates bananas. Mary loves apples. Mary loves bananas."
    assert generate_sentences(["Vlad", "John"], ["drives"], ["car", "motorcycle",
                                                             "bus"]) != "John drives bus. John drives car. John drives motorcycle. Vlad drives bus. Vlad drives car. Vlad drives motorcycle."
