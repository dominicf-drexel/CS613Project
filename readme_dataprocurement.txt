IPUMS Microdata project (https://www.ipums.org/)

This data is from the American Time Use Survey (ATUS), a time diary survey funded by the US Bureau of Labor Statistics (BLS) and fielded by the US Census Bureau.

Data extracts can only be downloaded from valid login sessions. A login can be created here:
https://uma.pop.umn.edu/atus/user/new

Data extracts must be specified through the online survey builder tool:
https://www.atusdata.org/atus-action/variables/group

Microdata consists of data presented at the individual level (as opposed to summary data).
The survey builder tool lets the user choose the features to study, corrective weights, and types of time use variables.

Features are categorized by type, and can relate to:
individual
individual and household members
individual and household members at the time of the CPS interview (before the survey)
households

Features may contain data quality flags: indicators that edits were made for missing, illegible or inconsistent values.
These can be found by:
Clicking the hyperlink for the feature, then:
Choosing the Flags section, then:
Clicking on the data quality flag field hyperlink, then:
Add to Cart

Weights are corrective, and adjust for:
overrepresentation of people and households with certain characteristics
oversampling of weekend diary information vs. weekday
differences in response rates among demographic groups and days of the week

Time use variables describe certain activities/filters. They show the number of minutes in a 24-hour period that the respondant engaged in the particular activity.
These can be further refined by:
where/when the activity took place
actively caring for children during the activity
eating or drinking during the activity
providing eldercare during the activity
who else was with them during the activity

Further, the extract will contain fields describing the data year(s) and identification information for joining to other extracts:
YEAR: survey year of data
CASEID: identifier unique to each household
SERIAL: identifier unique to each respondent
PERNUM: identifier unique to each person in a respondent's household
LINENO: identifier unique to each person in a respondent's household at the time of the interview


Example dataset:
Years:
2020
2021
2022
2023
2024

Features:
Person->Core Demographic->Core Demographic->AGE: Age
Person->Core Demographic->Core Demographic->SEX: Sex
Person->Education->Education->EDUC: Highest level of school completed
Person->Education->Education->EDUCYRS: Years of education
Person->Spouse Characteristic->Spouse Characteristic->SPOUSEPRES: Spouse or unmarried partner in household
Person->Spouse Characteristic->Spouse Characteristic->SPUSUALHRS: Usual work hours (spouse or partner)
Person->Spouse Characteristic->Spouse Characteristic->SPEARNWEEK: weekly earnings (spouse or partner)

Data Quality Flags:
QSPUSUALHRS
QEDUC
QAGE
QSEX
QEDUCYRS

Weights:
Person->Weights->Weights->WT06: Person Weight, 2006 methodology
Person->Weights->Weights->WT20: Person Weight, 2020 methodology

Variables:
ACT_CAREHH: Caring for and Helping Household members
ACT_EDUC: Educational activities
ACT_FOOD: Eat and drinking
ACT_HHACT: Household activities
ACT_HHSERV: Household services
ACT_PCARE: Personal care
ACT_PROFSERV: Professional and personal care services
ACT_PURCH: Consumer purchases
ACT_RELIG: Religions and spiritual activities
ACT_SOCIAL: Socializing, relaxing, and leisure
ACT_SPORTS: Sports, exercise, and recreation
ACT_WORK: Working and Work-related Activities

