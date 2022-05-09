<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="PRODUCT">
 <html>
<head><title>QN700 Neo QLED 8K</title>
</head>
 <body>
 <h2>Info about QN700 Neo QLED 8K</h2>
 <table border="1">

   <xsl:for-each select="Attributes">
        <tr>
            <th>Диагональ экрана</th>
            <td><xsl:value-of select="Screen_diagonal"/></td>
        </tr>
        <tr>
            <th>Разрешение</th>
            <td><xsl:value-of select="Resolution"/></td>
        </tr>
        <tr>
            <th>Частота матрицы</th>
            <td><xsl:value-of select="Matrix_frequency"/></td>
        </tr>
        <tr>
            <th>Ширина</th>
            <td><xsl:value-of select="Width"/></td>
        </tr>
        <tr>
            <th>Высота (с учетом подставки)</th>
            <td><xsl:value-of select="Heihgt"/></td>
        </tr>
        <tr>
            <th>Глубина (с учетом подставки)</th>
            <td><xsl:value-of select="Depth_with_stand"/></td>
        </tr>
        <tr>
            <th>Высота (без подставки):</th>
            <td><xsl:value-of select="Heihgt"/></td>
        </tr>
        <tr>
            <th>Толщина панели:</th>
            <td><xsl:value-of select="Panel_thickness"/></td>
        </tr>
        <tr>
            <th>Вес (с подставкой): </th>
            <td><xsl:value-of select="Weight_with_stand"/></td>
        </tr>
        <tr>
            <th>Вес (без подставкой): </th>
            <td><xsl:value-of select="Weight"/></td>
        </tr>
    </xsl:for-each>

 </table>
 </body>
 </html>
</xsl:template>
</xsl:stylesheet>
