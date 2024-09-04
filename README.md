# infinite-monkeys
This project simulates the "infinite monkey theorem" using Python. The theorem suggests that a monkey hitting keys at random on a typewriter for an infinite amount of time could almost surely type a given text, such as a sentence from Shakespeare. In this project, we replace the monkey with a Python function to see how long it would take to generate a specific sentence: "methinks it is like a weasel."

## Project Overview

The code in this repository includes various approaches to simulate this process:

1. **Random String Generation:** 
   - A function that generates a random string of 28 characters, chosen from the 26 letters of the alphabet plus a space.
   
2. **String Scoring:** 
   - A function that scores each randomly generated string by comparing it to the target sentence.
   
3. **Basic Infinite Monkeys Simulation:**
   - A function that repeatedly generates and scores strings, printing the best result every 100,000 tries, until the correct sentence is generated.

4. **Learning Infinite Monkeys:**
   - An enhanced version of the basic simulation where the "monkey" remembers correctly guessed characters and only randomizes the rest. This significantly reduces the time needed to find the correct sentence.

5. **Brute-Force Infinite Monkeys:**
   - A function that systematically brute-forces the string by checking every possible character until the target string is found.

## Functions

- **`get_sentence(character_pool, sentence_length)`**:
  Generates a random sentence from a given character pool.

- **`first_monkeys()`**:
  Calls `get_sentence` to generate a random sentence of length 28.

- **`score(st, target='methinks it is like a weasel')`**:
  Scores the generated string by comparing it to the target string.

- **`infinite_monkeys()`**:
  Runs the basic simulation, attempting to generate the target string by random chance.

- **`put_back(string, target='methinks it is like a weasel')`**:
  Generates a new string by keeping correctly guessed characters and randomizing the rest.

- **`learning_infinite_monkeys()`**:
  Runs the improved simulation where the monkey "learns" from previous attempts.

- **`char_check(target='methinks it is like a weasel')`**:
  Brute-forces the string by checking each character against the target.

- **`brute_force_infinite_monkeys()`**:
  Runs the brute-force simulation to find the target string.

## How to Run

1. Clone this repository to your local machine.
2. Open the notebook or Python script in your favorite Python IDE.
3. Run the cells in sequence, starting from the top.
4. Uncomment the relevant function calls to test each simulation method.

**Note:** The `infinite_monkeys()` function may take a significant amount of time to run, as it relies purely on random chance.

## Conclusion

This project illustrates different methods for solving a problem akin to the infinite monkey theorem, from pure randomness to more sophisticated approaches like learning and brute force. Each method demonstrates different computational strategies and their efficiency.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
