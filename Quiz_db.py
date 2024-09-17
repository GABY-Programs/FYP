import sqlite3


def create_connection():
    conn = sqlite3.connect('gabriel.db')
    c = conn.cursor()
    c.execute ('''
        CREATE TABLE IF NOT EXISTS quiz (
            id INTEGER PRIMARY KEY,
            questions TEXT NOT NULL,
            answer_1 TEXT NOT NULL,
            answer_2 TEXT NOT NULL,
            answer_3 TEXT NOT NULL,
            answer_4 TEXT NOT NULL,
            Correct_Answer TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def drop_table():
    with sqlite3.connect('gabriel.db') as conn:
        c = conn.cursor()
        c.execute('DROP TABLE IF EXISTS quiz')
        conn.commit()


def quiz_questions(questions, answer_1, answer_2, answer_3, answer_4, Correct_Answer):
    with sqlite3.connect('gabriel.db') as conn:
        c = conn.cursor()
        query = ("INSERT INTO quiz (questions, answer_1, answer_2, answer_3, answer_4, Correct_Answer)"
                 "VALUES (?,?,?,?,?,?)")
        values = (questions, answer_1, answer_2, answer_3, answer_4, Correct_Answer)
        c.execute(query, values)
        conn.commit()


drop_table()


create_connection()

#1
quiz_questions('Why is a keylogger bad to have on your computer?',
               'It improves computer performance.',
               'w It can capture sensitive information like password.',
               'It enhances security measures.',
               'It speeds up internet connectivity',
               'w It can capture sensitive information like password.')
#2
quiz_questions('What potential risks arise from the clipboard logging feature commonly employed by keyloggers?',
               'w Exposing sensitive information copied to the clipboard such as password or crypto wallets.',
               'Enhancing the speed of file transfers.',
               'Optimizing network connectivity.',
               'Accelerating internet browsing speed',
               'w Exposing sensitive information copied to the clipboard such as password or crypto wallets.')
#3
quiz_questions('What type of malware is known for disguising itself as a legitimate software?',
               'Spyware',
               'Ransomware',
               'Adware',
               'w Trojan',
               'w Trojan')
#4
quiz_questions('What is the primary purpose of antivirus software in cybersecurity?',
               'Enhancing computer graphics performance.',
               'w Detecting and removing malicious software.',
               'Preventing unauthorized access to a network.',
               'Spreading malware through your computer.',
               'w Detecting and removing malicious software.')
#5
quiz_questions('What is the purpose of multi-factor authentication(MFA) in cybersecurity?',
               'w Adding layers of security to the login process.',
               'Improving hardware performance.',
               'Simplifying software updates.',
               'Enhancing network speed.',
               'w Adding layers of security to the login process.')
#6
quiz_questions('what are potential risks of system specs logging?',
               'Exposing sensitive hardware and software configurations to unauthorized access.',
               'Compromising system performance due to excessive data logging activities.',
               'w Providing attackers with valuable information for crafting targeted cyber attacks.',
               'Violating user privacy by collecting and transmitting system details without consent.',
               'w Providing attackers with valuable information for crafting targeted cyber attacks.')
#7
quiz_questions('How does keylogging malware typically gain access to a users device.',
               'Asking for permission during software installation.',
               'w Through deceptive methods like phishing emails.',
               'Automatically installing during system updates.',
               'Purchasing it from official app stores',
               'w Through deceptive methods like phishing emails.')

#8
quiz_questions('How can users safeguard against keylogging malware?',
               'Sharing passwords with friends and family.',
               'w Regularly updating antivirus software.',
               'Disabling security features to improve system performance',
               'Using public Wi-Fi networks for online transactions.',
               'w Regularly updating antivirus software.')
#9
quiz_questions('How does malware differ from legitimate software?',
               'Malware often improves system performance.',
               'Legitimate software is usually free to download.',
               'w Malware steals data or causes harm to your computer.',
               'Legitimate software is always identified by antivirus programs.',
               'w Malware steals data or causes harm to your computer.')
#10
quiz_questions('Your computer slows down when you have malware on your computer?',
               'w True.',
               'False.',
               '.',
               '.',
               'w True.')
#11
quiz_questions('What is a keylogger primarily used for?',
               'w To record and capture a users keystrokes and login credentials.',
               'To display unwanted advertisements on a users computer.',
               'To encrypt a users data and make it inaccessible.',
               'To remove malicious software from a users computer.',
               'w To record and capture a users keystrokes and login credentials.')
#12
quiz_questions('What is an antivirus?',
               'Software that spreads virus.',
               'Medicine.',
               'w A software that is used to prevent, detect and remove malicious software.',
               'None of the above.',
               'w A software that is used to prevent, detect and remove malicious software.')
