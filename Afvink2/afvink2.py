from flask import Flask, render_template, request
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.Data import CodonTable


app = Flask(__name__)

@app.route('/', methods=["get"])
def translate():
    """er word een DNA sequentie verkregen van de html pagina en omgezet in
    een protein sequentie

    input: DNA sequentie

    output: protein sequentie
    """
    seq = request.args.get("Seq", "")
    try:
        bio_dna = Seq(seq, IUPAC.ambiguous_dna)
        standard_trans_table = CodonTable.ambiguous_dna_by_name["Standard"]
        eiwit_trans = bio_dna.translate(table=standard_trans_table)
    except:
        eiwit_trans = "kan niet vertalen"
    return render_template("afvink2.html", dna=seq, translate=eiwit_trans)
def main():
    app.run(debug=True)
main()
