import subprocess


def checkout(cmd, text=''):
    result = subprocess.run(cmd, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0 or text in result.stderr:
        return True
    else:
        return False


def get_out(cmd):
    res = subprocess.run(cmd, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf-8')
    return res.stdout.strip().split("\n"), res.stderr
