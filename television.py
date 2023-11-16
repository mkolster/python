class Television:
    """
    This class holds methods and variables to change the power, volume, and channel of the television.
    """
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:

        """
        This method initializes the status, muted, and volume, and channel variables.
        The volume and channel variables are set to default to minimum channel and volume setting.
        :return: No return statement
        """

        self._status: bool = False
        self._muted: bool = False
        self._volume: int = int(self.MIN_VOLUME)
        self._channel: int = int(self.MIN_CHANNEL)

    def power(self) -> bool:

        """
        This method checks and sets whether the television is on with a boolean value.
        :return: boolean value true if on and false if off
        """

        if not self._status:
            self._status = True
        else:
            self._status = False
        return self._status

    def mute(self) -> bool:

        """
        This method mutes or unmutes the television if television is on.
        When toggled from muted to unmuted, the original volume is retained.
        :return: boolean value true if muted, false if unmuted
        """
        if self._status:
            self._muted = not self._muted
        return self._muted

    def channel_up(self) -> int:
        """
        This method increases the channel by 1 if television is on.
        If channel is increased after hitting maximum, it loops back to minimum channel.
        :return: int value of channel
        """

        if self._status:
            if self._channel < self.MAX_CHANNEL:
                self._channel += 1
                # return self._channel
            elif self._channel == self.MAX_CHANNEL:
                self._channel = self.MIN_CHANNEL
                # return self._channel
            return self._channel
        else:
            return self._channel

    def channel_down(self) -> int:
        """
        This method decreases the channel by 1 if television is on.
        If channel is decreased beyond the minimum channel, it loops to the maximum channel.
        :return: int value of channel
        """
        if self._status:
            if self._channel > self.MIN_CHANNEL:
                self._channel -= 1
            elif self._channel == self.MIN_CHANNEL:
                self._channel = self.MAX_CHANNEL
            return self._channel
        else:
            return self._channel

    def volume_up(self) -> int:
        """
        This method increases the volume by 1 if television is on.
        If television is muted, this method unmutes it.
        Volume cannot be increased beyond maximum volume value.
        :return: int value of volume
        """

        if self._status:
            self._muted = False
            if self._volume < self.MAX_VOLUME:
                self._volume += 1
                return self._volume
            else:
                self._volume = self.MAX_VOLUME
                return self._volume
        else:
            return self._volume

    def volume_down(self) -> int:
        """
        This method decreases the volume by 1 if television is on.
        If television is muted, this method unmutes it.
        Volume cannot be decreased beyond minimum volume value.
        :return: int value of volume
        """
        if self._status:
            self._muted = False
            if self._volume > self.MIN_VOLUME:
                self._volume -= 1
                return self._volume
            else:
                self._volume = self.MIN_VOLUME
                return self._volume
        else:
            return self._volume

    def __str__(self) -> str:
        """
        This method returns the output of the television class.
        :return: preformatted string with values
        """
        if self._muted:
            return f'Power = [{self._status}], Channel = [{self._channel}], Volume = [{self.MIN_VOLUME}]'
        else:
            return f'Power = [{self._status}], Channel = [{self._channel}], Volume = [{self._volume}]'