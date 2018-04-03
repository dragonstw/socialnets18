import os
import numpy as np

admin_dir = 'admin'
work_dir = 'assignments'
grades_dir = 'grades'

def assign_reviewers(ls, tag=None):
    # brute force algorithm to find non-conflicting shuffle
    rv1 = np.random.permutation(ls)
    while np.any(rv1==ls):
        np.random.shuffle(rv1)

    log = open(os.path.join(
        grades_dir, "{}.peer_assignments.txt".format(hw_tag)), 'wb')

    # somewhat brute force algorithm to find second non-conflicting shuffle
    rv2 = []
    while True:
        try:
            rvtmp = list(np.random.permutation(ls))
            for i in reversed(xrange(len(rvtmp))):
                j = i
                while ls[i] == rvtmp[j] or rv1[i] == rvtmp[j]:
                    j -= 1
                if ls[i] == rvtmp[j] or rv1[i] == rvtmp[j]:
                    raise RuntimeError
                rv2.insert(0, rvtmp.pop(j))
            break
        except IndexError, RuntimeError:
            rv2 = []
    
    pairings = zip(ls, rv1, rv2)
    for p in pairings:
        if tag is None:
            print ",".join(p)
            log.write(",".join(p) + "\n")
        else:
            print tag.format(p[0], p[1], p[2])
            log.write(tag.format(p[0], p[1], p[2]) + "\n")

    log.close()
    return pairings


def read_rubric(hw_tag, header=None):
    listen = False
    out = ""
    with open(os.path.join(work_dir, "{}.md".format(hw_tag)), 'rb') as hw_file:
        for line in hw_file:
            if listen:
                out += line
            elif "# rubric" in line.lower():
                listen = True
                if header:
                    out = header + "\n"
                else:
                    out = line
            else:
                pass
    return out


def write_review_template(hw_tag):
    out_path = os.path.join(grades_dir, "{}.for_X_by_Y.md".format(hw_tag))
    rubric = read_rubric(hw_tag)
    with open(out_path, 'wb') as out_file:
        out_file.write(rubric)


if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description="Assign peer reviews and generate an eval form.")

    parser.add_argument('hw_list', metavar='hw_list', type=str, nargs='*',
                        default='hw0'.split(),
                        help='a homework assignment number or tag')
    parser.add_argument('-d', dest='due', action='store',
                        default=" by 12:00pm the day after tomorrow.",
                        help='a string describing the due date')
    parser.add_argument('-s', dest='student_file',
                        default=os.path.join(admin_dir, 'students.txt'),
                        type=argparse.FileType('r'),
                        help='edit admin/students.txt or supply another file')
    parser.add_argument('-a', '--assign', action='store_true',
                        help='choose to print out peer review assignments')
    
    opts = parser.parse_args()
    students = [s for s in opts.student_file.read().split("\n") if s]
    
    for hw_tag in opts.hw_list:
        if opts.assign:
            assignment_text = assign_reviewers(
                students,
                tag="{}, please complete a peer review on " + str(hw_tag) + \
                " for {} and {} " + opts.due )
            print

        write_review_template(hw_tag)
