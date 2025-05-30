transform RGBCycle(child):
    Model().shader('MakeVisualNovels.RGBMap').texture(child, main=True, fit=True).texture("images/rgb_heat.png", fit=False)
    u_remap_strength(0.0)
    linear 4.0 u_remap_strength(1.0)
    pause 3.0
    linear 4.0 u_remap_strength(-1.0)
    pause 3.0
    linear 4.0 u_remap_strength(0.0)

    Model().shader('MakeVisualNovels.RGBMap').texture(child, main=True, fit=True).texture("images/rgb_nightvision.png", fit=False)
    u_remap_strength(0.0)
    linear 4.0 u_remap_strength(2.0)
    pause 3.0
    linear 4.0 u_remap_strength(-2.0)
    pause 3.0
    linear 4.0 u_remap_strength(0.0)

    Model().shader('MakeVisualNovels.RGBMap').texture(child, main=True, fit=True).texture("images/rgb_dream.png", fit=False)
    u_remap_strength(0.0)
    linear 4.0 u_remap_strength(0.5)
    pause 3.0
    linear 4.0 u_remap_strength(-0.5)
    pause 3.0
    linear 4.0 u_remap_strength(0.0)

    Model().shader('MakeVisualNovels.RGBMap').texture(child, main=True, fit=True).texture("images/rgb_pastel.png", fit=False)
    u_remap_strength(0.0)
    linear 4.0 u_remap_strength(1.1)
    pause 3.0
    linear 4.0 u_remap_strength(-1.1)
    pause 3.0
    linear 4.0 u_remap_strength(0.0)

    Model().shader('MakeVisualNovels.RGBMap').texture(child, main=True, fit=True).texture("images/rgb_cold.png", fit=False)
    u_remap_strength(0.0)
    linear 4.0 u_remap_strength(1.5)
    pause 3.0
    linear 4.0 u_remap_strength(-1.5)
    pause 3.0
    linear 4.0 u_remap_strength(0.0)

    Model().shader('MakeVisualNovels.RGBMap').texture(child, main=True, fit=True).texture("images/rgb_fire.png", fit=False)
    u_remap_strength(0.0)
    linear 4.0 u_remap_strength(1.0)
    pause 3.0
    linear 4.0 u_remap_strength(-1.0)
    pause 3.0
    linear 4.0 u_remap_strength(0.0)

    Model().shader('MakeVisualNovels.RGBMap').texture(child, main=True, fit=True).texture("images/rgb_underwater.png", fit=False)
    u_remap_strength(0.0)
    linear 4.0 u_remap_strength(1.0)
    pause 3.0
    linear 4.0 u_remap_strength(-1.0)
    pause 3.0
    linear 4.0 u_remap_strength(0.0)

    Model().shader('MakeVisualNovels.RGBMap').texture(child, main=True, fit=True).texture("images/rgb_alien.png", fit=False)
    u_remap_strength(0.0)
    linear 4.0 u_remap_strength(2.0)
    pause 3.0
    linear 4.0 u_remap_strength(-2.0)
    pause 3.0
    linear 4.0 u_remap_strength(0.0)

    Model().shader('MakeVisualNovels.RGBMap').texture(child, main=True, fit=True).texture("images/rgb_invert.png", fit=False)
    u_remap_strength(0.0)
    linear 4.0 u_remap_strength(1.0)
    pause 3.0
    linear 4.0 u_remap_strength(-1.0)
    pause 3.0
    linear 4.0 u_remap_strength(0.0)

    Model().shader('MakeVisualNovels.RGBMap').texture(child, main=True, fit=True).texture("images/rgb_lava.png", fit=False)
    u_remap_strength(0.0)
    linear 4.0 u_remap_strength(1.5)
    pause 3.0
    linear 4.0 u_remap_strength(-1.5)
    pause 3.0
    linear 4.0 u_remap_strength(0.0)

    Model().shader('MakeVisualNovels.RGBMap').texture(child, main=True, fit=True).texture("images/rgb_glitch.png", fit=False)
    u_remap_strength(0.0)
    linear 4.0 u_remap_strength(2.0)
    pause 3.0
    linear 4.0 u_remap_strength(-2.0)
    pause 3.0
    linear 4.0 u_remap_strength(0.0)

    Model().shader('MakeVisualNovels.RGBMap').texture(child, main=True, fit=True).texture("images/rgb_neon.png", fit=False)
    u_remap_strength(0.0)
    linear 4.0 u_remap_strength(1.2)
    pause 3.0
    linear 4.0 u_remap_strength(-1.2)
    pause 3.0
    linear 4.0 u_remap_strength(0.0)

    Model().shader('MakeVisualNovels.RGBMap').texture(child, main=True, fit=True).texture("images/rgb_dusty.png", fit=False)
    u_remap_strength(0.0)
    linear 4.0 u_remap_strength(0.8)
    pause 3.0
    linear 4.0 u_remap_strength(-0.8)
    pause 3.0
    linear 4.0 u_remap_strength(0.0)

    Model().shader('MakeVisualNovels.RGBMap').texture(child, main=True, fit=True).texture("images/rgb_metal.png", fit=False)
    u_remap_strength(0.0)
    linear 4.0 u_remap_strength(1.3)
    pause 3.0
    linear 4.0 u_remap_strength(-1.3)
    pause 3.0
    linear 4.0 u_remap_strength(0.0)

    repeat


transform RGBLava(child):
    Model().shader('MakeVisualNovels.RGBMap').texture(child, main=True, fit=True).texture("images/rgb_lava.png", fit=False)
    u_remap_strength(1.5)

transform RGBGlitch(child):
    Model().shader('MakeVisualNovels.RGBMap').texture(child, main=True, fit=True).texture("images/rgb_glitch.png", fit=False)
    u_remap_strength(2.0)

transform RGBNeon(child):
    Model().shader('MakeVisualNovels.RGBMap').texture(child, main=True, fit=True).texture("images/rgb_neon.png", fit=False)
    u_remap_strength(1.2)

transform RGBDusty(child):
    Model().shader('MakeVisualNovels.RGBMap').texture(child, main=True, fit=True).texture("images/rgb_dusty.png", fit=False)
    u_remap_strength(0.8)

transform RGBMetal(child):
    Model().shader('MakeVisualNovels.RGBMap').texture(child, main=True, fit=True).texture("images/rgb_metal.png", fit=False)
    u_remap_strength(1.3)

transform RGBPastel(child):
    Model().shader('MakeVisualNovels.RGBMap').texture(child, main=True, fit=True).texture('images/rgb_pastel.png', fit=False)
    u_remap_strength(1.1)

transform RGBCold(child):
    Model().shader('MakeVisualNovels.RGBMap').texture(child, main=True, fit=True).texture('images/rgb_cold.png', fit=False)
    u_remap_strength(1.5)

transform RGBFire(child):
    Model().shader('MakeVisualNovels.RGBMap').texture(child, main=True, fit=True).texture('images/rgb_fire.png', fit=False)
    u_remap_strength(1.0)

transform RGBUnderwater(child):
    Model().shader('MakeVisualNovels.RGBMap').texture(child, main=True, fit=True).texture('images/rgb_underwater.png', fit=False)
    u_remap_strength(1.0)

transform RGBAlien(child):
    Model().shader('MakeVisualNovels.RGBMap').texture(child, main=True, fit=True).texture('images/rgb_alien.png', fit=False)
    u_remap_strength(0.0)
    linear 4.0 u_remap_strength(2.0)
    linear 4.0 u_remap_strength(-2.0)

transform RGBHeat(child):
    Model().shader('MakeVisualNovels.RGBMap').texture(child,main=True, fit=True).texture('images/rgb_heat.png', fit=False)
    u_remap_strength (1.0)

transform RGBNightvision(child):
    Model().shader('MakeVisualNovels.RGBMap').texture(child,main=True, fit=True).texture('images/rgb_nightvision.png', fit=False)
    u_remap_strength (2.0)

transform RGBDream(child):
    Model().shader('MakeVisualNovels.RGBMap').texture(child,main=True, fit=True).texture('images/rgb_dream.png', fit=False)
    u_remap_strength (0.5)

transform RGBInvert(child):
    Model().shader('MakeVisualNovels.RGBMap').texture(child,main=True, fit=True).texture('images/rgb_invert.png', fit=False)
    u_remap_strength (1.0)

transform RGBCustom(child, map, strength):
    Model().shader('MakeVisualNovels.RGBMap').texture(child,main=True, fit=True).texture(map, fit=False)
    u_remap_strength (strength)

