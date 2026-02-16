#!/usr/bin/env python3
"""
CodeMentor AI - DSA Learning Assistant

An AI-powered assistant that helps users understand DSA problems,
build approaches, and debug - without providing full copy-paste solutions.
"""

import sys
import json
from typing import Dict, List, Optional


class CodeMentorAI:
    """
    Main class for the DSA Learning Assistant.
    
    This assistant helps users:
    - Understand DSA problems and concepts
    - Build approaches step-by-step
    - Debug their code
    
    It never provides complete copy-paste solutions.
    """
    
    def __init__(self):
        self.session_context = []
        self.guidance_mode = "understanding"  # understanding, approach, debugging
    
    def understand_problem(self, problem_description: str) -> str:
        """
        Help users understand a DSA problem by breaking it down.
        
        Args:
            problem_description: The problem statement or question
            
        Returns:
            Guidance to help understand the problem
        """
        response = []
        response.append("🧠 Let's break down this problem:\n")
        response.append("1. **Key Concepts to Consider:**")
        response.append("   - What data structures might be relevant here?")
        response.append("   - What are the input/output requirements?")
        response.append("   - What are the constraints (time/space complexity)?")
        response.append("\n2. **Questions to Ask Yourself:**")
        response.append("   - What patterns do you recognize in this problem?")
        response.append("   - Have you solved similar problems before?")
        response.append("   - What would a brute force solution look like?")
        response.append("\n3. **Understanding Check:**")
        response.append("   - Can you explain the problem in your own words?")
        response.append("   - What are some example inputs and expected outputs?")
        response.append("\n💡 Think about these questions and let me know what you're thinking!")
        
        return "\n".join(response)
    
    def build_approach(self, problem_description: str, user_thoughts: Optional[str] = None) -> str:
        """
        Guide users to build their own approach to solving the problem.
        
        Args:
            problem_description: The problem statement
            user_thoughts: User's current thinking (optional)
            
        Returns:
            Guidance to help build an approach
        """
        response = []
        response.append("🎯 Let's build an approach together:\n")
        response.append("**Step 1: Start Simple**")
        response.append("   - What's the most straightforward way to solve this?")
        response.append("   - Don't worry about optimization yet")
        response.append("\n**Step 2: Identify Data Structures**")
        response.append("   - Would an array, hash map, stack, queue, or tree help?")
        response.append("   - How would you organize the data?")
        response.append("\n**Step 3: Outline the Algorithm**")
        response.append("   - Break it into smaller steps")
        response.append("   - What happens in each iteration/recursion?")
        response.append("   - What are your base cases and edge cases?")
        response.append("\n**Step 4: Analyze Complexity**")
        response.append("   - What's the time complexity of your approach?")
        response.append("   - Can you optimize it?")
        response.append("\n**Step 5: Pseudocode**")
        response.append("   - Write pseudocode before actual code")
        response.append("   - This helps clarify your logic")
        
        if user_thoughts:
            response.append("\n\n📝 Based on your thoughts, consider:")
            response.append("   - Are there any edge cases you might have missed?")
            response.append("   - Could there be a more efficient approach?")
        
        response.append("\n\n🚀 Try implementing your approach and let me know if you get stuck!")
        
        return "\n".join(response)
    
    def debug_code(self, code: str, error_description: Optional[str] = None) -> str:
        """
        Help users debug their code without giving them the solution.
        
        Args:
            code: The user's code
            error_description: Description of the error or issue
            
        Returns:
            Debugging guidance
        """
        response = []
        response.append("🔍 Let's debug this together:\n")
        response.append("**Debugging Strategy:**")
        response.append("   1. **Understand the Error:**")
        response.append("      - What is the error message telling you?")
        response.append("      - Which line is causing the issue?")
        response.append("\n   2. **Check Your Logic:**")
        response.append("      - Are your loop conditions correct?")
        response.append("      - Are you handling edge cases (empty input, single element)?")
        response.append("      - Are your indices within bounds?")
        response.append("\n   3. **Trace Through an Example:**")
        response.append("      - Pick a simple test case")
        response.append("      - Walk through your code line by line")
        response.append("      - What values do variables have at each step?")
        response.append("\n   4. **Common Issues to Check:**")
        response.append("      - Off-by-one errors (check your loop boundaries)")
        response.append("      - Null/None pointer issues")
        response.append("      - Integer overflow")
        response.append("      - Incorrect comparisons (< vs <=)")
        response.append("\n   5. **Use Print Statements:**")
        response.append("      - Add debug prints to see variable values")
        response.append("      - This helps identify where things go wrong")
        
        if error_description:
            response.append(f"\n\n💡 For the error you described: '{error_description}'")
            response.append("   - Try adding print statements around that area")
            response.append("   - Check if your assumptions about the data are correct")
        
        response.append("\n\n🎯 Try these debugging steps and see what you discover!")
        
        return "\n".join(response)
    
    def get_hint(self, problem_description: str, current_approach: Optional[str] = None) -> str:
        """
        Provide a hint without giving away the solution.
        
        Args:
            problem_description: The problem statement
            current_approach: User's current approach (optional)
            
        Returns:
            A helpful hint
        """
        response = []
        response.append("💡 Here's a hint to guide you:\n")
        response.append("**Think about:**")
        response.append("   - What information do you need to keep track of?")
        response.append("   - Is there a pattern in how the input changes?")
        response.append("   - Could you solve a smaller version of this problem first?")
        response.append("\n**Common DSA Patterns:**")
        response.append("   - Two pointers technique")
        response.append("   - Sliding window")
        response.append("   - Hash map for O(1) lookups")
        response.append("   - Recursion with memoization")
        response.append("   - Binary search for sorted data")
        response.append("   - DFS/BFS for graphs and trees")
        response.append("\n🤔 Which pattern might apply to your problem?")
        
        return "\n".join(response)
    
    def explain_concept(self, concept: str) -> str:
        """
        Explain a DSA concept to help users learn.
        
        Args:
            concept: The concept to explain (e.g., "binary search", "hash map")
            
        Returns:
            An explanation of the concept
        """
        # Common DSA concepts
        concepts = {
            "binary search": {
                "desc": "Binary Search is a search algorithm for sorted arrays",
                "key_points": [
                    "Only works on sorted data",
                    "Divides search space in half each iteration",
                    "Time complexity: O(log n)",
                    "Uses two pointers: left and right"
                ],
                "when_to_use": "When searching in a sorted array or when you need to find a boundary"
            },
            "two pointers": {
                "desc": "Two Pointers is a technique using two iterators to traverse data",
                "key_points": [
                    "Often used in arrays or linked lists",
                    "Pointers can move towards each other or in the same direction",
                    "Common in palindrome checks, pair finding, etc.",
                    "Usually reduces time complexity"
                ],
                "when_to_use": "When you need to find pairs, reverse arrays, or check palindromes"
            },
            "sliding window": {
                "desc": "Sliding Window maintains a subset of data that 'slides' through the array",
                "key_points": [
                    "Useful for contiguous subarrays/substrings",
                    "Window can be fixed or variable size",
                    "Avoids redundant calculations",
                    "Often achieves O(n) time complexity"
                ],
                "when_to_use": "When finding max/min subarray, substring problems"
            },
            "hash map": {
                "desc": "Hash Map (dictionary) provides O(1) average lookup, insertion, deletion",
                "key_points": [
                    "Trade space for time efficiency",
                    "Key-value pair storage",
                    "Perfect for counting, caching, quick lookups",
                    "Watch out for collision handling"
                ],
                "when_to_use": "When you need fast lookups or to track frequency/occurrence"
            },
            "dynamic programming": {
                "desc": "Dynamic Programming solves problems by breaking them into overlapping subproblems",
                "key_points": [
                    "Uses memoization (top-down) or tabulation (bottom-up)",
                    "Optimal substructure: solution contains optimal solutions to subproblems",
                    "Overlapping subproblems: same subproblems solved multiple times",
                    "Trade space for time efficiency"
                ],
                "when_to_use": "Optimization problems, counting problems, or when you see repeated calculations"
            }
        }
        
        concept_lower = concept.lower().strip()
        
        if concept_lower in concepts:
            info = concepts[concept_lower]
            response = []
            response.append(f"📚 **{concept.title()}**\n")
            response.append(f"{info['desc']}\n")
            response.append("**Key Points:**")
            for point in info['key_points']:
                response.append(f"   • {point}")
            response.append(f"\n**When to Use:**")
            response.append(f"   {info['when_to_use']}")
            response.append("\n\n💭 Does this help clarify the concept? Feel free to ask for examples!")
            return "\n".join(response)
        else:
            return (
                f"📚 Let me help you understand '{concept}':\n\n"
                "To give you the best explanation, could you clarify:\n"
                "   - Is this about a specific algorithm or data structure?\n"
                "   - What aspect of it are you struggling with?\n"
                "   - Have you seen any examples of it being used?\n\n"
                "Common concepts I can explain:\n"
                "   • Binary Search\n"
                "   • Two Pointers\n"
                "   • Sliding Window\n"
                "   • Hash Map\n"
                "   • Dynamic Programming\n"
                "   • And many more!"
            )
    
    def prevent_solution_request(self) -> str:
        """
        Politely decline when users ask for complete solutions.
        
        Returns:
            Message explaining the learning-focused approach
        """
        return (
            "🎓 I'm here to help you learn, not just provide answers!\n\n"
            "Instead of giving you the complete solution, let me help you:\n"
            "   1. **Understand** the problem better\n"
            "   2. **Build** your own approach\n"
            "   3. **Debug** any issues you encounter\n\n"
            "Learning to solve problems yourself is much more valuable than\n"
            "copying solutions. You've got this! 💪\n\n"
            "What specific part would you like help with?"
        )


def print_welcome():
    """Print welcome message."""
    print("=" * 60)
    print("  🎓 CodeMentor AI - Your DSA Learning Assistant")
    print("=" * 60)
    print("\nI'm here to help you learn Data Structures & Algorithms!")
    print("\nWhat I can do:")
    print("  • Help you understand problems")
    print("  • Guide you to build your own approach")
    print("  • Debug your code with you")
    print("\nWhat I won't do:")
    print("  • Give you copy-paste solutions")
    print("  • Do your homework for you")
    print("\nLet's learn together! 🚀\n")
    print("=" * 60)


def print_menu():
    """Print the menu options."""
    print("\n📋 What would you like help with?")
    print("  1. Understand a problem")
    print("  2. Build an approach")
    print("  3. Debug my code")
    print("  4. Get a hint")
    print("  5. Explain a concept")
    print("  6. Exit")
    print()


def main():
    """Main entry point for the CLI application."""
    mentor = CodeMentorAI()
    print_welcome()
    
    while True:
        print_menu()
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == "1":
            print("\n" + "=" * 60)
            print("📖 UNDERSTAND A PROBLEM")
            print("=" * 60)
            problem = input("\nDescribe your problem:\n> ").strip()
            if problem:
                print("\n" + mentor.understand_problem(problem))
            else:
                print("Please provide a problem description!")
        
        elif choice == "2":
            print("\n" + "=" * 60)
            print("🎯 BUILD AN APPROACH")
            print("=" * 60)
            problem = input("\nDescribe your problem:\n> ").strip()
            thoughts = input("\nWhat are you thinking so far? (optional, press Enter to skip):\n> ").strip()
            if problem:
                print("\n" + mentor.build_approach(problem, thoughts if thoughts else None))
            else:
                print("Please provide a problem description!")
        
        elif choice == "3":
            print("\n" + "=" * 60)
            print("🔍 DEBUG YOUR CODE")
            print("=" * 60)
            print("\nPaste your code (type 'END' on a new line when done):")
            code_lines = []
            while True:
                line = input()
                if line.strip() == "END":
                    break
                code_lines.append(line)
            code = "\n".join(code_lines)
            
            error = input("\nDescribe the issue you're facing (optional):\n> ").strip()
            if code:
                print("\n" + mentor.debug_code(code, error if error else None))
            else:
                print("Please provide some code to debug!")
        
        elif choice == "4":
            print("\n" + "=" * 60)
            print("💡 GET A HINT")
            print("=" * 60)
            problem = input("\nDescribe your problem:\n> ").strip()
            approach = input("\nWhat have you tried so far? (optional):\n> ").strip()
            if problem:
                print("\n" + mentor.get_hint(problem, approach if approach else None))
            else:
                print("Please provide a problem description!")
        
        elif choice == "5":
            print("\n" + "=" * 60)
            print("📚 EXPLAIN A CONCEPT")
            print("=" * 60)
            concept = input("\nWhat concept would you like to understand?\n> ").strip()
            if concept:
                print("\n" + mentor.explain_concept(concept))
            else:
                print("Please provide a concept name!")
        
        elif choice == "6":
            print("\n" + "=" * 60)
            print("👋 Thanks for using CodeMentor AI!")
            print("Keep learning and happy coding! 🚀")
            print("=" * 60 + "\n")
            break
        
        else:
            print("\n❌ Invalid option. Please choose 1-6.")
        
        input("\n[Press Enter to continue...]")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye! Keep learning!")
        sys.exit(0)
