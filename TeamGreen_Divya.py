import requests
import json
import pandas as pd
import seaborn as sns
def run():
    url="https://api.usa.gov/crime/fbi/ucr/estimates/states/"
    page="?page=1&per_page=200&output=json&api_key="
    api_key="iiHnOKfno2Mgkt5AynpvPpUQTEyxE77jo1RU8PIv"
    states=['co','wa','ak','or']
    response=[]
    year=[]
    aggravated_assault=[]
    burglary=[]
    caveats=[]
    homicide=[]
    larceny=[]
    motor_vehicle_theft=[]
    population=[]
    property_crime=[]
    rape_legacy=[]
    robbery=[]
    state_abbr=[]
    violent_crime=[]
    stateList=[]
    for state in states:
            #print(state)
            for i in range(22):
                response = requests.get(url+state+page+api_key).json()
                aggravated_assault.append(response["results"][i]["aggravated_assault"])
                burglary.append(response["results"][i]["burglary"])
                caveats.append(response["results"][i]["caveats"])
                homicide.append(response["results"][i]["homicide"])
                larceny.append(response["results"][i]["larceny"])
                motor_vehicle_theft.append(response["results"][i]["motor_vehicle_theft"])
                property_crime.append(response["results"][i]["property_crime"])
                rape_legacy.append(response["results"][i]["rape_legacy"])
                robbery.append(response["results"][i]["robbery"])
                violent_crime.append(response["results"][i]["violent_crime"])
                year.append(response["results"][i]["year"])
                state_abbr.append(response["results"][i]["state_abbr"])
                population.append(response["results"][i]["population"])
    crime_data = pd.DataFrame({
        "state_abbr":state_abbr,
        "year":year,
        "population":population,
        "aggravated_assault":aggravated_assault,
        "burglary":burglary,
        "homicide":homicide,
        "larceny":larceny,
        "motor_vehicle_theft":motor_vehicle_theft,
        "property_crime":property_crime,
        "rape_legacy":rape_legacy,
        "robbery":robbery,
        "violent_crime":violent_crime
        })
    crime_date_f=crime_data.loc[(crime_data["year"] == 2010)|(crime_data["year"] == 2016)].copy()
    total_Crime=crime_date_f.burglary+crime_date_f.aggravated_assault+ \
    crime_date_f.motor_vehicle_theft \
    +crime_date_f.property_crime+crime_date_f.violent_crime+crime_date_f.robbery+crime_date_f.homicide+ \
    crime_date_f.rape_legacy+crime_date_f.larceny
    crime_data['total_Crime']=total_Crime
    crime_data_long = crime_date_f.melt(id_vars=['state_abbr', 'year'],
                      value_name='Sum',
                        var_name='Crime_types')
    array = ['burglary', 'property_crime','violent_crime','motor_vehicle_theft']
    crime_data_long_1=crime_data_long.loc[crime_data_long["Crime_types"].isin(array)]
    ay = sns.factorplot(x="year", y="Sum",
                    hue="Crime_types", col="state_abbr",
                   data=crime_data_long_1, kind="bar",
                    size=4, aspect=.7);