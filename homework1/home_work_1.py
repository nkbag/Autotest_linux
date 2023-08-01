import string
import subprocess


def check_output(cmd, text, advance=False, word=None):
    if advance:
        found_list = text.split()
        for i in found_list:
            if i[-1] in string.punctuation:
                res = i.replace(i[-1], '')
                if word == res:
                    return True
        return False
    else:
        output = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
        if text in output.stdout and output.returncode == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    print(check_output('cat /etc/os-release', 'Jammy', True))