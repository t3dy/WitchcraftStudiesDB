#!/usr/bin/env python3
"""
Build web/js/data_bundle.js from all JSON files in the data/ directory.
Run after adding new database entries to update the website bundle.
"""

import json
import os
import sys

DATA_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
OUTPUT = os.path.join(os.path.dirname(os.path.dirname(__file__)), "web", "js", "data_bundle.js")

ENTITY_MAP = {
    "location": ("LOCATIONS", ["id", "name", "type", "region", "modern_location",
                                "coordinates", "lat", "lng",
                                "witchcraft_trials_significance", "witchcraft_significance",
                                "trial_events", "trial_event", "scholarly_sources"]),
    "trial_event": ("TRIALS", ["id", "name", "location_id", "start_year", "end_year",
                                "year_start", "year_end", "year", "year_accused",
                                "total_accused", "total_executed", "executions",
                                "accused_count", "execution_count",
                                "region", "outcome", "demonological_framework",
                                "key_details", "summary", "description",
                                "historiographical_significance", "scholarly_sources",
                                "review_status", "confidence"]),
    "demonological_concept": ("CONCEPTS", ["id", "name", "category_type", "time_period",
                                            "primary_locale", "scholarly_definition",
                                            "clark_intellectual_analysis",
                                            "hutton_social_analysis",
                                            "ginzburg_interrogation_analysis",
                                            "actor_perspective", "analyst_perspective",
                                            "scholarly_disagreement",
                                            "trial_examples", "related_concepts",
                                            "review_status", "confidence"]),
    "demonological_scholar": ("SCHOLARS", ["id", "name", "birth_year", "death_year",
                                            "birth_place", "academic_discipline",
                                            "primary_institution", "specialization",
                                            "historiographical_position", "core_argument",
                                            "major_works", "key_contributions",
                                            "scholarly_relationships",
                                            "review_status", "confidence"]),
    "text": ("TEXTS", ["id", "title", "author", "year_published", "year",
                        "publication_year", "language", "type", "text_type",
                        "significance", "summary", "description",
                        "scholarly_significance", "scholarly_sources",
                        "review_status", "confidence"]),
    "accused_person": ("ACCUSED", ["id", "name", "status", "trial_id", "location_id",
                                    "year_accused", "year_executed", "age_at_trial",
                                    "social_status", "gender", "occupation",
                                    "biography", "arrest_narrative",
                                    "confession_status", "torture_applied",
                                    "torture_method", "execution_details",
                                    "historiographical_significance",
                                    "review_status", "confidence"]),
    "healer_practitioner": ("HEALERS", ["id", "name", "status", "trial_id", "location_id",
                                         "year_active", "year_accused",
                                         "social_status", "gender", "tradition",
                                         "self_identification", "claimed_abilities",
                                         "biography", "practice_description",
                                         "relationship_to_prosecution",
                                         "historiographical_significance",
                                         "review_status", "confidence"]),
    "timeline_event": ("TIMELINE_EVENTS", ["id", "title", "year", "year_start", "year_end",
                                            "date", "type", "event_type", "significance",
                                            "region", "location_id",
                                            "description", "summary",
                                            "historiographical_notes",
                                            "related_trials", "related_concepts",
                                            "scholarly_sources",
                                            "review_status", "confidence"]),
}


def get_coords(obj):
    """Extract lat/lng from either flat fields or nested coordinates object."""
    if "lat" in obj and "lng" in obj:
        return obj["lat"], obj["lng"]
    if "coordinates" in obj and isinstance(obj["coordinates"], dict):
        c = obj["coordinates"]
        return c.get("latitude"), c.get("longitude")
    return None, None


def load_entity(entity_type, filepath):
    """Load a JSON file, normalize coordinates, and return the dict."""
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    # For locations, ensure flat lat/lng fields exist
    if entity_type == "location":
        lat, lng = get_coords(data)
        if lat is not None:
            data["lat"] = lat
            data["lng"] = lng

    return data


def load_all(entity_type):
    """Load all JSON files from a data subdirectory."""
    folder = os.path.join(DATA_ROOT, entity_type)
    if not os.path.isdir(folder):
        return []
    items = []
    for fname in sorted(os.listdir(folder)):
        if not fname.endswith(".json"):
            continue
        fpath = os.path.join(folder, fname)
        try:
            items.append(load_entity(entity_type, fpath))
        except Exception as e:
            print(f"  WARNING: skipping {fname}: {e}", file=sys.stderr)
    return items


def js_var(name, data):
    """Return a JavaScript global assignment string."""
    return f"window.{name} = {json.dumps(data, ensure_ascii=False, indent=2)};\n"


def main():
    lines = [
        "// WitchcraftStudiesDB Data Bundle",
        f"// Auto-generated by scripts/build_data_bundle.py",
        "// DO NOT EDIT — regenerate with: python scripts/build_data_bundle.py",
        "",
    ]

    totals = {}
    for entity_type, (global_name, _) in ENTITY_MAP.items():
        print(f"Loading {entity_type}...", file=sys.stderr)
        items = load_all(entity_type)
        totals[entity_type] = len(items)
        lines.append(js_var(global_name, items))
        lines.append("")

    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"\nWrote {OUTPUT}")
    for entity_type, count in totals.items():
        print(f"  {entity_type}: {count} entries")


if __name__ == "__main__":
    main()
