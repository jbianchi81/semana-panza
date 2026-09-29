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

elapsed_weeks = elapsed.days / 7

remaining = end - now

remaining_weeks = remaining.days / 7

print("Vamo por la semana %.02f🤰. Faltan %.02f🤱 (%s). Caray😂!" % (elapsed_weeks, remaining_weeks, end.strftime("%a, %d %b %Y")))
