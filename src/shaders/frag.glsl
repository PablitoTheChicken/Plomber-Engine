#version 330 core
out vec4 FragColor;

in vec3 Normal;  
in vec2 TexCoord;

// texture samplers
uniform sampler2D texture1;

uniform vec3 lightPositions[2];
uniform vec3 lightColors[2];

void main()
{
    // ambient
    float ambientStrength = 0.1;
    vec3 ambient = ambientStrength * lightColor;
  	
    // diffuse 
    vec3 norm = normalize(Normal);
    vec3 lightDir = normalize(lightPos - FragPos);
    float diff = max(dot(norm, lightDir), 0.0);
    vec3 diffuse = diff * lightColor;
            
    vec3 result = (ambient + diffuse) * objectColor;
    FragColor = vec4(result, 1.0);
}