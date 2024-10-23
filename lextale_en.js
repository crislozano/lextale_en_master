/******************* 
 * Lextale_En *
 *******************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2023.2.3.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'lextale_en';  // from the Builder filename that created this script
let expInfo = {
    'CUNYid*': '',
    'Name*': '',
    'LastName*': '',
    'College*': ["john-jay", "hostos"],
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
const lextale_en_instructions_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(lextale_en_instructions_loopLoopBegin(lextale_en_instructions_loopLoopScheduler));
flowScheduler.add(lextale_en_instructions_loopLoopScheduler);
flowScheduler.add(lextale_en_instructions_loopLoopEnd);


const lextale_en_practice_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(lextale_en_practice_loopLoopBegin(lextale_en_practice_loopLoopScheduler));
flowScheduler.add(lextale_en_practice_loopLoopScheduler);
flowScheduler.add(lextale_en_practice_loopLoopEnd);



flowScheduler.add(lextale_en_checkRoutineBegin());
flowScheduler.add(lextale_en_checkRoutineEachFrame());
flowScheduler.add(lextale_en_checkRoutineEnd());
const lextale_en_trial_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(lextale_en_trial_loopLoopBegin(lextale_en_trial_loopLoopScheduler));
flowScheduler.add(lextale_en_trial_loopLoopScheduler);
flowScheduler.add(lextale_en_trial_loopLoopEnd);


flowScheduler.add(lextale_en_endRoutineBegin());
flowScheduler.add(lextale_en_endRoutineEachFrame());
flowScheduler.add(lextale_en_endRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'instructions/lextale_en_instructions_text.xlsx', 'path': 'instructions/lextale_en_instructions_text.xlsx'},
    {'name': 'trials/lextale_practice_trials.xlsx', 'path': 'trials/lextale_practice_trials.xlsx'},
    {'name': 'trials/lextale_trials.xlsx', 'path': 'trials/lextale_trials.xlsx'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2023.2.3';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  psychoJS.setRedirectUrls('https://app.prolific.com/submissions/complete?cc=C72EX8CS', '');


  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["CUNYid*"]}_${expInfo["Name*"]}_${expInfo["LastName*"]}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var lextale_en_instructionsClock;
var text_lextale_en_instructions;
var key_resp_lextale_en_instructions;
var text_lextale_en_instructions_continue;
var lextale_en_practiceClock;
var text_lextale_en_practice_label;
var text_lextale_en_practice_word;
var key_resp_lextale_en_practice;
var text_lextale_en_practice_real_label;
var text_lextale_en_practice_false_label;
var lextale_en_practice_feedbackClock;
var text_lextale_eng_practice_feedback;
var key_resp_lextale_eng_practice_feedback;
var lextale_en_checkClock;
var text_lextale_en_check;
var key_resp_lextale_en_check;
var lextale_en_trialClock;
var text_lextale_en_trial_word;
var key_resp_lextale_en_trial;
var text_lextale_en_trial_real_label;
var text_lextale_en_trial_false_label;
var lextale_en_endClock;
var text_lextale_en_end;
var key_resp_lextale_en_end;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "lextale_en_instructions"
  lextale_en_instructionsClock = new util.Clock();
  text_lextale_en_instructions = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_lextale_en_instructions',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: 0.8, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_lextale_en_instructions = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_lextale_en_instructions_continue = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_lextale_en_instructions_continue',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "lextale_en_practice"
  lextale_en_practiceClock = new util.Clock();
  text_lextale_en_practice_label = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_lextale_en_practice_label',
    text: 'PRACTICE',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('red'),  opacity: 1,
    depth: 0.0 
  });
  
  text_lextale_en_practice_word = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_lextale_en_practice_word',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('blue'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_lextale_en_practice = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_lextale_en_practice_real_label = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_lextale_en_practice_real_label',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.3), (- 0.3)], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  text_lextale_en_practice_false_label = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_lextale_en_practice_false_label',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, (- 0.3)], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "lextale_en_practice_feedback"
  lextale_en_practice_feedbackClock = new util.Clock();
  text_lextale_eng_practice_feedback = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_lextale_eng_practice_feedback',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_lextale_eng_practice_feedback = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "lextale_en_check"
  lextale_en_checkClock = new util.Clock();
  text_lextale_en_check = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_lextale_en_check',
    text: 'Ready?\n\nPress the SPACE BAR to begin.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.09,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_lextale_en_check = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "lextale_en_trial"
  lextale_en_trialClock = new util.Clock();
  text_lextale_en_trial_word = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_lextale_en_trial_word',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('blue'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_lextale_en_trial = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_lextale_en_trial_real_label = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_lextale_en_trial_real_label',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.3), (- 0.3)], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  text_lextale_en_trial_false_label = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_lextale_en_trial_false_label',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, (- 0.3)], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "lextale_en_end"
  lextale_en_endClock = new util.Clock();
  text_lextale_en_end = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_lextale_en_end',
    text: 'End of the activity.\n\nThank you for participating!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_lextale_en_end = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var lextale_en_instructions_loop;
function lextale_en_instructions_loopLoopBegin(lextale_en_instructions_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    lextale_en_instructions_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'instructions/lextale_en_instructions_text.xlsx',
      seed: undefined, name: 'lextale_en_instructions_loop'
    });
    psychoJS.experiment.addLoop(lextale_en_instructions_loop); // add the loop to the experiment
    currentLoop = lextale_en_instructions_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisLextale_en_instructions_loop of lextale_en_instructions_loop) {
      snapshot = lextale_en_instructions_loop.getSnapshot();
      lextale_en_instructions_loopLoopScheduler.add(importConditions(snapshot));
      lextale_en_instructions_loopLoopScheduler.add(lextale_en_instructionsRoutineBegin(snapshot));
      lextale_en_instructions_loopLoopScheduler.add(lextale_en_instructionsRoutineEachFrame());
      lextale_en_instructions_loopLoopScheduler.add(lextale_en_instructionsRoutineEnd(snapshot));
      lextale_en_instructions_loopLoopScheduler.add(lextale_en_instructions_loopLoopEndIteration(lextale_en_instructions_loopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function lextale_en_instructions_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(lextale_en_instructions_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function lextale_en_instructions_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var lextale_en_practice_loop;
function lextale_en_practice_loopLoopBegin(lextale_en_practice_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    lextale_en_practice_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'trials/lextale_practice_trials.xlsx',
      seed: undefined, name: 'lextale_en_practice_loop'
    });
    psychoJS.experiment.addLoop(lextale_en_practice_loop); // add the loop to the experiment
    currentLoop = lextale_en_practice_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisLextale_en_practice_loop of lextale_en_practice_loop) {
      snapshot = lextale_en_practice_loop.getSnapshot();
      lextale_en_practice_loopLoopScheduler.add(importConditions(snapshot));
      lextale_en_practice_loopLoopScheduler.add(lextale_en_practiceRoutineBegin(snapshot));
      lextale_en_practice_loopLoopScheduler.add(lextale_en_practiceRoutineEachFrame());
      lextale_en_practice_loopLoopScheduler.add(lextale_en_practiceRoutineEnd(snapshot));
      lextale_en_practice_loopLoopScheduler.add(lextale_en_practice_feedbackRoutineBegin(snapshot));
      lextale_en_practice_loopLoopScheduler.add(lextale_en_practice_feedbackRoutineEachFrame());
      lextale_en_practice_loopLoopScheduler.add(lextale_en_practice_feedbackRoutineEnd(snapshot));
      lextale_en_practice_loopLoopScheduler.add(lextale_en_practice_loopLoopEndIteration(lextale_en_practice_loopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function lextale_en_practice_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(lextale_en_practice_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function lextale_en_practice_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var lextale_en_trial_loop;
function lextale_en_trial_loopLoopBegin(lextale_en_trial_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    lextale_en_trial_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'trials/lextale_trials.xlsx',
      seed: undefined, name: 'lextale_en_trial_loop'
    });
    psychoJS.experiment.addLoop(lextale_en_trial_loop); // add the loop to the experiment
    currentLoop = lextale_en_trial_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisLextale_en_trial_loop of lextale_en_trial_loop) {
      snapshot = lextale_en_trial_loop.getSnapshot();
      lextale_en_trial_loopLoopScheduler.add(importConditions(snapshot));
      lextale_en_trial_loopLoopScheduler.add(lextale_en_trialRoutineBegin(snapshot));
      lextale_en_trial_loopLoopScheduler.add(lextale_en_trialRoutineEachFrame());
      lextale_en_trial_loopLoopScheduler.add(lextale_en_trialRoutineEnd(snapshot));
      lextale_en_trial_loopLoopScheduler.add(lextale_en_trial_loopLoopEndIteration(lextale_en_trial_loopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function lextale_en_trial_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(lextale_en_trial_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function lextale_en_trial_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var t;
var frameN;
var continueRoutine;
var _key_resp_lextale_en_instructions_allKeys;
var lextale_en_instructionsComponents;
function lextale_en_instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'lextale_en_instructions' ---
    t = 0;
    lextale_en_instructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('lextale_en_instructions.started', globalClock.getTime());
    text_lextale_en_instructions.setText(instructions_text);
    key_resp_lextale_en_instructions.keys = undefined;
    key_resp_lextale_en_instructions.rt = undefined;
    _key_resp_lextale_en_instructions_allKeys = [];
    text_lextale_en_instructions_continue.setText(continue_text);
    // keep track of which components have finished
    lextale_en_instructionsComponents = [];
    lextale_en_instructionsComponents.push(text_lextale_en_instructions);
    lextale_en_instructionsComponents.push(key_resp_lextale_en_instructions);
    lextale_en_instructionsComponents.push(text_lextale_en_instructions_continue);
    
    for (const thisComponent of lextale_en_instructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function lextale_en_instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'lextale_en_instructions' ---
    // get current time
    t = lextale_en_instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_lextale_en_instructions* updates
    if (t >= 0.0 && text_lextale_en_instructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_lextale_en_instructions.tStart = t;  // (not accounting for frame time here)
      text_lextale_en_instructions.frameNStart = frameN;  // exact frame index
      
      text_lextale_en_instructions.setAutoDraw(true);
    }
    
    
    // *key_resp_lextale_en_instructions* updates
    if (t >= 0.0 && key_resp_lextale_en_instructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_lextale_en_instructions.tStart = t;  // (not accounting for frame time here)
      key_resp_lextale_en_instructions.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_lextale_en_instructions.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_lextale_en_instructions.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_lextale_en_instructions.clearEvents(); });
    }
    
    if (key_resp_lextale_en_instructions.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_lextale_en_instructions.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_lextale_en_instructions_allKeys = _key_resp_lextale_en_instructions_allKeys.concat(theseKeys);
      if (_key_resp_lextale_en_instructions_allKeys.length > 0) {
        key_resp_lextale_en_instructions.keys = _key_resp_lextale_en_instructions_allKeys[_key_resp_lextale_en_instructions_allKeys.length - 1].name;  // just the last key pressed
        key_resp_lextale_en_instructions.rt = _key_resp_lextale_en_instructions_allKeys[_key_resp_lextale_en_instructions_allKeys.length - 1].rt;
        key_resp_lextale_en_instructions.duration = _key_resp_lextale_en_instructions_allKeys[_key_resp_lextale_en_instructions_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_lextale_en_instructions_continue* updates
    if (t >= 1.5 && text_lextale_en_instructions_continue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_lextale_en_instructions_continue.tStart = t;  // (not accounting for frame time here)
      text_lextale_en_instructions_continue.frameNStart = frameN;  // exact frame index
      
      text_lextale_en_instructions_continue.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of lextale_en_instructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function lextale_en_instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'lextale_en_instructions' ---
    for (const thisComponent of lextale_en_instructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('lextale_en_instructions.stopped', globalClock.getTime());
    key_resp_lextale_en_instructions.stop();
    // the Routine "lextale_en_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_lextale_en_practice_allKeys;
var lextale_en_practiceComponents;
function lextale_en_practiceRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'lextale_en_practice' ---
    t = 0;
    lextale_en_practiceClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('lextale_en_practice.started', globalClock.getTime());
    text_lextale_en_practice_word.setText(word);
    key_resp_lextale_en_practice.keys = undefined;
    key_resp_lextale_en_practice.rt = undefined;
    _key_resp_lextale_en_practice_allKeys = [];
    text_lextale_en_practice_real_label.setText('REAL');
    text_lextale_en_practice_false_label.setText('FALSE');
    // keep track of which components have finished
    lextale_en_practiceComponents = [];
    lextale_en_practiceComponents.push(text_lextale_en_practice_label);
    lextale_en_practiceComponents.push(text_lextale_en_practice_word);
    lextale_en_practiceComponents.push(key_resp_lextale_en_practice);
    lextale_en_practiceComponents.push(text_lextale_en_practice_real_label);
    lextale_en_practiceComponents.push(text_lextale_en_practice_false_label);
    
    for (const thisComponent of lextale_en_practiceComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function lextale_en_practiceRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'lextale_en_practice' ---
    // get current time
    t = lextale_en_practiceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_lextale_en_practice_label* updates
    if (t >= 0.0 && text_lextale_en_practice_label.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_lextale_en_practice_label.tStart = t;  // (not accounting for frame time here)
      text_lextale_en_practice_label.frameNStart = frameN;  // exact frame index
      
      text_lextale_en_practice_label.setAutoDraw(true);
    }
    
    
    // *text_lextale_en_practice_word* updates
    if (t >= 0.5 && text_lextale_en_practice_word.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_lextale_en_practice_word.tStart = t;  // (not accounting for frame time here)
      text_lextale_en_practice_word.frameNStart = frameN;  // exact frame index
      
      text_lextale_en_practice_word.setAutoDraw(true);
    }
    
    
    // *key_resp_lextale_en_practice* updates
    if (t >= 0.5 && key_resp_lextale_en_practice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_lextale_en_practice.tStart = t;  // (not accounting for frame time here)
      key_resp_lextale_en_practice.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_lextale_en_practice.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_lextale_en_practice.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_lextale_en_practice.clearEvents(); });
    }
    
    if (key_resp_lextale_en_practice.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_lextale_en_practice.getKeys({keyList: ['1', '0'], waitRelease: false});
      _key_resp_lextale_en_practice_allKeys = _key_resp_lextale_en_practice_allKeys.concat(theseKeys);
      if (_key_resp_lextale_en_practice_allKeys.length > 0) {
        key_resp_lextale_en_practice.keys = _key_resp_lextale_en_practice_allKeys[0].name;  // just the first key pressed
        key_resp_lextale_en_practice.rt = _key_resp_lextale_en_practice_allKeys[0].rt;
        key_resp_lextale_en_practice.duration = _key_resp_lextale_en_practice_allKeys[0].duration;
        // was this correct?
        if (key_resp_lextale_en_practice.keys == correct_response) {
            key_resp_lextale_en_practice.corr = 1;
        } else {
            key_resp_lextale_en_practice.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_lextale_en_practice_real_label* updates
    if (t >= 0.25 && text_lextale_en_practice_real_label.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_lextale_en_practice_real_label.tStart = t;  // (not accounting for frame time here)
      text_lextale_en_practice_real_label.frameNStart = frameN;  // exact frame index
      
      text_lextale_en_practice_real_label.setAutoDraw(true);
    }
    
    
    // *text_lextale_en_practice_false_label* updates
    if (t >= 0.25 && text_lextale_en_practice_false_label.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_lextale_en_practice_false_label.tStart = t;  // (not accounting for frame time here)
      text_lextale_en_practice_false_label.frameNStart = frameN;  // exact frame index
      
      text_lextale_en_practice_false_label.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of lextale_en_practiceComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function lextale_en_practiceRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'lextale_en_practice' ---
    for (const thisComponent of lextale_en_practiceComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('lextale_en_practice.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (key_resp_lextale_en_practice.keys === undefined) {
      if (['None','none',undefined].includes(correct_response)) {
         key_resp_lextale_en_practice.corr = 1;  // correct non-response
      } else {
         key_resp_lextale_en_practice.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_lextale_en_practice.corr, level);
    }
    psychoJS.experiment.addData('key_resp_lextale_en_practice.keys', key_resp_lextale_en_practice.keys);
    psychoJS.experiment.addData('key_resp_lextale_en_practice.corr', key_resp_lextale_en_practice.corr);
    if (typeof key_resp_lextale_en_practice.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_lextale_en_practice.rt', key_resp_lextale_en_practice.rt);
        psychoJS.experiment.addData('key_resp_lextale_en_practice.duration', key_resp_lextale_en_practice.duration);
        routineTimer.reset();
        }
    
    key_resp_lextale_en_practice.stop();
    // the Routine "lextale_en_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var msg;
var _key_resp_lextale_eng_practice_feedback_allKeys;
var lextale_en_practice_feedbackComponents;
function lextale_en_practice_feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'lextale_en_practice_feedback' ---
    t = 0;
    lextale_en_practice_feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('lextale_en_practice_feedback.started', globalClock.getTime());
    // Run 'Begin Routine' code from code_4
    if ((key_resp_lextale_en_practice.corr === 1)) {
        msg = "Correct!";
    } else {
        msg = "Ooo! You made a mistake!";
    }
    
    text_lextale_eng_practice_feedback.setText(msg);
    key_resp_lextale_eng_practice_feedback.keys = undefined;
    key_resp_lextale_eng_practice_feedback.rt = undefined;
    _key_resp_lextale_eng_practice_feedback_allKeys = [];
    // keep track of which components have finished
    lextale_en_practice_feedbackComponents = [];
    lextale_en_practice_feedbackComponents.push(text_lextale_eng_practice_feedback);
    lextale_en_practice_feedbackComponents.push(key_resp_lextale_eng_practice_feedback);
    
    for (const thisComponent of lextale_en_practice_feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function lextale_en_practice_feedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'lextale_en_practice_feedback' ---
    // get current time
    t = lextale_en_practice_feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_lextale_eng_practice_feedback* updates
    if (t >= 0.0 && text_lextale_eng_practice_feedback.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_lextale_eng_practice_feedback.tStart = t;  // (not accounting for frame time here)
      text_lextale_eng_practice_feedback.frameNStart = frameN;  // exact frame index
      
      text_lextale_eng_practice_feedback.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_lextale_eng_practice_feedback.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_lextale_eng_practice_feedback.setAutoDraw(false);
    }
    
    // *key_resp_lextale_eng_practice_feedback* updates
    if (t >= 0.0 && key_resp_lextale_eng_practice_feedback.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_lextale_eng_practice_feedback.tStart = t;  // (not accounting for frame time here)
      key_resp_lextale_eng_practice_feedback.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_lextale_eng_practice_feedback.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_lextale_eng_practice_feedback.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_lextale_eng_practice_feedback.clearEvents(); });
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp_lextale_eng_practice_feedback.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_lextale_eng_practice_feedback.status = PsychoJS.Status.FINISHED;
        }
      
    if (key_resp_lextale_eng_practice_feedback.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_lextale_eng_practice_feedback.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_lextale_eng_practice_feedback_allKeys = _key_resp_lextale_eng_practice_feedback_allKeys.concat(theseKeys);
      if (_key_resp_lextale_eng_practice_feedback_allKeys.length > 0) {
        key_resp_lextale_eng_practice_feedback.keys = _key_resp_lextale_eng_practice_feedback_allKeys[_key_resp_lextale_eng_practice_feedback_allKeys.length - 1].name;  // just the last key pressed
        key_resp_lextale_eng_practice_feedback.rt = _key_resp_lextale_eng_practice_feedback_allKeys[_key_resp_lextale_eng_practice_feedback_allKeys.length - 1].rt;
        key_resp_lextale_eng_practice_feedback.duration = _key_resp_lextale_eng_practice_feedback_allKeys[_key_resp_lextale_eng_practice_feedback_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of lextale_en_practice_feedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function lextale_en_practice_feedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'lextale_en_practice_feedback' ---
    for (const thisComponent of lextale_en_practice_feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('lextale_en_practice_feedback.stopped', globalClock.getTime());
    key_resp_lextale_eng_practice_feedback.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_lextale_en_check_allKeys;
var lextale_en_checkComponents;
function lextale_en_checkRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'lextale_en_check' ---
    t = 0;
    lextale_en_checkClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('lextale_en_check.started', globalClock.getTime());
    key_resp_lextale_en_check.keys = undefined;
    key_resp_lextale_en_check.rt = undefined;
    _key_resp_lextale_en_check_allKeys = [];
    // keep track of which components have finished
    lextale_en_checkComponents = [];
    lextale_en_checkComponents.push(text_lextale_en_check);
    lextale_en_checkComponents.push(key_resp_lextale_en_check);
    
    for (const thisComponent of lextale_en_checkComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function lextale_en_checkRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'lextale_en_check' ---
    // get current time
    t = lextale_en_checkClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_lextale_en_check* updates
    if (t >= 0.0 && text_lextale_en_check.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_lextale_en_check.tStart = t;  // (not accounting for frame time here)
      text_lextale_en_check.frameNStart = frameN;  // exact frame index
      
      text_lextale_en_check.setAutoDraw(true);
    }
    
    
    // *key_resp_lextale_en_check* updates
    if (t >= 0.0 && key_resp_lextale_en_check.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_lextale_en_check.tStart = t;  // (not accounting for frame time here)
      key_resp_lextale_en_check.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_lextale_en_check.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_lextale_en_check.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_lextale_en_check.clearEvents(); });
    }
    
    if (key_resp_lextale_en_check.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_lextale_en_check.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_lextale_en_check_allKeys = _key_resp_lextale_en_check_allKeys.concat(theseKeys);
      if (_key_resp_lextale_en_check_allKeys.length > 0) {
        key_resp_lextale_en_check.keys = _key_resp_lextale_en_check_allKeys[_key_resp_lextale_en_check_allKeys.length - 1].name;  // just the last key pressed
        key_resp_lextale_en_check.rt = _key_resp_lextale_en_check_allKeys[_key_resp_lextale_en_check_allKeys.length - 1].rt;
        key_resp_lextale_en_check.duration = _key_resp_lextale_en_check_allKeys[_key_resp_lextale_en_check_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of lextale_en_checkComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function lextale_en_checkRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'lextale_en_check' ---
    for (const thisComponent of lextale_en_checkComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('lextale_en_check.stopped', globalClock.getTime());
    key_resp_lextale_en_check.stop();
    // the Routine "lextale_en_check" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_lextale_en_trial_allKeys;
var lextale_en_trialComponents;
function lextale_en_trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'lextale_en_trial' ---
    t = 0;
    lextale_en_trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('lextale_en_trial.started', globalClock.getTime());
    text_lextale_en_trial_word.setText(word);
    key_resp_lextale_en_trial.keys = undefined;
    key_resp_lextale_en_trial.rt = undefined;
    _key_resp_lextale_en_trial_allKeys = [];
    text_lextale_en_trial_real_label.setText('REAL');
    text_lextale_en_trial_false_label.setText('FALSE');
    // keep track of which components have finished
    lextale_en_trialComponents = [];
    lextale_en_trialComponents.push(text_lextale_en_trial_word);
    lextale_en_trialComponents.push(key_resp_lextale_en_trial);
    lextale_en_trialComponents.push(text_lextale_en_trial_real_label);
    lextale_en_trialComponents.push(text_lextale_en_trial_false_label);
    
    for (const thisComponent of lextale_en_trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function lextale_en_trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'lextale_en_trial' ---
    // get current time
    t = lextale_en_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_lextale_en_trial_word* updates
    if (t >= 0.5 && text_lextale_en_trial_word.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_lextale_en_trial_word.tStart = t;  // (not accounting for frame time here)
      text_lextale_en_trial_word.frameNStart = frameN;  // exact frame index
      
      text_lextale_en_trial_word.setAutoDraw(true);
    }
    
    
    // *key_resp_lextale_en_trial* updates
    if (t >= 0.5 && key_resp_lextale_en_trial.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_lextale_en_trial.tStart = t;  // (not accounting for frame time here)
      key_resp_lextale_en_trial.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_lextale_en_trial.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_lextale_en_trial.start(); }); // start on screen flip
    }
    
    if (key_resp_lextale_en_trial.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_lextale_en_trial.getKeys({keyList: ['1', '0'], waitRelease: false});
      _key_resp_lextale_en_trial_allKeys = _key_resp_lextale_en_trial_allKeys.concat(theseKeys);
      if (_key_resp_lextale_en_trial_allKeys.length > 0) {
        key_resp_lextale_en_trial.keys = _key_resp_lextale_en_trial_allKeys[0].name;  // just the first key pressed
        key_resp_lextale_en_trial.rt = _key_resp_lextale_en_trial_allKeys[0].rt;
        key_resp_lextale_en_trial.duration = _key_resp_lextale_en_trial_allKeys[0].duration;
        // was this correct?
        if (key_resp_lextale_en_trial.keys == correct_response) {
            key_resp_lextale_en_trial.corr = 1;
        } else {
            key_resp_lextale_en_trial.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_lextale_en_trial_real_label* updates
    if (t >= 0.25 && text_lextale_en_trial_real_label.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_lextale_en_trial_real_label.tStart = t;  // (not accounting for frame time here)
      text_lextale_en_trial_real_label.frameNStart = frameN;  // exact frame index
      
      text_lextale_en_trial_real_label.setAutoDraw(true);
    }
    
    
    // *text_lextale_en_trial_false_label* updates
    if (t >= 0.25 && text_lextale_en_trial_false_label.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_lextale_en_trial_false_label.tStart = t;  // (not accounting for frame time here)
      text_lextale_en_trial_false_label.frameNStart = frameN;  // exact frame index
      
      text_lextale_en_trial_false_label.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of lextale_en_trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function lextale_en_trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'lextale_en_trial' ---
    for (const thisComponent of lextale_en_trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('lextale_en_trial.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (key_resp_lextale_en_trial.keys === undefined) {
      if (['None','none',undefined].includes(correct_response)) {
         key_resp_lextale_en_trial.corr = 1;  // correct non-response
      } else {
         key_resp_lextale_en_trial.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_lextale_en_trial.corr, level);
    }
    psychoJS.experiment.addData('key_resp_lextale_en_trial.keys', key_resp_lextale_en_trial.keys);
    psychoJS.experiment.addData('key_resp_lextale_en_trial.corr', key_resp_lextale_en_trial.corr);
    if (typeof key_resp_lextale_en_trial.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_lextale_en_trial.rt', key_resp_lextale_en_trial.rt);
        psychoJS.experiment.addData('key_resp_lextale_en_trial.duration', key_resp_lextale_en_trial.duration);
        routineTimer.reset();
        }
    
    key_resp_lextale_en_trial.stop();
    // the Routine "lextale_en_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_lextale_en_end_allKeys;
var lextale_en_endComponents;
function lextale_en_endRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'lextale_en_end' ---
    t = 0;
    lextale_en_endClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('lextale_en_end.started', globalClock.getTime());
    key_resp_lextale_en_end.keys = undefined;
    key_resp_lextale_en_end.rt = undefined;
    _key_resp_lextale_en_end_allKeys = [];
    // keep track of which components have finished
    lextale_en_endComponents = [];
    lextale_en_endComponents.push(text_lextale_en_end);
    lextale_en_endComponents.push(key_resp_lextale_en_end);
    
    for (const thisComponent of lextale_en_endComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function lextale_en_endRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'lextale_en_end' ---
    // get current time
    t = lextale_en_endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_lextale_en_end* updates
    if (t >= 0.0 && text_lextale_en_end.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_lextale_en_end.tStart = t;  // (not accounting for frame time here)
      text_lextale_en_end.frameNStart = frameN;  // exact frame index
      
      text_lextale_en_end.setAutoDraw(true);
    }
    
    
    // *key_resp_lextale_en_end* updates
    if (t >= 0.0 && key_resp_lextale_en_end.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_lextale_en_end.tStart = t;  // (not accounting for frame time here)
      key_resp_lextale_en_end.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      key_resp_lextale_en_end.clock.reset();
      key_resp_lextale_en_end.start();
    }
    
    if (key_resp_lextale_en_end.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_lextale_en_end.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_lextale_en_end_allKeys = _key_resp_lextale_en_end_allKeys.concat(theseKeys);
      if (_key_resp_lextale_en_end_allKeys.length > 0) {
        key_resp_lextale_en_end.keys = _key_resp_lextale_en_end_allKeys[_key_resp_lextale_en_end_allKeys.length - 1].name;  // just the last key pressed
        key_resp_lextale_en_end.rt = _key_resp_lextale_en_end_allKeys[_key_resp_lextale_en_end_allKeys.length - 1].rt;
        key_resp_lextale_en_end.duration = _key_resp_lextale_en_end_allKeys[_key_resp_lextale_en_end_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of lextale_en_endComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function lextale_en_endRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'lextale_en_end' ---
    for (const thisComponent of lextale_en_endComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('lextale_en_end.stopped', globalClock.getTime());
    key_resp_lextale_en_end.stop();
    // the Routine "lextale_en_end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
