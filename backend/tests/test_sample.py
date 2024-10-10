
import backend.main_test as main_test



def test_sqrt():
    """Tests custom square root problem"""

    assert(main_test.custom_sqrt(9)==3)
    assert(main_test.custom_sqrt(16)==4)
    assert(main_test.custom_sqrt(25)==6)
    