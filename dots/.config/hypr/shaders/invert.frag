// Invert Colors

precision mediump float;
varying vec2 v_texcoord;
uniform sampler2D tex;

void main() {

    vec4 pixColor = texture2D(tex, v_texcoord);

    pixColor[0] = 1.0 - pixColor[0]; // Invertimos el canal rojo
    pixColor[1] = 1.0 - pixColor[1]; // Invertimos el canal verde
    pixColor[2] = 1.0 - pixColor[2]; // Invertimos el canal azul

    gl_FragColor = pixColor;
}
