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
        var HTMLExperimentEnd = '<p style="text-align: center;">&nbsp;</p>'+
        '<p style="text-align: center;">&nbsp;</p>'+
        '<p style="text-align: center;">&nbsp;</p>'+
        '<p style="text-align: center;">&nbsp;</p>'+
        '<p style="text-align: center;">You were on average <strong>'+mean_correct+'</strong>% correct!</p>'+
        '<p style="text-align: center;"><a class="twitter-share-button" href="https://twitter.com/share?ref_src=twsrc%5Etfw" data-size="large" data-text="I spotted '+mean_correct+'% of #deepfakes! Beat my score here: " data-url="https://tijl.github.io/demos/demo_faces" data-related="tgrootswagers" data-show-count="true" target="_blank">Share your result on twitter</a></p>'+
        '<p style="text-align: center;">&nbsp;</p>'+
        '<p style="text-align: left;">&nbsp;</p>'+
        '<p style="text-align: left;">This demo was developed by&nbsp;<a title="Website" href="https://tijl.github.io/" target="_blank"><strong>Tijl Grootswagers </strong></a>using <a href="https://www.jspsych.org/7.2/" target="_blank">jspsych7.2</a></p>'+
        '<p><a class="twitter-follow-button" href="https://twitter.com/tgrootswagers?ref_src=twsrc%5Etfw" data-show-count="true" target="_blank">Follow @tgrootswagers</a></p>'
        document.write(HTMLExperimentEnd)
    }
});

var surveyCode = jsPsych.data.getURLVariable('survey');

var debug = surveyCode==1234

if (!surveyCode) {
    surveyCode = 'test'
    console.log(surveyCode)
}

var categories = ['synthetic','real']
var taskdescription = "synthetic versus real"

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
    type: jsPsychHtmlKeyboardResponse,
    stimulus: "<img src='"+stimuli[20]+"''></img>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<img src='"+stimuli[30]+"''></img>",
    prompt: "In this experiment, you will see images of real and computer-generated people like the ones above.<br />"+
        "Your task is to categorise "+taskdescription+" people using these keys:<br />"+
        taskinstr+"<br /><br />Press [m] to continue",
    choices: ["m"],
    post_trial_gap: 200,
    response_ends_trial: true,
}
timeline.push(instr)

var instr = {
    type: jsPsychHtmlKeyboardResponse,
    stimulus: "",
    prompt: "The experiment starts now<br /><br />"+
        taskinstr+"<br /><br />Press [z] to continue",
    choices: ["z"],
    post_trial_gap: 1000,
    response_ends_trial: true,
}
timeline.push(instr)

for (var trialnr=0; trialnr<ntrials; trialnr++) { 

    var stim = stimuli[trialnr]
    var trial = {
        type: jsPsychHtmlKeyboardResponse,
        stimulus: "<img width=256px; src='"+stim+"''></img>",
        data: {trialnr:trialnr,test_part:'stim',stim:stim,task:taskinstr},
        choices: ['z','m'],
        prompt: taskinstr,
        response_ends_trial: true,
        on_finish: function(data){
            // Score the response as correct or incorrect.
            var isreal = data.stim.includes('Real')
            var correct = jsPsych.pluginAPI.compareKeys(data.response, "m") == isreal
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

// var feedback = {
//     type: jsPsychHtmlButtonResponse,
//     stimulus: function() {
//         var mean_correct = Math.round(100*jsPsych.data.get().filter({test_part: 'stim'}).select('correct').mean())
//         return '<p>You were on average '+mean_correct+'% correct!</p>'
//     },
//     data: {trialnr:trialnr,test_part:'feedback'},
//     choices: [],
//     choices: ['FINISHED'],
//     prompt: "<p>Click this button to exit the experiment</p>",
// }

// /* define debrief */
// var debrief_block = {
//     type: jsPsychHtmlKeyboardResponse,
//     stimulus: function() {
//         var mean_correct = Math.round(100*jsPsych.data.get().filter({test_part: 'stim'}).select('correct').mean())
//         return '<p>You were on average '+mean_correct+'% correct!</p>'
//     }
// };
// timeline.push(debrief_block);
// timeline.push(feedback)

/* start the experiment */
jsPsych.run(timeline)
