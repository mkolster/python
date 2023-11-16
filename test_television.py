from television import *


def test_init():
    tv = Television()
    assert tv.__str__() == 'Power = [False], Channel = [0], Volume = [0]'


def test_power():
    tv = Television()
    tv.power()
    assert tv.__str__() == 'Power = [True], Channel = [0], Volume = [0]'
    tv.power()
    assert tv.__str__() == 'Power = [False], Channel = [0], Volume = [0]'


def test_mute():
    tv = Television()
    tv.power()
    assert tv.__str__() == 'Power = [True], Channel = [0], Volume = [0]'
    tv.volume_up()
    tv.mute()
    assert tv.__str__() == 'Power = [True], Channel = [0], Volume = [0]'
    tv.mute()
    assert tv.__str__() == 'Power = [True], Channel = [0], Volume = [1]'
    tv.power()
    tv.mute()
    assert tv.__str__() == 'Power = [False], Channel = [0], Volume = [1]'
    tv.power()
    tv.mute()
    tv.power()
    tv.mute()
    assert tv.__str__() == 'Power = [False], Channel = [0], Volume = [0]'


def test_channel_up():
    tv = Television()
    tv.power()
    tv.channel_up()
    assert tv.__str__() == 'Power = [True], Channel = [1], Volume = [0]'
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert tv.__str__() == 'Power = [True], Channel = [0], Volume = [0]'
    tv.power()
    tv.channel_up()
    assert tv.__str__() == 'Power = [False], Channel = [0], Volume = [0]'


def test_channel_down():
    tv = Television()
    tv.power()
    tv.channel_down()
    assert tv.__str__() == 'Power = [True], Channel = [3], Volume = [0]'
    tv.power()
    tv.channel_down()
    assert tv.__str__() == 'Power = [False], Channel = [3], Volume = [0]'
    tv.power()
    tv.channel_down()
    tv.channel_down()
    assert tv.__str__() == 'Power = [True], Channel = [1], Volume = [0]'
    tv.channel_down()


def test_volume_up():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_up()
    assert tv.__str__() == 'Power = [True], Channel = [0], Volume = [2]'
    tv.volume_up()
    tv.volume_up()
    assert tv.__str__() == 'Power = [True], Channel = [0], Volume = [2]'
    tv.power()
    tv.volume_up()
    tv.volume_up()
    assert tv.__str__() == 'Power = [False], Channel = [0], Volume = [2]'
    tv.power()
    tv.volume_down()
    tv.volume_down()
    tv.mute()
    tv.volume_up()
    assert tv.__str__() == 'Power = [True], Channel = [0], Volume = [1]'


def test_volume_down():
    tv = Television()
    tv.power()
    tv.volume_down()
    tv.volume_down()
    assert tv.__str__() == 'Power = [True], Channel = [0], Volume = [0]'
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert tv.__str__() == 'Power = [True], Channel = [0], Volume = [1]'
    tv.power()
    tv.volume_down()
    assert tv.__str__() == 'Power = [False], Channel = [0], Volume = [1]'
    tv.power()
    tv.volume_down()
    assert tv.__str__() == 'Power = [True], Channel = [0], Volume = [0]'
    tv.volume_up()
    tv.volume_up()
    tv.mute()
    tv.volume_down()
    assert tv.__str__() == 'Power = [True], Channel = [0], Volume = [1]'
