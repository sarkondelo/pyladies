import piskvorky
#abych mohla otestovat modul, nemůžu mít něco, co volá input
def test_teh_na_prazdne_pole():
	pole = piskvorky.tah_pocitace('-------------------')
	assert len(pole) == 20
	assert pole.count('o') == 1
	assert pole.count ('-') == 19

def test_tah_chyba():
	with pytest.raises(ValueError)
	piskvorky.tah_pocitace('oxooxoxoxoxoxox')
