from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly


PELITYYPIT = {
    "a": KPSPelaajaVsPelaaja(),
    "b": KPSTekoaly(),
    "c": KPSParempiTekoaly(),
}


def luo_peli(tyyppi):
    return PELITYYPIT[tyyppi]
