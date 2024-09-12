# HTTP status codes program

# -------------------------
# Subprograms
# -------------------------
def http_status(status):
  match status:
    case 400:
      return "Bad request"
    case 401 | 403:
      return "Authentication Error"
    case 404:
      return "Not Found"
    case _:
      return "Unknown error"

# -------------------------
# Main program
# -------------------------
code = 404
print(http_status(code))
