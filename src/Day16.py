import input_util

hex_to_bin_translation_table = {
  '0':  '0000',
  '1':  '0001',
  '2':  '0010',
  '3':  '0011',
  '4':  '0100',
  '5':  '0101',
  '6':  '0110',
  '7':  '0111',
  '8':  '1000',
  '9':  '1001',
  'A':  '1010',
  'B':  '1011',
  'C':  '1100',
  'D':  '1101',
  'E':  '1110',
  'F':  '1111'
}

def hex_to_binary(hex_string):
  return "".join(map(lambda c: hex_to_bin_translation_table[c], hex_string.strip()))

def binary_to_decimal(binary_string):
  return int(binary_string, 2)

input = input_util.read_input_string("../input/day_16_input", hex_to_binary)
sample = input_util.read_input_string("../input/day_16_sample", hex_to_binary)

def parse_packet(binary_string):
  version = binary_to_decimal(binary_string[0:3])
  type = binary_to_decimal(binary_string[3:6])

  if type == 4:
    output = ""
    for i in range(6, len(binary_string), 5):
      output += binary_string[i+1:i+5]
      if binary_string[i] == '0':
        break

    return [version, type, i + 5, binary_to_decimal(output)]

  else:
    length_type_id = binary_string[6]
    version_sum = version

    if length_type_id == '0':
      expected_length = binary_to_decimal(binary_string[7:22])
      bits_read = 22
      sub_packets = []

      while bits_read - 22 < expected_length:
        sub_packet = parse_packet(binary_string[bits_read:expected_length+22])
        bits_read += sub_packet[2]
        version_sum += sub_packet[0]
        sub_packets.append(sub_packet)

    else:
      sub_packet_count = binary_to_decimal(binary_string[7:18])
      bits_read = 18
      sub_packets = []

      for i in range(0, sub_packet_count):
        sub_packet = parse_packet(binary_string[bits_read:])
        bits_read += sub_packet[2]
        version_sum += sub_packet[0]
        sub_packets.append(sub_packet)

    return [version_sum, type, bits_read, sub_packets]

def product(xs):
  p = 1
  for x in xs:
    p *= x
  return p

def evaluate(packet):
  payload = packet[3]
  if packet[1] == 0:
    return sum(map(lambda sub_packet: evaluate(sub_packet), payload))
  elif packet[1] == 1:
    return product(map(lambda sub_packet: evaluate(sub_packet), payload))
  elif packet[1] == 2:
    return min(map(lambda sub_packet: evaluate(sub_packet), payload))
  elif packet[1] == 3:
    return max(map(lambda sub_packet: evaluate(sub_packet), payload))
  elif packet[1] == 4:
    return payload
  elif packet[1] == 5:
    return 1 if evaluate(payload[0]) > evaluate(payload[1]) else 0
  elif packet[1] == 6:
    return 1 if evaluate(payload[0]) < evaluate(payload[1]) else 0
  elif packet[1] == 7:
    return 1 if evaluate(payload[0]) == evaluate(payload[1]) else 0

decoded_packet = parse_packet(input)
print(f'part 1: {decoded_packet[0]}')
print(f'part 2: {evaluate(decoded_packet)}')
