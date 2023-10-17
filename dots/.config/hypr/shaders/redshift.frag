// Redshift

precision mediump float;
varying vec2 v_texcoord;
uniform sampler2D tex;

void main() {

    vec4 pixColor = texture2D(tex, v_texcoord);

//    pixColor[0] *= 0.5;
    pixColor[1] *= 0.75;
    pixColor[2] *= 0.5;

    gl_FragColor = pixColor;
}
