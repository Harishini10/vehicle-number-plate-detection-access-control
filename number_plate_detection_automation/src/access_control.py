ALLOWED_PLATES = {
    "TS07FK4521",
    "DL04CE8890",
    "AP31BR6723",
    "GJ01HP4432",
    "UP32KT9045",
    "RJZCVO00",
    "TAV3657",
    "WB24ED3311",
    "KL07CM9022",
    "DL7CO1939",
    "TN10BU4453",
    "HR26DK8337",
    "MH14GT9981",
    "RJ20UA5576",
    "OD05CL2349",
    "CG04JR6678",
    "MP09CZ1123",
    "JK02BM4590",
    "AS01EC7744",
    "UK07AD7651"
}

def check_access(plate_text):
    if plate_text in ALLOWED_PLATES:
        return "ACCESS GRANTED"
    else:
        return "ACCESS DENIED"
