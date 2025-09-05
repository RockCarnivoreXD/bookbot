# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

# BookBot

A simple CLI tool that analyzes a text file (like a book) and prints useful stats: total word count and a frequency report of each letter.

## Overview
BookBot reads a `.txt` file, normalizes its text, and outputs:
- Total word count
- Letter frequency (a–z), sorted by most common

## How It Works
- Input: Path to a `.txt` file.
- Processing:
  - Read the file as text.
  - Split on whitespace to count words.
  - Convert characters to lowercase and tally occurrences of `a`–`z`.
- Output:
  - Prints a summary with the word count.
  - Prints a letter frequency report, highest frequency first.
- Key files:
  - `main.py`: CLI entry point; orchestrates reading, counting, and printing.
  - `books/`: Example input files (e.g., `frankenstein.txt`).

## Requirements
- Python 3.10+ (recommended)
- No external dependencies

## Installation
```bash
git clone https://github.com/RockCarnivoreXD/bookbot.git
cd bookbot