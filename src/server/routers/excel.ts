import { z } from 'zod';
import * as XLSX from 'xlsx';
import { router, publicProcedure } from '../trpc';
import { prisma } from '@/lib/prisma';

export const excelRouter = router({
  parseExcel: publicProcedure
    .input(z.object({
      fileBuffer: z.array(z.number()),
    }))
    .mutation(async ({ input }) => {
      try {
        const uint8Array = new Uint8Array(input.fileBuffer);
        const workbook = XLSX.read(uint8Array, { type: 'array' });

        const data: { [key: string]: any[] } = {};

        workbook.SheetNames.forEach((sheetName) => {
          const worksheet = workbook.Sheets[sheetName];
          // Lese die Daten als Array von Arrays
          const rawData = XLSX.utils.sheet_to_json(worksheet, { header: 'A', raw: false });
          
          if (sheetName === '1) Executive Summary') {
            // Extrahiere die relevanten Werte aus dem Executive Summary
            const summaryData = {
              aktienkurs: parseFloat(rawData.find((row: any) => row.A === 'Aktienkurs')?.C || '0'),
              umsatzGesamtMEUR: parseFloat(rawData.find((row: any) => row.A === 'Umsatz Gesamt')?.C || '0'),
              periodenErgebnisMEUR: parseFloat(rawData.find((row: any) => row.A === 'Periodenüberschuss/-fehlbetrag')?.C || '0'),
              absatzCopyClassic: parseInt(rawData.find((row: any) => row.A === 'Absatz Copy Classic')?.C || '0'),
              umsatzCopyClassicMEUR: parseFloat(rawData.find((row: any) => row.A === 'Umsatz Gesamt Copy Classic')?.C || '0'),
              // Diese Werte müssen noch ergänzt werden, falls in der Excel-Datei vorhanden
              geplanterAbsatz: parseInt(rawData.find((row: any) => row.A === 'Geplanter Absatz')?.C || '0'),
              tatsaechlicherAbsatz: parseInt(rawData.find((row: any) => row.A === 'Tatsächlicher Absatz')?.C || '0'),
            };
            data[sheetName] = [summaryData];
          } 
          else if (sheetName === '2) Marktforschungsbericht') {
            // Extrahiere die MarketResearchRow-Daten
            const marketData: any[] = [];
            
            // Find rows with company data (U1, U2, etc.)
            const companyRows = rawData.filter((row: any) => 
              row.A && row.A.startsWith('U') && /^U\d+$/.test(row.A)
            );
            
            companyRows.forEach((row: any) => {
              marketData.push({
                unternehmen: row.A || '',
                price: parseFloat(row.B || '0'),
                priceDeviation: parseFloat(row.C || '0'),
                technologyIndex: parseFloat(row.D || '0'),
                werbeBudget: parseFloat(row.E || '0'),
                ciBudget: parseFloat(row.F || '0'),
                vertriebsMitarb: parseInt(row.G || '0'),
                bekanntheitsIdx: parseFloat(row.H || '0'),
                kundenZufriedIdx: parseFloat(row.I || '0'),
              });
            });
            
            data[sheetName] = marketData;
          }
          else if (sheetName === 'Fertigungsbericht' || sheetName === '3) Fertigungsbericht') {
            // Extrahiere die ProductionReport-Daten
            const productionData = {
              plannedProduction: parseInt(rawData.find((row: any) => row.A === 'Geplante Produktion')?.C || '0'),
              actualProduction: parseInt(rawData.find((row: any) => row.A === 'Tatsächliche Produktion')?.C || '0'),
              utilizationMachinesPct: parseFloat(rawData.find((row: any) => row.A === 'Auslastung Anlagen')?.C?.replace('%', '') || '0') / 100,
              utilizationStaffPct: parseFloat(rawData.find((row: any) => row.A === 'Auslastung Mitarbeiter')?.C?.replace('%', '') || '0') / 100,
            };
            
            // Extrahiere die ProductionEquipment-Daten
            const equipmentData: any[] = [];
            
            // Find rows with equipment data
            const equipmentRows = rawData.filter((row: any) => 
              row.A && row.A.includes('Typ A #')
            );
            
            equipmentRows.forEach((row: any) => {
              const match = row.A.match(/Typ A #(\d+)/);
              const number = match ? parseInt(match[1]) : 0;
              
              equipmentData.push({
                type: 'Typ A',
                number: number,
                beschaffungsperiode: parseInt(row.B || '0'),
                beschaffungswertMEUR: parseFloat(row.C || '0'),
                restlaufzeit: parseInt(row.D || '0'),
                abschreibungMEUR: parseFloat(row.E || '0'),
                restbuchwertMEUR: parseFloat(row.F || '0'),
                sonstFixkostenMEUR: parseFloat(row.G || '0'),
                resterloesPct: parseFloat(row.H?.replace('%', '') || '0') / 100,
              });
            });
            
            data['productionReport'] = [productionData];
            data['productionEquipment'] = equipmentData;
          }
          else if (sheetName === 'Forschung & Entwicklung' || sheetName === '4) Forschung & Entwicklung') {
            // Extrahiere die RnDReport-Daten
            const rndData = {
              investTotalMEUR: parseFloat(rawData.find((row: any) => row.A === 'F&E-Investitionen gesamt')?.C || '0'),
              technologyIndex: parseFloat(rawData.find((row: any) => row.A === 'Technologieindex')?.C || '0'),
              ecologyIndex: parseFloat(rawData.find((row: any) => row.A === 'Ökologieindex')?.C || '0'),
              valueAnalysisIndex: parseFloat(rawData.find((row: any) => row.A === 'Wertanalyseindex')?.C || '0'),
              employeeCount: parseInt(rawData.find((row: any) => row.A === 'F&E-Mitarbeiter')?.C || '0'),
            };
            
            data['rndReport'] = [rndData];
          }
          // Weitere Sheets hier ergänzen...
          
          // Lagerbestand
          else if (sheetName === 'Lager' || sheetName === '5) Lager') {
            const inventoryData = {
              lagerendbestandEinsatzstoffe: parseInt(rawData.find((row: any) => row.A === 'Lagerendbestand Einsatzstoffe')?.C || '0'),
              lagerendbestandFertigerzeugn: parseInt(rawData.find((row: any) => row.A === 'Lagerendbestand Fertigerzeugnisse')?.C || '0'),
              zugangVonLieferantStueck: parseInt(rawData.find((row: any) => row.A === 'Zugang von Lieferant')?.C || '0'),
              zugangVonFertigungStueck: parseInt(rawData.find((row: any) => row.A === 'Zugang von Fertigung')?.C || '0'),
              abgangAnVertriebStueck: parseInt(rawData.find((row: any) => row.A === 'Abgang an Vertrieb')?.C || '0'),
              lagerwertMEUR: parseFloat(rawData.find((row: any) => row.A === 'Lagerwert')?.C || '0'),
            };
            
            data['inventoryReport'] = [inventoryData];
          }
          
          // Personal
          else if (sheetName === 'Personal' || sheetName === '6) Personal') {
            const personnelData = {
              totalBegin: parseInt(rawData.find((row: any) => row.A === 'Summe' && row.B)?.B || '0'),
              totalHired: parseInt(rawData.find((row: any) => row.A === 'Summe' && row.C)?.C || '0'),
              totalFired: parseInt(rawData.find((row: any) => row.A === 'Summe' && row.D)?.D || '0'),
              totalEnd: parseInt(rawData.find((row: any) => row.A === 'Summe' && row.E)?.E || '0'),
            };
            
            // Departmentdaten extrahieren
            const departmentRows = rawData.filter((row: any) => 
              row.A && ['Einkauf', 'Fertigung', 'F&E', 'Vertrieb', 'Verwaltung'].includes(row.A)
            );
            
            const departmentData = departmentRows.map((row: any) => ({
              department: row.A,
              beginCount: parseInt(row.B || '0'),
              hiredCount: parseInt(row.C || '0'),
              firedCount: parseInt(row.D || '0'),
              endCount: parseInt(row.E || '0'),
            }));
            
            data['personnelReport'] = [personnelData];
            data['personnelDepartments'] = departmentData;
          }
          
          // Für die Bilanzrechnung-bezogenen Sheets
          else if (sheetName === 'Bilanz' || sheetName === '13) Bilanz') {
            const balanceData = {
              anlagevermoegenMEUR: parseFloat(rawData.find((row: any) => row.A === 'Anlagevermögen')?.C || '0'),
              umlaufvermoegenMEUR: parseFloat(rawData.find((row: any) => row.A === 'Umlaufvermögen')?.C || '0'),
              eigenkapitalMEUR: parseFloat(rawData.find((row: any) => row.A === 'Eigenkapital')?.C || '0'),
              pensionsRueckstMEUR: parseFloat(rawData.find((row: any) => row.A === 'Pensionsrückstellungen')?.C || '0'),
              verbindlichkeitenMEUR: parseFloat(rawData.find((row: any) => row.A === 'Verbindlichkeiten')?.C || '0'),
              bilanzsummeMEUR: parseFloat(rawData.find((row: any) => row.A === 'Bilanzsumme')?.C || '0'),
              
              // Detaildaten
              grundstueckeMEUR: parseFloat(rawData.find((row: any) => row.A === 'Grundstücke und Bauten')?.C || '0'),
              maschinenMEUR: parseFloat(rawData.find((row: any) => row.A === 'Maschinen')?.C || '0'),
              fertigeErzeugnisseMEUR: parseFloat(rawData.find((row: any) => row.A === 'Fertige Erzeugnisse')?.C || '0'),
              forderungenMEUR: parseFloat(rawData.find((row: any) => row.A === 'Forderungen')?.C || '0'),
              kassenbestandMEUR: parseFloat(rawData.find((row: any) => row.A === 'Kassenbestand')?.C || '0'),
            };
            
            data['balanceSheet'] = [balanceData];
          }
          
          // Gewinn- und Verlustrechnung
          else if (sheetName === 'Gewinn- und Verlustrechnung' || sheetName === '10) Gewinn- und Verlustrechnung') {
            const incomeData = {
              umsatzMEUR: parseFloat(rawData.find((row: any) => row.A === 'Umsatz')?.C || '0'),
              sonstErtraegeMEUR: parseFloat(rawData.find((row: any) => row.A === 'Sonstige Erträge')?.C || '0'),
              bestandVeraendMEUR: parseFloat(rawData.find((row: any) => row.A === 'Bestandsveränderung')?.C || '0'),
              materialAufwandMEUR: parseFloat(rawData.find((row: any) => row.A === 'Materialaufwand')?.C || '0'),
              personalAufwandMEUR: parseFloat(rawData.find((row: any) => row.A === 'Personalaufwand')?.C || '0'),
              abschreibungenMEUR: parseFloat(rawData.find((row: any) => row.A === 'Abschreibungen')?.C || '0'),
              sonstAufwandMEUR: parseFloat(rawData.find((row: any) => row.A === 'Sonstiger Aufwand')?.C || '0'),
              betriebsergebnisMEUR: parseFloat(rawData.find((row: any) => row.A === 'Betriebsergebnis')?.C || '0'),
              finanzErgebnisMEUR: parseFloat(rawData.find((row: any) => row.A === 'Finanzergebnis')?.C || '0'),
              gewinnVorSteuernMEUR: parseFloat(rawData.find((row: any) => row.A === 'Gewinn vor Steuern')?.C || '0'),
              steuernMEUR: parseFloat(rawData.find((row: any) => row.A === 'Steuern')?.C || '0'),
              periodenErgebnisMEUR: parseFloat(rawData.find((row: any) => row.A === 'Periodenüberschuss/-fehlbetrag')?.C || '0'),
            };
            
            data['incomeStatement'] = [incomeData];
          }
        });

        return data;
      } catch (error) {
        console.error('Fehler beim Parsen der Excel-Datei:', error);
        throw new Error('Fehler beim Parsen der Excel-Datei');
      }
    }),

  importData: publicProcedure
    .input(z.object({
      data: z.record(z.array(z.any())),
    }))
    .mutation(async ({ input }) => {
      try {
        // Perioden-Nummer (zunächst 0 für die erste Periode)
        const periodNumber = 0;
        
        // Erstelle einen neuen Eintrag in der Period-Tabelle
        const period = await prisma.period.create({
          data: {
            periodNumber: periodNumber,
            
            // 1:1 Beziehungen
            executiveSummary: input.data['1) Executive Summary']?.[0] ? {
              create: {
                aktienkurs: input.data['1) Executive Summary'][0].aktienkurs,
                umsatzGesamtMEUR: input.data['1) Executive Summary'][0].umsatzGesamtMEUR,
                periodenErgebnisMEUR: input.data['1) Executive Summary'][0].periodenErgebnisMEUR,
                absatzCopyClassic: input.data['1) Executive Summary'][0].absatzCopyClassic,
                umsatzCopyClassicMEUR: input.data['1) Executive Summary'][0].umsatzCopyClassicMEUR,
                geplanterAbsatz: input.data['1) Executive Summary'][0].geplanterAbsatz,
                tatsaechlicherAbsatz: input.data['1) Executive Summary'][0].tatsaechlicherAbsatz,
              }
            } : undefined,
            
            // Produktionsdaten
            productionReport: input.data['productionReport']?.[0] ? {
              create: input.data['productionReport'][0]
            } : undefined,
            
            // Forschung & Entwicklung
            rndReport: input.data['rndReport']?.[0] ? {
              create: input.data['rndReport'][0]
            } : undefined,
            
            // Lagerdaten
            inventoryReport: input.data['inventoryReport']?.[0] ? {
              create: input.data['inventoryReport'][0]
            } : undefined,
            
            // Personaldaten
            personnelReport: input.data['personnelReport']?.[0] ? {
              create: {
                ...input.data['personnelReport'][0],
                // Füge Departments als verschachtelte Objekte hinzu
                departments: input.data['personnelDepartments']?.length ? {
                  create: input.data['personnelDepartments']
                } : undefined
              }
            } : undefined,
            
            // Bilanz
            balanceSheet: input.data['balanceSheet']?.[0] ? {
              create: input.data['balanceSheet'][0]
            } : undefined,
            
            // Gewinn- und Verlustrechnung
            incomeStatement: input.data['incomeStatement']?.[0] ? {
              create: input.data['incomeStatement'][0]
            } : undefined,
            
            // 1:n Beziehungen
            marketResearchRows: input.data['2) Marktforschungsbericht']?.length ? {
              create: input.data['2) Marktforschungsbericht']
            } : undefined,
            
            productionEquipments: input.data['productionEquipment']?.length ? {
              create: input.data['productionEquipment']
            } : undefined,
          }
        });

        return period;
      } catch (error) {
        console.error('Fehler beim Importieren der Daten:', error);
        throw new Error('Fehler beim Importieren der Daten');
      }
    }),
}); 