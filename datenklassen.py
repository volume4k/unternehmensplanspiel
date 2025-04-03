from dataclasses import dataclass

@dataclass
class Kostenartenrechnung:
    # Material
    Materialeinzelkosten: float
    Materialgemeinkosten: float
    
    # Betriebsstoffe
    Betriebsstoffeeinzelkosten: float
    Betriebsstoffegemeinkosten: float
    
    # Personal
    Personaleinzelkosten: float
    Personalgemeinkosten: float
    
    # Löhne/Gehälter
    LoehneGehaelterEinzelkosten: float
    LoehneGehaelterGemeinkosten: float
    
    # Einstellungen/Entlassungen/Training
    PersonalentwicklungEinzelkosten: float
    PersonalentwicklungGemeinkosten: float
    
    # Sozialplan
    SozialplanEinzelkosten: float
    SozialplanGemeinkosten: float
    
    # Personalnebenkosten
    PersonalnebenkostenEinzelkosten: float
    PersonalnebenkostenGemeinkosten: float
    
    # Pensionsrückstellungen
    PensionsrueckstellungenEinzelkosten: float
    PensionsrueckstellungenGemeinkosten: float
    
    # Abschreibungen
    AbschreibungenEinzelkosten: float
    AbschreibungenGemeinkosten: float
    
    # Gebäude
    GebaeudeEinzelkosten: float
    GebaeudeGemeinkosten: float
    
    # Fertigungsanlagen
    FertigungsanlagenEinzelkosten: float
    FertigungsanlagenGemeinkosten: float
    
    # Umwelttechnik
    UmwelttechnikEinzelkosten: float
    UmwelttechnikGemeinkosten: float
    
    # Fertigerzeugnisse
    FertigerzeugnisseEinzelkosten: float
    FertigerzeugnisseGemeinkosten: float
    
    # Sonstige Kosten
    SonstigeKostenEinzelkosten: float
    SonstigeKostenGemeinkosten: float

    # Sonstige fixe Kosten
    SonstigeFixeKostenEinzelkosten: float
    SonstigeFixeKostenGemeinkosten: float
    
    # Instandhaltung/Rationalisierung
    InstandhaltungEinzelkosten: float
    InstandhaltungGemeinkosten: float
    
    # Prozessoptimierung
    ProzessoptimierungEinzelkosten: float
    ProzessoptimierungGemeinkosten: float
    
    # Umweltabgabe
    UmweltabgabeEinzelkosten: float
    UmweltabgabeGemeinkosten: float
    
    # Nacharbeit/Ausschuss
    NacharbeitAusschussEinzelkosten: float
    NacharbeitAusschussGemeinkosten: float
    
    # Lagerkosten
    LagerkostenEinzelkosten: float
    LagerkostenGemeinkosten: float
    
    # Werbung/Marktforschung/Corporate Identity
    MarketingEinzelkosten: float
    MarketingGemeinkosten: float
    
    # Sonstige Kosten F&E
    SonstigeFuEEinzelkosten: float
    SonstigeFuEGemeinkosten: float
    
    # Transport/Logistik
    TransportLogistikEinzelkosten: float
    TransportLogistikGemeinkosten: float

    @property
    def summe_einzelkosten(self) -> float:
        """Berechnet die Summe aller Einzelkosten."""
        return sum([
            self.Materialeinzelkosten,
            self.Betriebsstoffeeinzelkosten,
            self.Personaleinzelkosten,
            self.LoehneGehaelterEinzelkosten,
            self.PersonalentwicklungEinzelkosten,
            self.SozialplanEinzelkosten,
            self.PersonalnebenkostenEinzelkosten,
            self.PensionsrueckstellungenEinzelkosten,
            self.AbschreibungenEinzelkosten,
            self.GebaeudeEinzelkosten,
            self.FertigungsanlagenEinzelkosten,
            self.UmwelttechnikEinzelkosten,
            self.FertigerzeugnisseEinzelkosten,
            self.SonstigeKostenEinzelkosten,
            self.SonstigeFixeKostenEinzelkosten,
            self.InstandhaltungEinzelkosten,
            self.ProzessoptimierungEinzelkosten,
            self.UmweltabgabeEinzelkosten,
            self.NacharbeitAusschussEinzelkosten,
            self.LagerkostenEinzelkosten,
            self.MarketingEinzelkosten,
            self.SonstigeFuEEinzelkosten,
            self.TransportLogistikEinzelkosten
        ])

    @property
    def summe_gemeinkosten(self) -> float:
        """Berechnet die Summe aller Gemeinkosten."""
        return sum([
            self.Materialgemeinkosten,
            self.Betriebsstoffegemeinkosten,
            self.Personalgemeinkosten,
            self.LoehneGehaelterGemeinkosten,
            self.PersonalentwicklungGemeinkosten,
            self.SozialplanGemeinkosten,
            self.PersonalnebenkostenGemeinkosten,
            self.PensionsrueckstellungenGemeinkosten,
            self.AbschreibungenGemeinkosten,
            self.GebaeudeGemeinkosten,
            self.FertigungsanlagenGemeinkosten,
            self.UmwelttechnikGemeinkosten,
            self.FertigerzeugnisseGemeinkosten,
            self.SonstigeKostenGemeinkosten,
            self.SonstigeFixeKostenGemeinkosten,
            self.InstandhaltungGemeinkosten,
            self.ProzessoptimierungGemeinkosten,
            self.UmweltabgabeGemeinkosten,
            self.NacharbeitAusschussGemeinkosten,
            self.LagerkostenGemeinkosten,
            self.MarketingGemeinkosten,
            self.SonstigeFuEGemeinkosten,
            self.TransportLogistikGemeinkosten
        ])

    @property
    def gesamtkosten(self) -> float:
        """Berechnet die Summe aller Kosten (Einzel- und Gemeinkosten)."""
        return self.summe_einzelkosten + self.summe_gemeinkosten

    # Properties für die Summen der einzelnen Kategorien
    @property
    def material_gesamt(self) -> float:
        return self.Materialeinzelkosten + self.Materialgemeinkosten

    @property
    def betriebsstoffe_gesamt(self) -> float:
        return self.Betriebsstoffeeinzelkosten + self.Betriebsstoffegemeinkosten

    @property
    def personal_gesamt(self) -> float:
        return self.Personaleinzelkosten + self.Personalgemeinkosten

    @property
    def loehne_gehaelter_gesamt(self) -> float:
        return self.LoehneGehaelterEinzelkosten + self.LoehneGehaelterGemeinkosten

    @property
    def personalentwicklung_gesamt(self) -> float:
        return self.PersonalentwicklungEinzelkosten + self.PersonalentwicklungGemeinkosten

    @property
    def sozialplan_gesamt(self) -> float:
        return self.SozialplanEinzelkosten + self.SozialplanGemeinkosten

    @property
    def personalnebenkosten_gesamt(self) -> float:
        return self.PersonalnebenkostenEinzelkosten + self.PersonalnebenkostenGemeinkosten

    @property
    def pensionsrueckstellungen_gesamt(self) -> float:
        return self.PensionsrueckstellungenEinzelkosten + self.PensionsrueckstellungenGemeinkosten

    @property
    def abschreibungen_gesamt(self) -> float:
        return self.AbschreibungenEinzelkosten + self.AbschreibungenGemeinkosten

    @property
    def gebaeude_gesamt(self) -> float:
        return self.GebaeudeEinzelkosten + self.GebaeudeGemeinkosten

    @property
    def fertigungsanlagen_gesamt(self) -> float:
        return self.FertigungsanlagenEinzelkosten + self.FertigungsanlagenGemeinkosten

    @property
    def umwelttechnik_gesamt(self) -> float:
        return self.UmwelttechnikEinzelkosten + self.UmwelttechnikGemeinkosten

    @property
    def fertigerzeugnisse_gesamt(self) -> float:
        return self.FertigerzeugnisseEinzelkosten + self.FertigerzeugnisseGemeinkosten

    @property
    def sonstige_kosten_gesamt(self) -> float:
        return self.SonstigeKostenEinzelkosten + self.SonstigeKostenGemeinkosten

    @property
    def sonstige_fixe_kosten_gesamt(self) -> float:
        return self.SonstigeFixeKostenEinzelkosten + self.SonstigeFixeKostenGemeinkosten

    @property
    def instandhaltung_gesamt(self) -> float:
        return self.InstandhaltungEinzelkosten + self.InstandhaltungGemeinkosten

    @property
    def prozessoptimierung_gesamt(self) -> float:
        return self.ProzessoptimierungEinzelkosten + self.ProzessoptimierungGemeinkosten

    @property
    def umweltabgabe_gesamt(self) -> float:
        return self.UmweltabgabeEinzelkosten + self.UmweltabgabeGemeinkosten

    @property
    def nacharbeit_ausschuss_gesamt(self) -> float:
        return self.NacharbeitAusschussEinzelkosten + self.NacharbeitAusschussGemeinkosten

    @property
    def lagerkosten_gesamt(self) -> float:
        return self.LagerkostenEinzelkosten + self.LagerkostenGemeinkosten

    @property
    def marketing_gesamt(self) -> float:
        return self.MarketingEinzelkosten + self.MarketingGemeinkosten

    @property
    def sonstige_fue_gesamt(self) -> float:
        return self.SonstigeFuEEinzelkosten + self.SonstigeFuEGemeinkosten

    @property
    def transport_logistik_gesamt(self) -> float:
        return self.TransportLogistikEinzelkosten + self.TransportLogistikGemeinkosten
    


@dataclass
class Kostenstellenrechnung:
    # Einkauf
    einkauf_material: float  # Materialkosten
    einkauf_einsatzstoffe: float  # Einsatzstoffe
    einkauf_betriebsstoffe: float  # Betriebsstoffe
    einkauf_personal: float  # Personalkosten
    einkauf_loehne_gehaelter: float  # Löhne/Gehälter
    einkauf_personalnebenkosten: float  # Personalnebenkosten
    einkauf_pensionsrueckstellungen: float  # Pensionsrückstellungen
    einkauf_abschreibungen: float  # Abschreibungen
    einkauf_gebaeude: float  # Gebäude
    einkauf_fertigungsanlagen: float  # Fertigungsanlagen
    einkauf_umwelttechnik: float  # Umwelttechnik
    einkauf_fertigerzeugnisse: float  # Fertigerzeugnisse
    einkauf_sonstige_kosten: float  # Sonstige Kosten
    einkauf_sonstige_fixe_kosten: float  # Sonstige fixe Kosten
    einkauf_instandhaltung: float  # Instandhaltung/Rationalisierung
    einkauf_prozessoptimierung: float  # Prozessoptimierung
    einkauf_umweltabgabe: float  # Umweltabgabe
    einkauf_nacharbeit_ausschuss: float  # Nacharbeit/Ausschuss
    einkauf_lagerkosten: float  # Lagerkosten
    einkauf_marketing: float  # Werbung/Marktforschung/Corporate Identity
    einkauf_sonstige_fue: float  # Sonstige Kosten F&E
    einkauf_transport_logistik: float  # Transport/Logistik

    # Fertigung
    fertigung_material: float
    fertigung_einsatzstoffe: float
    fertigung_betriebsstoffe: float
    fertigung_personal: float
    fertigung_loehne_gehaelter: float
    fertigung_personalnebenkosten: float
    fertigung_pensionsrueckstellungen: float
    fertigung_abschreibungen: float
    fertigung_gebaeude: float
    fertigung_fertigungsanlagen: float
    fertigung_umwelttechnik: float
    fertigung_fertigerzeugnisse: float
    fertigung_sonstige_kosten: float
    fertigung_sonstige_fixe_kosten: float
    fertigung_instandhaltung: float
    fertigung_prozessoptimierung: float
    fertigung_umweltabgabe: float
    fertigung_nacharbeit_ausschuss: float
    fertigung_lagerkosten: float
    fertigung_marketing: float
    fertigung_sonstige_fue: float
    fertigung_transport_logistik: float

    # F&E
    fue_material: float
    fue_einsatzstoffe: float
    fue_betriebsstoffe: float
    fue_personal: float
    fue_loehne_gehaelter: float
    fue_personalnebenkosten: float
    fue_pensionsrueckstellungen: float
    fue_abschreibungen: float
    fue_gebaeude: float
    fue_fertigungsanlagen: float
    fue_umwelttechnik: float
    fue_fertigerzeugnisse: float
    fue_sonstige_kosten: float
    fue_sonstige_fixe_kosten: float
    fue_instandhaltung: float
    fue_prozessoptimierung: float
    fue_umweltabgabe: float
    fue_nacharbeit_ausschuss: float
    fue_lagerkosten: float
    fue_marketing: float
    fue_sonstige_fue: float
    fue_transport_logistik: float

    # Vertrieb
    vertrieb_material: float
    vertrieb_einsatzstoffe: float
    vertrieb_betriebsstoffe: float
    vertrieb_personal: float
    vertrieb_loehne_gehaelter: float
    vertrieb_personalnebenkosten: float
    vertrieb_pensionsrueckstellungen: float
    vertrieb_abschreibungen: float
    vertrieb_gebaeude: float
    vertrieb_fertigungsanlagen: float
    vertrieb_umwelttechnik: float
    vertrieb_fertigerzeugnisse: float
    vertrieb_sonstige_kosten: float
    vertrieb_sonstige_fixe_kosten: float
    vertrieb_instandhaltung: float
    vertrieb_prozessoptimierung: float
    vertrieb_umweltabgabe: float
    vertrieb_nacharbeit_ausschuss: float
    vertrieb_lagerkosten: float
    vertrieb_marketing: float
    vertrieb_sonstige_fue: float
    vertrieb_transport_logistik: float

    # Verwaltung
    verwaltung_material: float
    verwaltung_einsatzstoffe: float
    verwaltung_betriebsstoffe: float
    verwaltung_personal: float
    verwaltung_loehne_gehaelter: float
    verwaltung_personalnebenkosten: float
    verwaltung_pensionsrueckstellungen: float
    verwaltung_abschreibungen: float
    verwaltung_gebaeude: float
    verwaltung_fertigungsanlagen: float
    verwaltung_umwelttechnik: float
    verwaltung_fertigerzeugnisse: float
    verwaltung_sonstige_kosten: float
    verwaltung_sonstige_fixe_kosten: float
    verwaltung_instandhaltung: float
    verwaltung_prozessoptimierung: float
    verwaltung_umweltabgabe: float
    verwaltung_nacharbeit_ausschuss: float
    verwaltung_lagerkosten: float
    verwaltung_marketing: float
    verwaltung_sonstige_fue: float
    verwaltung_transport_logistik: float

    # Properties für die Summen der einzelnen Kostenstellen
    @property
    def einkauf_gesamt(self) -> float:
        return sum([
            self.einkauf_material,
            self.einkauf_einsatzstoffe,
            self.einkauf_betriebsstoffe,
            self.einkauf_personal,
            self.einkauf_loehne_gehaelter,
            self.einkauf_personalnebenkosten,
            self.einkauf_pensionsrueckstellungen,
            self.einkauf_abschreibungen,
            self.einkauf_gebaeude,
            self.einkauf_fertigungsanlagen,
            self.einkauf_umwelttechnik,
            self.einkauf_fertigerzeugnisse,
            self.einkauf_sonstige_kosten,
            self.einkauf_sonstige_fixe_kosten,
            self.einkauf_instandhaltung,
            self.einkauf_prozessoptimierung,
            self.einkauf_umweltabgabe,
            self.einkauf_nacharbeit_ausschuss,
            self.einkauf_lagerkosten,
            self.einkauf_marketing,
            self.einkauf_sonstige_fue,
            self.einkauf_transport_logistik
        ])

    @property
    def fertigung_gesamt(self) -> float:
        return sum([
            self.fertigung_material,
            self.fertigung_einsatzstoffe,
            self.fertigung_betriebsstoffe,
            self.fertigung_personal,
            self.fertigung_loehne_gehaelter,
            self.fertigung_personalnebenkosten,
            self.fertigung_pensionsrueckstellungen,
            self.fertigung_abschreibungen,
            self.fertigung_gebaeude,
            self.fertigung_fertigungsanlagen,
            self.fertigung_umwelttechnik,
            self.fertigung_fertigerzeugnisse,
            self.fertigung_sonstige_kosten,
            self.fertigung_sonstige_fixe_kosten,
            self.fertigung_instandhaltung,
            self.fertigung_prozessoptimierung,
            self.fertigung_umweltabgabe,
            self.fertigung_nacharbeit_ausschuss,
            self.fertigung_lagerkosten,
            self.fertigung_marketing,
            self.fertigung_sonstige_fue,
            self.fertigung_transport_logistik
        ])

    @property
    def fue_gesamt(self) -> float:
        return sum([
            self.fue_material,
            self.fue_einsatzstoffe,
            self.fue_betriebsstoffe,
            self.fue_personal,
            self.fue_loehne_gehaelter,
            self.fue_personalnebenkosten,
            self.fue_pensionsrueckstellungen,
            self.fue_abschreibungen,
            self.fue_gebaeude,
            self.fue_fertigungsanlagen,
            self.fue_umwelttechnik,
            self.fue_fertigerzeugnisse,
            self.fue_sonstige_kosten,
            self.fue_sonstige_fixe_kosten,
            self.fue_instandhaltung,
            self.fue_prozessoptimierung,
            self.fue_umweltabgabe,
            self.fue_nacharbeit_ausschuss,
            self.fue_lagerkosten,
            self.fue_marketing,
            self.fue_sonstige_fue,
            self.fue_transport_logistik
        ])

    @property
    def vertrieb_gesamt(self) -> float:
        return sum([
            self.vertrieb_material,
            self.vertrieb_einsatzstoffe,
            self.vertrieb_betriebsstoffe,
            self.vertrieb_personal,
            self.vertrieb_loehne_gehaelter,
            self.vertrieb_personalnebenkosten,
            self.vertrieb_pensionsrueckstellungen,
            self.vertrieb_abschreibungen,
            self.vertrieb_gebaeude,
            self.vertrieb_fertigungsanlagen,
            self.vertrieb_umwelttechnik,
            self.vertrieb_fertigerzeugnisse,
            self.vertrieb_sonstige_kosten,
            self.vertrieb_sonstige_fixe_kosten,
            self.vertrieb_instandhaltung,
            self.vertrieb_prozessoptimierung,
            self.vertrieb_umweltabgabe,
            self.vertrieb_nacharbeit_ausschuss,
            self.vertrieb_lagerkosten,
            self.vertrieb_marketing,
            self.vertrieb_sonstige_fue,
            self.vertrieb_transport_logistik
        ])

    @property
    def verwaltung_gesamt(self) -> float:
        return sum([
            self.verwaltung_material,
            self.verwaltung_einsatzstoffe,
            self.verwaltung_betriebsstoffe,
            self.verwaltung_personal,
            self.verwaltung_loehne_gehaelter,
            self.verwaltung_personalnebenkosten,
            self.verwaltung_pensionsrueckstellungen,
            self.verwaltung_abschreibungen,
            self.verwaltung_gebaeude,
            self.verwaltung_fertigungsanlagen,
            self.verwaltung_umwelttechnik,
            self.verwaltung_fertigerzeugnisse,
            self.verwaltung_sonstige_kosten,
            self.verwaltung_sonstige_fixe_kosten,
            self.verwaltung_instandhaltung,
            self.verwaltung_prozessoptimierung,
            self.verwaltung_umweltabgabe,
            self.verwaltung_nacharbeit_ausschuss,
            self.verwaltung_lagerkosten,
            self.verwaltung_marketing,
            self.verwaltung_sonstige_fue,
            self.verwaltung_transport_logistik
        ])

    # Properties für die Summen der einzelnen Kategorien über alle Kostenstellen
    @property
    def material_gesamt(self) -> float:
        return (
            self.einkauf_material +
            self.fertigung_material +
            self.fue_material +
            self.vertrieb_material +
            self.verwaltung_material
        )
    
    @property
    def einsatzstoffe_gesamt(self) -> float:
        return (
            self.einkauf_einsatzstoffe +
            self.fertigung_einsatzstoffe +
            self.fue_einsatzstoffe +
            self.vertrieb_einsatzstoffe +
            self.verwaltung_einsatzstoffe
        )

    @property
    def betriebsstoffe_gesamt(self) -> float:
        return (
            self.einkauf_betriebsstoffe +
            self.fertigung_betriebsstoffe +
            self.fue_betriebsstoffe +
            self.vertrieb_betriebsstoffe +
            self.verwaltung_betriebsstoffe
        )

    @property
    def personal_gesamt(self) -> float:
        return (
            self.einkauf_personal +
            self.fertigung_personal +
            self.fue_personal +
            self.vertrieb_personal +
            self.verwaltung_personal
        )

    @property
    def loehne_gehaelter_gesamt(self) -> float:
        return (
            self.einkauf_loehne_gehaelter +
            self.fertigung_loehne_gehaelter +
            self.fue_loehne_gehaelter +
            self.vertrieb_loehne_gehaelter +
            self.verwaltung_loehne_gehaelter
        )

    @property
    def personalnebenkosten_gesamt(self) -> float:
        return (
            self.einkauf_personalnebenkosten +
            self.fertigung_personalnebenkosten +
            self.fue_personalnebenkosten +
            self.vertrieb_personalnebenkosten +
            self.verwaltung_personalnebenkosten
        )

    @property
    def pensionsrueckstellungen_gesamt(self) -> float:
        return (
            self.einkauf_pensionsrueckstellungen +
            self.fertigung_pensionsrueckstellungen +
            self.fue_pensionsrueckstellungen +
            self.vertrieb_pensionsrueckstellungen +
            self.verwaltung_pensionsrueckstellungen
        )

    @property
    def abschreibungen_gesamt(self) -> float:
        return (
            self.einkauf_abschreibungen +
            self.fertigung_abschreibungen +
            self.fue_abschreibungen +
            self.vertrieb_abschreibungen +
            self.verwaltung_abschreibungen
        )

    @property
    def gebaeude_gesamt(self) -> float:
        return (
            self.einkauf_gebaeude +
            self.fertigung_gebaeude +
            self.fue_gebaeude +
            self.vertrieb_gebaeude +
            self.verwaltung_gebaeude
        )

    @property
    def fertigungsanlagen_gesamt(self) -> float:
        return (
            self.einkauf_fertigungsanlagen +
            self.fertigung_fertigungsanlagen +
            self.fue_fertigungsanlagen +
            self.vertrieb_fertigungsanlagen +
            self.verwaltung_fertigungsanlagen
        )

    @property
    def umwelttechnik_gesamt(self) -> float:
        return (
            self.einkauf_umwelttechnik +
            self.fertigung_umwelttechnik +
            self.fue_umwelttechnik +
            self.vertrieb_umwelttechnik +
            self.verwaltung_umwelttechnik
        )

    @property
    def fertigerzeugnisse_gesamt(self) -> float:
        return (
            self.einkauf_fertigerzeugnisse +
            self.fertigung_fertigerzeugnisse +
            self.fue_fertigerzeugnisse +
            self.vertrieb_fertigerzeugnisse +
            self.verwaltung_fertigerzeugnisse
        )

    @property
    def sonstige_kosten_gesamt(self) -> float:
        return (
            self.einkauf_sonstige_kosten +
            self.fertigung_sonstige_kosten +
            self.fue_sonstige_kosten +
            self.vertrieb_sonstige_kosten +
            self.verwaltung_sonstige_kosten
        )

    @property
    def sonstige_fixe_kosten_gesamt(self) -> float:
        return (
            self.einkauf_sonstige_fixe_kosten +
            self.fertigung_sonstige_fixe_kosten +
            self.fue_sonstige_fixe_kosten +
            self.vertrieb_sonstige_fixe_kosten +
            self.verwaltung_sonstige_fixe_kosten
        )

    @property
    def instandhaltung_gesamt(self) -> float:
        return (
            self.einkauf_instandhaltung +
            self.fertigung_instandhaltung +
            self.fue_instandhaltung +
            self.vertrieb_instandhaltung +
            self.verwaltung_instandhaltung
        )

    @property
    def prozessoptimierung_gesamt(self) -> float:
        return (
            self.einkauf_prozessoptimierung +
            self.fertigung_prozessoptimierung +
            self.fue_prozessoptimierung +
            self.vertrieb_prozessoptimierung +
            self.verwaltung_prozessoptimierung
        )

    @property
    def umweltabgabe_gesamt(self) -> float:
        return (
            self.einkauf_umweltabgabe +
            self.fertigung_umweltabgabe +
            self.fue_umweltabgabe +
            self.vertrieb_umweltabgabe +
            self.verwaltung_umweltabgabe
        )

    @property
    def nacharbeit_ausschuss_gesamt(self) -> float:
        return (
            self.einkauf_nacharbeit_ausschuss +
            self.fertigung_nacharbeit_ausschuss +
            self.fue_nacharbeit_ausschuss +
            self.vertrieb_nacharbeit_ausschuss +
            self.verwaltung_nacharbeit_ausschuss
        )

    @property
    def lagerkosten_gesamt(self) -> float:
        return (
            self.einkauf_lagerkosten +
            self.fertigung_lagerkosten +
            self.fue_lagerkosten +
            self.vertrieb_lagerkosten +
            self.verwaltung_lagerkosten
        )

    @property
    def marketing_gesamt(self) -> float:
        return (
            self.einkauf_marketing +
            self.fertigung_marketing +
            self.fue_marketing +
            self.vertrieb_marketing +
            self.verwaltung_marketing
        )

    @property
    def sonstige_fue_gesamt(self) -> float:
        return (
            self.einkauf_sonstige_fue +
            self.fertigung_sonstige_fue +
            self.fue_sonstige_fue +
            self.vertrieb_sonstige_fue +
            self.verwaltung_sonstige_fue
        )

    @property
    def transport_logistik_gesamt(self) -> float:
        return (
            self.einkauf_transport_logistik +
            self.fertigung_transport_logistik +
            self.fue_transport_logistik +
            self.vertrieb_transport_logistik +
            self.verwaltung_transport_logistik
        )

    @property
    def gesamtkosten(self) -> float:
        """Berechnet die Summe aller Kostenstellen."""
        return (
            self.einkauf_gesamt +
            self.fertigung_gesamt +
            self.fue_gesamt +
            self.vertrieb_gesamt +
            self.verwaltung_gesamt
        )
    