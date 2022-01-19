from pathlib import Path
import sqlite3
import csv


# Connect to Database
def sql_connector(db_name):
    conn = sqlite3.connect(db_name)

    return conn


def main():
    data_path_db = str(Path('data/intermediate/fec_analysis_data.db'))
    data_path_raw = Path('/data/raw/')

    conn = sqlite3.connect(data_path_db)
    cur = conn.cursor()

    # Create the table for lobbying bundle
    cur.execute('''CREATE TABLE lobbyist_bundle
               (Committee_Id text, Committee_Name text ,Link_Image text, Committee_Election_State text, Committee_Election_District text, Report_Type text, Receipt_Date text, Coverage_Start_Date text, Coverage_End_Date text, Quarterly_Contribution text, Semi_Annual_Contribution text)''')

    
    # Create the table for independent expenditures
    cur.execute('''CREATE TABLE independent_expenditure
                (cand_id text, cand_name text, spe_id text, spe_nam text, ele_type text, can_office_state text, can_office_dis text, can_office text, cand_pty_aff text, exp_amo text, exp_date text, agg_amo text, sup_opp text, pur text, pay text, file_num text, amndt_ind text, tran_id text, image_num text, receipt_dat text, fec_election_yr text, prev_file_num text, dissem_dt text)''')

    # Raw Files
    file1 = open(str(data_path_raw) + '/lobbyist_bundle.csv')
    
    file2 = open(str(data_path_raw) + 'independent_expenditure_2010.csv')
    file3 = open(str(data_path_raw) + 'independent_expenditure_2012.csv')
    file4 = open(str(data_path_raw) + 'independent_expenditure_2014.csv')
    file5 = open(str(data_path_raw) + 'independent_expenditure_2016.csv')
    file6 = open(str(data_path_raw) + 'independent_expenditure_2018.csv')
    file7 = open(str(data_path_raw) + 'independent_expenditure_2020.csv')
    file8 = open(str(data_path_raw) + 'independent_expenditure_2022.csv')


    # Seed Lobbying Data

    seed_file = open(file1)
    rows = csv.reader(seed_file)

    cur.executemany("INSERT INTO lobbyist_bundle VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?", rows)


if __name__ == '__main__':
    main()