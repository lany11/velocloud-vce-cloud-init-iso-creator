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

META_DATA_PATH = "meta-data"
OUTPUT_ISO = "seed.iso"


def main():
    vco = input("Enter VCO address: ")
    activation_code = input("Enter activation code: ")

    user_data_content = USER_DATA_TEMPLATE.format(
        vco=vco, activation_code=activation_code
    )

    with open("user-data", "w") as f:
        f.write(user_data_content)

    with open(META_DATA_PATH, "rb") as f:
        meta_data_content = f.read()

    iso = pycdlib.PyCdlib()
    iso.new(
        interchange_level=1,
        joliet=3,
        rock_ridge="1.09",
        vol_ident="cidata",
    )

    iso.add_fp(
        open("user-data", "rb"),
        len(user_data_content.encode()),
        "/USERDATA.;1",
        joliet_path="/user-data",
        rr_name="user-data",
    )

    iso.add_fp(
        open(META_DATA_PATH, "rb"),
        len(meta_data_content),
        "/METADATA.;1",
        joliet_path="/meta-data",
        rr_name="meta-data",
    )

    iso.write(OUTPUT_ISO)
    iso.close()
    print(f"Created {OUTPUT_ISO}")


if __name__ == "__main__":
    main()
