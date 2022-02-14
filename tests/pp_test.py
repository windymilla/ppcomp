import argparse
from ppcomp.ppcomp import *

args = None

def test_load_text_file():
    textfile = PgdpFileText(args)
    textfile.load('fossilplants1.txt')
    length = len(textfile.text_lines)
    assert length == 19647
    textfile.process_args()
    assert not textfile.from_pgdp_rounds


def test_load_html_file():
    htmlfile = PgdpFileHtml(args)
    htmlfile.load('fossilplants1.html')
    length = len(htmlfile.text_lines)
    assert length == 24190
    assert htmlfile.tree


def test_load_pgdp_file():
    textfile = PgdpFileText(args)
    textfile.load('projectID123456.txt')
    length = len(textfile.text_lines)
    assert length == 19647
    textfile.process_args()
    assert textfile.from_pgdp_rounds


def load_args():
    args = ['fossilplants1.html', 'fossilplants1.txt']
    parser = argparse.ArgumentParser(description='Diff text document for PGDP PP.')
    parser.add_argument('filename', metavar='FILENAME', type=str,
                        help='input files', nargs=2)
    parser.add_argument('--ignore-case', action='store_true', default=False,
                        help='Ignore case when comparing')
    parser.add_argument('--extract-footnotes', action='store_true', default=False,
                        help='Extract and process footnotes separately')
    parser.add_argument('--suppress-footnote-tags', action='store_true', default=False,
                        help='TXT: Suppress "[Footnote ?:" marks')
    parser.add_argument('--suppress-illustration-tags', action='store_true', default=False,
                        help='TXT: Suppress "[Illustration:" marks')
    parser.add_argument('--suppress-sidenote-tags', action='store_true', default=False,
                        help='TXT: Suppress "[Sidenote:" marks')
    parser.add_argument('--ignore-format', action='store_true', default=False,
                        help='In Px/Fx versions, silence formatting differences')
    parser.add_argument('--suppress-proofers-notes', action='store_true', default=False,
                        help="In Px/Fx versions, remove [**proofreaders notes]")
    parser.add_argument('--regroup-split-words', action='store_true', default=False,
                        help="In Px/Fx versions, regroup split wo-* *rds")
    parser.add_argument('--txt-cleanup-type', type=str, default='b',
                        help="TXT: In Px/Fx versions, type of text cleaning -- (b)est effort,"
                             " (n)one, (p)roofers")
    parser.add_argument('--css-add-illustration', action='store_true', default=False,
                        help="HTML: add [Illustration ] tag")
    parser.add_argument('--css-add-sidenote', action='store_true', default=False,
                        help="HTML: add [Sidenote: ...]")
    parser.add_argument('--css-smcap', type=str, default=None,
                        help="HTML: Transform small caps into uppercase (U), lowercase (L) or"
                             " title case (T)")
    parser.add_argument('--css-bold', type=str, default=None,
                        help="HTML: Surround bold strings with this string")
    parser.add_argument('--css', type=str, default=[], action='append',
                        help="HTML: Insert transformation CSS")
    parser.add_argument('--css-no-default', action='store_true', default=False,
                        help="HTML: do not use default transformation CSS")
    parser.add_argument('--suppress-nbsp-num', action='store_true', default=False,
                        help="HTML: Suppress non-breakable spaces between numbers")
    parser.add_argument('--ignore-0-space', action='store_true', default=False,
                        help='HTML: suppress zero width space (U+200b)')
    parser.add_argument('--css-greek-title-plus', action='store_true', default=False,
                        help="HTML: use greek transliteration in title attribute")
    parser.add_argument('--simple-html', action='store_true', default=False,
                        help="HTML: Process the html file and print the output (debug)")
    args = parser.parse_args()

    # filename = ['tests/fossilplants1.html', 'tests/fossilplants1.txt'],
    # ignore_case = False,
    # extract_footnotes = False,
    # suppress_footnote_tags = False,
    # suppress_illustration_tags = False,
    # suppress_sidenote_tags = False,
    # ignore_format = False,
    # suppress_proofers_notes = False,
    # regroup_split_words = False,
    # txt_cleanup_type = 'b',
    # css_add_illustration = False,
    # css_add_sidenote = False,
    # css_smcap = None,
    # css_bold = None,
    # css = [],
    # css_no_default = False,
    # suppress_nbsp_num = False,
    # ignore_0_space = False,
    # css_greek_title_plus = False,
    # simple_html = False)

