#
#  ___                    __  __                      
# |   \ _  _ _ __  _ __  |  \/  |___ _ _ __ _ ___ _ _ 
# | |) | || | '  \| '_ \ | |\/| / -_) '_/ _` / -_) '_|
# |___/ \_,_|_|_|_| .__/ |_|  |_\___|_| \__, \___|_|  
#                 |_|                   |___/         
#
# Damian Strojek 2025, TestArmy S.A.
#

import csv
import time
import os
import glob

def process_all():
    print("\033[36mProcessing 1.5M POLAND GOOD QUALITY COMBOLIST.txt ...\033[0m")
    process_1_5_m_poland_combolist(True)
    print("\033[36mProcessing 1500000_data_random_websites.txt ...\033[0m")
    process_1500000_data_random_websites(True)
    print("\033[36mProcessing 3.5mlnPLmailpass.txt ...\033[0m")
    process_3_5mlnPLmailpass(True)
    print("\033[36mProcessing dump-agusiq-torrents.txt ...\033[0m")
    process_agusiq_torrents_dump(True)
    print("\033[36mProcessing bp-blogplay-users-dump.txt ...\033[0m")
    process_blogplay_users_dump(True)
    print("\033[36mProcessing cdprojectred.txt ...\033[0m")
    process_cdprojectred(True)
    #process_combo_2023(True)
    #process_combo_2024(True)
    print("\033[36mProcessing daniel_hosting.txt ...\033[0m")
    process_daniel_hosting(True)
    print("\033[36mProcessing Electroworld.txt ...\033[0m")
    process_electroworld(True)
    print("\033[36mProcessing inpost.txt ...\033[0m")
    process_inpost(True)
    print("\033[36mProcessing Ledger*.txt ...\033[0m")
    process_ledger(True)
    print("\033[36mProcessing pl2023_dump.txt ...\033[0m")
    process_pl2023_dump(True)
    print("\033[36mProcessing forum-torepublic*.txt ...\033[0m")
    process_torepublic(True)
    print("\033[36mProcessing wakacje_pl_forum_dump.txt ...\033[0m")
    process_wakacjepl_forum(True)
    print("\033[36mProcessing zapiszjako.pl_poczatek2016.txt ...\033[0m")
    process_zapiszjakopl(True)
    print("\033[36mProcessing Badoo.txt ...\033[0m")
    process_badoo(True)
    print("\033[36mProcessing sample.txt ...\033[0m")
    process_sample_txt(True)
    print("\033[36mProcessing tiktok_com_logpass.txt ...\033[0m")
    process_tiktok(True)
    print("\033[36mProcessing westernunion_com.txt ...\033[0m")
    process_westernunion_com(True)
    print("\033[36mProcessing all files in Dehashed Database directory ...\033[0m")
    process_dehashed_database(True)
    #process_canva_full_cleaned(True)

def process_all_individual():
    print("\033[36mProcessing 1.5M POLAND GOOD QUALITY COMBOLIST.txt ...\033[0m")
    process_1_5_m_poland_combolist()
    print("\033[36mProcessing 1500000_data_random_websites.txt ...\033[0m")
    process_1500000_data_random_websites()
    print("\033[36mProcessing 3.5mlnPLmailpass.txt ...\033[0m")
    process_3_5mlnPLmailpass()
    print("\033[36mProcessing dump-agusiq-torrents.txt ...\033[0m")
    process_agusiq_torrents_dump()
    print("\033[36mProcessing bp-blogplay-users-dump.txt ...\033[0m")
    process_blogplay_users_dump()
    print("\033[36mProcessing cdprojectred.txt ...\033[0m")
    process_cdprojectred()
    #process_combo_2023(True)
    #process_combo_2024(True)
    print("\033[36mProcessing daniel_hosting.txt ...\033[0m")
    process_daniel_hosting()
    print("\033[36mProcessing Electroworld.txt ...\033[0m")
    process_electroworld()
    print("\033[36mProcessing inpost.txt ...\033[0m")
    process_inpost()
    print("\033[36mProcessing Ledger*.txt ...\033[0m")
    process_ledger()
    print("\033[36mProcessing pl2023_dump.txt ...\033[0m")
    process_pl2023_dump()
    print("\033[36mProcessing forum-torepublic*.txt ...\033[0m")
    process_torepublic()
    print("\033[36mProcessing wakacje_pl_forum_dump.txt ...\033[0m")
    process_wakacjepl_forum()
    print("\033[36mProcessing zapiszjako.pl_poczatek2016.txt ...\033[0m")
    process_zapiszjakopl()
    print("\033[36mProcessing Badoo.txt ...\033[0m")
    process_badoo()
    print("\033[36mProcessing sample.txt ...\033[0m")
    process_sample_txt()
    print("\033[36mProcessing tiktok_com_logpass.txt ...\033[0m")
    process_tiktok()
    print("\033[36mProcessing westernunion_com.txt ...\033[0m")
    process_westernunion_com()
    print("\033[36mProcessing all files in Dehashed Database directory ...\033[0m")
    process_dehashed_database()
    #process_canva_full_cleaned(True)

# 1.5M POLAND GOOD QUALITY COMBOLIST.txt
def process_1_5_m_poland_combolist(mergeAll=False):
    inputFilename = "1.5M POLAND GOOD QUALITY COMBOLIST"
    inputFile = open(".\\dumps\\" + inputFilename + ".txt", "r", encoding="utf-8", errors="ignore")

    if mergeAll:
        outputFile = open("merge.csv", "w", newline="", encoding="utf-8")
    else:
        outputFile = open(inputFilename + ".csv", "w", newline="", encoding="utf-8")

    writer = csv.writer(outputFile)
    writer.writerow(["Source", "Date", "Username", "Email", "Password", "Hash"])
    
    start = time.time()

    for line in inputFile:
        line = line.strip()

        if ":" in line:
            id, password = line.split(":", 1)

            if not id and not password:
                continue

            # Source, Date, username, email, password, hash
            if "@" in id:
                writer.writerow(["1.5M Poland Combo List", "NULL", "NULL", id, password, "NULL"])
            else:
                writer.writerow(["1.5M Poland Combo List", "NULL", id, "NULL", password, "NULL"])

    end = time.time()
    print(f"\033[32mSuccess, completed in {round(end - start, 4)} sec.\033[0m")

    inputFile.close()
    outputFile.close()

# 1500000_data_random_websites.txt
def process_1500000_data_random_websites(mergeAll=False):
    inputFilename = "1500000_data_random_websites"
    inputFile = open(".\\dumps\\" + inputFilename + ".txt", "r", encoding="utf-8", errors="ignore")

    if mergeAll:
        outputFile = open("merge.csv", "a", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
    else:
        outputFile = open(inputFilename + ".csv", "w", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
        writer.writerow(["Source", "Date", "Username", "Email", "Password", "Hash"])
    
    start = time.time()

    for line in inputFile:
        line = line.strip()
        parts = line.split(":")

        if len(parts) >= 3:
            id = parts[-2].strip()
            password = parts[-1].strip()

            if not id and not password:
                continue

            # Source, Date, username, email, password, hash
            if "@" in id:
                writer.writerow(["1500000 Data Random Websites Combo", "NULL", "NULL", id, password, "NULL"])
            else:
                writer.writerow(["1500000 Data Random Websites Combo", "NULL", id, "NULL", password, "NULL"])

    end = time.time()
    print(f"\033[32mSuccess, completed in {round(end - start, 4)} sec.\033[0m")

    inputFile.close()
    outputFile.close()

# 3.5mlnPLmailpass.txt
def process_3_5mlnPLmailpass(mergeAll=False):
    inputFilename = "3.5mlnPLmailpass"
    inputFile = open(".\\dumps\\" + inputFilename + ".txt", "r", encoding="utf-8", errors="ignore")
    
    if mergeAll:
        outputFile = open("merge.csv", "a", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
    else:
        outputFile = open(inputFilename + ".csv", "w", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
        writer.writerow(["Source", "Date", "Username", "Email", "Password", "Hash"])
    
    start = time.time()

    for line in inputFile:
        line = line.strip()

        if ":" in line:
            id, password = line.split(":", 1)
            
            # Situation where there are dates in the email fields
            if checkDate(id):
                continue

            if not id and not password:
                continue

            # Source, Date, username, email, password, hash
            if "@" in id:
                writer.writerow(["3.5M PL Mail Pass Combo", "NULL", "NULL", id, password, "NULL"])
            else:
                writer.writerow(["3.5M PL Mail Pass Combo", "NULL", id, "NULL", password, "NULL"])

    end = time.time()
    print(f"\033[32mSuccess, completed in {round(end - start, 4)} sec.\033[0m")

    inputFile.close()
    outputFile.close()

# dump-agusiq-torrents.txt
def process_agusiq_torrents_dump(mergeAll=False):
    inputFilename = "dump-agusiq-torrents"
    inputFile = open(".\\dumps\\" + inputFilename + ".txt", "r", encoding="utf-8", errors="ignore")
    
    if mergeAll:
        outputFile = open("merge.csv", "a", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
    else:
        outputFile = open(inputFilename + ".csv", "w", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
        writer.writerow(["Source", "Date", "Username", "Email", "Password", "Hash"])
    
    start = time.time()

    for line in inputFile:
        line = line.strip()

        # Extract values inside parentheses
        if "INSERT INTO `users` VALUES (" in line:
            values_part = line.split("VALUES (")[-1]  # Get only the part after "VALUES ("
            values = values_part.split(",")  # Split by comma
            
            # Ensure we have enough values to extract
            if len(values) >= 7:
                username = values[2].strip().strip("'")
                passwordHash = values[3].strip().strip("'")
                email = values[6].strip().strip("'")

                # Source, Date, username, email, password, hash
                writer.writerow(["Dump from http://agusiq-torrents.pl/", "NULL", username, email, "NULL", passwordHash])

    end = time.time()
    print(f"\033[32mSuccess, completed in {round(end - start, 4)} sec.\033[0m")

    inputFile.close()
    outputFile.close()

# bp-blogplay-users-dump.txt
def process_blogplay_users_dump(mergeAll=False):
    inputFilename = "bp-blogplay-users-dump"
    inputFile = open(".\\dumps\\" + inputFilename + ".txt", "r", encoding="utf-8", errors="ignore")
    
    if mergeAll:
        outputFile = open("merge.csv", "a", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
    else:
        outputFile = open(inputFilename + ".csv", "w", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
        writer.writerow(["Source", "Date", "Username", "Email", "Password", "Hash"])
    
    start = time.time()

    for line in inputFile:
        line = line.strip()

        if "(" in line:
            values_part = line.split("(")[-1]  # Get only the part after "("
            values = values_part.split(",")  # Split by comma

            # Ensure we have enough values to extract
            if len(values) >= 5:
                username = values[1].strip().strip("'")
                passwordHash = values[2].strip().strip("'")
                email = values[4].strip().strip("'")

                # Source, Date, username, email, password, hash
                writer.writerow(["Dump of Database `blogplay`", "Dump generation time: Aug 11,2020", username, email, "NULL", passwordHash])

    end = time.time()
    print(f"\033[32mSuccess, completed in {round(end - start, 4)} sec.\033[0m")

    inputFile.close()
    outputFile.close()

# cdprojectred.txt
# https://www.cdprojekt.com/en/media/news/information-regarding-data-security/
def process_cdprojectred(mergeAll=False):
    inputFilename = "cdprojectred"
    inputFile = open(".\\dumps\\" + inputFilename + ".txt", "r", encoding="utf-8", errors="ignore")
    
    if mergeAll:
        outputFile = open("merge.csv", "a", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
    else:
        outputFile = open(inputFilename + ".csv", "w", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
        writer.writerow(["Source", "Date", "Username", "Email", "Password", "Hash"])
    
    start = time.time()

    for line in inputFile:
        line = line.strip()

        if ":" in line:
            email, password, salt = line.split(":")

            if not email or not password or not salt:
                continue

            # Source, Date, username, email, password, hash
            writer.writerow(["cdprojectred.txt", "Leak from data breach in year 2021", "NULL", email, "NULL", password+":"+salt])

    end = time.time()
    print(f"\033[32mSuccess, completed in {round(end - start, 4)} sec.\033[0m")

    inputFile.close()
    outputFile.close()

# combo_rez_2023.txt
# Date from 01-09-2023 to 30-11-2023
def process_combo_2023(mergeAll=False):
    inputFilename = "combo_rez_2023"
    inputFile = open(".\\dumps\\" + inputFilename + ".txt", "r", encoding="utf-8", errors="ignore")
    
    if mergeAll:
        outputFile = open("merge.csv", "a", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
    else:
        outputFile = open(inputFilename + ".csv", "w", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
        writer.writerow(["Source", "Date", "Username", "Email", "Password", "Hash"])
    
    start = time.time()

    for i, line in enumerate(inputFile):
        line = line.strip()

        if not i % 200000000:
            print("\033[36mProcessing line " + str(i) + " of combo_rez_2023.txt ...\033[0m")

        if ":" in line:
            credentials = line.split(":")

            if len(credentials) >= 2:
                id = credentials[0]
                password = credentials[1]

                if not id and not password:
                    continue

                # Additional filtering because there is too much data
                if len(id) <= 3 or len(id) <= 3 or len(id) > 75 or len(password) > 75:
                    continue
                
                # Source, Date, username, email, password, hash
                if "@" in id:
                    writer.writerow(["Combo", "01-09-2023 - 30-11-2023", "NULL", id, password, "NULL"])
                else:
                    writer.writerow(["Combo", "01-09-2023 - 30-11-2023", id, "NULL", password, "NULL"])

    end = time.time()
    print(f"\033[32mSuccess, completed in {round(end - start, 4)} sec.\033[0m")

    inputFile.close()
    outputFile.close()

# combo_rez_2024.txt
# Date from 01-12-2023 to 02-02-2024
def process_combo_2024(mergeAll=False):
    inputFilename = "combo_rez_2024"
    inputFile = open(".\\dumps\\" + inputFilename + ".txt", "r", encoding="utf-8", errors="ignore")
    
    if mergeAll:
        outputFile = open("merge.csv", "a", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
    else:
        outputFile = open(inputFilename + ".csv", "w", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
        writer.writerow(["Source", "Date", "Username", "Email", "Password", "Hash"])
    
    start = time.time()

    for i, line in enumerate(inputFile):
        line = line.strip()

        if not i % 150000000:
            print("\033[36mProcessing line " + str(i) + " of combo_rez_2024.txt ...\033[0m")

        if ":" in line:
            credentials = line.split(":")

            if len(credentials) >= 2:
                id = credentials[0]
                password = credentials[1]
                
                if not id and not password:
                    continue

                # Additional filtering because there is too much data
                if len(id) <= 3 or len(password) <= 3 or len(id) > 75 or len(password) > 75:
                    continue

                # Source, Date, username, email, password, hash
                if "@" in id:
                    writer.writerow(["Combo", "01-12-2023 - 02-02-2024", "NULL", id, password, "NULL"])
                else:
                    writer.writerow(["Combo", "01-12-2023 - 02-02-2024", id, "NULL", password, "NULL"])

    end = time.time()
    print(f"\033[32mSuccess, completed in {round(end - start, 4)} sec.\033[0m")

    inputFile.close()
    outputFile.close()

# daniel_hosting.txt
def process_daniel_hosting(mergeAll=False):
    inputFilename = "daniel_hosting"
    inputFile = open(".\\dumps\\" + inputFilename + ".txt", "r", encoding="utf-8", errors="ignore")
    
    if mergeAll:
        outputFile = open("merge.csv", "a", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
    else:
        outputFile = open(inputFilename + ".csv", "w", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
        writer.writerow(["Source", "Date", "Username", "Email", "Password", "Hash"])
    
    start = time.time()

    # daniel_hosting.txt
    for line in inputFile:
        line = line.strip()

        if "(" in line:
            values_part = line.split("(")[-1]  # Get only the part after "("
            values = values_part.split(",")  # Split by comma

            # Ensure we have enough values to extract
            if len(values) >= 4:
                username = values[2].strip().strip("'")
                passwordHash = values[3].strip().strip("'")

            # Source, Date, username, email, password, hash
            writer.writerow(["Onion database daniel_hosting", "NULL", username, "NULL", "NULL", passwordHash])

    inputFile.close()
    inputFilename = "daniel_hosting_emails"
    inputFile = open(".\\dumps\\" + inputFilename + ".txt", "r", encoding="utf-8", errors="ignore")

    # daniel_hosting_emails.txt
    for line in inputFile:
        line = line.strip()

        if "@" in line:
            if " " in line:
                parts = line.split(" ")
                email1 = parts[0]
                email2 = parts[-1]

                if email1:
                    # Source, Date, username, email, password, hash
                    writer.writerow(["Onion database daniel_hosting", "NULL", "NULL", email1, "NULL", "NULL"])
                if email2:
                    # Source, Date, username, email, password, hash
                    writer.writerow(["Onion database daniel_hosting", "NULL", "NULL", email2, "NULL", "NULL"])
            else:
                # Source, Date, username, email, password, hash
                writer.writerow(["Onion database daniel_hosting", "NULL", "NULL", line, "NULL", "NULL"])

    end = time.time()
    print(f"\033[32mSuccess, completed in {round(end - start, 4)} sec.\033[0m")

    inputFile.close()
    outputFile.close()

# Electroworld.txt
def process_electroworld(mergeAll=False):
    inputFilename = "Electroworld"
    inputFile = open(".\\dumps\\" + inputFilename + ".txt", "r", encoding="utf-8", errors="ignore")
    
    if mergeAll:
        outputFile = open("merge.csv", "a", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
    else:
        outputFile = open(inputFilename + ".csv", "w", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
        writer.writerow(["Source", "Date", "Username", "Email", "Password", "Hash"])
    
    start = time.time()

    for line in inputFile:
        line = line.strip()

        if "," in line:
            email, passwordHash = line.split(",")

            if not email or not passwordHash:
                continue

            # Source, Date, username, email, password, hash
            if "@" in email and not "aaa@aa.pl" in email:
                writer.writerow(["Electroworld", "NULL", "NULL", email, "NULL", passwordHash])

    end = time.time()
    print(f"\033[32mSuccess, completed in {round(end - start, 4)} sec.\033[0m")

    inputFile.close()
    outputFile.close()

# inpost.txt
# https://niebezpiecznik.pl/post/inpost-operator-paczkomatow-zhackowany-wyciekla-baza-zawierajaca-dane-na-temat-57-000-pracownikow/
def process_inpost(mergeAll=False):
    inputFilename = "inpost"
    inputFile = open(".\\dumps\\" + inputFilename + ".txt", "r", encoding="utf-8", errors="ignore")
    
    if mergeAll:
        outputFile = open("merge.csv", "a", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
    else:
        outputFile = open(inputFilename + ".csv", "w", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
        writer.writerow(["Source", "Date", "Username", "Email", "Password", "Hash"])
    
    start = time.time()

    # Line 0-250
    for i, line in enumerate(inputFile):
        if i >= 250:
            break

        line = line.strip()

        if "(" in line:
            values_part = line.split("(")[-1]  # Get only the part after "("
            values = values_part.split(",")  # Split by comma

            # Situation where there is a comma in the password field
            if len(values) == 14:
                email = values[7].strip().strip("'")
                password = values[9].strip().strip("'") + ',' + values[10].strip().strip("'")

                if not email or not password:
                    continue

                # Source, Date, username, email, password, hash
                writer.writerow(["Inpost Database Leak", "Generated on 3rd July 2017", "NULL", email, password, "NULL"])

            # Ensure we have enough values to extract
            elif len(values) >= 10:
                email = values[7].strip().strip("'")
                password = values[9].strip().strip("'")

                if not email or not password:
                    continue

                # Source, Date, username, email, password, hash
                writer.writerow(["Inpost Database Leak", "Generated on 3rd July 2017", "NULL", email, password, "NULL"])

    # Line 250-1440
    for i, line in enumerate(inputFile):
        if i >= 1190:
            break
        
        line = line.strip()

        if "(" in line:
            values_part = line.split("(")[-1]  # Get only the part after "("
            values = values_part.split(",")  # Split by comma

            # Ensure we have enough values to extract
            if len(values) >= 5:
                email = values[3].strip().strip("'")
                password = values[4].strip().strip("'")

                if not email or not password:
                    continue

                # Source, Date, username, email, password, hash
                writer.writerow(["Inpost Database Leak", "Generated on 3rd July 2017", "NULL", email, password, "NULL"])

    # Line 1440+
    for line in inputFile:
        line = line.strip()

        if ":" in line:
            email, password = line.split(":")

            if not email or not password:
                continue

            # Source, Date, username, email, password, hash
            writer.writerow(["Inpost Database Leak", "Generated on 3rd July 2017", "NULL", email, password, "NULL"])

    end = time.time()
    print(f"\033[32mSuccess, completed in {round(end - start, 4)} sec.\033[0m")

    inputFile.close()
    outputFile.close()

# Ledger*.txt
def process_ledger(mergeAll=False):
    inputFilename = "Ledger-All-Emails"
    inputFile = open(".\\dumps\\Ledger\\" + inputFilename + ".txt", "r", encoding="utf-8", errors="ignore")
    
    if mergeAll:
        outputFile = open("merge.csv", "a", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
    else:
        outputFile = open(inputFilename + ".csv", "w", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
        writer.writerow(["Source", "Date", "Username", "Email", "Password", "Hash"])
    
    start = time.time()

    # Ledger-All-Emails.txt
    for line in inputFile:
        email = line.strip()

        if not email:
            continue

        # Source, Date, username, email, password, hash
        writer.writerow(["Ledger", "NULL", "NULL", email, "NULL", "NULL"])

    inputFile.close()
    inputFilename = "Ledger"
    inputFile = open(".\\dumps\\Ledger\\" + inputFilename + ".txt", "r", encoding="utf-8", errors="ignore")
    
    # Ledger.txt
    for line in inputFile:
        line = line.strip()

        if "|" in line:
            email = line.split("|")[0].strip()

            if not email:
                continue

            # Source, Date, username, email, password, hash
            writer.writerow(["Ledger", "NULL", "NULL", email, "NULL", "NULL"])

    inputFile.close()
    inputFilename = "Ledger-Order-Buyers"
    inputFile = open(".\\dumps\\Ledger\\" + inputFilename + ".txt", "r", encoding="utf-8", errors="ignore")
    
    # Ledger-Order-Buyers.txt
    for line in inputFile:
        line = line.strip()

        if "|" in line:
            email = line.split("|")[0].strip()

            if not email:
                continue

            # Source, Date, username, email, password, hash
            writer.writerow(["Ledger", "NULL", "NULL", email, "NULL", "NULL"])

    end = time.time()
    print(f"\033[32mSuccess, completed in {round(end - start, 4)} sec.\033[0m")

    inputFile.close()
    outputFile.close()

# pl2023_dump.txt
def process_pl2023_dump(mergeAll=False):
    inputFilename = "pl2023_dump"
    inputFile = open(".\\dumps\\" + inputFilename + ".txt", "r", encoding="utf-8", errors="ignore")

    if mergeAll:
        outputFile = open("merge.csv", "a", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
    else:
        outputFile = open(inputFilename + ".csv", "w", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
        writer.writerow(["Source", "Date", "Username", "Email", "Password", "Hash"])
    
    start = time.time()

    for line in inputFile:
        line = line.strip()

        # If there is not at least two colons, skip. Colons are at the beginning and between id and password
        # Situations with multiple websites, no credentials inside
        if line.count(":") < 2 or line.count("http") >= 2:
            continue
        # Space between source and credentials
        elif line.count(" ") == 1:
            source, credentialsLine = line.split(" ")
            credentials = credentialsLine.split(":")

            if credentials == ":":
                continue
            
            if len(credentials) >= 2:
                id = credentials[-2]
                password = credentials[-1]

                if not source or not id or not password:
                    continue

                # Source, Date, username, email, password, hash
                if "@" in id:
                    writer.writerow([source, "2023", "NULL", id, password, "NULL"])
                else:
                    writer.writerow([source, "2023", id, "NULL", password, "NULL"])

        # Only colons in between source and credentials
        else:
            parts = line.split(":")
            if len(parts) >= 2:
                id = parts[-2]
                password = parts[-1]
                source = parts[0] + ":" + parts[1]
                
                if not id and not password:
                    continue

                # Source, Date, username, email, password, hash
                if "@" in id:
                    writer.writerow([source, "2023", "NULL", id, password, "NULL"])
                else:
                    writer.writerow([source, "2023", id, "NULL", password, "NULL"])

    end = time.time()
    print(f"\033[32mSuccess, completed in {round(end - start, 4)} sec.\033[0m")

    inputFile.close()
    outputFile.close()

# forum-torepublic*.txt
def process_torepublic(mergeAll=False):
    inputFilename = "forum-torepublic"
    inputFile = open(".\\dumps\\forum-torepublic\\" + inputFilename + ".txt", "r", encoding="utf-8", errors="ignore")

    if mergeAll:
        outputFile = open("merge.csv", "a", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
    else:
        outputFile = open(inputFilename + ".csv", "w", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
        writer.writerow(["Source", "Date", "Username", "Email", "Password", "Hash"])
    
    start = time.time()

    # forum-torepublic.txt
    # 4 records
    for line in inputFile:
        line = line.strip()

        if "'" in line:
            email, username, passwordHash, salt = line.split("'")

            # Source, Date, username, email, password, hash
            writer.writerow(["Forum torepublic dump", "Dump generated on 2015-12-19", username, email, "NULL", passwordHash+":"+salt])

    inputFile.close()
    inputFilename = "forum-torepublic-post-1"
    inputFile = open(".\\dumps\\forum-torepublic\\" + inputFilename + ".txt", "r", encoding="utf-8", errors="ignore")

    # forum-torepublic-post-1.txt
    # One line
    # Email addresses and passwords between ':' and '\n' between different credentials
    line = inputFile.readline().strip()
    pairs = line.split("\\n")

    for pair in pairs:
        if ":" in pair:
            parts = pair.split(":")
            email = parts[0]
            password = parts[1]

            if not email and not password:
                continue

            # Source, Date, username, email, password, hash
            writer.writerow(["Forum torepublic dump post 1", "Dump generated on 2015-12-19", "NULL", email, password, "NULL"])

    inputFile.close()
    inputFilename = "forum-torepublic-post-2"
    inputFile = open(".\\dumps\\forum-torepublic\\" + inputFilename + ".txt", "r", encoding="utf-8", errors="ignore")

    # forum-torepublic-post-2.txt
    # Email addresses separated by '\n'
    line = inputFile.readline().strip()
    parts = line.split("\\n")

    for email in parts:
        if "@" in email:
            # Source, Date, username, email, password, hash
            writer.writerow(["Forum torepublic dump post 2", "Dump generated on 2015-12-19", "NULL", email, "NULL", "NULL"])

    inputFile.close()
    inputFilename = "forum-torepublic-post-3"
    inputFile = open(".\\dumps\\forum-torepublic\\" + inputFilename + ".txt", "r", encoding="utf-8", errors="ignore")
    
    # forum-torepublic-post-3.txt
    # Emails and hashes separated by ':' and '\n' between credentials in the same line
    line = inputFile.readline().strip()
    pairs = line.split("\\n")

    for pair in pairs:
        if ":" in pair:
            parts = pair.split(":")
            email = parts[0]
            passwordHash = parts[1]

            if not email and not passwordHash:
                continue

            # Source, Date, username, email, password, hash
            writer.writerow(["Forum torepublic dump post 3", "Dump generated on 2015-12-19", "NULL", email, "NULL", passwordHash])

    inputFile.close()
    inputFilename = "forum-torepublic-post-4"
    inputFile = open(".\\dumps\\forum-torepublic\\" + inputFilename + ".txt", "r", encoding="utf-8", errors="ignore")

    # forum-torepublic-post-4.txt
    # Cracked hashes and plaintext passwords separated by ':' and in between '\n'
    line = inputFile.readline().strip()
    pairs = line.split("\\n")

    for pair in pairs:
        if ":" in pair:
            parts = pair.split(":")
            passwordHash = parts[0]
            password = parts[1]

            if not passwordHash and not password:
                continue

            # Source, Date, username, email, password, hash
            writer.writerow(["Forum torepublic dump post 4", "Dump generated on 2015-12-19", "NULL", "NULL", password, passwordHash])

    inputFile.close()
    inputFilename = "forum-torepublic-post-5"
    inputFile = open(".\\dumps\\forum-torepublic\\" + inputFilename + ".txt", "r", encoding="utf-8", errors="ignore")

    # forum-torepublic-post-5.txt
    # Emails and passwords separated by ';' and '\n' in between pairs
    line = inputFile.readline().strip()
    pairs = line.split("\\n")

    for pair in pairs:
        if ";" in pair:
            parts = pair.split(";")
            email = parts[0]
            password = parts[1]

            if not email and not password:
                continue

            # Source, Date, username, email, password, hash
            writer.writerow(["Forum torepublic dump post 5", "Dump generated on 2015-12-19", "NULL", email, password, "NULL"])

    inputFile.close()
    inputFilename = "forum-torepublic-post-6"
    inputFile = open(".\\dumps\\forum-torepublic\\" + inputFilename + ".txt", "r", encoding="utf-8", errors="ignore")

    # forum-torepublic-post-6.txt
    # Emails and hashes separated by tab and '\n' in between
    line = inputFile.readline().strip()
    pairs = line.split("\\n")

    for pair in pairs:
        parts = pair.split(" ")
        if len(parts) >= 3:
            email = parts[1]
            passwordHash = parts[2]

            if not email and not passwordHash:
                continue

            # Source, Date, username, email, password, hash
            writer.writerow(["Forum torepublic dump post 6", "Dump generated on 2015-12-19", "NULL", email, "NULL", passwordHash])

    inputFile.close()
    inputFilename = "forum-torepublic-post-7"
    inputFile = open(".\\dumps\\forum-torepublic\\" + inputFilename + ".txt", "r", encoding="utf-8", errors="ignore")

    # forum-torepublic-post-7.txt
    # Emails and hashes separated by tab and '\n' in between
    line = inputFile.readline().strip()
    pairs = line.split("\\n")

    for pair in pairs:
        parts = pair.split(" ")
        if len(parts) >= 6:
            email = parts[0]
            passwordHash = parts[5]

            if not email and not passwordHash:
                continue

            # Source, Date, username, email, password, hash
            writer.writerow(["Forum torepublic dump post 7", "Dump generated on 2015-12-19", "NULL", email, "NULL", passwordHash])

    inputFile.close()
    inputFilename = "forum-torepublic-post-8"
    inputFile = open(".\\dumps\\forum-torepublic\\" + inputFilename + ".txt", "r", encoding="utf-8", errors="ignore")

    # forum-torepublic-post-8.txt
    # Emails and hashes separated by tab and '\n' in between
    line = inputFile.readline().strip()
    pairs = line.split("\\n")

    for pair in pairs:
        parts = pair.split(":")
        # Lines with more information - email, sometimes cracked password and hash
        if len(parts) >= 3:
            email = parts[0]
            passwordHash = parts[1]
            if parts[2] == "":
                password = "NULL"
            else:
                password = parts[2]

            if not email and not passwordHash and not password:
                continue

            # Source, Date, username, email, password, hash
            writer.writerow(["Forum torepublic dump post 8", "Dump generated on 2015-12-19", "NULL", email, password, passwordHash])
        # Some lines have less information, only email and hash
        elif len(parts) == 2:
            email = parts[0]
            passwordHash = parts[1]

            if not email and not passwordHash:
                continue

            # Source, Date, username, email, password, hash
            writer.writerow(["Forum torepublic dump post 8", "Dump generated on 2015-12-19", "NULL", email, "NULL", passwordHash])

    inputFile.close()
    inputFilename = "forum-torepublic-post-9"
    inputFile = open(".\\dumps\\forum-torepublic\\" + inputFilename + ".txt", "r", encoding="utf-8", errors="ignore")

    # forum-torepublic-post-9.txt
    # Passwords and emails separated by ':' and '\n' in between
    line = inputFile.readline().strip()
    pairs = line.split("\\n")

    for pair in pairs:
        if ":" in pair:
            parts = pair.split(":")
            password = parts[0]
            email = parts[1]

            if not email and not password:
                continue

            # Source, Date, username, email, password, hash
            writer.writerow(["Forum torepublic dump post 9", "Dump generated on 2015-12-19", "NULL", email, password, "NULL"])

    inputFile.close()
    inputFilename = "forum-torepublic-post-10"
    inputFile = open(".\\dumps\\forum-torepublic\\" + inputFilename + ".txt", "r", encoding="utf-8", errors="ignore")

    # forum-torepublic-post-10.txt
    # Many data separated by <blank> and commas
    line = inputFile.readline().strip()
    pairs = line.split("<blank>")

    for pair in pairs:
        parts = pair.split(",")

        if len(parts) >= 6:
            password = parts[4]
            email = parts[5]

            if not email and not password:
                continue

            # Source, Date, username, email, password, hash
            writer.writerow(["Forum torepublic dump post 10", "Dump generated on 2015-12-19", "NULL", email, password, "NULL"])

    inputFile.close()
    inputFilename = "forum-torepublic-post-11"
    inputFile = open(".\\dumps\\forum-torepublic\\" + inputFilename + ".txt", "r", encoding="utf-8", errors="ignore")

    # forum-torepublic-post-11.txt
    # Password, email, and hash separated by commas and '\n' in between
    line = inputFile.readline().strip()
    pairs = line.split("\\n")

    for pair in pairs:
        parts = pair.split(",")

        if len(parts) >= 3:
            password = parts[0]
            email = parts[1]
            passwordHash = parts[2]

            if not email and not password and not passwordHash:
                continue

            # Source, Date, username, email, password, hash
            writer.writerow(["Forum torepublic dump post 11", "Dump generated on 2015-12-19", "NULL", email, password, passwordHash])

    inputFile.close()

    end = time.time()
    print(f"\033[32mSuccess, completed in {round(end - start, 4)} sec.\033[0m")

    outputFile.close()

# wakacje_pl_forum_dump.txt
# https://sekurak.pl/wyciek-z-forum-serwisu-wakacje-pl/
def process_wakacjepl_forum(mergeAll=False):
    inputFilename = "wakacje_pl_forum_dump"
    inputFile = open(".\\dumps\\" + inputFilename + ".txt", "r", encoding="utf-8", errors="ignore")

    if mergeAll:
        outputFile = open("merge.csv", "a", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
    else:
        outputFile = open(inputFilename + ".csv", "w", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
        writer.writerow(["Source", "Date", "Username", "Email", "Password", "Hash"])
    
    start = time.time()

    for line in inputFile:
        line = line.strip()
        linePart = line.split("VALUES")[-1]  # Get only the part after "VALUES ("
        lineUsers = linePart.split("(") 

        for user in lineUsers:
            userPart = user.split(",")
            
            if len(userPart) >= 71:
                username = userPart[4].strip().strip("'")
                email = userPart[6].strip().strip("'")
                secret = userPart[70].strip().strip("'")

                # Source, Date, username, email, password, hash
                writer.writerow(["Dump from wakacje.pl forum breach", "Dump generated on 2020-08-12, leaked at beginning of November 2021", username, email, "NULL", secret])

    end = time.time()
    print(f"\033[32mSuccess, completed in {round(end - start, 4)} sec.\033[0m")

    inputFile.close()
    outputFile.close()

# zapiszjako.pl_poczatek2016.txt
def process_zapiszjakopl(mergeAll=False):
    inputFilename = "zapiszjako.pl_poczatek2016"
    inputFile = open(".\\dumps\\" + inputFilename + ".txt", "r", encoding="utf-8", errors="ignore")

    if mergeAll:
        outputFile = open("merge.csv", "a", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
    else:
        outputFile = open(inputFilename + ".csv", "w", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
        writer.writerow(["Source", "Date", "Username", "Email", "Password", "Hash"])
    
    start = time.time()

    for line in inputFile:
        line = line.strip()

        if ":" in line:
            id, password = line.split(":", 1)

            if not id and not password:
                continue

            # Source, Date, username, email, password, hash
            if len(password) > 24:
                writer.writerow(["Zapiszjako.pl Data Breach poczatek 2016", "2016", "NULL", id, "NULL", password])
            else:
                writer.writerow(["Zapiszjako.pl Data Breach poczatek 2016", "2016", "NULL", id , password, "NULL"])

    end = time.time()
    print(f"\033[32mSuccess, completed in {round(end - start, 4)} sec.\033[0m")

    inputFile.close()
    outputFile.close()
    
# Badoo.txt
# https://monitor.mozilla.org/breach-details/Badoo
def process_badoo(mergeAll=False):
    inputFilename = "Badoo"
    inputFile = open(".\\dumps\\nowe-olha\\" + inputFilename + ".txt", "r", encoding="utf-8", errors="ignore")

    if mergeAll:
        outputFile = open("merge.csv", "a", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
    else:
        outputFile = open(inputFilename + ".csv", "w", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
        writer.writerow(["Source", "Date", "Username", "Email", "Password", "Hash"])

    start = time.time()

    for line in inputFile:
        line = line.strip()

        if ":" in line:
            id, password = line.split(":", 1)

            if not id and not password:
                continue

            # Source, Date, username, email, password, hash
            if "@" in id:
                writer.writerow(["Badoo breach", "Probably June 1, 2013", "NULL", id, password, "NULL"])
            else:
                writer.writerow(["Badoo breach", "Probably June 1, 2013", id, "NULL", password, "NULL"])

    end = time.time()
    print(f"\033[32mSuccess, completed in {round(end - start, 4)} sec.\033[0m")

    inputFile.close()
    outputFile.close()

# sample.txt
def process_sample_txt(mergeAll = False):
    inputFilename = "sample"
    inputFile = open(".\\dumps\\nowe-olha\\" + inputFilename + ".txt", "r", encoding="utf-8", errors="ignore")

    if mergeAll:
        outputFile = open("merge.csv", "a", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
    else:
        outputFile = open(inputFilename + ".csv", "w", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
        writer.writerow(["Source", "Date", "Username", "Email", "Password", "Hash"])
    
    start = time.time()

    for line in inputFile:
        line = line.strip()

        if ":" in line:
            parts = line.split(":")
            id = parts[-2]
            password = parts[-1]
            source = parts[0] + ":" + parts[1]

            if not id and not password and not source:
                continue

            # Additional filtering because there is too much data
            if len(id) <= 3 or len(id) <= 3 or len(id) > 75 or len(password) > 75:
                continue

            # Source, Date, username, email, password, hash
            if "@" in id:
                writer.writerow([source, "NULL", "NULL", id, password, "NULL"])
            else:
                writer.writerow([source, "NULL", id, "NULL", password, "NULL"])

    end = time.time()
    print(f"\033[32mSuccess, completed in {round(end - start, 4)} sec.\033[0m")

    inputFile.close()
    outputFile.close()

# tiktok_com_logpass.txt
# https://www.twingate.com/blog/tips/TikTok-data-breach
def process_tiktok(mergeAll = False):
    inputFilename = "tiktok_com_logpass"
    inputFile = open(".\\dumps\\nowe-olha\\" + inputFilename + ".txt", "r", encoding="utf-8", errors="ignore")

    if mergeAll:
        outputFile = open("merge.csv", "a", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
    else:
        outputFile = open(inputFilename + ".csv", "w", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
        writer.writerow(["Source", "Date", "Username", "Email", "Password", "Hash"])
    
    start = time.time()

    for line in inputFile:
        line = line.strip()

        if ":" in line:
            parts = line.split(":")
            id = parts[0]
            password = parts[1]

            if not id and not password:
                continue

            # Source, Date, username, email, password, hash
            if "@" in id:
                writer.writerow(["TikTok Breach Logpass", "Probably August 2020", "NULL", id, password, "NULL"])
            else:
                writer.writerow(["TikTok Breach Logpass", "Probably August 2020", id, "NULL", password, "NULL"])

    end = time.time()
    print(f"\033[32mSuccess, completed in {round(end - start, 4)} sec.\033[0m")

    inputFile.close()
    outputFile.close()

# westernunion_com.txt
def process_westernunion_com(mergeAll = False):
    inputFilename = "westernunion_com"
    inputFile = open(".\\dumps\\nowe-olha\\" + inputFilename + ".txt", "r", encoding="utf-8", errors="ignore")

    if mergeAll:
        outputFile = open("merge.csv", "a", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
    else:
        outputFile = open(inputFilename + ".csv", "w", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
        writer.writerow(["Source", "Date", "Username", "Email", "Password", "Hash"])
    
    start = time.time()

    lines = inputFile.readlines()
    for i in range(0, len(lines), 4):
        source = lines[i].strip().split(":", 1)[1]
        id = lines[i+1].strip().split(":", 1)[1]
        password = lines[i+2].strip().split(":", 1)[1]

        if not source and not id and not password:
            continue

        # Source, Date, username, email, password, hash
        if "@" in id:
            writer.writerow([source, "NULL", "NULL", id, password, "NULL"])
        else:
            writer.writerow([source, "NULL", id, "NULL", password, "NULL"])

    end = time.time()
    print(f"\033[32mSuccess, completed in {round(end - start, 4)} sec.\033[0m")

    inputFile.close()
    outputFile.close()

# \nowe-olha\DehashedDatabase\*.txt
def process_dehashed_database(mergeAll = False):
    inputFiles = glob.glob(os.path.join(".\\dumps\\nowe-olha\\DehashedDatabase\\", "*.txt"))

    if mergeAll:
        outputFile = open("merge.csv", "a", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
    else:
        outputFile = open("DehashedDatabase.csv", "w", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
        writer.writerow(["Source", "Date", "Username", "Email", "Password", "Hash"])

    start = time.time()

    for title in inputFiles:
        inputFilename = os.path.splitext(os.path.basename(title))[0]
        inputFile = open(".\\dumps\\nowe-olha\\DehashedDatabase\\" + inputFilename + ".txt", "r", encoding="utf-8", errors="ignore")

        print("\033[36mProcessing " + str(inputFilename) + " from DehashedDatabase ...\033[0m")

        for line in inputFile:
            line = line.strip()

            if ":" in line:
                parts = line.split(":")
                id = parts[0]
                password = parts[1]

                if not id and not password:
                    continue

                # Source, Date, username, email, password, hash
                if "@" in id:
                    writer.writerow([inputFilename, "NULL", "NULL", id, password, "NULL"])
                else:
                    writer.writerow([inputFilename, "NULL", id, "NULL", password, "NULL"])
        
        inputFile.close()

    end = time.time()
    print(f"\033[32mSuccess, completed in {round(end - start, 4)} sec.\033[0m")

    outputFile.close()

# CANVA_FULL_CLEANED.txt
def process_canva_full_cleaned(mergeAll = False):
    inputFilename = "CANVA_FULL_CLEANED"
    inputFile = open(".\\dumps\\nowe-olha\\" + inputFilename + ".txt", "r", encoding="utf-8", errors="ignore")

    if mergeAll:
        outputFile = open("merge.csv", "a", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
    else:
        outputFile = open(inputFilename + ".csv", "w", newline="", encoding="utf-8")
        writer = csv.writer(outputFile)
        writer.writerow(["Source", "Date", "Username", "Email", "Password", "Hash"])
    
    start = time.time()

    for i, line in enumerate(inputFile):
        line = line.strip()
        parts = line.split(",")

        if not i % 150000000:
            print("\033[36mProcessing line " + str(i) + " of CANVA_FULL_CLEANED.txt ...\033[0m")

        if len(parts) >= 22:
            email = parts[3]
            username = parts[6]
            passwordHash = parts[21]

            if not email and not username and not passwordHash:
                continue

            # Source, Date, username, email, password, hash
            writer.writerow(["CANVA_FULL_CLEANED.txt", "NULL", username, email, "NULL", passwordHash])

    end = time.time()
    print(f"\033[32mSuccess, completed in {round(end - start, 4)} sec.\033[0m")

    inputFile.close()
    outputFile.close()

# Check if it's a date with the format YYYY-MM-DD
def checkDate(line):
    if "-" in line:
        parts = line.split("-")
        
        if len(parts) == 3:
            year, month, day = parts
            if len(year) == 4 and len(month) == 2 and len(day) == 2:
                if year.isdigit() and month.isdigit() and day.isdigit():
                    if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                        return True
                    else:
                        return False

def main():
    options = {
        "i": process_all_individual,
        "m": process_all,
        "I": process_all_individual,
        "M": process_all,
        "1": process_1_5_m_poland_combolist,
        "2": process_1500000_data_random_websites,
        "3": process_3_5mlnPLmailpass,
        "4": process_agusiq_torrents_dump,
        "5": process_blogplay_users_dump,
        "6": process_cdprojectred,
        "7": process_combo_2023,
        "8": process_combo_2024,
        "9": process_daniel_hosting,
        "10": process_electroworld,
        "11": process_inpost,
        "12": process_ledger,
        "13": process_pl2023_dump,
        "14": process_torepublic,
        "15": process_wakacjepl_forum,
        "16": process_zapiszjakopl,
        "17": process_badoo,
        "18": process_sample_txt,
        "19": process_tiktok,
        "20": process_westernunion_com,
        "21": process_dehashed_database,
        "22": process_canva_full_cleaned
    }
    
    print("Choose a file to process:\n")
    print("\033[33;1mM\033[0m: \033[3mEverything Merged\033[0m")
    print("\033[33;1mI\033[0m: \033[3mEverything Individual\033[0m")
    print("\033[33;1m1\033[0m: 1.5M POLAND GOOD QUALITY COMBOLIST.txt")
    print("\033[33;1m2\033[0m: 1500000_data_random_websites.txt")
    print("\033[33;1m3\033[0m: 3.5mlnPLmailpass.txt")
    print("\033[33;1m4\033[0m: dump-agusiq-torrents.txt")
    print("\033[33;1m5\033[0m: bp-blogplay-users-dump.txt")
    print("\033[33;1m6\033[0m: cdprojectred.txt")
    print("\033[33;1m7\033[0m: combo_rez_2023.txt")
    print("\033[33;1m8\033[0m: combo_rez_2024.txt")
    print("\033[33;1m9\033[0m: daniel_hosting.txt")
    print("\033[33;1m10\033[0m: Electroworld.txt")
    print("\033[33;1m11\033[0m: inpost.txt")
    print("\033[33;1m12\033[0m: Ledger*.txt")
    print("\033[33;1m13\033[0m: pl2023_dump.txt")
    print("\033[33;1m14\033[0m: forum-torepublic.txt")
    print("\033[33;1m15\033[0m: wakacje_pl_forum_dump.txt")
    print("\033[33;1m16\033[0m: zapiszjako.pl_poczatek2016.txt")
    print("\033[33;1m17\033[0m: Badoo.txt")
    print("\033[33;1m18\033[0m: sample.txt")
    print("\033[33;1m19\033[0m: tiktok_com_logpass.txt")
    print("\033[33;1m20\033[0m: westernunion_com.txt")
    print("\033[33;1m21\033[0m: All files in Dehashed Database directory")
    print("\033[33;1m22\033[0m: CANVA_FULL_CLEANED.txt")
    
    choice = input("\n\033[33;1mEnter your choice: \033[0m")
    
    if choice in options:
        options[choice]()
    else:
        print("\033[31mInvalid choice. Please enter a valid number.\033[0m")

if __name__ == '__main__':
    main()