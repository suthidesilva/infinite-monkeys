import string, random, time

start_time, valid_characters, target_string = time.time(), string.ascii_lowercase + ' ', "methinks it is like a weasel"

def first_monkeys():
    return ''.join([valid_characters[random.randrange(len(valid_characters))] for _ in range (len(target_string))])

def score(st, target = target_string.lower()): 
    return sum([1 for i in range(len(st)) if st[i] == target[i]]) if len(st) == len(target) else 0

def put_back(string, target=target_string.lower()):
    return ''.join([letter if letter == target[index] else valid_characters[random.randrange(len(valid_characters))] for index, letter in enumerate(string)])

def infinite_monkeys():
    string, max_score, counter = first_monkeys(), 0, 0

    while max_score != len(target_string): 
        current_score, counter =  score(string), counter + 1

        if current_score > max_score: max_score = current_score
        print(f"Current string = {string}, score = {max_score}, attempts = {counter}.")
        string = put_back(string)
        
    return print(f'SUCCESS! target string ({target_string}) has been FOUND, it took {counter} attempts, {(time.time() - start_time):.0f} seconds, {((time.time() - start_time)*1000) % 60:.0f} milliseconds, {((time.time() - start_time)*1000000) % 360:.0f} microseconds, {((time.time() - start_time)*1000000000) % 21600:.0f} nanoseconds')

infinite_monkeys()