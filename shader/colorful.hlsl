sampler sampler0: register(s0);

float frame;

struct PSInput {
	float4 diffuse: COLOR0;
	float2 texCoord: TEXCOORD0;
	float2 vPos: VPOS;
};

struct PSOutput {
    float4 color: COLOR0;
};

// Thanks to http://www.chilliant.com/rgb2hsv.html
float3 HUEtoRGB(in float H) {
	float R = abs(H * 6 - 3) - 1;
	float G = 2 - abs(H * 6 - 2);
	float B = 2 - abs(H * 6 - 4);
	return saturate(float3(R, G, B));
}

float3 HSLtoRGB(in float3 HSL) {
	float3 RGB = HUEtoRGB(HSL.x);
	float C = (1 - abs(2 * HSL.z - 1)) * HSL.y;
	return (RGB - 0.5) * C + HSL.z;
}

PSOutput PSColorful(PSInput In): COLOR0 {
	PSOutput Out;
	float hue = frac((0.9 * (In.vPos.x + In.vPos.y) + 0.6 * frame) / 360);
	float3 hsl = float3(hue, 0.2, 0.2);
	float3 color = HSLtoRGB(hsl);
	Out.color.rgb = color;
	Out.color.a = In.diffuse.a;
	return Out;
}

technique TecColorful {
	pass P0 {
		PixelShader = compile ps_3_0 PSColorful();
	}
}
