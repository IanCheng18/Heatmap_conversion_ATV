import subprocess

# Things to change from private to ATV gitea
# database name => gitea => mysql_gitea
#
user_dict =	{
    "Ian Cheng": [2, 'cheng', 'cheng@atv-systems.de'],
    "Markus Kaden": [6, 'kaden', 'kaden@atv-systems.de'],
    "Torsten Voigt": [7, 'voigt', 'voigt@atv-systems.de'],
    "Ingo Berg": [8, 'berg', 'berg@atv-systems.de'],
    "Janina Freyboth": [9, 'freyboth', 'freyboth@atv-systems.de'],
    "Silvia Mehnert": [10, 'mehnert', 'mehnert@atv-systems.de'],
    "Steffen König": [11, 'koenig', 'koenig@atv-systems.de'],
    "Torsten Brischalle": [13, 'brischalle', 'brischalle@atv-systems.de'],
    "Julia König": [16, 'jkoenig', 'jkoenig@atv-systems.de'],
    "Georg Jahn": [19, 'jahn', 'jahn@atv-systems.de'],
    "Frank Ropos": [22, 'ropos', 'ropos@atv-systems.de'],
    "Volker Hänsel": [23, 'haensel', 'haensel@atv-systems.de'],
    "Chris Linders": [25, 'linders', 'linders@atv-systems.de'],
    "Christoph Klaus": [28, 'klaus', 'klaus@atv-systems.de'],
    "Benjamin Brückner": [31, 'brueckner', 'brueckner@atv-systems.de'],
    "Sarah Hauptmann": [34, 'hauptmann', 'sarah.hauptmann@atv-systems.de'],
    "Stefan Franke": [42, 'franke', 'franke@atv-systems.de'],
    "Nils Ziem": [43, 'ziem', 'ziem@atv-systems.de'],
    "Katja Röhnert": [46, 'roehnert', 'roehnert@atv-systems.de'],
    "Dirk Schulze": [47, 'schulze', 'schulze@atv-systems.de'],
    "Frank Sievers": [51, 'sievers', 'sievers@atv-systems.de'],
    "Kay-Erik Kunath": [54, 'kunath', 'kunath@atv-systems.de'],
    "Paulius Sakalas": [56, 'sakalas', 'sakalas@atv-systems.de'],
    "Nico Zocher": [57, 'zocher', 'zocher@atv-systems.de'],
    "Andreas Berdzentis": [59, 'berdzentis', 'berdzentis@atv-systems.de'],
    "Thomas Haufe": [61, 'haufe', 'haufe@atv-systems.de'],
    "Wolfgang Zschorn": [62, 'zschorn', 'zschorn@atv-systems.de'],
    "Alexander Conrad": [63, 'Conrad', 'conrad@atv-systems.de'],
    "Sylvia König": [65, 'koenigs', 'koenigs@atv-systems.de'],
    "Kristin Winter": [68, 'winter', 'winter@atv-systems.de'],
    "Steuer Prüfer": [70, 'pruefer', 'pruefer@localhost'],
    "Christian May": [71, 'may', 'may@atv-systems.de']
}


# Change to Unix Time Stamp, return unix_time_seconds
def to_unix_time(time):
    # print(time)
    year = int(time[0:4])
    month = int(time[5:7])
    day = int(time[8:10])
    hour = int(time[11:13])
    minute = int(time[14:16])
    second = int(time[17:19])
    # print(year, month, day, hour, minute, second)
    leap_year_count = int((year - 1972) / 4 + 1)
    # print("leap_year_count: ", leap_year_count)

    unix_time_days = ((year - 1970) * 365 + leap_year_count)

    # Counting final year days
    day_count_passed_month = 0
    if month == 2:
        day_count_passed_month = 31
    if month == 3:
        day_count_passed_month = 59
    if month == 4:
        day_count_passed_month = 90
    if month == 5:
        day_count_passed_month = 120
    if month == 6:
        day_count_passed_month = 151
    if month == 7:
        day_count_passed_month = 181
    if month == 8:
        day_count_passed_month = 212
    if month == 9:
        day_count_passed_month = 243
    if month == 10:
        day_count_passed_month = 273
    if month == 11:
        day_count_passed_month = 304
    if month == 12:
        day_count_passed_month = 334
    if (year / 4).is_integer():
        # print("This is leap year, check is February is passed")
        if month > 2:
            day_count_passed_month = day_count_passed_month + 1
    unix_time_days = unix_time_days + day_count_passed_month + day - 1
    unix_time_seconds = unix_time_days * 86400 + hour * 3600 + minute * 60 + second

    # Change timezone to Zulu(GMT) time
    str_length = len(time)
    # print(str_length)
    if str_length > 20:
        time_zone = int(time[21:23])
        unix_time_seconds = unix_time_seconds - time_zone * 3600
    return unix_time_seconds

# mysql_gitea
def get_repo_id(repo_name):
    # cmd_string = "mysql -uremoteroot -h192.168.2.189 -proot -sse \"SELECT id FROM gitea.repository WHERE NAME='{}';\"".format(repo_name)
    #
    # cmd = subprocess.Popen(cmd_string, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    #                        universal_newlines=True)
    #
    # subprocess_return = cmd.communicate()[0]
    # subprocess_return = int(subprocess_return)
    # print(subprocess_return)
    subprocess_return = "training_heatmap"
    return subprocess_return


def get_user_id(full_name):
    # cmd_string = "mysql -uremoteroot -h192.168.2.189 -proot -sse \"SELECT id FROM gitea.user WHERE NAME='{}';\"".format(full_name)
    #
    # cmd = subprocess.Popen(cmd_string, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    #                        universal_newlines=True)
    #
    # subprocess_return = cmd.communicate()[0]
    # # subprocess_return = int(subprocess_return)
    # print(subprocess_return, type(subprocess_return))
    subprocess_return = 123
    return subprocess_return

def get_commit_id():
    # cmd_string = "mysql -uremoteroot -h192.168.2.189 -proot -sse \"SELECT MAX(id) FROM gitea.action;\""
    #
    # cmd = subprocess.Popen(cmd_string, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    #                        universal_newlines=True)
    #
    # subprocess_return = cmd.communicate()[0]
    # commit_max_id = int(subprocess_return)
    # print(commit_max_id)
    commit_max_id = 999
    return commit_max_id

# get_repo_name("https://git.atvoigt.local/api/v1/repos/cheng/training_test/git/commits/86b455c2aba5a3e051a451ed27a99dbf8e31f0f8")
get_repo_id("training_heatmap")