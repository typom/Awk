import os


def exec_awk(awk_prg, source_file, target_file=None):
    sys_cmd_text = r'awk -f {0} {1}'
    if target_file:
        sys_cmd_text += " > {2}"
    sys_cmd = sys_cmd_text.format(awk_prg, source_file, target_file)
    os.system(sys_cmd)


awk_program = r'test.awk'
source_file = r'C:\Users\Alexandre\workspace\cestas\output\output01.csv'
field_list = "field_list.csv"

print("Program starting")

exec_awk("source/field_list.awk", source_file,
         "output/field_list.csv")

print("Program ended")
