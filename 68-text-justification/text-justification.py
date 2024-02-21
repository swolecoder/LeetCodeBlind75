
### Commented and Explained Code:

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []  # Resultant list of justified text
        curr = []  # Current line being processed
        width = 0  # Current line width including spaces between words
        i = 0  # Index to iterate through words

        while i < len(words):
            # Check if adding the next word exceeds maxWidth
            if width + len(words[i]) <= maxWidth:
                curr.append(words[i])
                # Add word length + 1 for the space; +1 is for the space after each word
                width += len(words[i]) + 1
                i += 1
            else:
                # Calculate extra spaces needed to justify the current line
                # Subtracting width from maxWidth and adding len(curr) accounts for
                # the extra space added after the last word in the line which isn't needed
                space = maxWidth - width + len(curr)
                added = 0  # Track of how many spaces added
                j = 0  # Index to loop through current line words

                # Distribute extra spaces between words until the line is justified
                while added < space:
                    if j >= len(curr) - 1:
                        j = 0  # Reset to start if we reach the end of the line
                    curr[j] += " "
                    added += 1
                    j += 1

                # Join the current line and add it to the result
                res.append(''.join(curr))
                # Reset for the next line
                curr = []
                width = 0

        # Handle the last line separately; it should be left-justified
        for i in range(len(curr) - 1):
            curr[i] += " "
        # For the last word, add spaces to the end to reach maxWidth
        # `maxWidth - width + 1` calculates the spaces needed after considering
        # the width has an extra space for the last word which isn't actually added
        
        curr[-1] += " " * (maxWidth - width + 1)

        # Append the last line to the result
        res.append(''.join(curr))
        return res
# ```

# ### Explanation for `+1`:

# - **During Word Addition:** When words are added to `curr`, a space is conceptually reserved after each word by adding `+1` to `width`. This is done to simplify space calculations, assuming a space follows every word except the last in a line. When calculating extra spaces needed for justification, this assumption helps in distributing spaces evenly.
  
# - **For the Last Line Padding:** The `+1` in `maxWidth - width + 1` for the last line accounts for the conceptual space after the last word in `width` calculation that isn't actually there. It adjusts the space calculation to ensure the last line is correctly padded to `maxWidth`.

# This approach ensures that all lines except the last are fully justified according to the problem's rules, with the last line being left-justified.