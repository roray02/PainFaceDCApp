# PainFace DataCollection App

The PainFace Data Collection App is a convenient GUI that can be used to easily record videos for the PainFace grimace analysis software. The PFDC App is compatible with the most updated version of Raspberry Pi OS (Bullseye)

## Folder Contents

The installation folder contains a [python script](https://github.com/roray02/PainFaceDCApp/blob/main/app/PainFaceDataCollectionGUI.py) that will be the primary means of running the app, and an image asset that is utilized by the app.

## Usage
1) Navigate to folder in which app is stored:
```bash
cd directory
```
2) Use this command to run the script:
```bash
python PainFaceDataCollectionGUI.py
```
3) The following interface will appear:
![gui1](https://user-images.githubusercontent.com/69780075/159828712-e32e9b4d-9d0e-4583-8ca7-3b6fa7f9d297.JPG)
4) Enter the desired file ID, directory in which the video & .csv file will be saved, and the recording duration values.
5) Adjust the camera settings to your desired levels, by using the "Open Preview" button to match your preferences.
6) Select if you would like the recording information to be saved in the daily .csv file, and click the "Start Recording" button to record your video!
7) Once the video is done recording, the following screen will pop up to confirm if you would like to continue recording videos or stop, and if you choose to continue, all the settings from the previous recording will be saved.
![gui2](https://user-images.githubusercontent.com/69780075/159829262-9ab601b5-56cc-4aa3-8f15-03c976acc13f.JPG)
8) The video recording data can be viewed at the created .csv file in the directory that was selected in Step 4, which will save all of the day's recording information in 1 file.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
