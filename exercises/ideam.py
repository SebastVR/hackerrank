def porcentaje_OD(oxigeno_disuelto, oxigeno_saturado):
    return self.oxigeno_disuelto() * 100 / self.oxigeno_saturado()


def sub_indice_OD(self):
    if self.porcentaje_OD:
        if self.porcentaje_OD < 1:
            return 1 - (1 - 0.01 * self.porcentaje_OD())
        else:
            return 1 - (0.01 * self.porcentaje_OD() - 1)


    def sub_indice_OD(self):
        if self.porcentaje_OD():
            if self.porcentaje_OD() < 1:
                return 1 - (1 - 0.01 * self.porcentaje_OD())
            else:
                return 1 - (0.01 * self.porcentaje_OD() - 1)