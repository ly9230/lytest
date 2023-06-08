from city_functions import city_function


def test_city_country():
    correct = city_function('santiago','chile','40000')
    assert correct == 'Santiago, Chile - population 40000'
