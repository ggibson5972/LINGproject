

def test_dev1():
    str = "(S (NP (DT the) (NN cat)) (VP (VBZ is) (PP (IN on) (NP (DT the) (NN bed)))) (. .))"


def test_dev2():
    str = "(S (NP (NNP John)) (VP (VBZ hit) (NP (DT the) (NN ball)))) (. .))"


def test_dev3():
    str = "(S (NP (NNP Tom)) (VP (VBZ ate) (NP (DT a) (JJ red) (NN apple)))) (. .))"


def test_dev4():
    str = "(S (NP (DT The) (JJ large) (NN cat)) (VP (VBZ ate) (NP (DT the) (JJ small ) (NN rat)))) (. .))"


def test_dev5():
    str = "(S (NP (DT The) (JJ large) (JJ grey) (NN elephant)) (VP (VBZ sat) (PP (IN on) (DT a) (NN Chair))) (. .))"


def test_dev6():
    str = "(S (NP (DT The) (NN cat)) (VP (VBZ thought) (S (NP (DT the) (NN tree)) (VP (VBN was) (JJ large)) (. .))"


def test_real1():
    str = "(S (PRN (-LRB- -LRB-) (: -) (: -) (-RRB- -RRB-)) (: -) (NP (JJ alpha) (NN Bisabolol)) (VP (VBZ has) (NP (DT" \
          "a) (JJ primary) (JJ antipeptic) (NN action)) (PP (VBG depending) (PP (IN on) (NP (NN dosage)))) (, ,) (SBAR" \
          "(WHNP (WDT which)) (S (VP (VBZ is) (RB not) (VP (VBN caused) (PP (IN by) (NP (NP (DT an) (NN alteration))" \
          "(PP (IN of) (NP (DT the) (NN p) (NN H) (NN value)))))))))) (. .))"


def test_real2():
    str = "(S (NP (NP (DT The) (JJ proteolytic) (NN activity)) (PP (IN of) (NP (NNP pepsin)))) (VP (VBZ is) (VP (VBN" \
          "reduced) (PP (IN by) (NP (CD 50) (NN percent))) (PP (IN through) (NP (NP (NN addition)) (PP (IN of) (NP (NN" \
          "bisabolol))))) (PP (IN in) (NP (NP (DT the) (NN ratio)) (PP (IN of) (NP (CD 1/0.5))))))) (. .))"


def test_real3():
    str = "(S (NP (NP (DT The) (JJ antipeptic) (NN action)) (PP (IN of) (NP (NN bisabolol)))) (ADVP (RB only)) (VP (VBZ" \
          "occurs) (PP (IN in) (NP (NP (NN case)) (PP (IN of) (NP (JJ direct) (NN contact)))))) (. .))"


def test_real4():
    str = "(S (PP (IN In) (NP (NP (NN case)) (PP (IN of) (NP (NP (DT a) (JJ previous) (NN contact)) (PP (IN with) (NP" \
          "(DT the) (NN substrate))))))) (, ,) (NP (DT the) (VBG inhibiting) (NN effect)) (VP (VBZ is) (VP (VBN lost)))" \
          "(. .))"

