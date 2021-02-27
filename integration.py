import pandas as pd
import pandasql
import seaborn as sns

df = pd.read_csv('acs2017_census_tract_data.csv')
df2 = pd.read_csv('COVID_county_data.csv')
population = 0
poverty_counter = 0
income_counter = 0
counter = 0
previous_county = ""
previous_state = ""
bad = 0

tmp={"State":[], "County":[], "TotalPop":[], "Poverty":[], "PerCapitaIncome":[]}
for index, row in df.iterrows():
    if(index == 0):
        population += row['TotalPop']
        poverty_counter += row['TotalPop']*row['Poverty']
        income_counter += row['IncomePerCap']*row['TotalPop']
        previous_state = row['State']
        previous_county = row['County']
    elif(row['TotalPop'] == 0 or row['Poverty'] == 0 or row['Income'] == 0):
        bad += 1
    elif(previous_county == row['County'] and previous_state == row['State'] and index != 0):
        population += row['TotalPop']
        poverty_counter += row['TotalPop']*(row['Poverty']/100)
        income_counter += row['Income']*row['TotalPop']
    elif (counter == (len(df) -1)):
        if(previous_county == row['County'] and previous_state == row['State']):
            population += row['TotalPop']
            poverty_counter += row['TotalPop']*row['Poverty']
            income_counter += row['IncomePerCap']*row['TotalPop']

            tmp["State"].append(row['State'])
            tmp["County"].append(row['County'])
            tmp["TotalPop"].append(population)
            tmp["Poverty"].append(((poverty_counter/population)*100))
            tmp["PerCapitaIncome"].append((income_counter)/population)
            break;
        else:
            tmp["State"].append(row['State'])
            tmp["County"].append(row['County'])
            tmp["TotalPop"].append(population)
            tmp["Poverty"].append(((poverty_counter/population)*100))
            tmp["PerCapitaIncome"].append((income_counter)/population)
            break;
    else:
        tmp["State"].append(previous_state)
        tmp["County"].append(previous_county)
        tmp["TotalPop"].append(population)
        tmp["Poverty"].append(((poverty_counter/population)*100))
        tmp["PerCapitaIncome"].append((income_counter)/population)

        population = 0 
        poverty_counter = 0
        income_counter = 0

        population += row['TotalPop']
        poverty_counter += row['TotalPop']*(row['Poverty']/100)
        income_counter += row['Income']

        previous_state = row['State']
        previous_county = row['County']

census_data = pd.DataFrame.from_dict(tmp)
for index, row in census_data.iterrows():
    if(row['State'] == "Virginia" and row['County'] == "Loudoun County"):
        print(row)
        print()
    elif(row['State'] == "Oregon" and row['County'] == "Washington County"):
        print(row)
        print()
    elif(row['State'] == "Kentucky" and row['County'] == "Harlan County"):
        print(row)
        print()
    elif(row['State'] == "Oregon" and row['County'] == "Malheur County"):
        print(row)
        print()

tmp2={"county":[], "state":[], "cases":[], "deaths":[], "dec_cases":[], "dec_deaths":[]}
for index, row in df2.iterrows():
    if(index == 0):
        cases += row['cases']

#print(census_data)
