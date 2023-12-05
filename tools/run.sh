script_dir=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
script_dir_name=$(basename $script_dir)
relative_path=$(realpath --relative-to="$script_dir" "$1")
# echo manim -qm $relative_path Main
# echo $script_dir_name
# docker run --rm -it -v "$script_dir:/manim" manimcommunity/manim manim -a -ql $relative_path
# docker run --rm -it -v "$script_dir:/manim" manimcommunity/manim manim -a -qh $relative_path
# docker run --rm -it -v "$script_dir:/manim" manimcommunity/manim manim -a -qk $relative_path
docker run --rm -it -v "$script_dir:/manim" mymanim manim -a -ql $relative_path --disable_caching