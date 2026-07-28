# Contributing

- Contributions are welcome, and this page covers what to expect.
  - Before you start
    - Open an issue describing the change, so you do not duplicate work someone else has started.
    - Say which Alibre Design version you are working against, because the API moves between releases.
  - Making a change
    - Work on a branch rather than the default branch.
    - Keep source files free of explanatory comments, because that prose belongs in your local developer notes.
    - Keep XML documentation comments and Python docstrings, because tooling reads them.
    - Keep spacing tight, meaning at most one blank line and no trailing whitespace.
    - Put code in `source/`, reference material in `documentation/`, and nothing loose in the repository root.
    - Leave build output, installers, and scratch files out of your commit.
  - Before you open a pull request
    - Build the affected solution and confirm it still succeeds.
    - Check that the README still describes what the project now does.
  - Opening a pull request
    - Describe what changed and why, and link the issue it closes.
    - Expect review comments, because a maintainer reads each change before it merges.
