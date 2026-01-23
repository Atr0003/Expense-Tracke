class INVALID_AMOUNT(Exception):
    code = "INVALID_AMOUNT"
    message = "Le montant doit être strictement positif"
    field = "amount"

class INVALID_CATEGORY(Exception):
    code = "INVALID_CATEGORY"
    message = "La catégorie fournie n'est pas valide"
    field = "category"

class INVALID_DATE(Exception):
    code = "INVALID_DATE"
    message = "La date fournie n'est pas valide"
    field = "date"

class INVALID_DESCRIPTION(Exception):
    code = "INVALID_DESCRIPTION"
    message = "La description fournie n'est pas valide"
    field = "description"

