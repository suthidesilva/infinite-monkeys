import string, random, time

start_time, valid_characters, target_string = time.time(), string.ascii_lowercase + ' ', "methinks it is like a weasel"

def get_sentence(character_pool, sentence_length):
    return ''.join([character_pool[random.randrange(len(character_pool))] for _ in range(sentence_length)])

def first_monkeys():
    return get_sentence(valid_characters, len(target_string))

def score(st, target = target_string.lower()): 
    return sum([1 for i in range(len(st)) if st[i] == target[i]]) if len(st) == len(target) else 0

def infinite_monkeys():
    max_score, counter = 0, 0

    while max_score != len(target_string): 
        string = first_monkeys()
        current_score, counter =  score(string), counter + 1

        if current_score > max_score: max_score, best_string = current_score, string
        if counter % 100000 == 0: print(f"Best string so far is {best_string} and it's score is {max_score}, after {counter} attempts.")

    return print(f'SUCCESS! target string ({target_string}) has been FOUND, it took exactly {counter} attempts, {((time.time() - start_time)/ 60):.0f} minutes {((time.time() - start_time)% 60):.0f} seconds.')

infinite_monkeys()