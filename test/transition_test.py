from minisoap.transition import Transition


def test_transition_base():
    tr = Transition([(0., 0.), (1., 1.)])
    assert tr.amplitude(.5) == .5 and tr.amplitude(
        .25) == .25 and tr.amplitude(.75) == .75


def test_transition_plus():
    tr = Transition([(0., 0.), (.5, 0.), (1., 1.)])
    assert tr.amplitude(.5) == 0 and tr.amplitude(
        .25) == 0 and tr.amplitude(.75) == .5


def test_transition_brutal():
    tr = Transition([(0., 1.), (.5, 0.), (.5, 1.), (1., 0.)])
    assert tr.amplitude(.5) == 1.0 and tr.amplitude(
        .25) == .5 and tr.amplitude(.75) == .5
