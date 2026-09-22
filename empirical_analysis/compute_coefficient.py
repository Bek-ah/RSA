from byu_pytest_utils import compute_coefficient


def main():

    # COMMENT AND UNCOMMENT appropriate lines as necessary

    filename = "_large_primes_runtimes.json"
    # filename = "_keypair_runtimes.json"
    # filename = "_encrypt_runtimes.json"
    # filename = "_decrypt_runtimes.json"

    def theoretical_big_o(n):
        # FILL THIS IN with your theoretical time complexity in terms of n
        return 1

    # Changing these values takes a slice of your runtimes corresponding with the indices

    start = None
    end = None

    compute_coefficient(filename, theoretical_big_o, start, end)


if __name__ == "__main__":
    main()
