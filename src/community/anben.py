from omnibelt import load_yaml, save_yaml
import omnifig as fig

import numpy as np
import matplotlib.pyplot as plt

from src import colors
from src.community.ad import AD_Pixel_Rendering

from .wd import WD_Pixel_Rendering

@fig.component('anben-renderer')
class AnbenPixelRenderer(AD_Pixel_Rendering):

    def _draw_unit(self, player, loc, utype, retreat=False):
        color = self.players[player].get('color', self.neutral_color)
        pos = self._get_unit_pos(loc, retreat=retreat)
    
        colors = self.pattern_colors.get(utype, {}).copy()
        colors[1] = color
    
        if 0 not in colors:
            colors[0] = '#000000'
        if 3 not in colors:
            colors[3] = '#ffffff'
    
        for x,y in zip(*pos):
            self._draw_pixel_pattern(
                self.pattern_bases[utype],
                x, y,
                colors,
                self.unit_overlay
            )