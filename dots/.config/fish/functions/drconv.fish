function drconv
    if test (count $argv) -lt 1
        echo "Usage: drconv archivo1 archivo2 ..."
        return 1
    end

    for file in $argv
        if test -f $file
            set output_file (dirname $file)/(basename -s .mp4 $file)_dr.mov
            ffmpeg -i $file -vcodec mjpeg -q:v 2 -acodec pcm_s16be -q:a 0 -f mov $output_file
            echo "Processed: $file -> $output_file"
        else
            echo "Skipping: $file (not a regular file)"
        end
    end
end
