// edge.scd
// SuperCollider script for local sound reconstruction
// Part of "Sound at the Edge" framework

(
s.waitForBoot {
    var activeSynths = Dictionary.new;
    var stopTasks = Dictionary.new;

    SynthDef(\simplePiano, { |freq=440, amp=0.5, gate=1|
        var env = EnvGen.kr(Env.adsr(0.01, 0.2, 0.6, 0.3), gate, doneAction: 2);
        var sig = SinOsc.ar(freq, 0, env * amp);
        Out.ar(0, sig!2);
    }).add;

    OSCdef(\midiHandler, { |msg, time, addr, recvPort|
        var args = msg[1..];
        if(args.size == 2) {
            var isOn = args[0].asInteger;
            var midiNote = args[1].asInteger;
            var freq = midiNote.midicps;

            if(isOn == 1) {
                ("🎧 Note ON: " ++ midiNote ++ " (" ++ freq ++ " Hz)").postln;

                if(stopTasks[midiNote].notNil) {
                    stopTasks[midiNote].stop;
                    stopTasks.removeAt(midiNote);
                };

                if(activeSynths[midiNote].isNil) {
                    var synth = Synth(\simplePiano, [\freq, freq]);
                    activeSynths[midiNote] = synth;
                };
            } {
                ("🔇 Note OFF: " ++ midiNote).postln;

                if(activeSynths[midiNote].notNil) {
                    activeSynths[midiNote].set(\gate, 0);
                    stopTasks[midiNote] = SystemClock.sched(0.5, {
                        activeSynths.removeAt(midiNote);
                    });
                };
            };
        };
    }, \midi);
}
)
