class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self._status = False
        self._muted = False
        self._volume = int(self.MIN_VOLUME)
        self._channel = int(self.MIN_CHANNEL)

    def power(self):
        if not self._status:
            self._status = True
        else:
            self._status = False
        return self._status

    def mute(self):
        if self._status:
            self._muted = not self._muted
            if self._muted:
                return self._muted
            else:
                return self._muted

    def channel_up(self):
        if self._status:
            if self._channel < self.MAX_CHANNEL:
                self._channel += 1
                return self._channel
            elif self._channel == self.MAX_CHANNEL:
                self._channel = self.MIN_CHANNEL
                return self._channel
        else:
            return self._channel

    def channel_down(self):
        if self._status:
            if self._channel > self.MIN_CHANNEL:
                self._channel -= 1
                return self._channel
            elif self._channel == self.MIN_CHANNEL:
                self._channel = self.MAX_CHANNEL
                return self._channel
        else:
            return self._channel

    def volume_up(self):
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

    def volume_down(self):
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

    def __str__(self):
        if self._muted:
            return f'Power = [{self._status}], Channel = [{self._channel}], Volume = [{self.MIN_VOLUME}]'
        else:
            return f'Power = [{self._status}], Channel = [{self._channel}], Volume = [{self._volume}]'