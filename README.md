#  SSH Brute Force Log Analyzer

A Python tool for analyzing SSH authentication logs to detect brute force attacks, suspicious activity, and access patterns — built without external libraries.

---

##  Overview

This project simulates and analyzes SSH login attempts stored in CSV format. It identifies malicious IPs, targeted users, attack patterns by hour, and potential successful intrusions after repeated failures.

Built with a clean modular architecture where each file has a single responsibility.

---

##  Architecture

```
ssh_logs.csv
     ↓
loader.py       → reads the file line by line (generator, memory efficient)
     ↓
cleaner.py      → validates and converts each line into a dictionary
     ↓
analyzer.py     → extracts security intelligence
     ↓
visualizer.py   → displays results in the console
exporter.py     → saves results to report.csv

main.py         → orchestrates the full pipeline
data_generator.py → generates realistic synthetic log data for testing
```

---

##  What It Analyzes

| Analysis | Description |
|---|---|
| Failed IPs | IPs with the most failed login attempts → ban candidates |
| Attacked Users | Most targeted usernames (root, admin, oracle...) |
| Success rate by country | Login success percentage per country |
| Suspicious IPs | IPs with SUCCESS after many FAILs → possible intrusion |
| Attacks by hour | Failed attempts distribution across 24 hours |

---

##  Project Structure

```
analyzer_ssh_bruteforce_logs/
├── main.py              # Entry point
├── loader.py            # CSV reader (generator)
├── cleaner.py           # Data validator and parser
├── analyzer.py          # Security analysis functions
├── visualizer.py        # Console output
├── exporter.py          # CSV report exporter
├── data_generator.py    # Synthetic log generator
├── ssh_logs.csv         # Generated log data (not tracked)
├── report.csv           # Analysis output (not tracked)
└── .gitignore
```

---

##  Usage

**1. Generate synthetic logs:**
```bash
python data_generator.py
```

**2. Run the analyzer:**
```bash
python main.py
```

Results are displayed in the console and saved to `report.csv`.

---

##  Key Concepts Applied

- **Generator functions** — `load_logs()` yields one line at a time for memory efficiency
- **Defensive programming** — `cleaner_logs()` validates every field before processing
- **Dictionary-based counting** — all analysis built without pandas or external libs
- **Separation of concerns** — each module has one job
- **Walrus operator** — used in main pipeline to filter and assign in a single expression

---

##  Requirements

- Python 3.8+
- No external libraries required

---

##  Sample Output

```
== IPs with more failed attempts ==
 185.220.101.42       1305 attempts
 192.168.2.20         1281 attempts

== Users with more failed attempts ==
 oracle               1293 attempts
 admin                1279 attempts

== Suspicious IPs (SUCCESS after many FAILs) ==
  185.220.101.42      fails: 1305   success: 400

== Failed attempts by hour ==
 15:00,    357 attempts  ████████████████████
 18:00,    345 attempts  ███████████████████
```

---

##  Author

Flores Falcon Natanael Emanuel

Built as a cybersecurity + Python learning project.