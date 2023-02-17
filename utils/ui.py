from qgis.PyQt.QtWidgets import QTableWidgetItem
from qgis.PyQt.QtCore import Qt

def create_label(text):
    """
    Create a simple label item
    :param text: String - The text to insert inside the cell
    :return: QTableWidgetItem - The item to insert
    """
    item = QTableWidgetItem(text)
    item.setFlags(Qt.NoItemFlags)
    item.setTextAlignment(Qt.AlignCenter)
    return item

def create_checkbox():
    """
    Create a simple checkbox item
    :return: QTableWidgetItem - The item to insert
    """
    item = QTableWidgetItem()
    item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
    item.setCheckState(Qt.Unchecked)
    return item

def create_rows(communes):
    """
    Create row items for the "Communes" table
    :param communes: List<QgsFeature> - A list of Feature instance representing communes
    :return: List<Dict> - Row items to insert
    """
    rows = []
    for c in communes:
        label, checkbox = create_label(c.attribute("nom")), create_checkbox()
        rows.append(dict(label=label, checkbox=checkbox))
    return rows