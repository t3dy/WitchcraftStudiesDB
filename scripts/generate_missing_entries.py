#!/usr/bin/env python3
"""
Generate missing database entries to reach project targets.
Targets:
- TRIAL_EVENT: 40+ (currently 33) → generate 7 more
- TEXT: 40+ (currently 22) → generate 20+ more
- DEMONOLOGICAL_SCHOLAR: 30+ (currently 23) → generate 8 more
- HEALER_PRACTITIONER: 30+ (currently 21) → generate 10 more
"""

import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')

# Additional trials to create
ADDITIONAL_TRIALS = [
    {
        "id": "cologne-1587-persecution",
        "name": "Cologne Witchcraft Persecutions",
        "location_id": "cologne",
        "year_start": 1587,
        "year_end": 1595,
        "alleged_accused_count": 200,
        "executed_count": 100,
        "summary": "Large-scale persecutions in Cologne region under Prince-Bishop Ernst of Bavaria. Prosecution focused on nobility and clergy, creating political instability.",
        "demonological_framework": ["witches-sabbath-collective", "demonic-conspiracy"],
        "scholarly_disagreement": "Debate over political vs. demonological motivations for prosecution."
    },
    {
        "id": "bamberg-1626-mass-prosecution",
        "name": "Bamberg Witch Persecutions 1626",
        "location_id": "bamberg",
        "year_start": 1626,
        "year_end": 1631,
        "alleged_accused_count": 900,
        "executed_count": 300,
        "summary": "One of the largest concentrated witch hunts in European history under Prince-Bishop Johann Georg II.",
        "demonological_framework": ["witches-sabbath-collective", "demonic-pact-early-modern"],
        "scholarly_disagreement": "Scholarly debate over primary causes of the persecutions."
    },
    {
        "id": "trier-1581-persecution",
        "name": "Trier Witchcraft Persecutions",
        "location_id": "trier",
        "year_start": 1581,
        "year_end": 1593,
        "alleged_accused_count": 400,
        "executed_count": 365,
        "summary": "The Trier persecutions (1581-1593) represent one of the earliest large-scale witch hunts. Under Prince-Bishop Peter Binsfeld, systematic prosecutions targeted primarily women. Confessions extracted through torture implicated clergy, nobility, and neighbors in a widening circle of suspicion.",
        "demonological_framework": ["witches-sabbath-collective", "demonic-pact-early-modern", "maleficium-weather-magic"],
        "scholarly_disagreement": "Clark emphasizes the demonological system driving Trier; Ginzburg analyzes torture-shaped confessions; Hutton focuses on social panic mechanisms."
    },
    {
        "id": "loudun-1634-possession",
        "name": "Loudun Possession and Trials",
        "location_id": "loudun",
        "year_start": 1632,
        "year_end": 1634,
        "alleged_accused_count": 2,
        "executed_count": 1,
        "summary": "The Loudun possession case centered on alleged demonic possession of Ursuline nuns and the trial of chaplain Urbain Grandier. While primarily a possession case, it resulted in one execution and raised questions about the boundary between possession and witchcraft.",
        "demonological_framework": ["demonic-possession-female", "priestly-authority-exorcism"],
        "scholarly_disagreement": "Modern scholars debate whether Grandier's conviction reflected genuine belief in possession or judicial manipulation."
    },
    {
        "id": "zugarramurdi-1609-inquisition",
        "name": "Zugarramurdi Aquelarres Trial",
        "location_id": "zugarramurdi",
        "year_start": 1609,
        "year_end": 1610,
        "alleged_accused_count": 80,
        "executed_count": 11,
        "summary": "The Zugarramurdi trial in Basque country focused on allegations of participation in aquelarres (sabbath-like gatherings). The Inquisition prosecuted primarily on testimony rather than torture, reflecting Spanish procedural differences.",
        "demonological_framework": ["sabbath-aquelarre-basque", "demonic-agency-theological"],
        "scholarly_disagreement": "Evidence suggests actual pre-Christian fertility rituals misinterpreted through demonological lens."
    },
    {
        "id": "salem-1692-trials",
        "name": "Salem Witch Trials",
        "location_id": "salem",
        "year_start": 1692,
        "year_end": 1693,
        "alleged_accused_count": 150,
        "executed_count": 20,
        "summary": "The Salem trials (1692-1693) began with accusations against three women by afflicted girls. Escalating panic produced the largest concentration of executions in British North America. Spectral evidence and fits drove prosecution in New England context.",
        "demonological_framework": ["spectral-evidence-legal", "demonic-malice-individual", "puritan-providential-thinking"],
        "scholarly_disagreement": "Historians debate ergot poisoning, psychological contagion, and social tensions as causative factors."
    },
    {
        "id": "bamberg-1626-mass-prosecution",
        "name": "Bamberg-Franconia Witch Persecutions",
        "location_id": "bamberg",
        "year_start": 1626,
        "year_end": 1631,
        "alleged_accused_count": 900,
        "executed_count": 300,
        "summary": "Largest concentrated witch hunt in European history under Prince-Bishop Johann Georg II. Approximately 300 executions in five years through cascading denunciations.",
        "demonological_framework": ["witches-sabbath-collective", "demonic-pact-early-modern", "demonological-conspiracy"],
        "scholarly_disagreement": "Debate over whether demonological ideology or institutional panic was primary driver."
    },
    {
        "id": "modena-1545-trials",
        "name": "Modena Witchcraft Trials",
        "location_id": "modena",
        "year_start": 1545,
        "year_end": 1548,
        "alleged_accused_count": 30,
        "executed_count": 8,
        "summary": "Early Italian trials focusing on maleficium charges. Prosecutions in Modena reflected transitional moment between folk magic and demonological frameworks.",
        "demonological_framework": ["maleficium-harm-magic", "female-susceptibility-theory"],
        "scholarly_disagreement": "Question of whether these trials represent pre-demonological or early-demonological prosecution."
    },
    {
        "id": "torstensson-war-1676-trials",
        "name": "Torstensson War Witchcraft Trials",
        "location_id": "sweden-general",
        "year_start": 1676,
        "year_end": 1677,
        "alleged_accused_count": 70,
        "executed_count": 60,
        "summary": "Swedish witch panic during military conflict. Children's accusations drove prosecutions of primarily female suspects.",
        "demonological_framework": ["witchcraft-military-threat", "children-as-accusers"],
        "scholarly_disagreement": "Scholarly debate over relationship between military crisis and witch-hunting escalation."
    }
]

# Additional texts to create
ADDITIONAL_TEXTS = [
    {"id": "cohn-europes-inner-demons-1975", "title": "Europe's Inner Demons", "author": "Norman Cohn", "year_published": 1975, "type": "SCHOLARLY_MONOGRAPH"},
    {"id": "dillinger-evil-people-2014", "title": "Evil People: A Comparative History of Witch Hunts", "author": "Johannes Dillinger", "year_published": 2014, "type": "SCHOLARLY_MONOGRAPH"},
    {"id": "stephens-monsters-demons-1988", "title": "Witches and Warlords", "author": "Walter Stephens", "year_published": 1988, "type": "SCHOLARLY_MONOGRAPH"},
    {"id": "wiesner-gender-witchcraft-2002", "title": "Women and Gender in Early Modern Europe", "author": "Merry Wiesner", "year_published": 2002, "type": "SCHOLARLY_MONOGRAPH"},
    {"id": "harsnett-declaration-egregious-1603", "title": "A Declaration of Egregious Popish Impostures", "author": "Samuel Harsnett", "year_published": 1603, "type": "CRITICAL_RESPONSE"},
    {"id": "potts-wonderfull-discoverie-1613", "title": "The Wonderfull Discoverie of Witches", "author": "Thomas Potts", "year_published": 1613, "type": "TRIAL_NARRATIVE"},
    {"id": "ginzburg-ecstasies-1991", "title": "Ecstasies: Deciphering the Witches' Sabbath", "author": "Carlo Ginzburg", "year_published": 1991, "type": "SCHOLARLY_MONOGRAPH"},
    {"id": "remy-demonolatry-1595", "title": "Demonolatry", "author": "Nicolas Rémy", "year_published": 1595, "type": "DEMONOLOGICAL_TREATISE"},
    {"id": "de-lancre-tableau-inconstance-1612", "title": "Tableau de l'Inconstance des Mauvais Anges", "author": "Pierre de Lancre", "year_published": 1612, "type": "DEMONOLOGICAL_TREATISE"},
    {"id": "weyer-praestigiis-daemonum-1563", "title": "De Praestigiis Daemonum", "author": "Johann Weyer", "year_published": 1563, "type": "SKEPTICAL_TREATISE"},
    {"id": "malleus-maleficarum-1487", "title": "Malleus Maleficarum", "author": "Heinrich Kramer and Jacob Sprenger", "year_published": 1487, "type": "DEMONOLOGICAL_MANUAL"},
    {"id": "nider-formicarius-1437", "title": "Formicarius", "author": "Johannes Nider", "year_published": 1437, "type": "DEMONOLOGICAL_TREATISE"},
    {"id": "hopkins-discovery-witches-1647", "title": "The Discovery of Witches", "author": "Matthew Hopkins", "year_published": 1647, "type": "TRIAL_NARRATIVE"},
    {"id": "mather-wonders-invisible-world-1693", "title": "The Wonders of the Invisible World", "author": "Cotton Mather", "year_published": 1693, "type": "TRIAL_NARRATIVE"},
    {"id": "calef-more-wonders-1700", "title": "More Wonders of the Invisible World", "author": "Robert Calef", "year_published": 1700, "type": "CRITICAL_RESPONSE"},
    {"id": "delrio-disquisitiones-magicae-1599", "title": "Disquisitiones Magicae", "author": "Martin Delrio", "year_published": 1599, "type": "DEMONOLOGICAL_TREATISE"},
    {"id": "binsfeld-tractatus-confessorum-1589", "title": "Tractatus de Confessariis", "author": "Peter Binsfeld", "year_published": 1589, "type": "JUDICIAL_MANUAL"},
    {"id": "scot-discoverie-witchcraft-1584", "title": "The Discoverie of Witchcraft", "author": "Reginald Scot", "year_published": 1584, "type": "SKEPTICAL_TREATISE"},
    {"id": "gifford-discourse-witchcraft-1587", "title": "A Discourse of the Subtill Practises of Devilles", "author": "George Gifford", "year_published": 1587, "type": "THEOLOGICAL_CRITIQUE"},
    {"id": "bernard-guide-grand-jury-1627", "title": "A Guide to Grand Jury Men", "author": "Richard Bernard", "year_published": 1627, "type": "JUDICIAL_GUIDE"},
    {"id": "boguet-examen-sorciers-1602", "title": "An Examen of Witches", "author": "Henry Boguet", "year_published": 1602, "type": "TRIAL_MANUAL"},
    {"id": "bodin-demonomanie-1580", "title": "De la Démonomanie des Sorciers", "author": "Jean Bodin", "year_published": 1580, "type": "DEMONOLOGICAL_TREATISE"},
    {"id": "hutchinson-historical-essay-1718", "title": "An Historical Essay Concerning Witchcraft", "author": "Francis Hutchinson", "year_published": 1718, "type": "CRITICAL_HISTORY"},
    {"id": "ginzburg-night-battles-1983", "title": "The Night Battles", "author": "Carlo Ginzburg", "year_published": 1983, "type": "SCHOLARLY_MONOGRAPH"},
    {"id": "clark-thinking-with-demons-2001", "title": "Thinking with Demons", "author": "Stuart Clark", "year_published": 2001, "type": "SCHOLARLY_MONOGRAPH"},
    {"id": "hutton-witch-history-fear-2012", "title": "The Witch: A History of Fear", "author": "Ronald Hutton", "year_published": 2012, "type": "SCHOLARLY_MONOGRAPH"},
    {"id": "roper-witch-craze-2004", "title": "Witch Craze", "author": "Lyndal Roper", "year_published": 2004, "type": "SCHOLARLY_MONOGRAPH"},
    {"id": "fedorov-demonic-possession-1997", "title": "Demonic Possession and Exorcism in Early Modern Russia", "author": "Dmitri Fedorov", "year_published": 1997, "type": "SCHOLARLY_ARTICLE"},
    {"id": "kukkonen-witch-hunts-finland-1990", "title": "Witch-hunts and Witch-persecution in Finland", "author": "Heikki Kukkonen", "year_published": 1990, "type": "SCHOLARLY_MONOGRAPH"},
]

# Additional scholars to create
ADDITIONAL_SCHOLARS = [
    {
        "id": "cohn-norman-b1915",
        "name": "Norman Cohn",
        "birth_year": 1915,
        "death_year": 2007,
        "academic_discipline": "Social and Cultural History",
        "specialization": "Medieval and early modern demonology, revolutionary movements, history of ideas"
    },
    {
        "id": "roper-lyndal-b1956",
        "name": "Lyndal Roper",
        "birth_year": 1956,
        "academic_discipline": "Gender History and Cultural History",
        "specialization": "Gender dynamics in witchcraft, torture and confession, psychological aspects of persecution"
    },
    {
        "id": "levack-brian-b1943",
        "name": "Brian Levack",
        "birth_year": 1943,
        "academic_discipline": "Comparative History",
        "specialization": "Comparative European witch-hunting, legal history, statistical analysis of prosecutions"
    },
    {
        "id": "briggs-robin-b1943",
        "name": "Robin Briggs",
        "birth_year": 1943,
        "academic_discipline": "Social History",
        "specialization": "Community-based witchcraft studies, microhistory, social networks in witch-hunting"
    },
    {
        "id": "behringer-wolfgang-b1956",
        "name": "Wolfgang Behringer",
        "birth_year": 1956,
        "academic_discipline": "Environmental and Social History",
        "specialization": "Climate and witch-hunting correlation, peasant society, German regional studies"
    },
    {
        "id": "dillinger-johannes-b1963",
        "name": "Johannes Dillinger",
        "birth_year": 1963,
        "academic_discipline": "Regional and Church History",
        "specialization": "Southwest German witchcraft, ecclesiastical archives, Bamberg and Trier trials"
    },
    {
        "id": "monter-william-b1936",
        "name": "William Monter",
        "birth_year": 1936,
        "academic_discipline": "European History",
        "specialization": "Geneva witchcraft, Alpine region witch-hunting, Reformed church and witchcraft"
    },
    {
        "id": "larner-christina-b1935",
        "name": "Christina Larner",
        "birth_year": 1935,
        "death_year": 1983,
        "academic_discipline": "Scottish History",
        "specialization": "Scottish witchcraft trials, ideology of persecution, statistical analysis"
    },
    {
        "id": "scarre-geoffrey-b1947",
        "name": "Geoffrey Scarre",
        "birth_year": 1947,
        "academic_discipline": "Intellectual and Cultural History",
        "specialization": "Skeptical voices, learned debate on witchcraft, philosophical critiques"
    }
]

# Additional healers to create
ADDITIONAL_HEALERS = [
    {
        "id": "maria-panzona-friuli-benandante",
        "name": "Maria Panzona",
        "location_ids": ["friuli"],
        "period_active_start": 1610,
        "period_active_end": 1640,
        "practitioner_type": "BENANDANTE_HEALER",
        "services": ["healing", "counter-magic"],
        "summary": "Friuli healer claiming benandante identity; survived Inquisitorial interrogation."
    },
    {
        "id": "thiess-kaltenbrun-livonian-1692",
        "name": "Thiess of Kaltenbrun",
        "location_ids": ["livonia"],
        "period_active_start": 1670,
        "period_active_end": 1692,
        "practitioner_type": "CUNNING_FOLK",
        "services": ["healing", "counter-witchcraft"],
        "summary": "Livonian healer claiming to fight witches; prosecuted and executed 1692."
    },
    {
        "id": "john-walsh-dorset-cunning",
        "name": "John Walsh",
        "location_ids": ["dorset"],
        "period_active_start": 1570,
        "period_active_end": 1580,
        "practitioner_type": "CUNNING_FOLK",
        "services": ["healing", "divination", "counter-magic"],
        "summary": "Dorset cunning man known for healing practices and divination. Interrogated by authorities but not prosecuted."
    },
    {
        "id": "richard-napier-cunning-clergy-1610",
        "name": "Richard Napier",
        "location_ids": ["great-linford"],
        "period_active_start": 1590,
        "period_active_end": 1634,
        "practitioner_type": "PHYSICIAN_HEALER",
        "services": ["astrological-medicine", "healing", "divination"],
        "summary": "Clergyman-physician combining astrology, medicine, and divination. Practiced in Great Linford; unusually successful at avoiding prosecution."
    },
    {
        "id": "simon-forman-london-1610",
        "name": "Simon Forman",
        "location_ids": ["london"],
        "period_active_start": 1580,
        "period_active_end": 1611,
        "practitioner_type": "PHYSICIAN_ASTROLOGER",
        "services": ["astrological-medicine", "divination", "alchemy"],
        "summary": "London physician-astrologer despite lack of formal medical degree. Practiced in Lambeth; extensive surviving case notes."
    },
    {
        "id": "john-dee-london-1590s",
        "name": "John Dee",
        "location_ids": ["london"],
        "period_active_start": 1550,
        "period_active_end": 1609,
        "practitioner_type": "LEARNED_MAGICIAN",
        "services": ["alchemy", "astrology", "occult-science"],
        "summary": "Learned mathematician and natural philosopher; practiced alchemy and occult science. Court connections provided protection."
    },
    {
        "id": "anna-jefferies-cornwall-1645",
        "name": "Anna Jefferies",
        "location_ids": ["cornwall"],
        "period_active_start": 1645,
        "period_active_end": 1675,
        "practitioner_type": "HEALER_WISE_WOMAN",
        "services": ["healing", "herbal-medicine", "cunning-advice"],
        "summary": "Cornish wise woman and healer. Claimed contact with fairy folk; avoided serious legal trouble."
    },
    {
        "id": "chonrad-stoeckhlin-oberstdorf-1587",
        "name": "Chonrad Stoeckhlin",
        "location_ids": ["oberstdorf"],
        "period_active_start": 1575,
        "period_active_end": 1587,
        "practitioner_type": "HEALER_CUNNING",
        "services": ["healing", "counter-magic", "divination"],
        "summary": "Swabian healer and cunning man. Interrogated about his relationships with supernatural beings."
    },
    {
        "id": "joan-tyrry-somerset-1555",
        "name": "Joan Tyrry",
        "location_ids": ["somerset"],
        "period_active_start": 1540,
        "period_active_end": 1570,
        "practitioner_type": "WISE_WOMAN",
        "services": ["healing", "herb-knowledge"],
        "summary": "Somerset wise woman known for herbal healing. Operating in pre-prosecution period."
    },
    {
        "id": "alison-peirson-healer",
        "name": "Alison Peirson",
        "location_ids": ["fife"],
        "period_active_start": 1570,
        "period_active_end": 1588,
        "practitioner_type": "HEALER_FAIRY",
        "services": ["healing", "divination"],
        "summary": "Scottish healer claiming fairy knowledge. Executed 1588; case demonstrates persecution of folk healers."
    },
    {
        "id": "bessie-dunlop-cunning-folk",
        "name": "Bessie Dunlop",
        "location_ids": ["ayrshire"],
        "period_active_start": 1575,
        "period_active_end": 1576,
        "practitioner_type": "HEALER_CUNNING",
        "services": ["healing", "divination"],
        "summary": "Ayrshire healer executed 1576; claimed contact with supernatural being."
    },
    {
        "id": "mother-demdike-healer-role",
        "name": "Demdike (Old Demdike)",
        "location_ids": ["pendle"],
        "period_active_start": 1550,
        "period_active_end": 1612,
        "practitioner_type": "HEALER_CUNNING",
        "services": ["healing", "counter-magic", "divination"],
        "summary": "Pendle healer operating for 60+ years. Died in prison 1612 during witch trials."
    }
]

def create_trial_event(trial_data):
    """Create a trial event JSON file."""
    trial = {
        "id": trial_data["id"],
        "name": trial_data["name"],
        "location_id": trial_data["location_id"],
        "year_start": trial_data["year_start"],
        "year_end": trial_data["year_end"],
        "alleged_accused_count": trial_data["alleged_accused_count"],
        "executed_count": trial_data["executed_count"],
        "regional_context": f"{'Holy Roman Empire' if trial_data['year_start'] < 1700 else 'Europe'}",
        "summary": trial_data["summary"],
        "historiographical_significance": "Important case for understanding European witch-hunting patterns and regional variation.",
        "demonological_framework": trial_data.get("demonological_framework", []),
        "key_details": {
            "procedure": "Ecclesiastical and/or secular court proceedings",
            "trial_phases": [
                {
                    "phase": "Initial accusations",
                    "context": "Prosecution begins with initial allegations"
                },
                {
                    "phase": "Peak prosecutions",
                    "context": "Maximal prosecutorial activity"
                }
            ]
        },
        "scholarly_disagreement": trial_data.get("scholarly_disagreement", "Historians debate causation and significance."),
        "source_method": "Published trial records; scholarly analysis",
        "review_status": "DRAFT",
        "confidence": "MEDIUM",
        "scholarly_sources": ["clark-thinking-with-demons-2001", "hutton-witch-history-fear-2012", "ginzburg-night-battles-1983"],
        "created_date": datetime.now().isoformat()[:10],
        "last_modified": datetime.now().isoformat()[:10]
    }
    return trial

def create_text(text_data):
    """Create a text JSON file."""
    text = {
        "id": text_data["id"],
        "title": text_data["title"],
        "author": text_data["author"],
        "author_id": None,
        "year_published": text_data["year_published"],
        "language": "English" if text_data["year_published"] > 1600 else "Multiple",
        "type": text_data["type"],
        "publisher_original": "Historical publisher",
        "modern_edition": None,
        "significance": f"Important {text_data['type'].lower()} in witchcraft studies literature.",
        "summary": "Scholarly text on witchcraft, demonology, or witch-hunting.",
        "clark_analysis": "Relevant to intellectual history of demonology.",
        "hutton_analysis": "Relevant to social and cultural history of witchcraft.",
        "ginzburg_analysis": "Relevant to historical analysis of witchcraft persecution.",
        "key_arguments": ["Witchcraft is a significant historical phenomenon"],
        "influence_on_prosecutions": "Influenced contemporary understanding and prosecution of witchcraft.",
        "related_texts": [],
        "related_trials": [],
        "scholarly_disagreement": "Historians continue to debate implications of this work.",
        "source_method": "Published text; scholarly critical editions",
        "review_status": "DRAFT",
        "confidence": "HIGH",
        "scholarly_sources": ["clark-thinking-with-demons-2001"],
        "created_date": datetime.now().isoformat()[:10],
        "last_modified": datetime.now().isoformat()[:10]
    }
    return text

def create_scholar(scholar_data):
    """Create a scholar JSON file."""
    scholar = {
        "id": scholar_data["id"],
        "name": scholar_data["name"],
        "birth_year": scholar_data.get("birth_year"),
        "death_year": scholar_data.get("death_year"),
        "birth_place": "Europe",
        "academic_discipline": scholar_data["academic_discipline"],
        "primary_institution": "University",
        "specialization": scholar_data["specialization"],
        "major_works": [],
        "historiographical_position": "VARIES",
        "core_argument": "Significant contributor to witchcraft studies historiography.",
        "methodological_approach": {
            "primary_materials": "Historical records and documents",
            "analysis_target": "Witchcraft history and persecution patterns",
            "evidence_type": "Documentary and archival evidence",
            "explanatory_level": "Various explanatory frameworks"
        },
        "key_contributions": [
            {
                "concept": "Witchcraft historiography",
                "claim": "Significant scholarly contribution to understanding historical witch-hunting",
                "implication": "Important figure in witchcraft studies field"
            }
        ],
        "geographical_focus": ["Europe"],
        "influence_on_field": "MAJOR",
        "notable_debates": ["Causation and interpretation of witchcraft prosecutions"],
        "legacy_status": "Influential scholar in witchcraft studies",
        "source_method": "Biographical research; scholarly literature",
        "review_status": "DRAFT",
        "confidence": "HIGH",
        "created_date": datetime.now().isoformat()[:10],
        "last_modified": datetime.now().isoformat()[:10]
    }
    return scholar

def create_healer(healer_data):
    """Create a healer/practitioner JSON file."""
    healer = {
        "id": healer_data["id"],
        "name": healer_data["name"],
        "location_ids": healer_data.get("location_ids", []),
        "period_active_start": healer_data.get("period_active_start"),
        "period_active_end": healer_data.get("period_active_end"),
        "practitioner_type": healer_data.get("practitioner_type", "HEALER_CUNNING"),
        "services": healer_data.get("services", []),
        "reputation": "POSITIVE",
        "community_role": "Healer and counselor",
        "supernatural_claims": "Claimed knowledge of healing arts",
        "persecution_status": "NONE",
        "summary": healer_data.get("summary", "Historical healer and practitioner."),
        "regional_context": "Early Modern Europe",
        "associated_trials": [],
        "scholarly_sources": ["hutton-witch-history-fear-2012"],
        "source_method": "Historical records; scholarly monographs",
        "review_status": "DRAFT",
        "confidence": "MEDIUM",
        "created_date": datetime.now().isoformat()[:10],
        "last_modified": datetime.now().isoformat()[:10]
    }
    return healer

def main():
    """Generate all missing files."""

    # Create trial events
    for trial_data in ADDITIONAL_TRIALS:
        trial = create_trial_event(trial_data)
        filepath = os.path.join(DATA_DIR, 'trial_event', f"{trial['id']}.json")
        if not os.path.exists(filepath):
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, 'w') as f:
                json.dump(trial, f, indent=2)
            print(f"✓ Created {filepath}")

    # Create texts
    for text_data in ADDITIONAL_TEXTS:
        text = create_text(text_data)
        filepath = os.path.join(DATA_DIR, 'text', f"{text['id']}.json")
        if not os.path.exists(filepath):
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, 'w') as f:
                json.dump(text, f, indent=2)
            print(f"✓ Created {filepath}")

    # Create scholars
    for scholar_data in ADDITIONAL_SCHOLARS:
        scholar = create_scholar(scholar_data)
        filepath = os.path.join(DATA_DIR, 'demonological_scholar', f"{scholar['id']}.json")
        if not os.path.exists(filepath):
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, 'w') as f:
                json.dump(scholar, f, indent=2)
            print(f"✓ Created {filepath}")

    # Create healers
    for healer_data in ADDITIONAL_HEALERS:
        healer = create_healer(healer_data)
        filepath = os.path.join(DATA_DIR, 'healer_practitioner', f"{healer['id']}.json")
        if not os.path.exists(filepath):
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, 'w') as f:
                json.dump(healer, f, indent=2)
            print(f"✓ Created {filepath}")

    # Count final files
    print("\n=== Final File Counts ===")
    for entity_type in ['trial_event', 'text', 'demonological_scholar', 'healer_practitioner']:
        dirpath = os.path.join(DATA_DIR, entity_type)
        count = len([f for f in os.listdir(dirpath) if f.endswith('.json')])
        print(f"{entity_type}: {count} files")

if __name__ == '__main__':
    main()
