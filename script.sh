text2wave -o left.wav left.txt
text2wave -o right.wav right.txt -eval "(voice_us1_mbrola)"
sox left.wav right.wav --channels 2 --combine merge stereo.wav mixer 0.8,0.2,0.2,0.8

#text2wave -o right.wav right.txt -eval "(voice_us1_mbrola)"

