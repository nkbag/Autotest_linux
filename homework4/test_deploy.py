from sshcheckers import ssh_checkout, upload_files


def test_1():
    res = []
    upload_files("0.0.0.0", "userok", "2222", "p7zip-full.deb",
                 "/home/userok/p7zip-full.deb")
    res.append(ssh_checkout("0.0.0.0", "userok", "2222", "echo '2222' | sudo -S dpkg -i /home/userok/p7zip-full.deb",
                            "Настраивается пакет"))
    res.append(ssh_checkout("0.0.0.0", "userok", "2222", "echo '2222' | sudo -S dpkg -s p7zip-full",
                            "Status: install ok installed"))
    assert all(res), "test1 FAIL"
