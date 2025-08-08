# Prompt: Profile and Optimize a Slow Function

A function in my codebase seems slow. I need you to analyze its performance, identify the bottleneck, and suggest optimizations.

Please analyze the function `[FUNCTION_NAME]` located in the file `[FILE_PATH]`.

## Your Analysis should contain:

**1. Profiling Results:**
-   Explain how you would profile this function using a standard Python tool like `cProfile`.
-   Show a summary of the profiling output, highlighting the top 1-3 functions that consume the most time (the bottlenecks).

**2. Diagnosis of the Bottleneck:**
-   In one or two sentences, explain *why* the identified functions are slow. (e.g., "It's performing a redundant calculation inside a tight loop," or "It's using an inefficient data structure for lookups.")

**3. The Optimization Plan:**
-   Propose a specific, concrete code change to fix the bottleneck.
-   Provide the change as a `diff` block so I can clearly see what to add and remove.
-   Do not suggest adding new, heavy dependencies unless absolutely necessary.

**4. Explanation of the Fix:**
-   Briefly explain why your proposed optimization works and how it improves performance. (e.g., "By caching the result, we avoid re-computing it on every iteration.")

---
## Context to Provide to the AI:

### The Source Code File to Profile

Filename: `<PASTE THE FILENAME OF THE SOURCE CODE FILE HERE>`

<PASTE THE ENTIRE CONTENT OF THE SOURCE CODE FILE HERE> ```
An Example Usage Script
A small script that calls the function in a way that demonstrates the performance issue.

# Example script to run the profiler on
<PASTE A SHORT SCRIPT THAT CALLS THE SLOW FUNCTION HERE>