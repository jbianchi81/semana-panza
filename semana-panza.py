#!/usr/bin/python3
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

date_str = os.getenv("INICIO")

if date_str:
    # Parse string into a datetime object (specify matching format)
    start = datetime.strptime(date_str, "%Y-%m-%d")
else:
    raise ValueError("Ingrese INICIO=YYYY-MM-DD en .env")

end = start + timedelta(7 * 39)

now = datetime.now()

elapsed = now - start

elapsed_weeks = int(elapsed.days / 7)

elapsed_days = int(elapsed.days - elapsed_weeks * 7)

remaining = end - now

remaining_weeks = int(remaining.days / 7)

remaining_days = int(remaining.days - remaining_weeks * 7)

print("Vamo por la semana %d día %d🤰. Faltan %d semanas y %d días🤱 (%s). Caray😂!" % (elapsed_weeks, elapsed_days, remaining_weeks, remaining_days, end.strftime("%a, %d %b %Y")))
