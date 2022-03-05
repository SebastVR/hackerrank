from fisicoquimico.ica import IcaNFS
from fisicoquimico.models import (
    CampannaFisicoquimico,
    Fisicoquimico,
    ParametroFisicoquimico,
)

# from monitoreos.models import FuenteHidrica

# parametros = ParametroFisicoquimico.objects.all()
# fuente = FuenteHidrica.objects.all()

campannas = CampannaFisicoquimico.objects.all()
campanna = campannas[4419]
ica = IcaNFS(campanna)


ica.campanna
ica.saturacion_oxigeno  # Decimal('98.1000')
ica.ph  # Decimal('6.7500')
ica.temperatura_agua  # Decimal('17.5000')
ica.DBO5  # Decimal('2.0000')
ica.coliformes_escherichia  # Decimal('31.0000')
ica.fosfatos
ica.nitratos
ica.indice_variacion_temp()
ica.solidos  # Decimal('75.0000')

ica.temperatura_ambiente  # Decimal('18.2000')
ica.turbiedad  # Decimal('1.0500')

ica.variacion_temperatura()  # Decimal('1.1000')
ica.get_eval_ica_NFS()  # True
ica.get_data()  # {'saturacion_oxigeno': Decimal('62.0000'), 'ph': Decimal('7.0400'), 'DBO5': Decimal('2.0000'), 'coliformes_fecales': Decimal('20.0000'), 'temperatura_agua': Decimal('14.9000'), 'fosfatos': None, 'nitratos': Decimal('1.5000'), 'solidos': Decimal('109.0000'), 'turbiedad': Decimal('1.4400')}
ica.get_indices()  # {'Indice SATOD': Decimal('62.3731308575983008412203776'), 'Indice pH': Decimal('91.73285078991010854716594'), 'Indice DBO5': Decimal('78.83119425918050568128000000'), 'Indice coliformes_fecales': Decimal('58.23575442639888070582034752'), 'Indice NO4': Decimal('90.94223943469085239020296212'), 'Indice variacion_temp': Decimal('76.37157239461318190000000000'), 'Indice turbiedad': Decimal('95.70777232159998148942042540'), 'Indice PO5': 0, 'Indice ST': Decimal('83.29716160949452224985200387')}

ica.indice_SATOD()  # Decimal('98.1475963192663235732321013')
ica.indice_pH()  # Decimal('87.74740262730056862746582')
ica.indice_coliformes_fecales()  # Decimal('52.89983762484721516384178198')
ica.indice_DBO5()  # Decimal('78.83119425918050568128000000')
ica.indice_NO4()  # Decimal('90.94223943469085239020296212')
ica.indice_variacion_temp()  # Decimal('87.69982507324218750000000000')
ica.indice_turbiedad()  # Decimal('96.89967063468104357216746233')
ica.indice_PO5()  # 0
ica.indice_ST()  # Decimal('85.46457502018772768264160156')
ica.get_ica()  # Decimal('78.59')
ica.get_ica_nfs()

from fisicoquimico.ica import IcaIdeam
from fisicoquimico.models import (
    CampannaFisicoquimico,
    Fisicoquimico,
    ParametroFisicoquimico,
)

campannas = CampannaFisicoquimico.objects.all()
campanna = campannas[4419]
ica = IcaIdeam(campanna)

ica.oxigeno_disuelto  # Decimal('7.4000')
ica.DQO_total  # Decimal('12.8000')
ica.conductividad_electrica  # Decimal('70.9000')
ica.altura  # 7522.965879265092
ica.ph  # Decimal('6.7500')
ica.solidos_suspendidos  # Decimal('7.0000')
ica.coliformes_escherichia  # Decimal('31.0000')
ica.fosfatos  # Revisar porque no da el valor deberia ser 0.153
ica.nitratos  # Decimal('1.5000')

ica.get_psdo()  # Decimal('129.5318291322183342754151192')
ica.get_iod()  # Decimal('0.704681708677816630281620222')
ica.get_isst()  # Decimal('0.9989999999999999999791833183')
ica.get_dqo()  # Decimal('0.91000000000000003108624468950438313186168670654296875')
ica.get_ice()  # Decimal('0.8340925244495494850871733524')
ica.get_iph()  # Decimal('0.8793089964780976753235851909')
ica.get_icf()  # Decimal('0.979999999999999982236431605997495353221893310546875')
ica.get_ntpt()  # Error
ica.get_intpt()  # Error
ica.get_eval_ica_i5()  # Error
ica.ica5()  # Error
ica.get_calidad_5()
ica.get_eval_ica_i6()  # Error
ica.ica6()  # Error
ica.get_eval_ica_i7()  # Error
ica.ica7()  # Error


from fisicoquimico.ica import IcaIcomi
from fisicoquimico.models import (
    CampannaFisicoquimico,
    Fisicoquimico,
    ParametroFisicoquimico,
)

campannas = CampannaFisicoquimico.objects.all()
campanna = campannas[4419]
ica = IcaIcomi(campanna)

ica.alcalinidad_total  # Decimal('36.1000')
ica.conductividad_electrica  # Decimal('70.9000')
ica.dureza_total  # Decimal('33.1000')

ica.get_ialct()  # 0
ica.get_iceicomi()  # Decimal('0.1659074755504505149128266476')
ica.get_idt()  # Decimal('0.003955880579621608503679285798')
ica.ica_icomi()  # Decimal('0.05662111871002404113883531113')


from fisicoquimico.ica import IcaIcomo
from fisicoquimico.models import (
    CampannaFisicoquimico,
    Fisicoquimico,
    ParametroFisicoquimico,
)

campannas = CampannaFisicoquimico.objects.all()
campanna = campannas[4419]
ica = IcaIcomo(campanna)

ica.saturacion_oxigeno  # Decimal('98.1000')
ica.coliformes_totales  # Decimal('1872.0000')
ica.DBO5  # Decimal('2.0000')
ica.get_sat_od()  # Decimal('0.0189999999999999795788352408')
ica.get_cot()  # Decimal('0.392491272865168540152281430')
ica.get_idbo5()  # 0
ica.ica_icomo()  # Decimal('0.1371637576217228399103722236')

from fisicoquimico.ica import IcaIcosus
from fisicoquimico.models import (
    CampannaFisicoquimico,
    Fisicoquimico,
    ParametroFisicoquimico,
)

campannas = CampannaFisicoquimico.objects.all()
campanna = campannas[4419]
ica = IcaIcosus(campanna)

ica.solidos_suspendidos  # Decimal('7.0000')
ica.ica_icosus()  # 0


from fisicoquimico.ica import IcaPH
from fisicoquimico.models import (
    CampannaFisicoquimico,
    Fisicoquimico,
    ParametroFisicoquimico,
)

campannas = CampannaFisicoquimico.objects.all()
campanna = campannas[4419]
ica = IcaPH(campanna)

ica.ph  # Decimal('6.7500')
ica.ica_icoph()  # Decimal('0.0023116024853360767239707218578814718057401478290557861328125')


from fisicoquimico.ica import IcaCetesb
from fisicoquimico.models import (
    CampannaFisicoquimico,
    Fisicoquimico,
    ParametroFisicoquimico,
)

campannas = CampannaFisicoquimico.objects.all()
campanna = campannas[4419]
ica = IcaCetesb(campanna)

ica.coliformes_escherichia  # Decimal('31.0000')
ica.ph  # Decimal('6.7500')
ica.DBO5  # Decimal('2.0000')
ica.nitratos  # Decimal('1.5000')
ica.fosfatos  #
ica.turbiedad  # Decimal('1.0500')
ica.solidos  # Decimal('75.0000')
ica.saturacion_oxigeno  # Decimal('98.1000')

ica.get_ecoli()  # DecDecimal('52.64065691354371838084330702')
ica.get_phcetesb()  # Decimal('84.3319882031249560025258639')
ica.get_idbo5()  # Decimal('81.42692399999999789826816977')
ica.get_no3()  # Decimal('92.52000000000000223820961764')
ica.get_fo4()  # no aparece el valor de los fosfatos
ica.get_variacion_tem()  # Decimal('89.4000')
ica.get_ntu()  # Decimal('96.12262514488338450209656418')
ica.get_st()  # Decimal('94.18837659321462275942036870')
ica.get_sat_od()  # Decimal('95.94375744265866417895751168')


from fisicoquimico.ica import IcaLangelier
from fisicoquimico.models import (
    CampannaFisicoquimico,
    Fisicoquimico,
    ParametroFisicoquimico,
)

campannas = CampannaFisicoquimico.objects.all()
campanna = campannas[4419]
ica = IcaLangelier(campanna)

ica.get_cd()  # Decimal('1.126597071180136025105504591')
ica.get_ct()  # Decimal('0.4202499999999999676230668342')
ica.get_ca()  # Decimal('1.564078767135859402650709941')
ica.get_isl()  # Decimal('-2.239074161684004249349350754')


from fisicoquimico.ica import IcaDinius
from fisicoquimico.models import (
    CampannaFisicoquimico,
    Fisicoquimico,
    ParametroFisicoquimico,
)

campannas = CampannaFisicoquimico.objects.all()
campanna = campannas[3987]
ica = IcaDinius(campanna)

ica.get_psod()  # Decimal('91.00199999999999570521325154')
ica.get_ecoli()  # Decimal('0.3529852449257641001455437282')
ica.get_ph()  # Decimal('85.72352082084059260585632247')
ica.get_dbo()  # Decimal('0.1528768970880874031569709487')
ica.get_nitratos()  # Decimal('0.2411005795116574887619130635')
ica.get_alcalinidad()  # Decimal('0.3288725571268443301611018674')
ica.get_color()  # Decimal('0.2133123352332865611412701164')
ica.variacion_temperatura()
ica.get_desviacion_temp()  # Decimal('94.89864249913838990273934180')
ica.get_ce()  # Decimal('0.03090899446000817841465993159')
ica.get_dureza_total()  # Decimal('0.01222697258119630787716375812')
ica.get_cloruros()  # Decimal('0.1088034659949417995258568292')
ica.get_colt()  # Decimal('0.1955661800701854224947206829')


### Models fisicoquimico ###

from monitoreos.models import FuenteHidrica

fuente1 = FuenteHidrica.objects.all()



from formularios.forms import InsituFuenteForm 

variable = InsituFuenteForm.objects.all()



from fisicoquimico.ica import IcaDinius
from fisicoquimico.models import (
    CampannaFisicoquimico,
    Fisicoquimico,
    ParametroFisicoquimico,
)

campannas = CampannaFisicoquimico.objects.all()
campanna = campannas[3987]
ica = IcaDinius(campanna)