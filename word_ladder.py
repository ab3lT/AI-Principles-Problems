from collections import deque

def word_ladder(beginWord, endWord, wordList):
    """
    Find the shortest transformation sequence from beginWord to endWord.

    Parameters:
    beginWord (str): The starting word.
    endWord (str): The target word.
    wordList (list): A list of valid words for transformation.

    Returns:
    int: The length of the shortest transformation sequence, or 0 if no such sequence exists.

    Example:
    >>> word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
    5
    """
    word_set = set(wordList)
    if endWord not in word_set:
        return 0

    # Initialize BFS queue
    queue = deque([(beginWord, 1)])  # (current_word, transformation_steps)

    while queue:
        current_word, steps = queue.popleft()

        if current_word == endWord:
            return steps

        # Generate all possible words with one-letter transformations
        for i in range(len(current_word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                transformed_word = current_word[:i] + c + current_word[i + 1:]

                if transformed_word in word_set:
                    word_set.remove(transformed_word)  # Mark as visited
                    queue.append((transformed_word, steps + 1))

    return 0  # No transformation sequence found

def main():
    """
    Main function to solve the Word Ladder problem with user input.
    """
    # print("Enter the begin word:")
    # beginWord = input().strip()

    # print("Enter the end word:")
    # endWord = input().strip()

    # print("Enter the word list (comma-separated):")
    # wordList = input().strip().split(",")
    
    beginWord = "cot"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    result = word_ladder(beginWord, endWord, wordList)

    if result:
        print(f"The shortest transformation sequence length is: {result}")
    else:
        print("No transformation sequence exists.")

if __name__ == "__main__":
    main()
