var researcher_name = "Dr. Tijl Grootswagers"
var researcher_email = "T.Grootswagers@westernsydney.edu.au" //(X@student.westernsydney.edu.au)
var time_required = "2"

/* initialize jsPsych */
var jsPsych = initJsPsych({
    show_progress_bar: true,
    auto_update_progress_bar: false,
    message_progress_bar: 'Experiment progress',
    show_preload_progress_bar: true,
    on_finish: function(data) {
        var mean_correct = Math.round(100*data.filter({test_part: 'stim'}).select('correct').mean())
        window.location.href = "../finish.html?id="+btoa(btoa(mean_correct))
    }
});

var surveyCode = jsPsych.data.getURLVariable('survey');

var debug = surveyCode==1234

if (!surveyCode) {
    surveyCode = 'test'
    console.log(surveyCode)
}

var categories = ['AI','REAL']
var taskdescription = "AI versus REAL"

var online = document.currentScript.getAttribute('data-online')=="1"
if (online) {
    console.log("online mode")
} else {
    console.log("offline mode")
}
function endExperiment(dataset,callback) {
    console.log(dataset) // comment out to avoid console log
    setTimeout(callback,500)
}

/* shuffle function */
function shuffle(a) {
    var j, x, i;
    for (i = a.length - 1; i > 0; i--) {
        j = Math.floor(Math.random() * (i + 1));
        x = a[i];
        a[i] = a[j];
        a[j] = x;
    }
    return a;
}

var start = Math.floor(20*Math.random()>0.5);
stimuli = []
for (var i=start;i<stimlist.length;i+=20) {
    stimuli.push(stimlist[i])
}
shuffle(stimlist);
shuffle(stimuli);
if (debug) {
    stimuli = stimuli.slice(0,2) //for debugging
}

//console.log(stimuli)
var nstimuli = stimuli.length
var ntrials = stimuli.length
var taskinstr = "[z] "+categories[0]+" ----- "+categories[1]+" [m]"

/* create timeline */
var timeline = []

// these array can be passed into the preload plugin using the images, audio 
// and video parameters
var preload = {
    type: jsPsychPreload,
    images: stimuli,
    max_load_time: 600000,
    message: 'Please wait while the experiment loads. This may take a few minutes.',
    error_message: 'The experiment failed to load. Please try again or contact the researcher.'
}
timeline.push(preload)

var instr = {
    type: jsPsychHtmlButtonResponse,
    stimulus: "<p>Welcome!</p><p><img width=256px; src='"+stimlist[0]+"''></img>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<img width=256px; src='"+stimlist[1]+"''></img></p>"+
    "<p>In this demo, you will see real and AI-generated images like the ones above.</p>"+
        "<p>Categorise images as AI or REAL as best as you can</p>"+
        "<p>It will take just a few minutes</p>"+
        "<p>Press the button to start</p>",
    choices: ["START"],
    prompt: "<p>DISCLAIMER: This page does not store your responses after you close this window.<br />Your responses are not saved nor used for any purpose other than displaying your accuracy.</p>",
    post_trial_gap: 200,
    response_ends_trial: true,
}
timeline.push(instr)

for (var trialnr=0; trialnr<ntrials; trialnr++) { 

    var stim = stimuli[trialnr]
    var trial = {
        type: jsPsychHtmlButtonResponse,
        stimulus: "<img width=256px; src='"+stim+"''></img>",
        data: {trialnr:trialnr,test_part:'stim',stim:stim,task:taskinstr},
        choices: ['AI','REAL'],
        response_ends_trial: true,
        on_finish: function(data){
            // Score the response as correct or incorrect.
            var isreal = data.stim.includes('Real')
            var correct = (data.response==1) == isreal
            if(correct){
              data.correct = true;
            } else {
              data.correct = false; 
            }
          },
    }
    timeline.push(trial)

    var feedback = {
        type: jsPsychHtmlKeyboardResponse,
        stimulus: function() {
            var last_trial_correct = jsPsych.data.get().last(1).values()[0].correct;
            //console.log(noresponse)
            if (last_trial_correct) {
                return '<p style="color:green;">CORRECT</p>'
            } else {
                return '<p style="color:red;">INCORRECT</p>'
            }
        },
        data: {trialnr:trialnr,test_part:'feedback'},
        choices: [],
        trial_duration: 1000,
        response_ends_trial: false,
        on_finish: function(){
            var count = jsPsych.data.get().filter({test_part: 'stim'}).count()
            jsPsych.setProgressBar(count/ntrials)
        }
    }
    timeline.push(feedback)
}

/* start the experiment */
jsPsych.run(timeline)
