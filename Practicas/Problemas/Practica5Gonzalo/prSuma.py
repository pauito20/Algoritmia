from typing import List, Tuple

from bt_scheme import infinity


def suma_max(izq, der, edificios ):

    centro = (izq + der) // 2

    ind_izq = centro
    ind_grande_izq = ind_izq
    ind_peq_izq = izq
    ind_valle = -1
    valle = infinity
    while ind_izq > 0:
        if edificios[ind_izq - 1] < edificios[ind_izq]:
            if ind_izq - 1 < ind_grande_izq and (edificios[ind_grande_izq] - edificios[ind_izq - 1]) < valle:
                valle = edificios[ind_grande_izq] - edificios[ind_izq - 1]
                ind_valle = ind_izq - 1
        else:
            if ind_valle > ind_izq - 1:
                if edificios[ind_izq -1] < edificios[ind_grande_izq]:
                    ind_peq_izq = ind_izq - 1
                else:
                    ind_peq_izq = ind_grande_izq
                    ind_grande_izq = ind_izq - 1
        ind_izq -= 1
    '''    
    if not (ind_peq_izq < ind_valle < ind_grande_izq):
        ind_izq = ind_grande_izq
        valle = infinity
        while ind_izq > 0:
            if edificios[ind_izq - 1] < edificios[ind_izq]:
                if ind_izq - 1 < ind_grande_izq and (edificios[ind_grande_izq] - edificios[ind_izq - 1]) < valle:
                    valle = edificios[ind_peq_izq] - edificios[ind_izq - 1]
                    ind_valle = ind_izq - 1
            else:
                if ind_valle > ind_izq - 1:
                    if edificios[ind_izq - 1] < edificios[ind_grande_izq]:
                        ind_peq_izq = ind_izq - 1
                    else:
                        ind_peq_izq = ind_grande_izq
                        ind_grande_izq = ind_izq - 1
            ind_izq -= 1
    '''
    res_centro_izq = [ind_peq_izq, ind_grande_izq, ind_valle, valle]


    # POR LA DERECHA Y AUMENTAMOS
    ind_der = centro + 1
    ind_grande_der = der
    ind_peq_der = centro + 1
    ind_valle = -1
    valle = infinity
    while ind_der < der:
        print(f"ind_der {ind_der}, ind_grande {ind_grande_der}, ind peq {ind_peq_der}, indValle { ind_valle}, valle = {valle}")
        if edificios[ind_der + 1] < edificios[ind_der]:
            if ind_der + 1 > ind_peq_der and (edificios[ind_peq_der] - edificios[ind_der + 1]) < valle:
                valle = edificios[ind_peq_der] - edificios[ind_der + 1]
                ind_valle = ind_der + 1
        else:
            if ind_valle < ind_der + 1:
                if edificios[ind_der + 1] > edificios[ind_grande_der]:
                    if edificios[ind_der + 1] < edificios[ind_peq_der]:
                        ind_grande_der = ind_peq_der
                        ind_peq_der = ind_der + 1
                    else:
                        ind_peq_der = ind_grande_der
                        ind_grande_der = ind_der + 1

                elif edificios[ind_der + 1] > edificios[ind_peq_der]:
                    ind_peq_der = ind_der + 1
        ind_der += 1


    res_centro_der = [ind_peq_der, ind_grande_der, ind_valle, valle]

    if (res_centro_izq[3] > res_centro_der[3]):
        return res_centro_izq
    else:
        return res_centro_der


if __name__ == "__main__":

    edificios = [3,2,1]

    dep = [97402359, 591682484, 455824010, 63469422, 887825708, 607151284, 132931337, 239701015, 677129423, 673701294, 625988157, 66423869, 619659572, 628720318, 425932422, 53246120, 237384805, 50017773, 597714384, 921773491, 142995372, 310965606, 450047121, 154892714, 580557052, 126478449, 613013911, 331229839, 601571671, 876309004, 732294822, 194053475, 110655225, 624488421, 613326043, 686028114, 201724978, 399858817, 104615285, 588136139, 764623113, 67419150, 605985841, 63996270, 664656493, 221146488, 533021002, 730573910, 570930265, 459123744, 834543047, 337312956, 499936197, 628742261, 991537634, 486603021, 388246103, 321872364, 266746014, 852958474, 193023079, 750539558, 837335689, 262096639, 87891152, 616782764, 322390038, 563925449, 531627138, 939671730, 368804212, 783235913, 481932047, 309170819, 653864768, 78598836, 126772165, 549683696, 448955963, 177126710, 812973888, 367279628, 163192150, 525020129, 452795163, 42098470, 717491317, 83344354, 820951720, 599229279, 615281917, 847283416, 940037142, 878700211, 336883828, 365203601, 746567716, 376001183, 638199796, 533300499]


    print(suma_max(0, len(edificios) -1 , edificios))
    print(suma_max(0, len(dep) - 1, dep))
