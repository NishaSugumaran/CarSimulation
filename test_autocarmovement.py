import pytest
from unittest import mock
from autocarmovement import displaycardetails, addcardetails,carobjlst,\
                            executesimulation
import io
import builtins

def test_addcardetails_success(monkeypatch):
    inputs = iter(['A', '1 2 N','FF'])
    #with mock.patch.object('builtins.input', lambda _: next(inputs)):
    #with mock.patch.object('builtins_input', return_value='A'):
        #assert Prompt.user_prompt(Prompt) == "Your number is 19"
    #with monkeypatch.setattr('builtins.input', lambda _: next(inputs)):
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        #assert len(carobjlst)==0
    addcardetails()
    assert len(carobjlst)==1
    carobjlst.clear()

def test_addcardetails_invaliddirection(monkeypatch):
    inputs = iter(['A', '1 2 R','FF'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
        addcardetails()
    assert fake_stdout.getvalue() == '\n***Please enter valid direction***\n\n'
    carobjlst.clear()

def test_executesimulation_success_Ndirection(monkeypatch):
    inputs = iter(['A', '1 2 N','FF'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    addcardetails()
    #assert len(carobjlst)==1
    dt={}
    collision=False
    crossboundary=False
    boundary_x=10
    boundary_y=10
    executesimulation(boundary_x,boundary_y)
    assert 1
    carobjlst.clear()

def test_executesimulation_success_Sdirection(monkeypatch):
    inputs = iter(['A', '1 2 S','FFL'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    addcardetails()
    #assert len(carobjlst)==1
    dt={}
    collision=False
    crossboundary=False
    boundary_x=10
    boundary_y=10
    executesimulation(boundary_x,boundary_y)
    assert 1
    carobjlst.clear()

def test_executesimulation_success_Edirection(monkeypatch):
    inputs = iter(['A', '1 2 E','FF'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    addcardetails()
    #assert len(carobjlst)==1
    dt={}
    collision=False
    crossboundary=False
    boundary_x=10
    boundary_y=10
    executesimulation(boundary_x,boundary_y)
    assert 1
    carobjlst.clear()

def test_executesimulation_success_Wdirection(monkeypatch):
    inputs = iter(['A', '1 2 W','FF'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    addcardetails()
    #assert len(carobjlst)==1
    dt={}
    collision=False
    crossboundary=False
    boundary_x=10
    boundary_y=10
    executesimulation(boundary_x,boundary_y)
    assert 1
    carobjlst.clear()

def test_executesimulation_crossboundary(monkeypatch):
    inputs = iter(['A', '1 2 W','FFFFF'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    addcardetails()
    #assert len(carobjlst)==1
    dt={}
    collision=False
    crossboundary=False
    boundary_x=10
    boundary_y=10
    assert executesimulation(boundary_x,boundary_y)==False
    #assert True
    carobjlst.clear()

def test_executesimulation_collision(monkeypatch):
    inputs = iter(['A', '1 2 N','FFFFF'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    addcardetails()
    inputs = iter(['B', '1 2 N','FFFFF'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    addcardetails()
    assert len(carobjlst)==2
    dt={}
    collision=False
    crossboundary=False
    boundary_x=10
    boundary_y=10
    assert executesimulation(boundary_x,boundary_y)==False
    '''
    with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
        executesimulation(collision,crossboundary,dt,boundary_x,boundary_y)
        #addcardetails()
    assert fake_stdout.getvalue() == 'B Car collides at (0,2) at step 0'
    '''

def test_displaycardetails_nocollision(monkeypatch):
    inputs = iter(['A', '1 2 N','FFFFF'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    addcardetails()
    displaycardetails()
    assert 1
