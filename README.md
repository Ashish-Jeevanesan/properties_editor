# 📝 Property File Editor

A simple yet powerful desktop application for bulk editing property files. Built with Python and `tkinter`, this tool provides a user-friendly graphical interface to modify properties across multiple files simultaneously.

## ✨ Features

*   **🖼️ Graphical User Interface:** An intuitive and easy-to-use interface for all your property editing needs.
*   **📂 Bulk Editing:** Modify a specific property in numerous files within a directory at once.
*   **🔍 Pattern-Based File Selection:** Use glob patterns (e.g., `Company_*.properties`, `**/*.txt`) to precisely select the files you want to process.
*   **⚙️ Conditional Updates:** The application is smart! It only modifies files if the property's current value is different from the new one you provide.
*   **🤔 Flexible Handling of Missing Properties:** You decide what to do when a property doesn't exist in a file:
    *   **Ask:** Prompt for a decision for each file.
    *   **Add:** Automatically add the property and its value.
    *   **Skip:** Simply ignore the files where the property is missing.
*   **📜 Real-time Logging:** A dedicated output window shows you the progress and results of the file processing in real-time.
*   **💻 Cross-Platform:** Runs on Windows, macOS, and Linux without any modifications.

## 🚀 Getting Started

### Prerequisites

*   Python 3.x

### Installation & Usage

No installation is required!

1.  Download or clone the `property_editor_gui.py` file.
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you saved the file.
4.  Run the application with the following command:

    ```bash
    python property_editor_gui.py
    ```

## 📖 How to Use

1.  **Launch the application.**
2.  **Select a Folder:** Click the **Browse...** button to choose the directory containing your property files.
3.  **Specify File Pattern:** Enter a pattern to match your files (e.g., `*.properties`, `config.txt`, `settings-?.ini`).
4.  **Enter Property Details:**
    *   **Property Name:** The name of the property you want to change (e.g., `database.url`).
    *   **New Property Value:** The new value you want to set.
5.  **Choose an Action:** Select how to handle files where the property is missing.
6.  **Process:** Click the **Process Files** button to start the editing process.
7.  **Review Output:** The output log will display a summary of all actions taken.

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📄 License

This project is not licensed. For open-source projects, it's recommended to add a license. The [MIT License](https://opensource.org/licenses/MIT) is a popular and permissive choice.