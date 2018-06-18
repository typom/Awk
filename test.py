import os


def exec_awk(awk_prg, source_file, target_file=None):
    print("execute {}".format(awk_prg))
    sys_cmd_text = r'awk -f {0} {1}'
    if target_file:
        sys_cmd_text += " > {2}"
    sys_cmd = sys_cmd_text.format(awk_prg, source_file, target_file)
    os.system(sys_cmd)


awk_program = r'test.awk'
source_file = r'C:\Users\Alexandre\workspace\cestas\output\output01.csv'

print("Program starting")

exec_awk("source/field_list.awk", source_file,
         "output/field_list.csv")
exec_awk("source/accounts.awk", source_file,
         "output/accounts.csv")
exec_awk("source/simplout.awk", source_file,
         "output/simplout.csv")

# exec_awk("source/test.awk", source_file,
#         "output/delme.csv")
print("Program ended")
