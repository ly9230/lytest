import pytest
from survey import AnonymousSurvey


@pytest.fixture
def language_survey():
    """一个可供所有函数使用的AnoymousSurvey实例"""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey


def test_store_single_response(language_survey):
    language_survey.store_response('English')
    assert 'English' in language_survey.responses


def test_store_three_response(language_survey):
    """三个答案会被储存"""
    responses = ['English', 'Spanish', 'Chinese']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses
