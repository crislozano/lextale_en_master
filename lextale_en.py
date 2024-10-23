#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on Wed Oct 23 18:09:00 2024
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'lextale_en'  # from the Builder filename that created this script
expInfo = {
    'CUNYid*': '',
    'Name*': '',
    'LastName*': '',
    'College*': ["john-jay", "hostos"],
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s_%s' % (expInfo['CUNYid*'], expInfo['Name*'], expInfo['LastName*'], expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/cristinalozano/John Jay College Dropbox/Cristina Lozano/research/materials/proficiency/lextale/lextale_en_master/lextale_en.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1710, 1107], fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='iohub')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "lextale_en_instructions" ---
    text_lextale_en_instructions = visual.TextStim(win=win, name='text_lextale_en_instructions',
        text='',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=0.8, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_lextale_en_instructions = keyboard.Keyboard()
    text_lextale_en_instructions_continue = visual.TextStim(win=win, name='text_lextale_en_instructions_continue',
        text='',
        font='Arial',
        pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "lextale_en_practice" ---
    text_lextale_en_practice_label = visual.TextStim(win=win, name='text_lextale_en_practice_label',
        text='PRACTICE',
        font='Arial',
        pos=(0, 0.3), height=0.1, wrapWidth=None, ori=0, 
        color='red', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    text_lextale_en_practice_word = visual.TextStim(win=win, name='text_lextale_en_practice_word',
        text='',
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
        color='blue', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_lextale_en_practice = keyboard.Keyboard()
    text_lextale_en_practice_real_label = visual.TextStim(win=win, name='text_lextale_en_practice_real_label',
        text='',
        font='Arial',
        pos=(-0.3, -0.3), height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-3.0);
    text_lextale_en_practice_false_label = visual.TextStim(win=win, name='text_lextale_en_practice_false_label',
        text='',
        font='Arial',
        pos=(0.3, -0.3), height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "lextale_en_practice_feedback" ---
    text_lextale_eng_practice_feedback = visual.TextStim(win=win, name='text_lextale_eng_practice_feedback',
        text='',
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_lextale_eng_practice_feedback = keyboard.Keyboard()
    
    # --- Initialize components for Routine "lextale_en_check" ---
    text_lextale_en_check = visual.TextStim(win=win, name='text_lextale_en_check',
        text='Ready?\n\nPress the SPACE BAR to begin.',
        font='Arial',
        pos=(0, 0), height=0.09, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_lextale_en_check = keyboard.Keyboard()
    
    # --- Initialize components for Routine "lextale_en_trial" ---
    text_lextale_en_trial_word = visual.TextStim(win=win, name='text_lextale_en_trial_word',
        text='',
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
        color='blue', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_lextale_en_trial = keyboard.Keyboard()
    text_lextale_en_trial_real_label = visual.TextStim(win=win, name='text_lextale_en_trial_real_label',
        text='',
        font='Arial',
        pos=(-0.3, -0.3), height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-2.0);
    text_lextale_en_trial_false_label = visual.TextStim(win=win, name='text_lextale_en_trial_false_label',
        text='',
        font='Arial',
        pos=(0.3, -0.3), height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "lextale_en_end" ---
    text_lextale_en_end = visual.TextStim(win=win, name='text_lextale_en_end',
        text='End of the activity.\n\nThank you for participating!',
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_lextale_en_end = keyboard.Keyboard()
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # set up handler to look after randomisation of conditions etc
    lextale_en_instructions_loop = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('instructions/lextale_en_instructions_text.xlsx'),
        seed=None, name='lextale_en_instructions_loop')
    thisExp.addLoop(lextale_en_instructions_loop)  # add the loop to the experiment
    thisLextale_en_instructions_loop = lextale_en_instructions_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLextale_en_instructions_loop.rgb)
    if thisLextale_en_instructions_loop != None:
        for paramName in thisLextale_en_instructions_loop:
            globals()[paramName] = thisLextale_en_instructions_loop[paramName]
    
    for thisLextale_en_instructions_loop in lextale_en_instructions_loop:
        currentLoop = lextale_en_instructions_loop
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisLextale_en_instructions_loop.rgb)
        if thisLextale_en_instructions_loop != None:
            for paramName in thisLextale_en_instructions_loop:
                globals()[paramName] = thisLextale_en_instructions_loop[paramName]
        
        # --- Prepare to start Routine "lextale_en_instructions" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('lextale_en_instructions.started', globalClock.getTime())
        text_lextale_en_instructions.setText(instructions_text)
        key_resp_lextale_en_instructions.keys = []
        key_resp_lextale_en_instructions.rt = []
        _key_resp_lextale_en_instructions_allKeys = []
        text_lextale_en_instructions_continue.setText(continue_text)
        # keep track of which components have finished
        lextale_en_instructionsComponents = [text_lextale_en_instructions, key_resp_lextale_en_instructions, text_lextale_en_instructions_continue]
        for thisComponent in lextale_en_instructionsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "lextale_en_instructions" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_lextale_en_instructions* updates
            
            # if text_lextale_en_instructions is starting this frame...
            if text_lextale_en_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_lextale_en_instructions.frameNStart = frameN  # exact frame index
                text_lextale_en_instructions.tStart = t  # local t and not account for scr refresh
                text_lextale_en_instructions.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_lextale_en_instructions, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_lextale_en_instructions.status = STARTED
                text_lextale_en_instructions.setAutoDraw(True)
            
            # if text_lextale_en_instructions is active this frame...
            if text_lextale_en_instructions.status == STARTED:
                # update params
                pass
            
            # *key_resp_lextale_en_instructions* updates
            waitOnFlip = False
            
            # if key_resp_lextale_en_instructions is starting this frame...
            if key_resp_lextale_en_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_lextale_en_instructions.frameNStart = frameN  # exact frame index
                key_resp_lextale_en_instructions.tStart = t  # local t and not account for scr refresh
                key_resp_lextale_en_instructions.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_lextale_en_instructions, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_resp_lextale_en_instructions.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_lextale_en_instructions.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_lextale_en_instructions.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_lextale_en_instructions.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_lextale_en_instructions.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_lextale_en_instructions_allKeys.extend(theseKeys)
                if len(_key_resp_lextale_en_instructions_allKeys):
                    key_resp_lextale_en_instructions.keys = _key_resp_lextale_en_instructions_allKeys[-1].name  # just the last key pressed
                    key_resp_lextale_en_instructions.rt = _key_resp_lextale_en_instructions_allKeys[-1].rt
                    key_resp_lextale_en_instructions.duration = _key_resp_lextale_en_instructions_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_lextale_en_instructions_continue* updates
            
            # if text_lextale_en_instructions_continue is starting this frame...
            if text_lextale_en_instructions_continue.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                text_lextale_en_instructions_continue.frameNStart = frameN  # exact frame index
                text_lextale_en_instructions_continue.tStart = t  # local t and not account for scr refresh
                text_lextale_en_instructions_continue.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_lextale_en_instructions_continue, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_lextale_en_instructions_continue.status = STARTED
                text_lextale_en_instructions_continue.setAutoDraw(True)
            
            # if text_lextale_en_instructions_continue is active this frame...
            if text_lextale_en_instructions_continue.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in lextale_en_instructionsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "lextale_en_instructions" ---
        for thisComponent in lextale_en_instructionsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('lextale_en_instructions.stopped', globalClock.getTime())
        # the Routine "lextale_en_instructions" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'lextale_en_instructions_loop'
    
    
    # set up handler to look after randomisation of conditions etc
    lextale_en_practice_loop = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('trials/lextale_practice_trials.xlsx'),
        seed=None, name='lextale_en_practice_loop')
    thisExp.addLoop(lextale_en_practice_loop)  # add the loop to the experiment
    thisLextale_en_practice_loop = lextale_en_practice_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLextale_en_practice_loop.rgb)
    if thisLextale_en_practice_loop != None:
        for paramName in thisLextale_en_practice_loop:
            globals()[paramName] = thisLextale_en_practice_loop[paramName]
    
    for thisLextale_en_practice_loop in lextale_en_practice_loop:
        currentLoop = lextale_en_practice_loop
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisLextale_en_practice_loop.rgb)
        if thisLextale_en_practice_loop != None:
            for paramName in thisLextale_en_practice_loop:
                globals()[paramName] = thisLextale_en_practice_loop[paramName]
        
        # --- Prepare to start Routine "lextale_en_practice" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('lextale_en_practice.started', globalClock.getTime())
        text_lextale_en_practice_word.setText(word)
        key_resp_lextale_en_practice.keys = []
        key_resp_lextale_en_practice.rt = []
        _key_resp_lextale_en_practice_allKeys = []
        text_lextale_en_practice_real_label.setText('REAL')
        text_lextale_en_practice_false_label.setText('FALSE')
        # keep track of which components have finished
        lextale_en_practiceComponents = [text_lextale_en_practice_label, text_lextale_en_practice_word, key_resp_lextale_en_practice, text_lextale_en_practice_real_label, text_lextale_en_practice_false_label]
        for thisComponent in lextale_en_practiceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "lextale_en_practice" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_lextale_en_practice_label* updates
            
            # if text_lextale_en_practice_label is starting this frame...
            if text_lextale_en_practice_label.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_lextale_en_practice_label.frameNStart = frameN  # exact frame index
                text_lextale_en_practice_label.tStart = t  # local t and not account for scr refresh
                text_lextale_en_practice_label.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_lextale_en_practice_label, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_lextale_en_practice_label.status = STARTED
                text_lextale_en_practice_label.setAutoDraw(True)
            
            # if text_lextale_en_practice_label is active this frame...
            if text_lextale_en_practice_label.status == STARTED:
                # update params
                pass
            
            # *text_lextale_en_practice_word* updates
            
            # if text_lextale_en_practice_word is starting this frame...
            if text_lextale_en_practice_word.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                text_lextale_en_practice_word.frameNStart = frameN  # exact frame index
                text_lextale_en_practice_word.tStart = t  # local t and not account for scr refresh
                text_lextale_en_practice_word.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_lextale_en_practice_word, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_lextale_en_practice_word.status = STARTED
                text_lextale_en_practice_word.setAutoDraw(True)
            
            # if text_lextale_en_practice_word is active this frame...
            if text_lextale_en_practice_word.status == STARTED:
                # update params
                pass
            
            # *key_resp_lextale_en_practice* updates
            waitOnFlip = False
            
            # if key_resp_lextale_en_practice is starting this frame...
            if key_resp_lextale_en_practice.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                key_resp_lextale_en_practice.frameNStart = frameN  # exact frame index
                key_resp_lextale_en_practice.tStart = t  # local t and not account for scr refresh
                key_resp_lextale_en_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_lextale_en_practice, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_resp_lextale_en_practice.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_lextale_en_practice.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_lextale_en_practice.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_lextale_en_practice.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_lextale_en_practice.getKeys(keyList=['1','0'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_lextale_en_practice_allKeys.extend(theseKeys)
                if len(_key_resp_lextale_en_practice_allKeys):
                    key_resp_lextale_en_practice.keys = _key_resp_lextale_en_practice_allKeys[0].name  # just the first key pressed
                    key_resp_lextale_en_practice.rt = _key_resp_lextale_en_practice_allKeys[0].rt
                    key_resp_lextale_en_practice.duration = _key_resp_lextale_en_practice_allKeys[0].duration
                    # was this correct?
                    if (key_resp_lextale_en_practice.keys == str(correct_response)) or (key_resp_lextale_en_practice.keys == correct_response):
                        key_resp_lextale_en_practice.corr = 1
                    else:
                        key_resp_lextale_en_practice.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_lextale_en_practice_real_label* updates
            
            # if text_lextale_en_practice_real_label is starting this frame...
            if text_lextale_en_practice_real_label.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
                # keep track of start time/frame for later
                text_lextale_en_practice_real_label.frameNStart = frameN  # exact frame index
                text_lextale_en_practice_real_label.tStart = t  # local t and not account for scr refresh
                text_lextale_en_practice_real_label.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_lextale_en_practice_real_label, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_lextale_en_practice_real_label.status = STARTED
                text_lextale_en_practice_real_label.setAutoDraw(True)
            
            # if text_lextale_en_practice_real_label is active this frame...
            if text_lextale_en_practice_real_label.status == STARTED:
                # update params
                pass
            
            # *text_lextale_en_practice_false_label* updates
            
            # if text_lextale_en_practice_false_label is starting this frame...
            if text_lextale_en_practice_false_label.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
                # keep track of start time/frame for later
                text_lextale_en_practice_false_label.frameNStart = frameN  # exact frame index
                text_lextale_en_practice_false_label.tStart = t  # local t and not account for scr refresh
                text_lextale_en_practice_false_label.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_lextale_en_practice_false_label, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_lextale_en_practice_false_label.status = STARTED
                text_lextale_en_practice_false_label.setAutoDraw(True)
            
            # if text_lextale_en_practice_false_label is active this frame...
            if text_lextale_en_practice_false_label.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in lextale_en_practiceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "lextale_en_practice" ---
        for thisComponent in lextale_en_practiceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('lextale_en_practice.stopped', globalClock.getTime())
        # check responses
        if key_resp_lextale_en_practice.keys in ['', [], None]:  # No response was made
            key_resp_lextale_en_practice.keys = None
            # was no response the correct answer?!
            if str(correct_response).lower() == 'none':
               key_resp_lextale_en_practice.corr = 1;  # correct non-response
            else:
               key_resp_lextale_en_practice.corr = 0;  # failed to respond (incorrectly)
        # store data for lextale_en_practice_loop (TrialHandler)
        lextale_en_practice_loop.addData('key_resp_lextale_en_practice.keys',key_resp_lextale_en_practice.keys)
        lextale_en_practice_loop.addData('key_resp_lextale_en_practice.corr', key_resp_lextale_en_practice.corr)
        if key_resp_lextale_en_practice.keys != None:  # we had a response
            lextale_en_practice_loop.addData('key_resp_lextale_en_practice.rt', key_resp_lextale_en_practice.rt)
            lextale_en_practice_loop.addData('key_resp_lextale_en_practice.duration', key_resp_lextale_en_practice.duration)
        # the Routine "lextale_en_practice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "lextale_en_practice_feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('lextale_en_practice_feedback.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_4
        if key_resp_lextale_en_practice.corr == 1:
            msg = "Correct!"
        else:
            msg = "Ooo! You made a mistake!"
        text_lextale_eng_practice_feedback.setText(msg)
        key_resp_lextale_eng_practice_feedback.keys = []
        key_resp_lextale_eng_practice_feedback.rt = []
        _key_resp_lextale_eng_practice_feedback_allKeys = []
        # keep track of which components have finished
        lextale_en_practice_feedbackComponents = [text_lextale_eng_practice_feedback, key_resp_lextale_eng_practice_feedback]
        for thisComponent in lextale_en_practice_feedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "lextale_en_practice_feedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_lextale_eng_practice_feedback* updates
            
            # if text_lextale_eng_practice_feedback is starting this frame...
            if text_lextale_eng_practice_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_lextale_eng_practice_feedback.frameNStart = frameN  # exact frame index
                text_lextale_eng_practice_feedback.tStart = t  # local t and not account for scr refresh
                text_lextale_eng_practice_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_lextale_eng_practice_feedback, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_lextale_eng_practice_feedback.status = STARTED
                text_lextale_eng_practice_feedback.setAutoDraw(True)
            
            # if text_lextale_eng_practice_feedback is active this frame...
            if text_lextale_eng_practice_feedback.status == STARTED:
                # update params
                pass
            
            # if text_lextale_eng_practice_feedback is stopping this frame...
            if text_lextale_eng_practice_feedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_lextale_eng_practice_feedback.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_lextale_eng_practice_feedback.tStop = t  # not accounting for scr refresh
                    text_lextale_eng_practice_feedback.frameNStop = frameN  # exact frame index
                    # update status
                    text_lextale_eng_practice_feedback.status = FINISHED
                    text_lextale_eng_practice_feedback.setAutoDraw(False)
            
            # *key_resp_lextale_eng_practice_feedback* updates
            waitOnFlip = False
            
            # if key_resp_lextale_eng_practice_feedback is starting this frame...
            if key_resp_lextale_eng_practice_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_lextale_eng_practice_feedback.frameNStart = frameN  # exact frame index
                key_resp_lextale_eng_practice_feedback.tStart = t  # local t and not account for scr refresh
                key_resp_lextale_eng_practice_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_lextale_eng_practice_feedback, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_resp_lextale_eng_practice_feedback.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_lextale_eng_practice_feedback.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_lextale_eng_practice_feedback.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp_lextale_eng_practice_feedback is stopping this frame...
            if key_resp_lextale_eng_practice_feedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_lextale_eng_practice_feedback.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_lextale_eng_practice_feedback.tStop = t  # not accounting for scr refresh
                    key_resp_lextale_eng_practice_feedback.frameNStop = frameN  # exact frame index
                    # update status
                    key_resp_lextale_eng_practice_feedback.status = FINISHED
                    key_resp_lextale_eng_practice_feedback.status = FINISHED
            if key_resp_lextale_eng_practice_feedback.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_lextale_eng_practice_feedback.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_lextale_eng_practice_feedback_allKeys.extend(theseKeys)
                if len(_key_resp_lextale_eng_practice_feedback_allKeys):
                    key_resp_lextale_eng_practice_feedback.keys = _key_resp_lextale_eng_practice_feedback_allKeys[-1].name  # just the last key pressed
                    key_resp_lextale_eng_practice_feedback.rt = _key_resp_lextale_eng_practice_feedback_allKeys[-1].rt
                    key_resp_lextale_eng_practice_feedback.duration = _key_resp_lextale_eng_practice_feedback_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in lextale_en_practice_feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "lextale_en_practice_feedback" ---
        for thisComponent in lextale_en_practice_feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('lextale_en_practice_feedback.stopped', globalClock.getTime())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'lextale_en_practice_loop'
    
    
    # --- Prepare to start Routine "lextale_en_check" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('lextale_en_check.started', globalClock.getTime())
    key_resp_lextale_en_check.keys = []
    key_resp_lextale_en_check.rt = []
    _key_resp_lextale_en_check_allKeys = []
    # keep track of which components have finished
    lextale_en_checkComponents = [text_lextale_en_check, key_resp_lextale_en_check]
    for thisComponent in lextale_en_checkComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "lextale_en_check" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_lextale_en_check* updates
        
        # if text_lextale_en_check is starting this frame...
        if text_lextale_en_check.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_lextale_en_check.frameNStart = frameN  # exact frame index
            text_lextale_en_check.tStart = t  # local t and not account for scr refresh
            text_lextale_en_check.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_lextale_en_check, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_lextale_en_check.status = STARTED
            text_lextale_en_check.setAutoDraw(True)
        
        # if text_lextale_en_check is active this frame...
        if text_lextale_en_check.status == STARTED:
            # update params
            pass
        
        # *key_resp_lextale_en_check* updates
        waitOnFlip = False
        
        # if key_resp_lextale_en_check is starting this frame...
        if key_resp_lextale_en_check.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_lextale_en_check.frameNStart = frameN  # exact frame index
            key_resp_lextale_en_check.tStart = t  # local t and not account for scr refresh
            key_resp_lextale_en_check.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_lextale_en_check, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp_lextale_en_check.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_lextale_en_check.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_lextale_en_check.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_lextale_en_check.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_lextale_en_check.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_lextale_en_check_allKeys.extend(theseKeys)
            if len(_key_resp_lextale_en_check_allKeys):
                key_resp_lextale_en_check.keys = _key_resp_lextale_en_check_allKeys[-1].name  # just the last key pressed
                key_resp_lextale_en_check.rt = _key_resp_lextale_en_check_allKeys[-1].rt
                key_resp_lextale_en_check.duration = _key_resp_lextale_en_check_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in lextale_en_checkComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "lextale_en_check" ---
    for thisComponent in lextale_en_checkComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('lextale_en_check.stopped', globalClock.getTime())
    # the Routine "lextale_en_check" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    lextale_en_trial_loop = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('trials/lextale_trials.xlsx'),
        seed=None, name='lextale_en_trial_loop')
    thisExp.addLoop(lextale_en_trial_loop)  # add the loop to the experiment
    thisLextale_en_trial_loop = lextale_en_trial_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLextale_en_trial_loop.rgb)
    if thisLextale_en_trial_loop != None:
        for paramName in thisLextale_en_trial_loop:
            globals()[paramName] = thisLextale_en_trial_loop[paramName]
    
    for thisLextale_en_trial_loop in lextale_en_trial_loop:
        currentLoop = lextale_en_trial_loop
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisLextale_en_trial_loop.rgb)
        if thisLextale_en_trial_loop != None:
            for paramName in thisLextale_en_trial_loop:
                globals()[paramName] = thisLextale_en_trial_loop[paramName]
        
        # --- Prepare to start Routine "lextale_en_trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('lextale_en_trial.started', globalClock.getTime())
        text_lextale_en_trial_word.setText(word)
        key_resp_lextale_en_trial.keys = []
        key_resp_lextale_en_trial.rt = []
        _key_resp_lextale_en_trial_allKeys = []
        text_lextale_en_trial_real_label.setText('REAL')
        text_lextale_en_trial_false_label.setText('FALSE')
        # keep track of which components have finished
        lextale_en_trialComponents = [text_lextale_en_trial_word, key_resp_lextale_en_trial, text_lextale_en_trial_real_label, text_lextale_en_trial_false_label]
        for thisComponent in lextale_en_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "lextale_en_trial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_lextale_en_trial_word* updates
            
            # if text_lextale_en_trial_word is starting this frame...
            if text_lextale_en_trial_word.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                text_lextale_en_trial_word.frameNStart = frameN  # exact frame index
                text_lextale_en_trial_word.tStart = t  # local t and not account for scr refresh
                text_lextale_en_trial_word.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_lextale_en_trial_word, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_lextale_en_trial_word.status = STARTED
                text_lextale_en_trial_word.setAutoDraw(True)
            
            # if text_lextale_en_trial_word is active this frame...
            if text_lextale_en_trial_word.status == STARTED:
                # update params
                pass
            
            # *key_resp_lextale_en_trial* updates
            waitOnFlip = False
            
            # if key_resp_lextale_en_trial is starting this frame...
            if key_resp_lextale_en_trial.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                key_resp_lextale_en_trial.frameNStart = frameN  # exact frame index
                key_resp_lextale_en_trial.tStart = t  # local t and not account for scr refresh
                key_resp_lextale_en_trial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_lextale_en_trial, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_resp_lextale_en_trial.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_lextale_en_trial.clock.reset)  # t=0 on next screen flip
            if key_resp_lextale_en_trial.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_lextale_en_trial.getKeys(keyList=['1','0'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_lextale_en_trial_allKeys.extend(theseKeys)
                if len(_key_resp_lextale_en_trial_allKeys):
                    key_resp_lextale_en_trial.keys = _key_resp_lextale_en_trial_allKeys[0].name  # just the first key pressed
                    key_resp_lextale_en_trial.rt = _key_resp_lextale_en_trial_allKeys[0].rt
                    key_resp_lextale_en_trial.duration = _key_resp_lextale_en_trial_allKeys[0].duration
                    # was this correct?
                    if (key_resp_lextale_en_trial.keys == str(correct_response)) or (key_resp_lextale_en_trial.keys == correct_response):
                        key_resp_lextale_en_trial.corr = 1
                    else:
                        key_resp_lextale_en_trial.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_lextale_en_trial_real_label* updates
            
            # if text_lextale_en_trial_real_label is starting this frame...
            if text_lextale_en_trial_real_label.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
                # keep track of start time/frame for later
                text_lextale_en_trial_real_label.frameNStart = frameN  # exact frame index
                text_lextale_en_trial_real_label.tStart = t  # local t and not account for scr refresh
                text_lextale_en_trial_real_label.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_lextale_en_trial_real_label, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_lextale_en_trial_real_label.status = STARTED
                text_lextale_en_trial_real_label.setAutoDraw(True)
            
            # if text_lextale_en_trial_real_label is active this frame...
            if text_lextale_en_trial_real_label.status == STARTED:
                # update params
                pass
            
            # *text_lextale_en_trial_false_label* updates
            
            # if text_lextale_en_trial_false_label is starting this frame...
            if text_lextale_en_trial_false_label.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
                # keep track of start time/frame for later
                text_lextale_en_trial_false_label.frameNStart = frameN  # exact frame index
                text_lextale_en_trial_false_label.tStart = t  # local t and not account for scr refresh
                text_lextale_en_trial_false_label.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_lextale_en_trial_false_label, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_lextale_en_trial_false_label.status = STARTED
                text_lextale_en_trial_false_label.setAutoDraw(True)
            
            # if text_lextale_en_trial_false_label is active this frame...
            if text_lextale_en_trial_false_label.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in lextale_en_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "lextale_en_trial" ---
        for thisComponent in lextale_en_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('lextale_en_trial.stopped', globalClock.getTime())
        # check responses
        if key_resp_lextale_en_trial.keys in ['', [], None]:  # No response was made
            key_resp_lextale_en_trial.keys = None
            # was no response the correct answer?!
            if str(correct_response).lower() == 'none':
               key_resp_lextale_en_trial.corr = 1;  # correct non-response
            else:
               key_resp_lextale_en_trial.corr = 0;  # failed to respond (incorrectly)
        # store data for lextale_en_trial_loop (TrialHandler)
        lextale_en_trial_loop.addData('key_resp_lextale_en_trial.keys',key_resp_lextale_en_trial.keys)
        lextale_en_trial_loop.addData('key_resp_lextale_en_trial.corr', key_resp_lextale_en_trial.corr)
        if key_resp_lextale_en_trial.keys != None:  # we had a response
            lextale_en_trial_loop.addData('key_resp_lextale_en_trial.rt', key_resp_lextale_en_trial.rt)
            lextale_en_trial_loop.addData('key_resp_lextale_en_trial.duration', key_resp_lextale_en_trial.duration)
        # the Routine "lextale_en_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'lextale_en_trial_loop'
    
    
    # --- Prepare to start Routine "lextale_en_end" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('lextale_en_end.started', globalClock.getTime())
    key_resp_lextale_en_end.keys = []
    key_resp_lextale_en_end.rt = []
    _key_resp_lextale_en_end_allKeys = []
    # keep track of which components have finished
    lextale_en_endComponents = [text_lextale_en_end, key_resp_lextale_en_end]
    for thisComponent in lextale_en_endComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "lextale_en_end" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_lextale_en_end* updates
        
        # if text_lextale_en_end is starting this frame...
        if text_lextale_en_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_lextale_en_end.frameNStart = frameN  # exact frame index
            text_lextale_en_end.tStart = t  # local t and not account for scr refresh
            text_lextale_en_end.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_lextale_en_end, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_lextale_en_end.status = STARTED
            text_lextale_en_end.setAutoDraw(True)
        
        # if text_lextale_en_end is active this frame...
        if text_lextale_en_end.status == STARTED:
            # update params
            pass
        
        # *key_resp_lextale_en_end* updates
        
        # if key_resp_lextale_en_end is starting this frame...
        if key_resp_lextale_en_end.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_lextale_en_end.frameNStart = frameN  # exact frame index
            key_resp_lextale_en_end.tStart = t  # local t and not account for scr refresh
            key_resp_lextale_en_end.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_lextale_en_end, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp_lextale_en_end.status = STARTED
            # keyboard checking is just starting
            key_resp_lextale_en_end.clock.reset()  # now t=0
        if key_resp_lextale_en_end.status == STARTED:
            theseKeys = key_resp_lextale_en_end.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_lextale_en_end_allKeys.extend(theseKeys)
            if len(_key_resp_lextale_en_end_allKeys):
                key_resp_lextale_en_end.keys = _key_resp_lextale_en_end_allKeys[-1].name  # just the last key pressed
                key_resp_lextale_en_end.rt = _key_resp_lextale_en_end_allKeys[-1].rt
                key_resp_lextale_en_end.duration = _key_resp_lextale_en_end_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in lextale_en_endComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "lextale_en_end" ---
    for thisComponent in lextale_en_endComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('lextale_en_end.stopped', globalClock.getTime())
    # the Routine "lextale_en_end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
