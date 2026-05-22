from pathlib import Path
import json

DATA_DIR = Path("data")
PROFILES_FILE = DATA_DIR / "profiles.json"
RESERVATIONS_FILE = DATA_DIR / "reservations.json"

def load_profiles_data():
  if PROFILES_FILE.exists():
    with open(PROFILES_FILE, "r") as f:
      profiles = f.read()
      if profiles.strip():
        return json.loads(profiles)
  return []

def save_profiles_data(data):
  DATA_DIR.mkdir(parents=True, exist_ok=True)
  with open(PROFILES_FILE, "w") as f:
    json.dump(data, f, indent=4)

def load_reservations_data():
  if RESERVATIONS_FILE.exists():
    with open(RESERVATIONS_FILE, "r") as f:
      reservations = f.read()
      if reservations.strip():
        return json.loads(reservations)
  return []

def save_reservations_data(data):
  DATA_DIR.mkdir(parents=True, exist_ok=True)
  with open(RESERVATIONS_FILE, "w") as f:
    json.dump(data, f, indent=4)