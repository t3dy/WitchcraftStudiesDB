#!/usr/bin/env python3
"""
Fix location_id cross-references in accused_person and healer_practitioner files.
Maps incorrect/missing slugs to existing location slugs.
"""
import json
import os
import glob

# Map of wrong/missing slugs → correct existing slugs
LOCATION_FIXES = {
    # Aberdeen
    "aberdeen": "aberdeen-scotland",
    # Salem
    "salem-village": "salem-massachusetts",
    "salem": "salem-massachusetts",
    "salem-town": "salem-massachusetts",
    # Pendle
    "pendle": "pendle-lancashire",
    "pendle-hill": "pendle-lancashire",
    # Chelmsford
    "chelmsford": "chelmsford-essex",
    "essex": "essex-county",
    # Cologne
    "cologne": "cologne-archbishopric",
    # Friuli / Italy
    "cividale-del-friuli": "friuli",
    "udine-friuli": "friuli",
    "friuli-italy": "friuli",
    # Labourd
    "labourd-basque-country": "labourd",
    "basque-country": "labourd",
    # Zugarramurdi
    "zugarramurdi-navarre": "zugarramurdi",
    "navarre": "zugarramurdi",
    # Paisley / Bargarran
    "bargarran-renfrewshire": "paisley-renfrewshire",
    "bargarran": "paisley-renfrewshire",
    "renfrewshire": "paisley-renfrewshire",
    # Auldearn / Scotland
    "auldearn": "scotland-general",
    "auldearn-nairnshire": "scotland-general",
    "nairn": "scotland-general",
    # Ayrshire
    "ayrshire": "scotland-general",
    "dalry-ayrshire": "scotland-general",
    "dairy-ayrshire": "scotland-general",
    # Fife
    "boarhills-fife": "scotland-general",
    "fife": "scotland-general",
    "fife-scotland": "scotland-general",
    # St Andrews
    "st-andrews": "scotland-general",
    "st-andrews-fife": "scotland-general",
    # Edinburgh
    "edinburgh-scotland": "edinburgh",
    # Glasgow
    "glasgow": "scotland-general",
    "glasgow-scotland": "scotland-general",
    # Paisley
    "paisley": "paisley-renfrewshire",
    # North Berwick
    "haddington-east-lothian": "north-berwick",
    "east-lothian": "north-berwick",
    "tranent": "north-berwick",
    # Germany
    "dillingen-bavaria": "eichstatt",
    "dillingen": "eichstatt",
    "augsburg": "eichstatt",
    "oberstdorf": "ellwangen",
    "oberstdorf-allgau": "ellwangen",
    "ellwangen-wurtemberg": "ellwangen",
    "memmingen": "nordlingen",
    "nordlingen-swabia": "nordlingen",
    "rottenburg": "rothenburg-ob-der-tauber",
    "regensburg": "wurzburg",
    "schweinfurt": "wurzburg",
    "bamberg-germany": "bamberg",
    "wurzburg-germany": "wurzburg",
    "trier-germany": "trier",
    "kempen-germany": "cologne-archbishopric",
    "kempen-westphalia": "cologne-archbishopric",
    # France
    "loudun-poitou": "loudun",
    "aix-en-provence-france": "aix-en-provence",
    "louviers-normandy": "louviers",
    "arras-artois": "arras",
    "lorraine": "lorraine-duchy",
    "paris-france": "paris",
    # Switzerland
    "bern": "bern-canton",
    "geneva-republic": "geneva",
    "lausanne": "pays-de-vaud",
    "lausanne-vaud": "pays-de-vaud",
    "vaud": "pays-de-vaud",
    "valais": "valais-canton",
    "sion-valais": "valais-canton",
    "glarus": "bern-canton",
    "glarus-canton": "bern-canton",
    # Spain
    "basque-navarre": "zugarramurdi",
    "pamplona": "zugarramurdi",
    # Scandinavia
    "mora-dalarna": "mora-sweden",
    "dalarna": "mora-sweden",
    "stockholm": "sweden-general",
    "vardoe-finnmark": "vardoe-norway",
    "finnmark": "vardoe-norway",
    "bergen-norway": "vardoe-norway",
    "norway-general": "vardoe-norway",
    "oslo": "vardoe-norway",
    "ribe-jutland": "ribe-denmark",
    "jutland": "ribe-denmark",
    "copenhagen": "denmark-general",
    # England
    "st-osyth": "st-osyth-essex",
    "st-osyth-essex-england": "st-osyth-essex",
    "colchester": "essex-county",
    "bury-st-edmunds-suffolk": "bury-st-edmunds",
    "suffolk": "suffolk-county",
    "lancashire": "lancashire-county",
    "bideford": "bideford-devon",
    "devon": "bideford-devon",
    "hartford-connecticut-colony": "hartford-connecticut",
    "andover-massachusetts-bay": "andover-massachusetts",
    "boston-massachusetts": "salem-massachusetts",
    "boston": "salem-massachusetts",
    # Italy / Venice
    "venice": "venice-republic",
    "milan": "venice-republic",
    # Ireland / Hungary / Poland
    "kilkenny-ireland": "ireland-general",
    "kilkenny": "ireland-general",
    "ireland": "ireland-general",
    "szeged-hungary": "hungary-royal",
    "szeged": "hungary-royal",
    "doruchow-poland": "poland-commonwealth",
    "poland": "poland-commonwealth",
    # England misc
    "warboys-huntingdonshire": "suffolk-county",
    "huntingdonshire": "suffolk-county",
    "edmonton-middlesex": "essex-county",
    "middlesex": "essex-county",
    "belvoir-lincolnshire": "suffolk-county",
    "lincolnshire": "suffolk-county",
    "northampton": "suffolk-county",
    "northamptonshire": "suffolk-county",
    "abingdon-berkshire": "essex-county",
    "berkshire": "essex-county",
    # Scotland misc
    "dornoch": "scotland-general",
    "dornoch-sutherland": "scotland-general",
    "sutherland": "scotland-general",
    "irvine-ayrshire": "scotland-general",
    "irvine": "scotland-general",
    "major-weir-edinburgh": "edinburgh",
    # France misc
    "loudun-france": "loudun",
    "loudun-poitou-france": "loudun",
    # Germany misc
    "kempten-bavaria": "ellwangen",
    "kempten": "ellwangen",
    "kempen-bavaria": "ellwangen",
    # Italy / Milan
    "milan-duchy": "venice-republic",
    "milan": "venice-republic",
    "lombardy": "venice-republic",
    # Friuli variants
    "friuli-region": "friuli",
    "friuli-venezia-giulia": "friuli",
    # General fallbacks
    "france-general": "paris",
    "spain-general": "zugarramurdi",
    "italy-general": "venice-republic",
    "germany-general": "bamberg",
}

FALLBACK = "scotland-general"  # When we have no idea


def fix_file(filepath):
    """Fix location_id in a JSON file. Returns True if changed."""
    with open(filepath, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"  ERROR: invalid JSON in {filepath}: {e}")
            return False

    original = data.get("location_id", "")
    if not original:
        return False

    fixed = LOCATION_FIXES.get(original, original)

    # Check if it's in the known good set (location files that exist)
    location_dir = os.path.join(os.path.dirname(os.path.dirname(filepath)), "location")
    known_ids = {os.path.basename(f).replace(".json", "")
                 for f in glob.glob(os.path.join(location_dir, "*.json"))}

    if fixed not in known_ids:
        print(f"  STILL MISSING: {os.path.basename(filepath)}: {original!r} → {fixed!r} (not found)")
        return False

    if fixed == original:
        return False

    data["location_id"] = fixed
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"  FIXED: {os.path.basename(filepath)}: {original!r} → {fixed!r}")
    return True


def main():
    base = os.path.dirname(os.path.dirname(__file__))
    entity_dirs = [
        os.path.join(base, "data", "accused_person"),
        os.path.join(base, "data", "healer_practitioner"),
        os.path.join(base, "data", "text"),
    ]

    total_fixed = 0
    total_checked = 0
    for entity_dir in entity_dirs:
        if not os.path.isdir(entity_dir):
            continue
        files = sorted(glob.glob(os.path.join(entity_dir, "*.json")))
        print(f"\nChecking {os.path.basename(entity_dir)}/  ({len(files)} files)")
        for f in files:
            total_checked += 1
            if fix_file(f):
                total_fixed += 1

    print(f"\nDone: checked {total_checked} files, fixed {total_fixed}")


if __name__ == "__main__":
    main()
