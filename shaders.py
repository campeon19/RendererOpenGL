# Christian Daniel Pérez De León
# Carne: 19710
# Graficas por Computador

# GLSL

# Shader hecho en clase
vertex_shader = """
#version 450
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec2 texCoords;
uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;
uniform float tiempo;
uniform float valor;
uniform vec3 pointLight;
out vec3 outColor;
out vec2 outTexCoords;
void main()
{
    vec4 norm = vec4(normal, 0.0);
    vec4 pos = vec4(position, 1.0) + norm * valor;
    pos = modelMatrix * pos;
    vec4 light = vec4(pointLight, 1.0);
    float intensity = dot(modelMatrix * norm, normalize(light - pos));
    gl_Position = projectionMatrix * viewMatrix * pos;
    outColor = vec3(1.0,1.0 - valor * 2,1.0-valor * 2) * intensity;
    outTexCoords = texCoords;
}
"""


fragment_shader = """
#version 450
layout (location = 0) out vec4 fragColor;
in vec3 outColor;
in vec2 outTexCoords;
uniform sampler2D tex;
void main()
{
    fragColor = vec4(outColor, 1) * texture(tex, outTexCoords);
}
"""

# Toon shader
vertex_toonShader = """
#version 450
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec2 texCoords;
uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;
uniform float tiempo;
uniform float valor;
uniform vec3 pointLight;
out vec3 outColor;
out vec2 outTexCoords;
out float outIntensity;
void main()
{
    vec4 norm = vec4(normal, 0.0);
    vec4 pos = vec4(position, 1.0) + norm * valor;
    pos = modelMatrix * pos;
    vec4 light = vec4(pointLight, 1.0);
    outIntensity = dot(modelMatrix * norm, normalize(light - pos));
    gl_Position = projectionMatrix * viewMatrix * pos;
    outColor = vec3(1.0,1.0 - valor * 2,1.0-valor * 2);
    outTexCoords = texCoords;
}
"""

fragment_toonShader = """
#version 450
layout (location = 0) out vec4 fragColor;
in vec3 outColor;
in vec2 outTexCoords;
in float outIntensity;
uniform sampler2D tex;
void main()
{
    float intensity1 = outIntensity;
    if (outIntensity >= 0.8){
        intensity1 = 1;
    }
    else if (outIntensity >= 0.5){
        intensity1 = 0.5;
    }
    else if (outIntensity >= 0.2){
        intensity1 = 0.2;
    }
    else{
        intensity1 = 0;
    }
    fragColor = vec4(outColor, 1) * texture(tex, outTexCoords) * intensity1;
}
"""

# Inversion de colores
vertex_Shader2 = """
#version 450
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec2 texCoords;
uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;
uniform float tiempo;
uniform float valor;
uniform vec3 pointLight;
out vec3 outColor;
out vec2 outTexCoords;
out float outIntensity;
void main()
{
    vec4 norm = vec4(normal, 0.0);
    vec4 pos = vec4(position, 1.0) + norm * valor;
    pos = modelMatrix * pos;
    vec4 light = vec4(pointLight, 1.0);
    outIntensity = dot(modelMatrix * norm, normalize(light - pos));
    gl_Position = projectionMatrix * viewMatrix * pos;
    outColor = vec3(1.0,1.0 - valor * 2,1.0-valor * 2);
    outTexCoords = texCoords;
}
"""

fragment_Shader2 = """
#version 450
layout (location = 0) out vec4 fragColor;
in vec3 outColor;
in vec2 outTexCoords;
in float outIntensity;
uniform sampler2D tex;
void main()
{
    float b = (outColor[0] - 1) * -1;
    float g = (outColor.y - 1) * -1;
    float r = (outColor.z - 1) * -1;

    vec4 color1 = vec4(outColor, 1) * texture(tex, outTexCoords);

    fragColor = vec4(1 - color1.w, 1 - color1.x, 1 - color1.y, 1) * outIntensity;
}
"""

# Shader que agrega lineas verticales al objeto
vertex_Shader3 = """
#version 450
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec2 texCoords;
uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;
uniform float tiempo;
uniform float valor;
uniform vec3 pointLight;
out vec3 outColor;
out vec2 outTexCoords;
out vec3 outposition;
out vec3 outnormal;
out float outIntensity;
void main()
{
    outposition = position;
    outnormal = normal;
    vec4 norm = vec4(normal, 0.0);
    vec4 pos = vec4(position, 1.0) + norm * valor;
    pos = modelMatrix * pos;
    vec4 light = vec4(pointLight, 1.0);
    outIntensity = dot(modelMatrix * norm, normalize(light - pos));
    gl_Position = projectionMatrix * viewMatrix * pos;
    outColor = vec3(1.0,1.0 - valor * 2,1.0-valor * 2);
    outTexCoords = texCoords;
}
"""


fragment_Shader3 = """
#version 450
layout (location = 0) out vec4 fragColor;
in vec3 outColor;
in vec2 outTexCoords;
in vec3 outposition;
in vec3 outnormal;
in float outIntensity;
uniform sampler2D tex;

float pulse(float val, float dst) {
  return floor(mod(val*dst,1.0)+2.5);
}

void main()
{
    vec3 cpos = outposition;
    vec3 color = vec3(1.0, pulse(cpos.y,10.0), 1.0);

    fragColor = vec4(color, 1) * texture(tex, outTexCoords) * outIntensity;
}
"""

# Shader de luz de sirena de emergencia
vertex_Shader4 = """
#version 450
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec2 texCoords;
uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;
uniform float tiempo;
uniform float valor;
uniform vec3 pointLight;
out vec3 outColor;
out vec2 outTexCoords;
out vec3 outposition;
out vec3 outnormal;
out float outIntensity;
void main()
{
    outposition = position;
    outnormal = normal;
    vec4 norm = vec4(normal, 0.0);
    vec4 pos = vec4(position, 1.0) + norm * valor;
    pos = modelMatrix * pos;
    vec4 light = vec4(pointLight, 1.0);
    outIntensity = dot(modelMatrix * norm, normalize(light - pos));
    gl_Position = projectionMatrix * viewMatrix * pos;
    outColor = vec3(1.0,1.0 - valor * 2,1.0-valor * 2);
    outTexCoords = texCoords;
}
"""


fragment_Shader4 = """
#version 450
layout (location = 0) out vec4 fragColor;
in vec3 outColor;
in vec2 outTexCoords;
in vec3 outposition;
in vec3 outnormal;
in float outIntensity;
uniform sampler2D tex;
uniform float tiempo;

void main()
{
    float t = tiempo * 2;
    vec3 dir1 = vec3(cos(t),0,sin(t)); 
    vec3 dir2 = vec3(sin(t),0,cos(t));

    float diffuse1 = pow(dot(outnormal,dir1),2.0);
    float diffuse2 = pow(dot(outnormal,dir2),2.0);

    vec3 col1 = diffuse1 * vec3(1,0,0);
    vec3 col2 = diffuse2 * vec3(0,0,1);

    fragColor = vec4(col1 + col2, 1) * texture(tex, outTexCoords);
}
"""

# Shader que agrega lineas transparenes y deformaciones en x y z
vertex_Shader5 = """
#version 450
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec2 texCoords;
uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;
uniform float tiempo;
uniform float valor;
uniform vec3 pointLight;
const float pi=3.14159;
out vec3 outColor;
out vec2 outTexCoords;
out vec3 outposition;
out vec3 outnormal;
out float outIntensity;

vec2 Rotate2D(vec2 vec_in, float angle)
{
  vec2 vec_out;
  vec_out.x=cos(angle)*vec_in.x-sin(angle)*vec_in.y;
  vec_out.y=sin(angle)*vec_in.x+cos(angle)*vec_in.y;
  return vec_out;
}

void main()
{
    outposition = position;
    outnormal = normal;
    vec4 norm = vec4(normal, 0.0);
    vec4 pos = vec4(position, 1.0) + norm * valor;
    pos.xz = Rotate2D(pos.xz,0.5*pi*position.y*sin(2.0*tiempo));
    pos = modelMatrix * pos;
    vec4 light = vec4(pointLight, 1.0);
    outIntensity = dot(modelMatrix * norm, normalize(light - pos));
    gl_Position = projectionMatrix * viewMatrix * pos;
    outColor = vec3(1.0,1.0,1.0);
    outTexCoords = texCoords;
}
"""


fragment_Shader5 = """
#version 450
layout (location = 0) out vec4 fragColor;
in vec3 outColor;
in vec2 outTexCoords;
in vec3 outposition;
in vec3 outnormal;
in float outIntensity;
uniform sampler2D tex;
uniform float tiempo;

void main()
{
    fragColor = vec4(outColor, 1) * texture(tex, outTexCoords) * outIntensity;

    if(sin(90.0 * outposition.x)>0.5) discard;
}
"""

vertex_Shader6 = """
#version 450
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec2 texCoords;
uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;
uniform float tiempo;
uniform float valor;
uniform vec3 pointLight;
out vec3 outColor;
out vec2 outTexCoords;
out vec3 outposition;
out vec3 outnormal;
out float outIntensity;
void main()
{
    outposition = position;
    outnormal = normal;
    vec4 norm = vec4(normal, 0.0);
    vec4 pos = vec4(position, 1.0);
    pos = modelMatrix * pos;
    vec4 light = vec4(pointLight, 1.0);
    outIntensity = dot(modelMatrix * norm, normalize(light - pos));
    gl_Position = projectionMatrix * viewMatrix * pos;
    outColor = vec3(1.0,1.0,1.0);
    outTexCoords = texCoords;
}
"""


fragment_Shader6 = """
#version 450
layout (location = 0) out vec4 fragColor;
in vec3 outColor;
in vec2 outTexCoords;
in vec3 outposition;
in vec3 outnormal;
in float outIntensity;
uniform sampler2D tex;
uniform float tiempo;

vec3 color() {
  
  vec3 color = vec3(0.0, 0.0, 0.0);
  
  if( abs(mod( abs(outposition.x), abs(.2 * sin(tiempo) )   )) < .1){
    color.x = .2;
  }
  
  
  if( abs(mod(outposition.y, .2 * sin(tiempo + 1.0))) < .1){
    color.z = .9;
  }

  return color;
}

void main()
{
    fragColor = vec4(color(), 1) * outIntensity;
}
"""