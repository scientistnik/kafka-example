from karma_data import KarmaData

karma = KarmaData()

def example(msg):
  karma.send(msg.value)

print("Start hearing...")
karma.hearing(example)