import serial


class Powerwalker:

  def connect(self):
    """Connect to PDU device."""
    self.serial = serial.Serial(
      port=self.port,
      baudrate=2400,
      parity=serial.PARITY_NONE,
      stopbits=serial.STOPBITS_ONE,
      bytesize=serial.EIGHTBITS,
      timeout=1
    )


  def send(self, cmd):
    """Send custom command."""
    self.serial.write(bytes(cmd + '\r', 'utf-8'))
    response = self.serial.readline()

    if response[0] != 40:
      raise ValueError('Response malformed')

    return response[1:].decode('utf-8').rstrip()


  def status_code(self, code, keys):
    d = {}
    i = 0

    for status in list(code):
      d[keys[i]] = status
      i += 1

    return d