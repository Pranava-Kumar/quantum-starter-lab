# Prompt: Debug a Failing Pytest Test

A test is failing in my project. I need your help to diagnose and fix the bug.

Please answer the following questions based on the context I provide below.

1.  **Diagnosis**: In one or two clear sentences, what is the most likely cause of this error?
2.  **The Fix**: Propose the smallest possible code change to fix the bug. Please provide the fix as a `diff` block.
3.  **Explanation**: Briefly explain *why* your proposed fix works.
4.  **Further Issues**: Are there any other potential issues or edge cases that this error might be pointing to?

---

## Context for the Bug

### 1. The Full Error Log from `pytest`

<PASTE THE FULL ERROR LOG HERE> ```
2. The Failing Test File
Filename: <PASTE THE FILENAME OF THE TEST FILE HERE>

<PASTE THE ENTIRE CONTENT OF THE TEST FILE HERE>
3. The Source Code Being Tested
Filename: <PASTE THE FILENAME OF THE SOURCE CODE FILE HERE>

<PASTE THE ENTIRE CONTENT OF THE SOURCE CODE FILE HERE>

**Quick beginner tip on how to use this:**
When a test fails on GitHub Actions (or locally), you would:
1.  Copy the content of this Markdown file.
2.  Paste it into your AI chat window.
3.  Fill in the `<PASTE ... HERE>` sections with the actual error message and code from your project.
4.  Send the prompt. The AI will then have all the necessary information to give you a high-quality, actionable answer.