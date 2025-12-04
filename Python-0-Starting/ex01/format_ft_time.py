import time
from datetime import datetime

# * Obtener timestamp actual (segundos desde 1970-01-01)
timestamp = time.time()

# * número con comas + notación científica
formatted_timestamp = f"Seconds since January 1, 1970: {timestamp:,.4f} or {timestamp:.2e} in scientific notation"
date_formatted = datetime.now().strftime("%b %d %Y")


print(formatted_timestamp)
print(date_formatted)
