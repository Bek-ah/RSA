import json
import matplotlib.pyplot as plt


def main():

    # COMMENT AND UNCOMMENT appropriate lines as necessary

    filename = "_large_primes_runtimes.json"
    # filename = '_keypair_runtimes.json'
    # filename = '_encrypt_runtimes.json'
    # filename = '_decrypt_runtimes.json'

    with open(filename, "r") as f:
        runtimes = json.load(f)

    # FILL THIS IN with your theoretical time complexity in terms of n
    def theoretical_big_o(n):
        return 1

    # FILL THIS IN from result using compute_coefficient
    coeff = 1

    nn, times = zip(*runtimes)
    nn = [n[0] for n in nn]

    # Plot empirical values
    fig = plt.figure()
    plt.scatter(nn, times, marker="o")

    predicted_runtime = [coeff * theoretical_big_o(*n) for n, t in runtimes]

    # Plot theoretical fit
    plt.plot(nn, predicted_runtime, c="k", ls=":", lw=2, alpha=0.5)

    # Update title, legend, and axis labels as needed
    plt.legend(["Observed", "Theoretical O(FILL ME IN)"])
    plt.xlabel("n")
    plt.ylabel("Runtime (sec)")
    plt.title("Time for FILL ME IN")

    fig.show()
    fig.savefig("empirical.svg")


if __name__ == "__main__":
    main()
