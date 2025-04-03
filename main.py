import pandas as pd
import numpy as np

from datenklassen import Kostenartenrechnung, Kostenstellenrechnung

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

# Read all sheets from the Excel file
excel_file = 'reports.xls'
dfs = pd.read_excel(excel_file, sheet_name=None, header=3)

# Display all available sheets
print("Verfügbare Blätter in der Excel-Datei:")
for sheet_name in dfs.keys():
    print(f"- {sheet_name}")

# # Display content of each sheet
# for sheet_name, df in dfs.items():
#     print(f"\n=== Inhalt von {sheet_name} ===\n")
#     print(df)
#     print("\n" + "="*50)


# Create the Kostenartenrechnung object from the Kostenartenrechnung sheet
kosten_df = dfs['7) Kostenartenrechnung']

# Print column names for debugging
print("\nVerfügbare Spalten:")
print(kosten_df.columns)

# Hilfsfunktion für leere Werte
def get_value(df, row, col):
    val = df.iloc[row][col]
    if pd.isna(val) or str(val).strip() == '':  # Prüft auf NaN, None, leere Strings oder nur Leerzeichen
        return 0.0
    return float(val)

# Erstelle das Kostenartenrechnung-Objekt
kar = Kostenartenrechnung(
    # Material
    Materialeinzelkosten=get_value(kosten_df, 2, 'Einzelkosten'),  # Einsatzstoffe/Teile
    Materialgemeinkosten=get_value(kosten_df, 2, 'Gemeinkosten'),
    
    # Betriebsstoffe
    Betriebsstoffeeinzelkosten=get_value(kosten_df, 3, 'Einzelkosten'),
    Betriebsstoffegemeinkosten=get_value(kosten_df, 3, 'Gemeinkosten'),
    
    # Personal
    Personaleinzelkosten=get_value(kosten_df, 4, 'Einzelkosten'),
    Personalgemeinkosten=get_value(kosten_df, 4, 'Gemeinkosten'),
    
    # Löhne/Gehälter
    LoehneGehaelterEinzelkosten=get_value(kosten_df, 5, 'Einzelkosten'),
    LoehneGehaelterGemeinkosten=get_value(kosten_df, 5, 'Gemeinkosten'),
    
    # Einstellungen/Entlassungen/Training
    PersonalentwicklungEinzelkosten=get_value(kosten_df, 6, 'Einzelkosten'),
    PersonalentwicklungGemeinkosten=get_value(kosten_df, 6, 'Gemeinkosten'),
    
    # Sozialplan
    SozialplanEinzelkosten=get_value(kosten_df, 7, 'Einzelkosten'),
    SozialplanGemeinkosten=get_value(kosten_df, 7, 'Gemeinkosten'),
    
    # Personalnebenkosten
    PersonalnebenkostenEinzelkosten=get_value(kosten_df, 8, 'Einzelkosten'),
    PersonalnebenkostenGemeinkosten=get_value(kosten_df, 8, 'Gemeinkosten'),
    
    # Pensionsrückstellungen
    PensionsrueckstellungenEinzelkosten=get_value(kosten_df, 9, 'Einzelkosten'),
    PensionsrueckstellungenGemeinkosten=get_value(kosten_df, 9, 'Gemeinkosten'),
    
    # Abschreibungen
    AbschreibungenEinzelkosten=get_value(kosten_df, 10, 'Einzelkosten'),
    AbschreibungenGemeinkosten=get_value(kosten_df, 10, 'Gemeinkosten'),
    
    # Gebäude
    GebaeudeEinzelkosten=get_value(kosten_df, 11, 'Einzelkosten'),
    GebaeudeGemeinkosten=get_value(kosten_df, 11, 'Gemeinkosten'),
    
    # Fertigungsanlagen
    FertigungsanlagenEinzelkosten=get_value(kosten_df, 12, 'Einzelkosten'),
    FertigungsanlagenGemeinkosten=get_value(kosten_df, 12, 'Gemeinkosten'),
    
    # Umwelttechnik
    UmwelttechnikEinzelkosten=get_value(kosten_df, 13, 'Einzelkosten'),
    UmwelttechnikGemeinkosten=get_value(kosten_df, 13, 'Gemeinkosten'),
    
    # Fertigerzeugnisse
    FertigerzeugnisseEinzelkosten=get_value(kosten_df, 14, 'Einzelkosten'),
    FertigerzeugnisseGemeinkosten=get_value(kosten_df, 14, 'Gemeinkosten'),
    
    # Sonstige Kosten
    SonstigeKostenEinzelkosten=get_value(kosten_df, 15, 'Einzelkosten'),
    SonstigeKostenGemeinkosten=get_value(kosten_df, 15, 'Gemeinkosten'),
    
    # Sonstige fixe Kosten
    SonstigeFixeKostenEinzelkosten=get_value(kosten_df, 16, 'Einzelkosten'),
    SonstigeFixeKostenGemeinkosten=get_value(kosten_df, 16, 'Gemeinkosten'),
    
    # Instandhaltung/Rationalisierung
    InstandhaltungEinzelkosten=get_value(kosten_df, 17, 'Einzelkosten'),
    InstandhaltungGemeinkosten=get_value(kosten_df, 17, 'Gemeinkosten'),
    
    # Prozessoptimierung
    ProzessoptimierungEinzelkosten=get_value(kosten_df, 18, 'Einzelkosten'),
    ProzessoptimierungGemeinkosten=get_value(kosten_df, 18, 'Gemeinkosten'),
    
    # Umweltabgabe
    UmweltabgabeEinzelkosten=get_value(kosten_df, 19, 'Einzelkosten'),
    UmweltabgabeGemeinkosten=get_value(kosten_df, 19, 'Gemeinkosten'),
    
    # Nacharbeit/Ausschuss
    NacharbeitAusschussEinzelkosten=get_value(kosten_df, 20, 'Einzelkosten'),
    NacharbeitAusschussGemeinkosten=get_value(kosten_df, 20, 'Gemeinkosten'),
    
    # Lagerkosten
    LagerkostenEinzelkosten=get_value(kosten_df, 21, 'Einzelkosten'),
    LagerkostenGemeinkosten=get_value(kosten_df, 21, 'Gemeinkosten'),
    
    # Werbung/Marktforschung/Corporate Identity
    MarketingEinzelkosten=get_value(kosten_df, 22, 'Einzelkosten'),
    MarketingGemeinkosten=get_value(kosten_df, 22, 'Gemeinkosten'),
    
    # Sonstige Kosten F&E
    SonstigeFuEEinzelkosten=get_value(kosten_df, 23, 'Einzelkosten'),
    SonstigeFuEGemeinkosten=get_value(kosten_df, 23, 'Gemeinkosten'),
    
    # Transport/Logistik
    TransportLogistikEinzelkosten=get_value(kosten_df, 24, 'Einzelkosten'),
    TransportLogistikGemeinkosten=get_value(kosten_df, 24, 'Gemeinkosten')
)

# Überprüfe die Summen
print("\nBerechnete Summen:")
print(f"Summe Einzelkosten: {kar.summe_einzelkosten:.2f} MEUR")
print(f"Summe Gemeinkosten: {kar.summe_gemeinkosten:.2f} MEUR")
print(f"Gesamtkosten: {kar.gesamtkosten:.2f} MEUR")

# Ausgabe der Gesamtkosten pro Kategorie
print("\nGesamtkosten pro Kategorie:")
print(f"Material: {kar.material_gesamt:.2f} MEUR")
print(f"Betriebsstoffe: {kar.betriebsstoffe_gesamt:.2f} MEUR")
print(f"Personal: {kar.personal_gesamt:.2f} MEUR")
print(f"Löhne/Gehälter: {kar.loehne_gehaelter_gesamt:.2f} MEUR")
print(f"Personalentwicklung: {kar.personalentwicklung_gesamt:.2f} MEUR")
print(f"Sozialplan: {kar.sozialplan_gesamt:.2f} MEUR")
print(f"Personalnebenkosten: {kar.personalnebenkosten_gesamt:.2f} MEUR")
print(f"Pensionsrückstellungen: {kar.pensionsrueckstellungen_gesamt:.2f} MEUR")
print(f"Abschreibungen: {kar.abschreibungen_gesamt:.2f} MEUR")
print(f"Gebäude: {kar.gebaeude_gesamt:.2f} MEUR")
print(f"Fertigungsanlagen: {kar.fertigungsanlagen_gesamt:.2f} MEUR")
print(f"Umwelttechnik: {kar.umwelttechnik_gesamt:.2f} MEUR")
print(f"Fertigerzeugnisse: {kar.fertigerzeugnisse_gesamt:.2f} MEUR")
print(f"Sonstige Kosten: {kar.sonstige_kosten_gesamt:.2f} MEUR")
print(f"Sonstige fixe Kosten: {kar.sonstige_fixe_kosten_gesamt:.2f} MEUR")
print(f"Instandhaltung: {kar.instandhaltung_gesamt:.2f} MEUR")
print(f"Prozessoptimierung: {kar.prozessoptimierung_gesamt:.2f} MEUR")
print(f"Umweltabgabe: {kar.umweltabgabe_gesamt:.2f} MEUR")
print(f"Nacharbeit/Ausschuss: {kar.nacharbeit_ausschuss_gesamt:.2f} MEUR")
print(f"Lagerkosten: {kar.lagerkosten_gesamt:.2f} MEUR")
print(f"Marketing: {kar.marketing_gesamt:.2f} MEUR")
print(f"Sonstige F&E: {kar.sonstige_fue_gesamt:.2f} MEUR")
print(f"Transport/Logistik: {kar.transport_logistik_gesamt:.2f} MEUR")

# Vergleiche mit den Summen aus der Excel-Datei
excel_summe = get_value(kosten_df, 25, 'Summe')
print(f"\nSumme laut Excel: {excel_summe:.2f} MEUR")
print(f"Differenz: {abs(excel_summe - kar.gesamtkosten):.2f} MEUR")

# Kostenstellenrechnung
kostenstellen_df = dfs['8) Kostenstellenrechnung']

# Print column names for debugging
print("\nVerfügbare Spalten:")
print(kostenstellen_df.columns)

# Erstellen Sie das Kostenstellenrechnung-Objekt
kst = Kostenstellenrechnung(
    # Materialakosten
    einkauf_material=get_value(kostenstellen_df, 1, 'Einkauf'),
    fertigung_material=get_value(kostenstellen_df, 1, 'Fertigung'),
    fue_material=get_value(kostenstellen_df, 1, 'F&E'),
    vertrieb_material=get_value(kostenstellen_df, 1, 'Vertrieb'),
    verwaltung_material=get_value(kostenstellen_df, 1, 'Verwaltung'),

    # Einsatzstoffe
    einkauf_einsatzstoffe=get_value(kostenstellen_df, 2, 'Einkauf'),
    fertigung_einsatzstoffe=get_value(kostenstellen_df, 2, 'Fertigung'),
    fue_einsatzstoffe=get_value(kostenstellen_df, 2, 'F&E'),
    vertrieb_einsatzstoffe=get_value(kostenstellen_df, 2, 'Vertrieb'),
    verwaltung_einsatzstoffe=get_value(kostenstellen_df, 2, 'Verwaltung'),

    # Betriebsstoffe
    einkauf_betriebsstoffe=get_value(kostenstellen_df, 3, 'Einkauf'),
    fertigung_betriebsstoffe=get_value(kostenstellen_df, 3, 'Fertigung'),
    fue_betriebsstoffe=get_value(kostenstellen_df, 3, 'F&E'),
    vertrieb_betriebsstoffe=get_value(kostenstellen_df, 3, 'Vertrieb'),
    verwaltung_betriebsstoffe=get_value(kostenstellen_df, 3, 'Verwaltung'),

    # Personal
    einkauf_personal=get_value(kostenstellen_df, 4, 'Einkauf'),
    fertigung_personal=get_value(kostenstellen_df, 4, 'Fertigung'),
    fue_personal=get_value(kostenstellen_df, 4, 'F&E'),
    vertrieb_personal=get_value(kostenstellen_df, 4, 'Vertrieb'),
    verwaltung_personal=get_value(kostenstellen_df, 4, 'Verwaltung'),

    # Löhne/Gehälter
    einkauf_loehne_gehaelter=get_value(kostenstellen_df, 5, 'Einkauf'),
    fertigung_loehne_gehaelter=get_value(kostenstellen_df, 5, 'Fertigung'),
    fue_loehne_gehaelter=get_value(kostenstellen_df, 5, 'F&E'),
    vertrieb_loehne_gehaelter=get_value(kostenstellen_df, 5, 'Vertrieb'),
    verwaltung_loehne_gehaelter=get_value(kostenstellen_df, 5, 'Verwaltung'),

    # Personalnebenkosten
    einkauf_personalnebenkosten=get_value(kostenstellen_df, 6, 'Einkauf'),
    fertigung_personalnebenkosten=get_value(kostenstellen_df, 6, 'Fertigung'),
    fue_personalnebenkosten=get_value(kostenstellen_df, 6, 'F&E'),
    vertrieb_personalnebenkosten=get_value(kostenstellen_df, 6, 'Vertrieb'),
    verwaltung_personalnebenkosten=get_value(kostenstellen_df, 6, 'Verwaltung'),

    # Pensionsrückstellungen
    einkauf_pensionsrueckstellungen=get_value(kostenstellen_df, 7, 'Einkauf'),
    fertigung_pensionsrueckstellungen=get_value(kostenstellen_df, 7, 'Fertigung'),
    fue_pensionsrueckstellungen=get_value(kostenstellen_df, 7, 'F&E'),
    vertrieb_pensionsrueckstellungen=get_value(kostenstellen_df, 7, 'Vertrieb'),
    verwaltung_pensionsrueckstellungen=get_value(kostenstellen_df, 7, 'Verwaltung'),

    # Abschreibungen
    einkauf_abschreibungen=get_value(kostenstellen_df, 8, 'Einkauf'),
    fertigung_abschreibungen=get_value(kostenstellen_df, 8, 'Fertigung'),
    fue_abschreibungen=get_value(kostenstellen_df, 8, 'F&E'),
    vertrieb_abschreibungen=get_value(kostenstellen_df, 8, 'Vertrieb'),
    verwaltung_abschreibungen=get_value(kostenstellen_df, 8, 'Verwaltung'),

    # Gebäude
    einkauf_gebaeude=get_value(kostenstellen_df, 9, 'Einkauf'),
    fertigung_gebaeude=get_value(kostenstellen_df, 9, 'Fertigung'),
    fue_gebaeude=get_value(kostenstellen_df, 9, 'F&E'),
    vertrieb_gebaeude=get_value(kostenstellen_df, 9, 'Vertrieb'),
    verwaltung_gebaeude=get_value(kostenstellen_df, 9, 'Verwaltung'),

    # Fertigungsanlagen
    einkauf_fertigungsanlagen=get_value(kostenstellen_df, 10, 'Einkauf'),
    fertigung_fertigungsanlagen=get_value(kostenstellen_df, 10, 'Fertigung'),
    fue_fertigungsanlagen=get_value(kostenstellen_df, 10, 'F&E'),
    vertrieb_fertigungsanlagen=get_value(kostenstellen_df, 10, 'Vertrieb'),
    verwaltung_fertigungsanlagen=get_value(kostenstellen_df, 10, 'Verwaltung'),

    # Umwelttechnik
    einkauf_umwelttechnik=get_value(kostenstellen_df, 11, 'Einkauf'),
    fertigung_umwelttechnik=get_value(kostenstellen_df, 11, 'Fertigung'),
    fue_umwelttechnik=get_value(kostenstellen_df, 11, 'F&E'),
    vertrieb_umwelttechnik=get_value(kostenstellen_df, 11, 'Vertrieb'),
    verwaltung_umwelttechnik=get_value(kostenstellen_df, 11, 'Verwaltung'),

    # Fertigerzeugnisse
    einkauf_fertigerzeugnisse=get_value(kostenstellen_df, 12, 'Einkauf'),
    fertigung_fertigerzeugnisse=get_value(kostenstellen_df, 12, 'Fertigung'),
    fue_fertigerzeugnisse=get_value(kostenstellen_df, 12, 'F&E'),
    vertrieb_fertigerzeugnisse=get_value(kostenstellen_df, 12, 'Vertrieb'),
    verwaltung_fertigerzeugnisse=get_value(kostenstellen_df, 12, 'Verwaltung'),

    # Sonstige Kosten
    einkauf_sonstige_kosten=get_value(kostenstellen_df, 13, 'Einkauf'),
    fertigung_sonstige_kosten=get_value(kostenstellen_df, 13, 'Fertigung'),
    fue_sonstige_kosten=get_value(kostenstellen_df, 13, 'F&E'),
    vertrieb_sonstige_kosten=get_value(kostenstellen_df, 13, 'Vertrieb'),
    verwaltung_sonstige_kosten=get_value(kostenstellen_df, 13, 'Verwaltung'),

    # Sonstige fixe Kosten
    einkauf_sonstige_fixe_kosten=get_value(kostenstellen_df, 14, 'Einkauf'),
    fertigung_sonstige_fixe_kosten=get_value(kostenstellen_df, 14, 'Fertigung'),
    fue_sonstige_fixe_kosten=get_value(kostenstellen_df, 14, 'F&E'),
    vertrieb_sonstige_fixe_kosten=get_value(kostenstellen_df, 14, 'Vertrieb'),
    verwaltung_sonstige_fixe_kosten=get_value(kostenstellen_df, 14, 'Verwaltung'),

    # Instandhaltung/Rationalisierung
    einkauf_instandhaltung=get_value(kostenstellen_df, 15, 'Einkauf'),
    fertigung_instandhaltung=get_value(kostenstellen_df, 15, 'Fertigung'),
    fue_instandhaltung=get_value(kostenstellen_df, 15, 'F&E'),
    vertrieb_instandhaltung=get_value(kostenstellen_df, 15, 'Vertrieb'),
    verwaltung_instandhaltung=get_value(kostenstellen_df, 15, 'Verwaltung'),
    
    # Prozessoptimierung
    einkauf_prozessoptimierung=get_value(kostenstellen_df, 16, 'Einkauf'),
    fertigung_prozessoptimierung=get_value(kostenstellen_df, 16, 'Fertigung'),
    fue_prozessoptimierung=get_value(kostenstellen_df, 16, 'F&E'),
    vertrieb_prozessoptimierung=get_value(kostenstellen_df, 16, 'Vertrieb'),
    verwaltung_prozessoptimierung=get_value(kostenstellen_df, 16, 'Verwaltung'),
    
    # Umweltabgabe
    einkauf_umweltabgabe=get_value(kostenstellen_df, 17, 'Einkauf'),
    fertigung_umweltabgabe=get_value(kostenstellen_df, 17, 'Fertigung'),
    fue_umweltabgabe=get_value(kostenstellen_df, 17, 'F&E'),
    vertrieb_umweltabgabe=get_value(kostenstellen_df, 17, 'Vertrieb'),
    verwaltung_umweltabgabe=get_value(kostenstellen_df, 17, 'Verwaltung'),
    
    # Nacharbeit/Ausschuss
    einkauf_nacharbeit_ausschuss=get_value(kostenstellen_df, 18, 'Einkauf'),
    fertigung_nacharbeit_ausschuss=get_value(kostenstellen_df, 18, 'Fertigung'),
    fue_nacharbeit_ausschuss=get_value(kostenstellen_df, 18, 'F&E'),
    vertrieb_nacharbeit_ausschuss=get_value(kostenstellen_df, 18, 'Vertrieb'),
    verwaltung_nacharbeit_ausschuss=get_value(kostenstellen_df, 18, 'Verwaltung'),
    
    # Lagerkosten
    einkauf_lagerkosten=get_value(kostenstellen_df, 19, 'Einkauf'),
    fertigung_lagerkosten=get_value(kostenstellen_df, 19, 'Fertigung'),
    fue_lagerkosten=get_value(kostenstellen_df, 19, 'F&E'),
    vertrieb_lagerkosten=get_value(kostenstellen_df, 19, 'Vertrieb'),
    verwaltung_lagerkosten=get_value(kostenstellen_df, 19, 'Verwaltung'),
    
    # Werbung/Marktforschung/Corporate Identity
    einkauf_marketing=get_value(kostenstellen_df, 20, 'Einkauf'),
    fertigung_marketing=get_value(kostenstellen_df, 20, 'Fertigung'),
    fue_marketing=get_value(kostenstellen_df, 20, 'F&E'),
    vertrieb_marketing=get_value(kostenstellen_df, 20, 'Vertrieb'),
    verwaltung_marketing=get_value(kostenstellen_df, 20, 'Verwaltung'),

    # Sonstige F&E
    einkauf_sonstige_fue=get_value(kostenstellen_df, 21, 'Einkauf'),
    fertigung_sonstige_fue=get_value(kostenstellen_df, 21, 'Fertigung'),
    fue_sonstige_fue=get_value(kostenstellen_df, 21, 'F&E'),
    vertrieb_sonstige_fue=get_value(kostenstellen_df, 21, 'Vertrieb'),
    verwaltung_sonstige_fue=get_value(kostenstellen_df, 21, 'Verwaltung'),

    # Transport/Logistik
    einkauf_transport_logistik=get_value(kostenstellen_df, 22, 'Einkauf'),
    fertigung_transport_logistik=get_value(kostenstellen_df, 22, 'Fertigung'),
    fue_transport_logistik=get_value(kostenstellen_df, 22, 'F&E'),
    vertrieb_transport_logistik=get_value(kostenstellen_df, 22, 'Vertrieb'),
    verwaltung_transport_logistik=get_value(kostenstellen_df, 22, 'Verwaltung'),   
)

# Überprüfe die Summen
print("\nBerechnete Summen:")
print(f"Summe Einzelkosten: {kst.einkauf_gesamt:.2f} MEUR")
print(f"Summe Gemeinkosten: {kst.fertigung_gesamt:.2f} MEUR")
print(f"Gesamtkosten: {kst.gesamtkosten:.2f} MEUR")

    
    

    
    
    
    

    
    

    
