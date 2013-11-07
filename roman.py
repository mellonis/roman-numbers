class Roman(object):
    value = 0

    def __init__(self, value):
        try:
            self.value = int(value)
        except:
            value = str(value).upper().replace(' ', '')
            self.value = value

