# limf #
Pomf.se clone uploading tool
## Installation #
`pip install limf`  
Yep, that's all
###limf#
Main executable - uploads the file and can encrypt it if asked.  
Also can decrypt when right links is given.  
If file is uploaded to different host than chosen, it
just means that chosen host doesn't work.
###limfshot.sh #
Tool for making screenshots, uploading them, and putting link in clipboard.
Useful when used as bind to key.
####Depends #
* Python 3 - required for tool to work
* Requests library - required for tool to work
* scrot - for doing screenshots (limfshot.sh)
* xclip - for putting link into clipboard (limfshot.sh)  
* gpg - for encryption and decrytion
