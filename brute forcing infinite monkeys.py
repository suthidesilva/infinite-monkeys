import string, time

start_time, valid_characters, target_string = time.time(), string.ascii_lowercase + ' ', "methinks it is like a weasel"

def char_check(target=target_string.lower()):
    return ''.join([letter for letter in target for ch in valid_characters if ch == letter])

def infinite_monkeys():
    return print(f'SUCCESS! target string ({char_check()}) has been FOUND, it took {(time.time() - start_time):.0f} seconds, {((time.time() - start_time)*1000) % 60:.0f} milliseconds, {((time.time() - start_time)*1000000) % 360:.0f} microseconds, {((time.time() - start_time)*1000000000) % 21600:.0f} nanoseconds')

infinite_monkeys()