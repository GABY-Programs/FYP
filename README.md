# Demonstration Tool Features

This tool showcases various functions to demonstrate how threat actors can gather sensitive information from a user's system. Below are the key features of the tool:

### 1. Keystroke Logging
- **Function Duration:** 30 seconds (Exits if 'Esc' is pressed)
- **Description:** Logs all keystrokes during the session. After pressing the Keystroke Logging button, open Chrome and type as if unaware of the keylogger. After the function ends, you can view sensitive information (emails, passwords, etc.) that a threat actor might have stolen and sent to a remote Command & Control (C&C) server.

### 2. Screen Capture
- **Function Duration:** 30 seconds (Captures a screenshot every 5 seconds)
- **Description:** Takes periodic screenshots. Start opening files or applications after pressing the Screen Capture button. After the session ends, you can view these screenshots, which could reveal sensitive information that could be sent to a C&C server for malicious use.

### 3. Clipboard Logging
- **Function Duration:** 30 seconds
- **Description:** Logs clipboard history. After pressing the Clipboard Logging button, start copying information like emails, passwords, and crypto keys. After the function ends, you'll see a log of your clipboard history in a `.txt` file, illustrating how easily a threat actor could steal sensitive data.

### 4. Keystroke Logging and Screen Capture
- **Function Duration:** 30 seconds
- **Description:** Combines the functionality of keystroke logging and screen capture, running both simultaneously. See features 1 and 2 above for detailed explanations.

### 5. Stealth Mode (Anti-Emulation)
- **Description:** This feature, common in keyloggers and malware, halts the tool when a user opens surveillance applications like Task Manager or Process Hacker. During the session, you'll receive emulated malware activity notifications. To stop the function, open Task Manager to simulate how malware goes dormant.

### 6. System Specs Logging
- **Description:** Logs system information like CPU, GPU, memory, etc. This is often used by malware to assess if a machine is powerful enough for resource-intensive activities, like crypto mining. The system specs are saved in a `.txt` file for review.

### 7. Logging Running Applications
- **Description:** Logs all active applications on your system and saves the information in a `.txt` file. This allows a threat actor to view your running apps and infer the kind of software you commonly use.

### 8. Delete Folder and Files
- **Description:** Deletes all files created by the application, including screenshots and logs, to prevent cluttering your system with unnecessary files after using the tool.

### 9. Open File Location
- **Description:** Opens the folder where all screenshots and log files are saved, making it easier to access the output of each function.

### 10. Quiz
- **Description:** The quiz button launches a quiz with 12 multiple-choice questions. Full-screen the application and complete the quiz. After submitting, press "Return" to go back to the main menu.

### 11. Exit
- **Description:** Closes the application completely.

---

**Disclaimer:** This tool is for educational purposes only. It aims to demonstrate how sensitive data can be compromised by malicious actors.
