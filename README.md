get_dpreview
============
Python script that will fetch an image from dpreviews finnished challenges. The image is a random image from the first five stpots on all the challeges present on the first page (its easy to change te script to get only winners, for example).

dpreview
--------
This is a great photography site that hosts regular challenges. This challenges usually have entries with very high quality, being a good source for things like desktop wallpapers. For more information go to site: http://www.dpreview.com/

Desktop wallpaper in Linux
--------------------------
A simple way to have a different wallpaper on Linux (I tried this on KDE/Kubuntu):
1) Copy an image to your home folder, named wallpaper1.jpg
2) Set that image as the wallpaper
3) Run this script to get a new image from dpreview and overwrite the old one

Crontab line used to change wallpaper every 5 minutes:
*/5 * * * * python /home/user/python/get_dpreview/get_dpreview.py /home/user/wallpaper1.jpg && convert /home/user/wallpaper1.jpg -resize '1366x768' /home/user/wallpaper1.jpg && convert /home/user/wallpaper1.jpg -profile /usr/share/color/icc/colord/sRGB.icc /home/user/wallpaper1.jpg

convert is there to fix some image issues (Adobe profiles) and to get the image to a smaller size.
