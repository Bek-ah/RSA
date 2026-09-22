import json
import os
import sys
from pathlib import Path

this_folder = os.path.dirname(__file__)
sys.path.append(os.path.join(this_folder, ".."))

from encrypt_decrypt_files import main as encrypt_decrypt
from byu_pytest_utils import (
    measure_runtime,
    compute_average_runtimes,
    print_markdown_table,
)


def _encrypt(key_file, message_file, output_file):

    encrypt_decrypt(key_file, message_file, output_file)

    return key_file


def _encrypt_preprocess(number, _, N, e):
    with open("encrypted_files/public.txt", "w") as f:
        f.writelines([str(N), "\n", str(e)])

    key_file = Path("encrypted_files/public.txt")
    message_file = Path("1Nephi.txt")
    output_file = Path(f"encrypted_files/encrypted_{number}.txt")

    return key_file, message_file, output_file


def _encrypt_postprocess(key_file):
    os.remove(key_file)


def _decrypt(key_file, message_file, output_file):

    encrypt_decrypt(key_file, message_file, output_file)

    return key_file, message_file, output_file


def _decrypt_preprocess(number, _, N, d):
    with open("encrypted_files/private.txt", "w") as f:
        f.writelines([str(N), "\n", str(d)])

    key_file = Path("encrypted_files/private.txt")
    message_file = Path(f"encrypted_files/encrypted_{number}.txt")
    output_file = Path(f"encrypted_files/decrypted_{number}.txt")

    return key_file, message_file, output_file


def _decrypt_postprocess(key_file, message_file, output_file):
    os.remove(key_file)
    os.remove(message_file)
    os.remove(output_file)


def main(e_tuples, d_tuples, recursion_limit):

    measure_runtime(
        run=_encrypt,
        inputs=e_tuples,
        recursion_limit=recursion_limit,
        preprocessing=_encrypt_preprocess,
        postprocessing=_encrypt_postprocess,
        output_group=[1],
    )

    measure_runtime(
        run=_decrypt,
        inputs=d_tuples,
        recursion_limit=recursion_limit,
        preprocessing=_decrypt_preprocess,
        postprocessing=_decrypt_postprocess,
        output_group=[1],
    )

    with open("_encrypt_runtimes.json", "r") as f:
        runtimes = json.load(f)

    ave_runtimes = compute_average_runtimes(runtimes)

    print_markdown_table(ave_runtimes, ["Size", "Encryption Time (Sec)"])

    with open("_decrypt_runtimes.json", "r") as f:
        runtimes = json.load(f)

    ave_runtimes = compute_average_runtimes(runtimes)

    print_markdown_table(ave_runtimes, ["Size", "Decryption Time (Sec)"])


if __name__ == "__main__":
    with open("_keypairs.json", "r") as f:
        keypairs = json.load(f)

        encryption = [
            (number, size, N, e) for number, (size, N, e, _) in enumerate(keypairs)
        ]
        decryption = [
            (number, size, N, d) for number, (size, N, _, d) in enumerate(keypairs)
        ]

    recursion_limit = encryption[-1][1] * 2

    main(encryption, decryption, recursion_limit)
