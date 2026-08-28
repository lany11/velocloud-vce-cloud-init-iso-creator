import io
import os

import pycdlib

USER_DATA_TEMPLATE = """\
#cloud-config
password: arista123
chpasswd: {{ expire: False }}
ssh_pwauth: True
velocloud:
  vce:
    vco: {vco}
    activation_code: {activation_code}
    vco_ignore_cert_errors: false
"""

META_DATA_CONTENT = """\
instance-id: vce
local-hostname: vce
"""

OUTPUT_FILENAME = "seed.iso"


def main():
    vco = input("Enter VCO address: ")
    activation_code = input("Enter activation code: ")

    default_dir = os.path.expanduser("~")
    output_dir = input(f"Enter output directory [{default_dir}]: ").strip()
    if not output_dir:
        output_dir = default_dir

    if not os.path.isdir(output_dir):
        print(f"Error: '{output_dir}' is not a valid directory.")
        return

    output_path = os.path.join(output_dir, OUTPUT_FILENAME)

    user_data_bytes = USER_DATA_TEMPLATE.format(
        vco=vco, activation_code=activation_code
    ).encode()
    meta_data_bytes = META_DATA_CONTENT.encode()

    iso = pycdlib.PyCdlib()
    iso.new(
        interchange_level=1,
        joliet=3,
        rock_ridge="1.09",
        sys_ident="LINUX",
        vol_ident="cidata",
    )

    iso.add_fp(
        io.BytesIO(user_data_bytes),
        len(user_data_bytes),
        "/USER_DAT.;1",
        joliet_path="/user-data",
        rr_name="user-data",
    )

    iso.add_fp(
        io.BytesIO(meta_data_bytes),
        len(meta_data_bytes),
        "/META_DAT.;1",
        joliet_path="/meta-data",
        rr_name="meta-data",
    )

    iso.write(output_path)
    iso.close()
    print(f"Created {output_path}")


if __name__ == "__main__":
    main()
