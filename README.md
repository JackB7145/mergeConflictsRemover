# Force Merge Conflict Override Script

This script is used to forcefully override all merge conflicts between two development branches in a Git repository. It preserves only the changes made in the **feature branch** and removes any changes from the **dev branch**.

> **Warning:** This operation is **destructive** to the **dev branch** as it removes its changes. Be sure to back up your work or create a new branch before proceeding.

---

## Purpose

This script automates the process of:

- Resolving merge conflicts by keeping **only** the changes made in the **feature branch**.
- Discarding any changes from the **dev branch** during the merge.

It is intended to be used when you want to force a merge where the **feature branch** fully overrides the **dev branch**.

---

## Prerequisites

Before running the script, ensure that:

- **Git** is installed on your machine.
- The repository is a valid **Git repository**.
- Your main development branches are named `feature-branch` (the feature branch) and `dev-branch` (the development branch).
- You must add the **merge conflict file** provided into the `input.txt` file located in the `./bin/input.txt` directory **before** running the script.

---

