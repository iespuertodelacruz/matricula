STUDENT_DATA = {
    "name": "Nombre largo Pero Muy Largo",
    "surname": "Apellido Bastante Largo",
    "nif": "12345678y",
    "nie": "",
    "passport": "",
    "gender": "M",
    "home_phone": "",
    "mobile_phone": "555555555",
    "email": "test@test.com",
    "birth_date": "1/6/2005",
    "birth_country": "Spain and More Things Here",
    "birth_province": "Testing very Laaarge",
    "birth_town": "Puerto de la Cruz Y de los Muelles",
    "nationality": "Spanish",
    "social_security_number": "",
    "address": "Street Chrome, 10",
    "zipcode": "54321",
    "hometown": "Puerto de la Cruz",
    "lastyear_institution": "IES Puerto de la Cruz - Telesforo Bravo",
    "lastyear_studies": "Computing"
}

RESPONSIBLE_DATA = {
    "1": {
        "name": "Frank ahora pongo un nombre que no cabe",
        "surname": "Mayer esto es un super apellido larguísimo",
        "link": "PAD",
        "nif": "12345678Y",
        "nie": "",
        "passport": "",
        "gender": "H",
        "mobile_phone": "555555555",
        "email": "test@test.com",
        "birth_date": "1/6/1984",
        "job": "Carpintero pero además Informático y también otras cosas",
        "separated": False,
        "parental_auth": True,
        "children_custody": False
    },
    "2": {
        "ignore_info": False,
        "name": "Andrea",
        "surname": "Magnet Press",
        "link": "MAD",
        "nif": "12345678Y",
        "nie": "",
        "passport": "",
        "gender": "M",
        "mobile_phone": "555555555",
        "email": "test@test.com",
        "birth_date": "1/6/1985",
        "job": "Scientist",
        "separated": False,
        "parental_auth": True,
        "children_custody": True
    }
}

ACADEMIC_DATA = {
    "1ESO": {
        "global": {
            "specific_subject1": "VAO",
            "specific_subject2": "SGN"
        }
    },
    "1PMAR": {
        "global": {
            "specific_subject": "VAO",
        }
    },
    "2ESO": {
        "global": {
            "specific_subject1": "VAO",
            "specific_subject2": "SGN"
        }
    },
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
            "specific_subject1_order3": "MTA",
            "specific_subject1_order4": "FOT",
            "specific_subject1_order5": "MYS",
            "specific_subject1_order6": "TLA",
            "specific_subject1_order7": "RLG",
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
            "specific_subject1_order3": "MTA",
            "specific_subject1_order4": "FOT",
            "specific_subject1_order5": "MYS",
            "specific_subject1_order6": "TLA",
            "specific_subject1_order7": "RLG",
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
    },
    "1FPB": {
        "global": {
            "topic": "FPB"
        }
    },
    "2FPB": {
        "global": {
            "topic": "FPB"
        }
    },
    "1CFGM": {
        "global": {
            "topic": "ELE",
            "remarks": """
Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de
texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde
el año 1500, cuando un impresor (N. del T. persona que se dedica a la
imprenta) desconocido usó una galería de textos y los mezcló de tal manera que
logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino
que tambien ingresó como texto de relleno en documentos electrónicos,
quedando esencialmente igual al original. Fue popularizado en los 60s con la
creación de las hojas "Letraset", las cuales contenian pasajes de Lorem
Ipsum, y más recientemente con software de autoedición, como por ejemplo Aldus
PageMaker, el cual incluye versiones de Lorem Ipsum.
            """,
            "access_via": "TEC"
        }
    },
    "2CFGM": {
        "global": {
            "topic": "TEL",
            "remarks": """
Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de
texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde
el año 1500, cuando un impresor (N. del T. persona que se dedica a la
imprenta) desconocido usó una galería de textos y los mezcló de tal manera que
logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino
que tambien ingresó como texto de relleno en documentos electrónicos,
quedando esencialmente igual al original. Fue popularizado en los 60s con la
creación de las hojas "Letraset", las cuales contenian pasajes de Lorem
Ipsum, y más recientemente con software de autoedición, como por ejemplo Aldus
PageMaker, el cual incluye versiones de Lorem Ipsum.
            """,
        }
    },
    "1CFGS": {
        "global": {
            "topic": "ASR",
            "remarks": """
Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de
texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde
el año 1500, cuando un impresor (N. del T. persona que se dedica a la
imprenta) desconocido usó una galería de textos y los mezcló de tal manera que
logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino
que tambien ingresó como texto de relleno en documentos electrónicos,
quedando esencialmente igual al original. Fue popularizado en los 60s con la
creación de las hojas "Letraset", las cuales contenian pasajes de Lorem
Ipsum, y más recientemente con software de autoedición, como por ejemplo Aldus
PageMaker, el cual incluye versiones de Lorem Ipsum.
            """,
            "access_via": "TEC"
        }
    },
    "2CFGS": {
        "global": {
            "topic": "GIT",
            "remarks": """
Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de
texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde
el año 1500, cuando un impresor (N. del T. persona que se dedica a la
imprenta) desconocido usó una galería de textos y los mezcló de tal manera que
logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino
que tambien ingresó como texto de relleno en documentos electrónicos,
quedando esencialmente igual al original. Fue popularizado en los 60s con la
creación de las hojas "Letraset", las cuales contenian pasajes de Lorem
Ipsum, y más recientemente con software de autoedición, como por ejemplo Aldus
PageMaker, el cual incluye versiones de Lorem Ipsum.
            """,
        }
    },
    "3CFGS": {
        "global": {
            "topic": "DAM",
            "remarks": """
Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de
texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde
el año 1500, cuando un impresor (N. del T. persona que se dedica a la
imprenta) desconocido usó una galería de textos y los mezcló de tal manera que
logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino
que tambien ingresó como texto de relleno en documentos electrónicos,
quedando esencialmente igual al original. Fue popularizado en los 60s con la
creación de las hojas "Letraset", las cuales contenian pasajes de Lorem
Ipsum, y más recientemente con software de autoedición, como por ejemplo Aldus
PageMaker, el cual incluye versiones de Lorem Ipsum.
            """,
        }
    },
}

AUTH_DATA = {
    "pick": {
        "nif1": "12345678Y",
        "long_name1": "Pepe Sánchez Marrero",
        "nif2": "87654321H",
        "long_name2": "Antonio Con un Apellido Largo",
        "nif3": "77777777T",
        "long_name3": "Mary The Long Surname",
        "nif4": "22222222R",
        "long_name4": "Camile Boris Juvenil",
    },
}

EXTRA_DATA = {
    "auth_image_use": True,
    "has_health_problem": True,
    "health_problem": """El síndrome de Asperger (SA) es un conjunto de
características mentales y
conductuales que forma parte de los trastornos del espectro autista.
Se encuadra dentro de los trastornos generalizados del desarrollo
(CIE-10; Capítulo V; F84). La persona afectada muestra dificultades,
de gravedad variable, en la interacción social y en la comunicación, así como
actividades e intereses en áreas que suelen ser muy restringidas y en muchos
casos estereotipias.
Se diferencia del autismo infantil temprano que describió Leo Kanner y de otras
formas menos específicas en que en el trastorno de Asperger no se observa
retraso en el desarrollo del lenguaje, y no existe una perturbación
clínicamente significativa en su adquisición. No hay retardo, por ejemplo, en
la edad en que aparecen las primeras palabras y frases, aunque pueden existir
particularidades cualitativas (por ejemplo, gramaticales) que llamen la
atención, así como una preservación generalizada de la inteligencia.
    """
}
