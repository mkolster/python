from television import Television


def television_test():
    tv = Television()
    assert str(tv) == 'Power = [False], Channel = [0], Volume = [0]'
    tv.power()
    assert str(tv) == 'Power = [True], Channel = [0], Volume = [0]'


    #
    # assert not tv._status
    # assert not tv._muted
    # assert tv._volume == 0
    # assert tv._channel == 0

# print(television_test())







