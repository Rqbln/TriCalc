<div align="center">

# 🏊🚴🏃 TriCalc

**Professional Triathlon Time Estimator - Calculate your race times across all official distances**

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.45.1-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Web-lightgrey)](https://streamlit.io/)
[![Status](https://img.shields.io/badge/Status-Active-success)]()

![Preview of TriCalc app](preview.png)

</div>

---

## 📋 Table of Contents

- [About](#-about)
- [Features](#-features)
- [Supported Distances](#-supported-distances)
- [Technologies Used](#-technologies-used)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 About

**TriCalc** is a simple, interactive web application built with Streamlit that helps triathletes estimate their total race time across all official triathlon distances — from Super Sprint to full Ironman.

Whether you're planning your first triathlon or optimizing your performance for an Ironman, TriCalc provides real-time calculations with pace indicators, comparison to average times, and the ability to lock specific disciplines to focus on your strengths.

### Key Highlights

- ⚡ **Real-time calculations** - Instant updates as you adjust your times
- 🎯 **Target time tracking** - Set goals and see how close you are
- 🔒 **Lock disciplines** - Fix your best segments and optimize others
- 📊 **Pace indicators** - Visual feedback for swim, bike, and run paces
- 📐 **Average comparison** - Compare your estimates to distance averages

---

## ✨ Features

### 🏊 Swim Analysis
- ✅ Customizable swim time estimation
- ✅ Pace calculation in min/100m
- ✅ Percentage difference vs. average
- ✅ Lock option to fix swim time

### 🚴 Bike Analysis
- ✅ Adjustable bike time estimation
- ✅ Speed calculation in km/h
- ✅ Performance comparison metrics
- ✅ Lock option to fix bike time

### 🏃 Run Analysis
- ✅ Flexible run time estimation
- ✅ Pace calculation in min/km
- ✅ Real-time performance feedback
- ✅ Lock option to fix run time

### 🎯 Target Time Management
- ✅ Set custom target race time
- ✅ Real-time difference calculation
- ✅ Visual comparison with estimated total

### 📊 Distance Support
- ✅ Super Sprint (XS)
- ✅ Sprint (S)
- ✅ Olympic (M)
- ✅ Half Ironman (L)
- ✅ Full Ironman (XL)

---

## 📏 Supported Distances

| Distance | Swim | Bike | Run | Avg Time |
|----------|------|------|-----|----------|
| **Super Sprint (XS)** | 0.4 km | 10 km | 2.5 km | ~55 min |
| **Sprint (S)** | 0.75 km | 20 km | 5 km | ~90 min |
| **Olympic (M)** | 1.5 km | 40 km | 10 km | ~160 min |
| **Half Ironman (L)** | 1.9 km | 90 km | 21.1 km | ~360 min |
| **Full Ironman (XL)** | 3.8 km | 180 km | 42.2 km | ~750 min |

---

## 🛠️ Technologies Used

| Technology | Version | Usage |
|------------|---------|-------|
| [Python](https://www.python.org/) | 3.8+ | Main programming language |
| [Streamlit](https://streamlit.io/) | 1.45.1 | Web framework and UI |

### Why Streamlit?

- 🚀 **Rapid development** - Build interactive web apps with pure Python
- 📊 **Built-in widgets** - Sliders, metrics, and visualizations out of the box
- 🎨 **Modern UI** - Clean, responsive interface without CSS/HTML
- 🔄 **Real-time updates** - Automatic reactivity to user inputs

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
- **pip** - Python package manager (usually included with Python)

### Verify Installation

```bash
python --version  # Should be 3.8 or higher
pip --version     # Should be installed
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/TriCalc.git
cd TriCalc
```

### 2. Create a Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- `streamlit==1.45.1`

---

## 💻 Usage

### Start the Application

```bash
streamlit run app.py
```

The application will automatically open in your default web browser at `http://localhost:8501`.

### Using TriCalc

1. **Select Distance** - Choose your target triathlon distance from the dropdown
2. **Adjust Times** - Use sliders to set your estimated times for each discipline
3. **Lock Disciplines** - Check the "Lock" boxes to fix times for your strongest segments
4. **Set Target** - Optionally set a target total time to track your progress
5. **View Results** - See your estimated total time, average time, and difference from target

### Example Workflow

```
1. Select "M / Olympic" distance
2. Lock your swim time at 28 minutes (your strength)
3. Adjust bike time to 75 minutes
4. Adjust run time to 48 minutes
5. Set target time to 150 minutes
6. View: Estimated 151 min, 9 min above average, 1 min from target
```

---

## 📁 Project Structure

```
TriCalc/
│
├── 📄 app.py              # Main Streamlit application
├── 📄 requirements.txt    # Python dependencies
├── 📄 LICENSE            # MIT License
├── 📄 README.md          # Project documentation
└── 🖼️ preview.png        # Application preview image
```

### Key Files

| File | Description |
|------|-------------|
| `app.py` | Main application logic with Streamlit interface |
| `requirements.txt` | Python package dependencies |
| `preview.png` | Screenshot of the application interface |

---

## 🧮 How It Works

### Time Calculation

The application calculates total race time as:

```
Total Time = Swim Time + Bike Time + Run Time
```

### Pace Calculations

- **Swim Pace**: `(Swim Time / Swim Distance) × 100` → min/100m
- **Bike Speed**: `Bike Distance / (Bike Time / 60)` → km/h
- **Run Pace**: `Run Time / Run Distance` → min/km

### Percentage Difference

For each discipline and total time:

```
% Difference = ((Average - Your Time) / Average) × 100
```

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'feat: Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Contribution Guidelines

- Follow [Conventional Commits](https://www.conventionalcommits.org/) for commit messages
- Add comments for complex calculations
- Test your changes before submitting
- Update documentation if necessary
- Keep the code simple and readable

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

```
MIT License

Copyright (c) 2025 Robin :)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing web framework
- The triathlon community for inspiration and feedback
- All contributors and users of TriCalc

---

## 📞 Support

If you encounter any issues or have questions:

- 🐛 **Report bugs** - Open an issue on GitHub
- 💡 **Suggest features** - Create a feature request
- 📧 **Contact** - Reach out through GitHub

---

<div align="center">

**Made with ❤️ for the triathlon community**

[⬆ Back to top](#-tricalc)

</div>
