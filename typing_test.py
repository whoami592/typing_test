import time
import random

def typing_test():
    # Cybersecurity-themed quote for the typing test
    quote = "Ethical hacking is the art of securing systems by thinking like a malicious hacker."
    print("\nWelcome to the Speed Typing Test by Sabaz Ali Khan!")
    print("Type the following quote as fast as you can:\n")
    print(quote)
    print("\nPress Enter when you're ready to start...")
    input()

    # Record start time
    start_time = time.time()

    # Get user input
    user_input = input("Start typing: ")

    # Record end time
    end_time = time.time()

    # Calculate time taken
    time_taken = end_time - start_time
    minutes = time_taken / 60

    # Calculate WPM
    words = quote.split()
    user_words = user_input.split()
    word_count = len(user_words)
    wpm = word_count / minutes if minutes > 0 else 0

    # Calculate accuracy
    correct_chars = sum(1 for c1, c2 in zip(quote, user_input) if c1 == c2)
    total_chars = len(quote)
    accuracy = (correct_chars / total_chars) * 100 if total_chars > 0 else 0

    # Display results
    print("\n--- Typing Test Results ---")
    print(f"Time Taken: {time_taken:.2f} seconds")
    print(f"Words Per Minute (WPM): {wpm:.2f}")
    print(f"Accuracy: {accuracy:.2f}%")
    print("\nKeep practicing to secure your typing skills like an ethical hacker!")

if __name__ == "__main__":
    typing_test()