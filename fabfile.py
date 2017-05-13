from fabric.api import env, local, prefix, cd, run

env.hosts = ["matricula.iespuertodelacruz.es"]


def deploy():
    local("git push")
    with prefix("source ~/.virtualenvs/matricula/bin/activate"):
        with cd("~/matricula"):
            run("git pull")
            run("pip install -r requirements.txt")
            run("bower install")
            run("supervisorctl restart matricula")
