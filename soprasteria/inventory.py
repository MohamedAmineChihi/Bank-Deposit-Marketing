from dataclasses import dataclass


@dataclass
class _COLUMNS:
    date: str = "date"
    variation_emploi: str = "tx_var_emploi"
    indice_prix: str = "idx_prix_conso"
    indice_consommateur: str = "idx_conf_conso"


@dataclass
class _MARKETING_COLUMNS:
    education: str = "education"
    job: str = "job"
    relation: str = "relation"
    contact: str = "contact"
    resultat_derniere_campagne: str = "resultat_derniere_campagne"
    pret_perso: str = "pret_perso"


COLUMNS = _COLUMNS()
MARKETING_COLUMNS = _MARKETING_COLUMNS()
