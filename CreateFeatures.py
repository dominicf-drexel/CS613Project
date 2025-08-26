from typing import List, Tuple

def CategoricalToOperable_SEX(value: str, row: list) -> List[str]:
    row.append(1 if value == "01" else 0)
    row.append(1 if value == "02" else 0)
    row.append(1 if value == "99" else 0)

    fields: list[str] = ["SEX_Male", "SEX_Female", "SEX_NIU (Not in universe)"]
    return fields
def CategoricalToOperable_EDUC(value: str, row: list) -> List[str]:
    row.append(1 if value == "010" else 0)
    row.append(1 if value == "011" else 0)
    row.append(1 if value == "012" else 0)
    row.append(1 if value == "013" else 0)
    row.append(1 if value == "014" else 0)
    row.append(1 if value == "015" else 0)
    row.append(1 if value == "016" else 0)
    row.append(1 if value == "017" else 0)
    row.append(1 if value == "020" else 0)
    row.append(1 if value == "021" else 0)
    row.append(1 if value == "030" else 0)
    row.append(1 if value == "031" else 0)
    row.append(1 if value == "032" else 0)
    row.append(1 if value == "040" else 0)
    row.append(1 if value == "041" else 0)
    row.append(1 if value == "042" else 0)
    row.append(1 if value == "043" else 0)
    row.append(1 if value == "999" else 0)

    fields: list[str] = [
    "EDUC_Less than 1st grade"
    , "EDUC_1st, 2nd, 3rd, or 4th grade"
    , "EDUC_5th or 6th grade"
    , "EDUC_7th or 8th grade"
    , "EDUC_9th grade"
    , "EDUC_10th grade"
    , "EDUC_11th grade"
    , "EDUC_12th grade - no diploma"

    , "EDUC_High school graduate - GED"
    , "EDUC_High school graduate - diploma"

    , "EDUC_Some college but no degree"
    , "EDUC_Associate degree - occupational vocational"
    , "EDUC_Associate degree - academic program"

    , "EDUC_Bachelor's degree (BA, AB, BS, etc.)"
    , "EDUC_Master's degree (MA, MS, MEng, MEd, MSW, etc.)"
    , "EDUC_Professional school degree (MD, DDS, DVM, etc.)"
    , "EDUC_Doctoral degree (PhD, EdD, etc.)"

    , "EDUC_NIU (Not in universe)"
    ]
    return fields

def CategoricalToOperable_EDUCYRS(value: str, row: list) -> List[str]:
    row.append(1 if value == "100" else 0)
    row.append(1 if value == "101" else 0)
    row.append(1 if value == "102" else 0)
    row.append(1 if value == "105" else 0)
    row.append(1 if value == "107" else 0)
    row.append(1 if value == "109" else 0)
    row.append(1 if value == "110" else 0)
    row.append(1 if value == "111" else 0)
    row.append(1 if value == "112" else 0)
    row.append(1 if value == "200" else 0)
    row.append(1 if value == "213" else 0)
    row.append(1 if value == "214" else 0)
    row.append(1 if value == "215" else 0)
    row.append(1 if value == "216" else 0)
    row.append(1 if value == "217" else 0)
    row.append(1 if value == "300" else 0)
    row.append(1 if value == "316" else 0)
    row.append(1 if value == "317" else 0)
    row.append(1 if value == "318" else 0)
    row.append(1 if value == "319" else 0)
    row.append(1 if value == "320" else 0)
    row.append(1 if value == "321" else 0)
    row.append(1 if value == "999" else 0)

    fields: list[str] = [
    "EDUCYRS_Grades 1-12"
    , "EDUCYRS_Less than first grade"
    , "EDUCYRS_First through fourth grade"
    , "EDUCYRS_Fifth through sixth grade"
    , "EDUCYRS_Seventh through eighth grade"
    , "EDUCYRS_Ninth grade"
    , "EDUCYRS_Tenth grade"
    , "EDUCYRS_Eleventh grade"
    , "EDUCYRS_Twelfth grade"

    , "EDUCYRS_College"
    , "EDUCYRS_College--one year"
    , "EDUCYRS_College--two years"
    , "EDUCYRS_College--three years"
    , "EDUCYRS_College--four years"

    , "EDUCYRS_Bachelor's degree"
    , "EDUCYRS_Advanced degree"
    , "EDUCYRS_Master's degree"
    , "EDUCYRS_Master's degree--one year program"
    , "EDUCYRS_Master's degree--two year program"
    , "EDUCYRS_Master's degree--three+ year program"
    , "EDUCYRS_Professional degree"
    , "EDUCYRS_Doctoral degree"

    , "EDUCYRS_NIU (Not in universe)"
    ]
    return fields

def CategoricalToOperable_SPOUSEPRES(value: str, row: list) -> List[str]:
    row.append(1 if value == "01" else 0)
    row.append(1 if value == "02" else 0)
    row.append(1 if value == "03" else 0)
    row.append(1 if value == "99" else 0)

    fields: list[str] = [
    "SPOUSEPRES_Spouse present"
    , "SPOUSEPRES_Unmarried partner present"
    , "SPOUSEPRES_No spouse or unmarried partner present"
    , "SPOUSEPRES_NIU (Not in universe)"
    ]
    return fields

def CategoricalToOperable_SPUSUALHRS(value: str, row: list) -> List[str]:
    row.append(0 if value in ["995", "999"] else int(value))
    row.append(1 if value == "995" else 0)
    row.append(1 if value == "999" else 0)

    fields: list[str] = [
    "SPUSUALHRS"
    , "SPUSUALHRS_Hours vary"
    , "SPUSUALHRS_NIU (Not in universe)"
    ]
    return fields

def CategoricalToOperable_QSPUSUALHRS(value: str, row: list) -> List[str]:
    row.append(1 if value == "000" else 0)
    row.append(1 if value == "011" else 0)
    row.append(1 if value == "998" else 0)
    row.append(1 if value == "999" else 0)

    fields: list[str] = [
    "QSPUSUALHRS_Value - no change"
    , "QSPUSUALHRS_Blank to value"
    , "QSPUSUALHRS_Blank"
    , "QSPUSUALHRS_NIU (Not in universe)"
    ]
    return fields
def CategoricalToOperable_QEDUC(value: str, row: list) -> List[str]:
    row.append(1 if value == "000" else 0)
    row.append(1 if value == "001" else 0)
    row.append(1 if value == "021" else 0)
    row.append(1 if value == "022" else 0)
    row.append(1 if value == "023" else 0)
    row.append(1 if value == "041" else 0)
    row.append(1 if value == "042" else 0)
    row.append(1 if value == "043" else 0)
    row.append(1 if value == "050" else 0)
    row.append(1 if value == "052" else 0)
    row.append(1 if value == "053" else 0)
    row.append(1 if value == "999" else 0)

    fields: list[str] = [
    "QEDUC_Value - no change"
    , "QEDUC_Blank - no change"
    , "QEDUC_Blank to longitudinal value"
    , "QEDUC_Don't know to longitudinal value"
    , "QEDUC_Refused to longitudinal value"
    , "QEDUC_Blank to allocated value"
    , "QEDUC_Don't know to allocated value"
    , "QEDUC_Refused to allocated value"
    , "QEDUC_Value to blank"
    , "QEDUC_Don't know to blank"
    , "QEDUC_Refused to blank"
    , "QEDUC_NIU (Not in universe)"
    ]
    return fields

def CategoricalToOperable_QAGE(value: str, row: list) -> List[str]:
    row.append(1 if value == "000" else 0)
    row.append(1 if value == "002" else 0)
    row.append(1 if value == "003" else 0)
    row.append(1 if value == "011" else 0)
    row.append(1 if value == "020" else 0)
    row.append(1 if value == "021" else 0)
    row.append(1 if value == "022" else 0)
    row.append(1 if value == "023" else 0)
    row.append(1 if value == "041" else 0)
    row.append(1 if value == "042" else 0)
    row.append(1 if value == "043" else 0)
    row.append(1 if value == "060" else 0)
    row.append(1 if value == "999" else 0)

    fields: list[str] = [
    "QAGE_Value - no change"
    , "QAGE_Don't know - no change"
    , "QAGE_Refused - no change"
    , "QAGE_Blank to value"
    , "QAGE_Value to longitudinal value"
    , "QAGE_Blank to longitudinal value"
    , "QAGE_Don't know to longitudinal value"
    , "QAGE_Refused to longitudinal value"
    , "QAGE_Blank to allocated value"
    , "QAGE_Don't know to allocated value"
    , "QAGE_Refused to allocated value"
    , "QAGE_Topcoded"
    , "QAGE_NIU (Not in universe)"
    ]
    return fields

def CategoricalToOperable_QSEX(value: str, row: list) -> List[str]:
    row.append(1 if value == "000" else 0)
    row.append(1 if value == "001" else 0)
    row.append(1 if value == "002" else 0)
    row.append(1 if value == "011" else 0)
    row.append(1 if value == "012" else 0)
    row.append(1 if value == "013" else 0)
    row.append(1 if value == "022" else 0)
    row.append(1 if value == "023" else 0)
    row.append(1 if value == "041" else 0)
    row.append(1 if value == "042" else 0)
    row.append(1 if value == "043" else 0)
    row.append(1 if value == "050" else 0)
    row.append(1 if value == "052" else 0)
    row.append(1 if value == "053" else 0)
    row.append(1 if value == "998" else 0)
    row.append(1 if value == "999" else 0)

    fields: list[str] = [
    "QSEX_Value - no change"
    , "QSEX_Blank - no change"
    , "QSEX_Don't know - no change"
    , "QSEX_Blank to value"
    , "QSEX_Don't know to value"
    , "QSEX_Refused to value"
    , "QSEX_Don't know to longitudinal value"
    , "QSEX_Refused to longitudinal value"
    , "QSEX_Blank To Allocated Value"
    , "QSEX_Don't Know To Allocated Value"
    , "QSEX_Refused To Allocated Value"
    , "QSEX_Value To Blank"
    , "QSEX_Don’t know to blank"
    , "QSEX_Refused to blank"
    , "QSEX_Blank"
    , "QSEX_NIU (Not in universe)"
    ]
    return fields

def CategoricalToOperable_QEDUCYRS(value: str, row: list) -> List[str]:
    row.append(1 if value == "00" else 0)
    row.append(1 if value == "01" else 0)
    row.append(1 if value == "99" else 0)

    fields: list[str] = [
    "QEDUCYRS_Not allocated"
    , "QEDUCYRS_Allocated"
    , "QEDUCYRS_NIU (Not in universe)"
    ]
    return fields




def ConsolidatedCategoricalToOperable_EDUC(value: str, row: list) -> List[str]:
    row.append(1 if value in ["010", "011", "012", "013", "014", "015", "016", "017"] else 0)
    row.append(1 if value in ["020", "021"] else 0)
    row.append(1 if value in ["030"] else 0)
    row.append(1 if value in ["031", "032"] else 0)
    row.append(1 if value in ["040"] else 0)
    row.append(1 if value in ["041", "042", "043"] else 0)
    row.append(1 if value == "999" else 0)

    fields: list[str] = [
    "EDUC_Less than HS Graduate"
    , "EDUC_High school graduate"
    , "EDUC_Some college"
    , "EDUC_Associate degree"
    , "EDUC_Bachelor's degree"
    , "EDUC_Graduate or Professional degree"

    , "EDUC_NIU (Not in universe)"
    ]
    return fields


def CategoricalToOperable(fieldname: str, value: str, row: list) -> List[str] | None:
    if (fieldname.casefold() == "SEX".casefold()):
        return CategoricalToOperable_SEX(value, row)
    elif (fieldname.casefold() == "EDUC".casefold()):
        return ConsolidatedCategoricalToOperable_EDUC(value, row)
    elif (fieldname.casefold() == "EDUCYRS".casefold()):
        return CategoricalToOperable_EDUCYRS(value, row)
    elif (fieldname.casefold() == "SPOUSEPRES".casefold()):
        return CategoricalToOperable_SPOUSEPRES(value, row)
    elif (fieldname.casefold() == "SPUSUALHRS".casefold()):
        return CategoricalToOperable_SPUSUALHRS(value, row)
    elif (fieldname.casefold() == "QSPUSUALHRS".casefold()):
        return CategoricalToOperable_QSPUSUALHRS(value, row)
    elif (fieldname.casefold() == "QEDUC".casefold()):
        return CategoricalToOperable_QEDUC(value, row)
    elif (fieldname.casefold() == "QAGE".casefold()):
        return CategoricalToOperable_QAGE(value, row)
    elif (fieldname.casefold() == "QSEX".casefold()):
        return CategoricalToOperable_QSEX(value, row)
    elif (fieldname.casefold() == "QEDUCYRS".casefold()):
        return CategoricalToOperable_QEDUCYRS(value, row)

    else:
        return None

def ContinuousToCategorical_AGE(value: str, row: list) -> List[str]:
    intvalue: int = -1
    try:
        intvalue = int(value)
    except:
        raise Exception()
    
    breaks: list[int] = [
         5,
        10,
        15,
        20,
        25,
        30,
        35,
        40,
        45,
        50,
        55,
        60,
        65,
        70,
        75,
        80,
        85,
    ]

    fields: list[str] = []
    prev: int = 0
    for i in range(len(breaks)):
        fieldvalue: int = 1 if intvalue >= prev and intvalue <= breaks[i] else 0
        fieldlabel: str = f"Age: {prev} to {breaks[i]}"
        row.append(fieldvalue)
        fields.append(fieldlabel)
        prev = breaks[i]

    lastfieldvalue: int = 1 if intvalue >= prev else 0
    lastfieldlabel: str = f"Age: {prev} and over"
    row.append(lastfieldvalue)
    fields.append(lastfieldlabel)

    return fields

def ContinuousToCategorical(fieldname: str, value: str, row: list) -> List[str] | None:
    if (fieldname.casefold() == "AGE".casefold()):
        return ContinuousToCategorical_AGE(value, row)
    else:
        return None

def TransformIntoFeatures(rowdata: list[list[str]], columnnames: list[str]) -> Tuple[list[list[str]], list[str]]:
    readyrows: list = []
    readycolumnnames: list = []

    for i in range(len(rowdata)):
        newrow = []

        for j in range(len(columnnames)):
            value = rowdata[i][j]
            columnname: str = columnnames[j]

            createdcolumns: list[str] | None = None
            
            createdcolumns = CategoricalToOperable(columnname, value, newrow)
            if (createdcolumns is not None):
                readycolumnnames.extend(createdcolumns)
                continue
    
            createdcolumns = ContinuousToCategorical(columnname, value, newrow)
            if (createdcolumns is not None):
                readycolumnnames.extend(createdcolumns)
                continue

            newrow.append(float(0 if value == "" else value))

            fields: list[str] = [columnname]
            readycolumnnames.extend(fields)

        readyrows.append(newrow)

    return (readyrows, readycolumnnames)
