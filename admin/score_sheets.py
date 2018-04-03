import os
import re
from collections import defaultdict
# import shutil
import argparse
from admin.peer_reviewers import read_rubric

admin_dir = 'admin'
grades_dir = 'grades'

if __name__=="__main__":
    parser = argparse.ArgumentParser(
        description="Output homework score sheets for students")

    parser.add_argument('hw_tag', metavar='hw', type=str,
                        help='a homework assignment number or tag')
    parser.add_argument('-t', dest='template', action='store',
                        default=os.path.join('admin', 'score.md'),
                        help='an optional score.md-like template to copy')
    parser.add_argument('-s', dest='student_file',
                        default=os.path.join(admin_dir, 'students.txt'),
                        type=argparse.FileType('r'),
                        help='edit admin/students.txt or supply another file')

    opts = parser.parse_args()
    students = [s for s in opts.student_file.read().split("\n") if s]

    # Read in the template
    score_text = ""
    with open(opts.template, 'rb') as templ_file:
        rubric = read_rubric(opts.hw_tag, header="## Instructor Score: /100")
        # score_text = "# {} AGGREGATED SCORE: /100\n".format(opts.hw_tag)\
        #              + "*******************\n\n"\
        #              + "# Grades\n"\
        #              + rubric + "\n\n"\
        #              + "## Peer Grading: /100, /100\n"\
        #              + "## Late Penalty: 0%\n\n\n"
        # score_text += templ_file.read()
        template = templ_file.read()

    # Check peer review files in the grades directory
    grades_for = defaultdict(list)
    for f in os.listdir(grades_dir):
        m = re.match("{}.for_(.*)_by_(.*)\.md".format('hw0'), f)
        if not m:
            continue
        else:
            gradee = m.group(1)
            grader = m.group(2)
            if gradee not in students or grader not in students:
                print "WARNING: {} inconsistent w/ students.txt".format(f)
            grades_for[gradee].append(f)

    # Generate score sheets for each student
    for student in students:
        template_name = os.path.split(opts.template)[-1]
        scorefile = os.path.join(
            grades_dir, "{}.{}.{}".format(opts.hw_tag, student, template_name))

        # # Look for peer reviews
        # if len(grades_for[student]) != 2:
        #     print "WARNING: there are {} reviews for {}".format(
        #         len(grades_for[student]), student)
        # peer1, peer2 = "", ""
        # try:
        #     with open(os.path.join(
        #             grades_dir, grades_for[student][0]), 'rb') as fpeer1:
        #         peer1 = fpeer1.read()
        #     with open(os.path.join(
        #             grades_dir, grades_for[student][1]), 'rb') as fpeer2:
        #         peer2 = fpeer2.read()
        # except:
        #     pass

        # Write altogether
        with open(scorefile, 'wb') as scoref:
            scoref.write(template.format(rubric))
