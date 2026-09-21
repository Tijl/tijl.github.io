
var researcher_name = "Dr. Tijl Grootswagers"
var researcher_email = "T.Grootswagers@westernsydney.edu.au" //(X@student.westernsydney.edu.au)
var time_required = "2"

var debrief = '<p>Thank you for taking the time to complete this experiment.</p>'+
    '<p>Click here if you like to be contacted for paid research opportunities at the MARCS institute: <a href="https://forms.gle/F5QpQuSXGaf5mQQm7">https://forms.gle/F5QpQuSXGaf5mQQm7</a>'

var finishURL = 'https://uws.sona-systems.com/webstudy_credit.aspx?experiment_id=1591&credit_token=deef91f32896434090af2a2c326c9a77&survey_code='

/* initialize jsPsych */
var jsPsych = initJsPsych({
    show_progress_bar: true,
    auto_update_progress_bar: false,
    message_progress_bar: 'Experiment progress',
    show_preload_progress_bar: true,
    on_finish: function() { 
        window.location.href = "../finish.html"
    }
});

var surveyCode = jsPsych.data.getURLVariable('survey');

var debug = surveyCode==1234

if (!surveyCode) {
    surveyCode = 'test'
    console.log(surveyCode)
}
var finishURLcode = finishURL + surveyCode;
var HTMLExperimentEnd = '<div id="endscreen" class="endscreen" style="width:1000px"><div class="endscreen" style="text-align:center; border:0px solid; padding:10px; font-size:120%; width:800px; float:right">'+
    '<p><br><br><br>Experiment Finished!</p><p>'+debrief+'</div></div>';   

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

stimuli = []
images = []
for (var i=0;i<stimlist.length;i++) {
    stimuli.push(stimlist[i])
    images.push(stimlist[i])
}
shuffle(stimuli);
//stimuli = stimuli.slice(0,2) //for debugging

console.log(stimuli)
var nstimuli = stimuli.length

/* create triplets */
var ntrials = 40;
if (debug) {ntrials=2};
var triplets = []
for (var e1=0;e1<nstimuli;e1++){
for (var e2=e1+1;e2<nstimuli;e2++){
for (var e3=e2+1;e3<nstimuli;e3++){
    shuffle(triplets.push([e1,e2,e3]));
}}}
triplets = shuffle(triplets);
triplets = triplets.slice(0,ntrials)
console.log(triplets)

/* create timeline */
var timeline = []

// these array can be passed into the preload plugin using the images, audio 
// and video parameters
var preload = {
    type: jsPsychPreload,
    images: stimuli.concat(['arrangement_demo.png']),
    max_load_time: 600000,
    message: 'Please wait while the experiment loads. This may take a few minutes.',
    error_message: 'The experiment failed to load. Please try again or contact the researcher.'
}
timeline.push(preload)

var instr = {
    type: jsPsychHtmlButtonResponse,
    stimulus: "<p><img src='"+stimuli[20]+"''></img>&nbsp<img src='"+stimuli[30]+"''></img>&nbsp<img src='"+stimuli[40]+"''></img></p>"+"<p>In this experiment, you will see sets of 3 simple images.</p>"+
            "<p>Use the mouse to select which image is the most different from the other two (the odd one out).</p>" +
            "<p>Do not think about it too long, and go with your first response.</p>",
    choices: ["START"],
    prompt: "<p>DISCLAIMER: This page does not store your responses after you close this window.<br />Your responses are not saved nor used for any purpose.</p>",
    post_trial_gap: 200,
    response_ends_trial: true,
}
timeline.push(instr)

for (var trialnr=0; trialnr<ntrials; trialnr++) { 
    var trial = {
        type: jsPsychHtmlTriplet,
        stimulus: '',
        choices: triplets[trialnr],
        button_html: ['<img src="'+images[triplets[trialnr][0]]+'">',
                    '<img src="'+images[triplets[trialnr][1]]+'">',
                    '<img src="'+images[triplets[trialnr][2]]+'">'],
        prompt: 'click on the odd one out',
        margin_horizontal: '8px',
        margin_vertical: '4px',
        data: {stim0:images[triplets[trialnr][0]],
               stim1:images[triplets[trialnr][1]],
               stim2:images[triplets[trialnr][2]],
               trialnr:trialnr,
               test_part:'triplet'},
        post_trial_gap: 500,
        on_finish: function(data){
            var count = jsPsych.data.get().filter({test_part: 'triplet'}).count()
            jsPsych.setProgressBar(count/ntrials)
        },
    }
    timeline.push(trial)
}

for (var i=0; i<100; i++) { 
    var feedback = {
        type: jsPsychImageButtonResponse,
        stimulus: stimuli[i],
        stimulus_width: 100,
        maintain_aspect_ratio: true,
        trial_duration: 50,
        choices: [],
        prompt: "<p>Calculating arrangement: "+i+"%</p>",
    }
    timeline.push(feedback)
}

var feedback = {
    type: jsPsychImageButtonResponse,
    stimulus: 'arrangement_demo.png',
    stimulus_width: 500,
    maintain_aspect_ratio: true,
    choices: ['FINISHED'],
    prompt: "<p>An example resulting stimulus arrangement is shown above.</p><p>Click the button to exit the experiment</p>",
}
timeline.push(feedback)

/* start the experiment */
jsPsych.run(timeline)
