import pytest
import C15

@pytest.mark.skip("Not Implemented")
def test_q0_only_one_is_odd():
    assert C15.q0_only_one_is_odd(2, 3)
    assert C15.q0_only_one_is_odd(3, 4)
    assert not C15.q0_only_one_is_odd(3, 5)
    assert not C15.q0_only_one_is_odd(6, 6)
    assert C15.q0_only_one_is_odd(6, 5)

@pytest.mark.skip("Not Implemented")
def test_q1_is_substring():
    assert C15.q1_is_substring("interesting", "interest")
    assert C15.q1_is_substring("calculator", "calc")
    assert not C15.q1_is_substring("hot", "not")
    assert not C15.q1_is_substring("Hello", "hello")


@pytest.mark.skip("Not Implemented")
def test_q2_BMM():
    assert C15.q2_BMM(3, 3) == 3
    assert C15.q2_BMM(9, 12) == 3
    assert C15.q2_BMM(25, 40) == 5
    assert C15.q2_BMM(36, 48) == 12


@pytest.mark.skip("Not Implemented")
def test_q3_KMM():
    assert C15.q3_KMM(3, 3) == 3
    assert C15.q3_KMM(9, 12) == 36
    assert C15.q3_KMM(25, 40) == 200
    assert C15.q3_KMM(36, 48) == 144

@pytest.mark.skip("Not Implemented")
def test_q4_remove_vowel_chr():
    assert C15.q4_remove_vowel_chr("close") == "cls"
    assert C15.q4_remove_vowel_chr("open") == "pn"
    assert C15.q4_remove_vowel_chr("codes") == "cds"
    assert C15.q4_remove_vowel_chr("aioue") == ""


@pytest.mark.skip("Not Implemented")
def test_q5_is_sum_of_squares():
    assert C15.q5_is_sum_of_squares(25)
    assert not C15.q5_is_sum_of_squares(12)

@pytest.mark.skip("Not Implemented")
def test_q6_nth_prime_number():
    assert C15.q6_nth_prime_number(2) == 3
    assert C15.q6_nth_prime_number(4) == 7
    assert C15.q6_nth_prime_number(5) == 11
    assert C15.q6_nth_prime_number(8) == 19


@pytest.mark.skip("Not Implemented")
def test_q7_interpolate_strings():
    strings = ["12", "ab"] 
    assert C15.q7_interpolate_strings(strings) == "1a2b"
    strings = ["123", "123", "123"] 
    assert C15.q7_interpolate_strings(strings) == "111222333"
    strings = ["abc", "def", "ghi"] 
    assert C15.q7_interpolate_strings(strings) == "adgbehcfi"    
    strings = ["ive", "ler", "oh."] 
    assert C15.q7_interpolate_strings(strings) == "iloveher."        
    strings = ["tsst", "hsyi", "ioit", "ses", "ian"] 
    assert C15.q7_interpolate_strings(strings) == "thisissoeasyisntit"



@pytest.mark.skip("Not Implemented")
def test_q8_Caesar_encoder():
    assert C15.q8_Caesar_encoder("close") == "forvh"
    assert C15.q8_Caesar_encoder("open") == "rshq"
    assert C15.q8_Caesar_encoder("codes") == "frghv"
    assert C15.q8_Caesar_encoder("python") == "sbwkrq"
