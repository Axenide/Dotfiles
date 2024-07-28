function vcompatlb
    if test (count $argv) -lt 1
        echo "Usage: vcompat archivo.mp4 [tasa_de_bits]"
        return 1
    end

    set input_file $argv[1]
    set output_file (dirname $input_file)/(basename -s .mp4 $input_file)_converted.mp4

    if test (count $argv) -ge 2
        set bitrate $argv[2]"M"
    else
        set bitrate 1"M"
    end

    ffmpeg -i $input_file -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" -c:v libx264 -profile:v high -level:v 4.2 -pix_fmt yuv420p -movflags +faststart -b:v $bitrate -c:a aac -strict -2 $output_file
end
