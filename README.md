# Geco Habit Tracker

> Note: On first launch, if your terminal blocks standard input, the app will automatically assign "Guest" as the username to prevent crashing.

**Geco Habit Tracker** is a terminal-based Python application designed to help you build and maintain daily habits. \
The system is built around the idea of "not breaking the chain", a method of daily consistency tracking.

---

### Features

- Add daily habits with a desired number of days (up to 100)
- Mark each day as:
  - `[+]` Completed
  - `[-]` Missed
  - `[ ]` Not yet marked
- Automatically formats long habit chains into multiple lines (20 squares per line)
- See all current habits and their daily tracking status
- See a list of fully completed habits
- Detect broken habits and list them separately
- Delete any habit
- Change your saved username
- Local data persistence with `habits.json`


---

### Technologies Used

- Python 3.8+
- JSON for data storage
- `sys.stdout.write` and `time.sleep` for animation effects

---

### Requirements

- Python 3.8 or higher
- No external libraries required
- Uses only Python standard libraries:
  - `json`
  - `os`
  - `sys`
  - `time`

---

### How to Use

1. Download this repository
2. Run the Python file:
   ```bash
   python3 geco_habit_tracker.py
   ```
3. Follow the interactive terminal prompts to manage your habits.
4. Your progress will be saved automatically in local files.

---

### File Structure

```
├── geco_habit_tracker.py   # Main application
├── habits.json             # Data file (auto-created)
├── user_name.txt           # Stores your username
├── README.md               # Project description
```
---
### Contacts

If you have any questions, you can find me here:

- GitHub: [@irmakbkd](https://github.com/irmakbkd)
- Email: *bekdemirirmak@gmail.com*

---

### Credits

Project developed by **Irmak Bekdemir** as part of the "Python for Data Analysis" course.

Instructor: **Dr. Mustafa Murat ARAT**\
Final Project — Summer 2025

---

> Built with 🩵 and Python by Irmak.
