import q2

def test_CheckOdd():
    out1 = q2.CheckOdd(5)
    assert out1==True

    out2 = q2.CheckOdd(6)
    assert out2 == False

    out3 = q2.CheckOdd(4)
    assert out3 == False

    out4 = q2.CheckOdd(19)
    assert out4 == True

