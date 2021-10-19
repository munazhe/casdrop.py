# Casdrop 

## Things you need before we get started: 

A. You know your TV `(CASDROP_TV_NAME)` and Speaker `(CASDROP_SPKR_NAME)` name. 

B. Your machine is running python `~> 3.9.7` (not mandatory, but you need at least python 3).

C. Install all dependencies to run this program: `pip install requirements.txt`

&nbsp;
&nbsp;

## Once that's done...

**Step1**. Open a new terminal on your unix/linux based computer 
> **NOTE**: make sure you're running in a BASH environment

&nbsp;
**Step2**. Open `params.sh` and edit the `<>` with your own values

&nbsp;
**Step3**. Run the following command in your terminal:
	***ONLY RUN THIS ONCE!***

	`bash params.sh #you may need to run this command with elevated privileges`

&nbsp;
**Step4**. Do the following:

	1. Start a simple HTTP server:
		`python -m SimpleHTTPServer`

	2. Start the casting service: 
		`python3 casdrop.py`

	3. Drop a file in your watch `CASDROP_WATCH_FOLDER` folder

	**At this point, depending on which file (.mp4 || .mp3) you uploaded it should start streaming on the device.**


&nbsp;
&nbsp;
### Reference: 
- `CASDROP_WATCH_FOLDER` => A folder you drop files in, to cast to device(s)

- `CASDROP_SERVER_URL` => The `IP` address you get from `SimpleHTTPServer` a.k.a `(http://<ip_address>)`

- `CASDROP_SPKR_NAME` and CASDROP_TV_NAME=> Displayed name of devices with (Ussually shown in cast menu on YouTube or Spotify mobile app)

### Here's my sample `param.sh` file
![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/suis1utat4vqnlhl42cv.png)


&nbsp;
### Features, Suggestions, TODO:

Currently you can drop a `.mp3` or `.mp4` which will cast with zero problem. However, I plan on adding more features down 
the road...

**Let me know in the comments if you'd like me to make a video explaining this is more detail**
