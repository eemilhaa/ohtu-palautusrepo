from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from tekoaly import default_tekoaly
from tekoaly_parannettu import default_parannettu_tekoaly


PELITYYPIT = {
    "a": KPSPelaajaVsPelaaja(),
    "b": KPSTekoaly(default_tekoaly),
    "c": KPSTekoaly(default_parannettu_tekoaly),
}


def luo_peli(tyyppi):
    return PELITYYPIT[tyyppi]
