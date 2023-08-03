from checkout import checkout, FOLDER_OUT, FOLDER_TST, FOLDER_folder1, FOLDER_folder_tst


def test_step1():
    res = checkout(f"cd {FOLDER_TST}; 7z a ../out/arx2", "Everything is Ok")
    res_2 = checkout(f"ls {FOLDER_OUT}", "arx2.7z")
    assert res and res_2, "test1 FAIL"


def test_step2():
    res = checkout(f"cd {FOLDER_OUT}; 7z e arx2.7z -o{FOLDER_folder1} -y", "Everything is Ok")
    res_2 = checkout(f"ls {FOLDER_folder1}", "test1.txt")
    assert res and res_2, "test2 FAIL"


def test_step3():
    assert checkout(f"cd {FOLDER_OUT}; 7z t arx2.7z", "Everything is Ok"), "test3 FAIL"


def test_step4():
    assert checkout(f"cd {FOLDER_OUT}; 7z u arx2.7z", "Everything is Ok"), "test4 FAIL"


def test_step5():
    assert checkout(f"cd {FOLDER_OUT}; 7z l arx2.7z", "test1.txt"), "test5 FAIL"


def test_step6():
    assert checkout(f"cd {FOLDER_OUT}; 7z d arx2.7z", "Everything is Ok"), "test6 FAIL"


def test_step7():
    res = checkout(f"cd {FOLDER_TST}; 7z a {FOLDER_OUT}/arx2.7z", "Everything is Ok")
    res_2 = checkout(f"cd {FOLDER_OUT}; 7z x fld1.7z -o{FOLDER_folder_tst} -y", "Everything is Ok")
    assert res and res_2, "test7 FAIL"
