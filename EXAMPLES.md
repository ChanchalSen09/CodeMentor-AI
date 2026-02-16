# Example Usage of CodeMentor AI

## Example 1: Understanding a Problem

**User Input:**
```
Option: 1 (Understand a problem)
Problem: Find the longest substring without repeating characters
```

**CodeMentor Response:**
```
🧠 Let's break down this problem:

1. Key Concepts to Consider:
   - What data structures might be relevant here?
   - What are the input/output requirements?
   - What are the constraints (time/space complexity)?

2. Questions to Ask Yourself:
   - What patterns do you recognize in this problem?
   - Have you solved similar problems before?
   - What would a brute force solution look like?

3. Understanding Check:
   - Can you explain the problem in your own words?
   - What are some example inputs and expected outputs?

💡 Think about these questions and let me know what you're thinking!
```

---

## Example 2: Building an Approach

**User Input:**
```
Option: 2 (Build an approach)
Problem: Reverse a linked list
User Thoughts: I think I need to change the pointers somehow
```

**CodeMentor Response:**
```
🎯 Let's build an approach together:

Step 1: Start Simple
   - What's the most straightforward way to solve this?
   - Don't worry about optimization yet

Step 2: Identify Data Structures
   - Would an array, hash map, stack, queue, or tree help?
   - How would you organize the data?

Step 3: Outline the Algorithm
   - Break it into smaller steps
   - What happens in each iteration/recursion?
   - What are your base cases and edge cases?

Step 4: Analyze Complexity
   - What's the time complexity of your approach?
   - Can you optimize it?

Step 5: Pseudocode
   - Write pseudocode before actual code
   - This helps clarify your logic

📝 Based on your thoughts, consider:
   - Are there any edge cases you might have missed?
   - Could there be a more efficient approach?

🚀 Try implementing your approach and let me know if you get stuck!
```

---

## Example 3: Debugging Code

**User Input:**
```
Option: 3 (Debug my code)
Code:
def binary_search(arr, target):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid
        else:
            right = mid
    return -1
END

Error: The function sometimes gets stuck in infinite loop
```

**CodeMentor Response:**
```
🔍 Let's debug this together:

Debugging Strategy:
   1. Understand the Error:
      - What is the error message telling you?
      - Which line is causing the issue?

   2. Check Your Logic:
      - Are your loop conditions correct?
      - Are you handling edge cases (empty input, single element)?
      - Are your indices within bounds?

   3. Trace Through an Example:
      - Pick a simple test case
      - Walk through your code line by line
      - What values do variables have at each step?

   4. Common Issues to Check:
      - Off-by-one errors (check your loop boundaries)
      - Null/None pointer issues
      - Integer overflow
      - Incorrect comparisons (< vs <=)

   5. Use Print Statements:
      - Add debug prints to see variable values
      - This helps identify where things go wrong

💡 For the error you described: 'The function sometimes gets stuck in infinite loop'
   - Try adding print statements around that area
   - Check if your assumptions about the data are correct

🎯 Try these debugging steps and see what you discover!
```

---

## Example 4: Getting a Hint

**User Input:**
```
Option: 4 (Get a hint)
Problem: Find if there are two numbers in array that sum to target
Approach: I'm thinking of checking every pair
```

**CodeMentor Response:**
```
💡 Here's a hint to guide you:

Think about:
   - What information do you need to keep track of?
   - Is there a pattern in how the input changes?
   - Could you solve a smaller version of this problem first?

Common DSA Patterns:
   - Two pointers technique
   - Sliding window
   - Hash map for O(1) lookups
   - Recursion with memoization
   - Binary search for sorted data
   - DFS/BFS for graphs and trees

🤔 Which pattern might apply to your problem?
```

---

## Example 5: Explaining a Concept

**User Input:**
```
Option: 5 (Explain a concept)
Concept: sliding window
```

**CodeMentor Response:**
```
📚 Sliding Window

Sliding Window maintains a subset of data that 'slides' through the array

Key Points:
   • Useful for contiguous subarrays/substrings
   • Window can be fixed or variable size
   • Avoids redundant calculations
   • Often achieves O(n) time complexity

When to Use:
   When finding max/min subarray, substring problems

💭 Does this help clarify the concept? Feel free to ask for examples!
```

---

## Example 6: When User Asks for Complete Solution

**User Input:**
```
Can you just give me the code for two sum problem?
```

**CodeMentor Response (using prevent_solution_request):**
```
🎓 I'm here to help you learn, not just provide answers!

Instead of giving you the complete solution, let me help you:
   1. Understand the problem better
   2. Build your own approach
   3. Debug any issues you encounter

Learning to solve problems yourself is much more valuable than
copying solutions. You've got this! 💪

What specific part would you like help with?
```

---

## Tips for Best Results

1. **Be Specific**: Provide clear problem descriptions
2. **Share Your Thinking**: Let the assistant know what you've tried
3. **Ask Follow-ups**: Don't hesitate to ask for clarification
4. **Practice Active Learning**: Try implementing suggestions before asking for more help
5. **Iterate**: If stuck, try the debugging or hint features

## Learning Path Suggestion

1. Start with **"Explain a concept"** to understand fundamentals
2. Use **"Understand a problem"** when starting a new problem
3. Move to **"Build an approach"** to plan your solution
4. Implement your solution
5. Use **"Debug my code"** if you encounter issues
6. Use **"Get a hint"** if completely stuck

Remember: The goal is to learn, not to get quick answers! 🚀
