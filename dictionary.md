# Commands dictionary

## Control Commands
* **execute** : Execute commands in pipeline
* **reset** : Reset pipeline
* **stop** : Stop program
* **show** : Show pipeline content
* **streams** : Show open streams
* **tracks** : Show available tracks

## Operation commands

### Main operations
* **open** *[file_path, file_id]* : Open new input stream at *file_path* and stores it with id *file_id*
* **close** *[file_id]* : Close input stream with id *file_id*
* **read** *[file_id, track_id, t="all"]* : Read t seconds of *file_id* and stores the track with *track_id* in the available tracks
* **write** *[file_path, track_id]* : Write the track with id *track_id* in *file_path*
* **free** *[track_id]* : Deletes the track with id *track_id* from available tracks
* **record** *[nchannels, framerate]* : Start recording from sound card
* **stop_record** *[track_id, nframes]* : Stop recording from sound card and store *nframes* frames in *track_id*



 
