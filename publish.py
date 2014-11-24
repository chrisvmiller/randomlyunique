import os
import shutil
import datetime
import git


def copytree(src, dst, symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            if not os.path.exists(d) or os.stat(src).st_mtime - os.stat(dst).st_mtime > 1:
                shutil.copy2(s, d)


def publish_site():
    full_path = os.path.abspath('.')
    repo = git.Repo(full_path)

    repo.git.checkout('master')
    repo.git.reset('--hard', 'HEAD^')
    repo.git.checkout('pelican')

    os.system("make html")

    output_path = os.path.join(full_path, 'output')
    copytree(output_path, full_path)

    repo.git.checkout('master')
    repo.git.add('.')
    repo.git.commit(m=' Blog update for {0} '.format(datetime.date.today()))
    os.system('git push origin master -f')

    repo.git.checkout('pelican')


publish_site()