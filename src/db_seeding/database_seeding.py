import sqlite3
import csv
import os
from pathlib import Path


def db_deleter(db_path):
    if os.path.exists(db_path):
        os.remove(db_path)
    else:
        pass


def main():

    parent_folder = str(Path(__file__).resolve().parents[2])
    data_path_db = str(parent_folder +
                       '/data/intermediate/fec_analysis_database.db') 
    data_path_raw = str(parent_folder + '/data/raw/')
    
    # Database Deletion Tool - Comment Out When Not In Use
    # db_deleter(data_path_db)

    conn = sqlite3.connect(data_path_db)
    cur = conn.cursor()

    # Create the table for lobbying bundle
    cur.execute('''CREATE TABLE lobbyist_bundle
               (Committee_Id text, Committee_Name text ,Link_Image text, Committee_Election_State text, Committee_Election_District text, Report_Type text, Receipt_Date text, Coverage_Start_Date text, Coverage_End_Date text, Quarterly_Contribution text, Semi_Annual_Contribution text)''')

    
    # Create the table for independent expenditures
    cur.execute('''CREATE TABLE independent_expenditure
                (cand_id text, cand_name text, spe_id text, spe_nam text, ele_type text, can_office_state text, can_office_dis text, can_office text, cand_pty_aff text, exp_amo text, exp_date text, agg_amo text, sup_opp text, pur text, pay text, file_num text, amndt_ind text, tran_id text, image_num text, receipt_dat text, fec_election_yr text, prev_file_num text, dissem_dt text)''')

    # Raw Files
    file1 = open(data_path_raw + 'lobbyist_bundle.csv', encoding='utf-8')
    
    file2 = open(str(data_path_raw) + 'independent_expenditure_2010.csv')
    file3 = open(str(data_path_raw) + 'independent_expenditure_2012.csv')
    file4 = open(str(data_path_raw) + 'independent_expenditure_2014.csv')
    file5 = open(str(data_path_raw) + 'independent_expenditure_2016.csv')
    file6 = open(str(data_path_raw) + 'independent_expenditure_2018.csv')
    file7 = open(str(data_path_raw) + 'independent_expenditure_2020.csv')
    file8 = open(str(data_path_raw) + 'independent_expenditure_2022.csv')

    independent_files = [file2, file3, file4, file5, file6, file7, file8]

    # Seed Lobbying Data

    seed_file = file1
    rows = csv.reader(seed_file, delimiter=',')
    
    for row in rows:
        cur.execute("INSERT INTO lobbyist_bundle VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", row)
    

    # Seeding Expenditure Data

    for file in independent_files:
        rows = csv.reader(file, delimiter=',')

        for row in rows:
            cur.execute("INSERT INTO independent_expenditure VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", row)

            
    conn.commit()


if __name__ == '__main__':
   main()

