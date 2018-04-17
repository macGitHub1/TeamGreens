# Import Dependencies
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Import our data into pandas from CSV
OR_string = 'OR_marijuna_sales_tax_revenue_2016-2018.csv'
OR_sales_df = pd.read_csv(OR_string)

# Import our data into pandas from CSV
CO_string = 'CO_marijuana_tax_revenue_2010-2015.csv'
CO_sales_df = pd.read_csv(CO_string)

# Import our data into pandas from CSV
WA_string = 'WA_marijuana_sales_tax_revenue_FY2015-2018.csv'
WA_sales_df = pd.read_csv(WA_string)

def runOrg():
    # Create empty list for years and totals (recreatioanl use) - OR
    OR_local_totals_list = []
    OR_state_totals_list = []
    OR_years_list = []
    OR_local_years_list = []

    # Create a group based on the values in the 'year' column
    OR_year_group = OR_sales_df.groupby('year')

    # Create a group based on the values in the 'year' column
    OR_state_tax_group = OR_sales_df.groupby("state_tax_received")

    # Generate the sum of state sales by year
    OR_state_sales_2018 = OR_sales_df.loc[(OR_sales_df["year"] == 2018)]
    OR_state_totals_list.append(OR_state_sales_2018["state_tax_received"].sum())

    OR_years_list.append(2018)
    # Create a dataframe for the for Years and Totals
    OR_state_summary_table = pd.DataFrame({"Years":OR_years_list, "Totals":OR_state_totals_list})

    # Format totals into $$ by thousands
    OR_state_summary_table["Totals"] = OR_state_summary_table["Totals"].map("${:,}".format)

    # Generate the sum of state sales by year
    OR_state_sales_2017 = OR_sales_df.loc[(OR_sales_df["year"] == 2017)]
    OR_state_totals_list.append(OR_state_sales_2017["state_tax_received"].sum())
    OR_years_list.append(2017)

    # Create a dataframe for the for Years and Totals
    OR_state_summary_table = pd.DataFrame({"Years":OR_years_list, "Totals":OR_state_totals_list})

    # Generate the sum of state sales by year
    OR_state_sales_2016 = OR_sales_df.loc[(OR_sales_df["year"] == 2016)]
    OR_state_totals_list.append(OR_state_sales_2016["state_tax_received"].sum())
    OR_years_list.append(2016)

    # Create a dataframe for the for Years and Totals
    state_summary_table = pd.DataFrame({"Years":OR_years_list, "Totals":OR_state_totals_list})
    OR_years_list

    # Create a bar chart based on "Totals" and "Years" for recreational use under special taxes
    OR_state_sales_chart = plt.bar(OR_state_summary_table["Years"], OR_state_summary_table["Totals"])

    # Set the xlabel and ylabel using class methods
    plt.xlabel("Years Revenue Reported")
    plt.ylabel("State Taxes (in millions)")
    plt.title("State Taxes for Marijuana Sales in Oregon")

    # Create and save figure of results
    plt.savefig('StateMJsalesOR')

    # Plot graph
    plt.show()

def runCO():
    # Create empty list for years and totals (medical use) - CO
    totals_list = []
    years_list = []

    # Create empty list for years and totals (special recreational use) - CO
    spec_rec_totals_list = []
    spec_rec_years_list = []

    # Create empty list for years and totals (recreatioanl use) - CO
    rec_totals_list = []
    rec_years_list = []

    # Create a group based on the values in the 'year' column
    year_group = CO_sales_df.groupby("year")

    # Create a group based on the values in the 'year' column
    medical_group = CO_sales_df.groupby("medical_MJ _sales_tax _total")

    # Generate the sum of medical sales by year
    medical_sales_2015 = CO_sales_df.loc[(CO_sales_df["year"] == 2015)]
    totals_list.append(medical_sales_2015["medical_MJ _sales_tax _total"].sum())
    years_list.append(2015)

    # Generate the sum of medical sales by year
    medical_sales_2014 = CO_sales_df.loc[(CO_sales_df["year"] == 2014)]
    totals_list.append(medical_sales_2014["medical_MJ _sales_tax _total"].sum())
    years_list.append(2014)

    # Generate the sum of medical sales by year
    medical_sales_2013 = CO_sales_df.loc[(CO_sales_df["year"] == 2013)]
    totals_list.append(medical_sales_2013["medical_MJ _sales_tax _total"].sum())
    years_list.append(2013)

    # Generate the sum of medical sales by year
    medical_sales_2012 = CO_sales_df.loc[(CO_sales_df["year"] == 2012)]
    totals_list.append(medical_sales_2012["medical_MJ _sales_tax _total"].sum())
    years_list.append(2012)

    # Generate the sum of medical sales by year
    medical_sales_2011 = CO_sales_df.loc[(CO_sales_df["year"] == 2011)]
    totals_list.append(medical_sales_2011["medical_MJ _sales_tax _total"].sum())
    years_list.append(2011)

    # Generate the sum of medical sales by year
    medical_sales_2010 = CO_sales_df.loc[(CO_sales_df["year"] == 2010)]
    totals_list.append(medical_sales_2010["medical_MJ _sales_tax _total"].sum())
    years_list.append(2010)

    # Create a dataframe for the for Years and Totals
    summary_table = pd.DataFrame({"Years":years_list, "Totals":totals_list})

    # Create a bar chart based on "Totals" and "Years"
    sales_chart = plt.bar(summary_table["Years"], summary_table["Totals"])

    # Set the xlabel and ylabel using class methods
    plt.xlabel("Years Revenue Reported")
    plt.ylabel("Total Taxes (in millions)")
    plt.title("Medical Marijuana Sales in Colorado")

    # Create and save figure of results
    plt.savefig('medicalMJsalesCO')

    # Plot graph
    plt.show()

    # Generate the sum of recreational sales by year
    spec_rec_sales_2015 = CO_sales_df.loc[(CO_sales_df["year"] == 2015)]
    spec_rec_totals_list.append(spec_rec_sales_2015["special_retail_sales_tax_rate_ONLY"].sum())
    spec_rec_years_list.append(2015)

    # Generate the sum of recreational sales by year
    spec_rec_sales_2014 = CO_sales_df.loc[(CO_sales_df["year"] == 2014)]
    spec_rec_totals_list.append(spec_rec_sales_2014["special_retail_sales_tax_rate_ONLY"].sum())
    spec_rec_years_list.append(2014)

    # Create a dataframe for the for Years and Totals
    spec_rec_summary_table = pd.DataFrame({"Years":spec_rec_years_list, "Totals":spec_rec_totals_list})

    # Format totals into $$ by thousands
    spec_rec_summary_table["Totals"] = spec_rec_summary_table["Totals"].map("${:,}".format)

    # Create a bar chart based on "Totals" and "Years" for recreational use under special taxes
    spec_rec_sales_chart = plt.bar(spec_rec_summary_table["Years"], spec_rec_summary_table["Totals"])

    # Set the xlabel and ylabel using class methods
    plt.xlabel("Years Revenue Reported")
    plt.ylabel("Special Taxes (in millions)")
    plt.title("Special Taxed Retail Marijuana Sales in Colorado")

    # Create and save figure of results
    plt.savefig('SpecRecMJsalesCO')

    # Plot graph
    plt.show()

    # Generate the sum of recreational sales by year
    rec_sales_2015 = CO_sales_df.loc[(CO_sales_df["year"] == 2015)]
    rec_totals_list.append(rec_sales_2015["retail_combo_sales_tax_total"].sum())
    rec_years_list.append(2015)

    # Generate the sum of recreational sales by year
    rec_sales_2014 = CO_sales_df.loc[(CO_sales_df["year"] == 2014)]
    rec_totals_list.append(rec_sales_2014["retail_combo_sales_tax_total"].sum())
    rec_years_list.append(2014)

    # Create a dataframe for the for Years and Totals
    rec_summary_table = pd.DataFrame({"Years":rec_years_list, "Totals":rec_totals_list})

    # Format totals into $$ by thousands
    rec_summary_table["Totals"] = rec_summary_table["Totals"].map("${:,}".format)

    # Create a bar chart based on "Totals" and "Years" for recreational use under special taxes
    rec_sales_chart = plt.bar(rec_summary_table["Years"], rec_summary_table["Totals"])

    # Set the xlabel and ylabel using class methods
    plt.xlabel("Years Revenue Reported")
    plt.ylabel("Retail Taxes (in millions)")
    plt.title("Total Retail Taxes for Marijuana Sales in Colorado")

    # Create and save figure of results
    plt.savefig('RecMJsalesCO')

    # Plot graph
    plt.show()

def runWA():
    # Create a bar chart based on "Totals" and "Years" for recreational use under special taxes
    WA_excise_tax_chart = plt.bar(WA_sales_df["FY"], WA_sales_df["excise_tax"])

    # Set the xlabel and ylabel using class methods
    plt.xlabel("Years Revenue Reported")
    plt.ylabel("Excise Taxes (in millions)")
    plt.title("Excise Taxes for Marijuana Sales in Washington")

    # Create and save figure of results
    plt.savefig('ExciseMJsalesWA')

    # Plot graph
    plt.show()