STUDENT_DATA = {
    "name": "Nombre largo",
    "surname": "Apellido Bastante Largo",
    "nif": "12345678y",
    "nie": "",
    "passport": "",
    "gender": "M",
    "home_phone": "",
    "mobile_phone": "555555555",
    "email": "test@test.com",
    "birth_date": "1/6/2005",
    "birth_country": "Spain",
    "birth_province": "Testing",
    "birth_town": "Puerto de la Cruz",
    "nationality": "Spanish",
    "social_security_number": "",
    "address": "Street Chrome, 10",
    "zipcode": "54321",
    "hometown": "Puerto de la Cruz",
    "lastyear_institution": "IES Puerto de la Cruz - Telesforo Bravo",
    "lastyear_studies": "Computing"
}

RESPONSIBLE1_DATA = {
    "name": "Frank",
    "surname": "Mayer",
    "nif": "12345678Y",
    "nie": "",
    "passport": "",
    "gender": "H",
    "mobile_phone": "555555555",
    "email": "test@test.com",
    "birth_date": "1/6/1984",
    "job": "Carpenter",
    "parental_auth": True,
    "children_custody": False
}

RESPONSIBLE2_DATA = {
    "ignore_info": False,
    "name": "Andrea",
    "surname": "Magnet Press",
    "nif": "12345678Y",
    "nie": "",
    "passport": "",
    "gender": "M",
    "mobile_phone": "555555555",
    "email": "test@test.com",
    "birth_date": "1/6/1985",
    "job": "Scientist",
    "parental_auth": True,
    "children_custody": True
}

ACADEMIC_DATA = {
    "2PMAR": {
        "global": {
            "specific_subject1": "VAO",
            "specific_subject2_order1": "EUP",
            "specific_subject2_order2": "MUS",
            "specific_subject2_order3": "IVY",
        }
    },
    "3ESO": {
        "global": {
            "specific_subject1": "VAO",
            "specific_subject2": "SGN",
            "core_subject": "SAA",
            "specific_subject3_order1": "CUC",
            "specific_subject3_order2": "MUS",
            "specific_subject3_order3": "TEE",
            "specific_subject3_order4": "EUP",
            "specific_subject3_order5": "IVY",
        }
    },
    "PostPMAR": {
        "global": {
            "specific_subject1": "VAO",
            "specific_subject2_order1": "SGA",
            "specific_subject2_order2": "AEZ",
            "specific_subject2_order3": "CUF",
            "specific_subject2_order4": "CUC",
            "specific_subject2_order5": "EPV",
            "specific_subject2_order6": "FIL",
            "specific_subject2_order7": "SGN",
            "specific_subject2_order8": "MUS",
            "specific_subject2_order9": "TEE",
            "specific_subject2_order10": "TGD",
            "core_subjects": "CIE+IVY"
        }
    },
    "4ESO": {
        "global": {
            "training_itinerary": "EAC",
            "specific_subject1": "VAO",
            "specific_subject2_order1": "SGA",
            "specific_subject2_order2": "AEZ",
            "specific_subject2_order3": "CUF",
            "specific_subject2_order4": "CUC",
            "specific_subject2_order5": "EPV",
            "specific_subject2_order6": "FIL",
            "specific_subject2_order7": "SGN",
            "specific_subject2_order8": "MUS",
            "specific_subject2_order9": "TEE",
            "specific_subject2_order10": "TGD",
        },
        "itinerary": {
            "EAC": {
                "core_subjects": "BIG+FYQ"
            },
            "EAP": {
                "core_subjects": "CIE+IVY"
            }
        }
    },
    "1CIE": {
        "global": {
            "training_itinerary": "CCS",
            "specific_subject1": "TFY"
        },
        "itinerary": {
            "CCS": {
                "specific_subject2_order1": "CUF",
                "specific_subject2_order2": "SGG",
                "specific_subject2_order3": "SGA",
                "specific_subject2_order4": "TNI",
                "specific_subject2_order5": "DBT",
            },
            "TEC": {
                "specific_subject2_order1": "CUF",
                "specific_subject2_order2": "SGG",
                "specific_subject2_order3": "SGA",
                "specific_subject2_order4": "TNI",
                "specific_subject2_order5": "BIG",
            }
        }
    },
    "1SOC": {
        "global": {
            "training_itinerary": "HUM",
            "specific_subject1": "TFY"
        },
        "itinerary": {
            "HUM": {
                "core_subject_order1": "LIE",
                "core_subject_order2": "GRI",
                "specific_subject2_order1": "CUF",
                "specific_subject2_order2": "SGG",
                "specific_subject2_order3": "SGA",
                "specific_subject2_order4": "ECO",
                "specific_subject2_order5": "DAI",
            },
            "SOC": {
                "specific_subject2_order1": "CUF",
                "specific_subject2_order2": "SGG",
                "specific_subject2_order3": "SGA",
                "specific_subject2_order4": "ECO",
                "specific_subject2_order5": "GRI",
                "specific_subject2_order6": "LIE",
            }
        }
    },
    "2CIE": {
        "global": {
            "training_itinerary": "CCS",
            "specific_subject1_order1": "ACF",
            "specific_subject1_order2": "AYS",
            "specific_subject1_order3": "BIL",
            "specific_subject1_order4": "RLG",
            "specific_subject1_order5": "FOT",
            "specific_subject1_order6": "MYS",
            "specific_subject1_order7": "AST",
            "specific_subject1_order8": "LCA",
            "specific_subject1_order9": "HIC",
            "specific_subject1_order10": "MNC",
        },
        "itinerary": {
            "CCS": {
                "core_subject_order1": "GEO",
                "core_subject_order2": "QUI",
                "specific_subject2_order1": "CTM",
                "specific_subject2_order2": "HFI",
                "specific_subject2_order3": "IYS",
                "specific_subject2_order4": "PSI",
                "specific_subject2_order5": "SGA",
                "specific_subject2_order6": "SGN",
                "specific_subject2_order7": "TFL",
                "specific_subject2_order8": "TII",
                "specific_subject2_order9": "DBT",
            },
            "TEC": {
                "core_subject_order1": "DB2",
                "core_subject_order2": "QUI",
                "specific_subject2_order1": "CTM",
                "specific_subject2_order2": "HFI",
                "specific_subject2_order3": "IYS",
                "specific_subject2_order4": "PSI",
                "specific_subject2_order5": "SGA",
                "specific_subject2_order6": "SGN",
                "specific_subject2_order7": "TFL",
                "specific_subject2_order8": "TII",
                "specific_subject2_order9": "GEO",
            },
        }
    },
    "2SOC": {
        "global": {
            "training_itinerary": "HUM",
            "specific_subject1_order1": "ACF",
            "specific_subject1_order2": "AYS",
            "specific_subject1_order3": "BIL",
            "specific_subject1_order4": "RLG",
            "specific_subject1_order5": "FOT",
            "specific_subject1_order6": "MYS",
            "specific_subject1_order7": "AST",
            "specific_subject1_order8": "LCA",
            "specific_subject1_order9": "HIC",
            "specific_subject1_order10": "MNC",
        },
        "itinerary": {
            "HUM": {
                "core_subject_order1": "GEO",
                "core_subject_order2": "GR2",
                "core_subject_order3": "HFI",
                "core_subject_order4": "HAR",
                "specific_subject2_order1": "DA2",
                "specific_subject2_order2": "FUE",
                "specific_subject2_order3": "HFI",
                "specific_subject2_order4": "HMD",
                "specific_subject2_order5": "PSI",
                "specific_subject2_order6": "SGA",
                "specific_subject2_order7": "SGN",
                "specific_subject2_order8": "TFL",
                "specific_subject2_order9": "ECN",
            },
            "SOC": {
                "core_subject_order1": "ECN",
                "core_subject_order2": "GEO",
                "core_subject_order3": "HFI",
                "specific_subject2_order1": "DA2",
                "specific_subject2_order2": "FUE",
                "specific_subject2_order3": "HFI",
                "specific_subject2_order4": "HMD",
                "specific_subject2_order5": "PSI",
                "specific_subject2_order6": "SGA",
                "specific_subject2_order7": "SGN",
                "specific_subject2_order8": "TFL",
                "specific_subject2_order9": "GR2",
                "specific_subject2_order10": "HAR",
            }
        }
    }
}
