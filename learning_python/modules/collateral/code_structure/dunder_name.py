# Importable code
print(f"Before if: {__name__}")


def dns_ip(dns="8.8.8.8"):
    print(f"DNS Server: {dns}")


if __name__ == "__main__":

    print(f"After if: {__name__}")

    # Executable code
    dns_ip()
    dns_ip(dns="1.1.1.1")
