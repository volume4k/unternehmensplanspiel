"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { CheckCircle2, XCircle, AlertCircle } from "lucide-react";

interface DataPreviewProps {
  data: {
    [key: string]: any[]
  };
  onConfirm: () => void;
  onCancel: () => void;
}

export function DataPreview({ data, onConfirm, onCancel }: DataPreviewProps) {
  const [activeTab, setActiveTab] = useState("executive-summary");

  const validateData = (sheetName: string, sheetData: any[]) => {
    const errors: string[] = [];
    const warnings: string[] = [];

    switch (sheetName) {
      case "1) Executive Summary":
        if (sheetData.length === 0) {
          errors.push("Keine Daten gefunden");
          return { errors, warnings };
        }

        const firstRow = sheetData[0];
        if (typeof firstRow.aktienkurs !== 'number' || firstRow.aktienkurs <= 0) {
          errors.push("Ungültiger Aktienkurs");
        }
        if (typeof firstRow.umsatzGesamtMEUR !== 'number' || firstRow.umsatzGesamtMEUR <= 0) {
          errors.push("Ungültiger Gesamtumsatz");
        }
        if (typeof firstRow.periodenErgebnisMEUR !== 'number') {
          errors.push("Ungültiger Periodenüberschuss/-fehlbetrag");
        }
        break;
      case "2) Marktforschungsbericht":
        if (sheetData.length === 0) {
          warnings.push("Keine Marktforschungsdaten gefunden");
        } else {
          // Validiere die erste Zeile der Marktforschungsdaten
          const firstRow = sheetData[0];
          if (!firstRow.unternehmen) {
            warnings.push("Unternehmen nicht angegeben");
          }
          if (typeof firstRow.price !== 'number' || firstRow.price <= 0) {
            warnings.push("Ungültiger Preis bei mindestens einem Unternehmen");
          }
        }
        break;
      case "productionReport":
        if (sheetData.length === 0) {
          warnings.push("Keine Produktionsdaten gefunden");
        } else {
          const firstRow = sheetData[0];
          if (typeof firstRow.plannedProduction !== 'number') {
            warnings.push("Geplante Produktion nicht angegeben");
          }
          if (typeof firstRow.actualProduction !== 'number') {
            warnings.push("Tatsächliche Produktion nicht angegeben");
          }
        }
        break;
      case "productionEquipment":
        if (sheetData.length === 0) {
          warnings.push("Keine Fertigungsanlagen gefunden");
        }
        break;
      case "rndReport":
        if (sheetData.length === 0) {
          warnings.push("Keine F&E-Daten gefunden");
        }
        break;
      case "inventoryReport":
        if (sheetData.length === 0) {
          warnings.push("Keine Lagerdaten gefunden");
        }
        break;
      case "balanceSheet":
        if (sheetData.length === 0) {
          warnings.push("Keine Bilanzdaten gefunden");
        }
        break;
      case "incomeStatement":
        if (sheetData.length === 0) {
          warnings.push("Keine GuV-Daten gefunden");
        }
        break;
    }

    return { errors, warnings };
  };

  const renderValidationStatus = (sheetName: string, sheetData: any[]) => {
    const { errors, warnings } = validateData(sheetName, sheetData);

    return (
      <div className="space-y-4">
        {errors.length > 0 && (
          <div className="bg-red-50 border border-red-200 rounded-lg p-4">
            <div className="flex items-center gap-2 text-red-700 mb-2">
              <XCircle className="h-5 w-5" />
              <h3 className="font-medium">Fehler gefunden</h3>
            </div>
            <ul className="list-disc list-inside space-y-1 text-sm text-red-600">
              {errors.map((error, index) => (
                <li key={index}>{error}</li>
              ))}
            </ul>
          </div>
        )}
        {warnings.length > 0 && (
          <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-4">
            <div className="flex items-center gap-2 text-yellow-700 mb-2">
              <AlertCircle className="h-5 w-5" />
              <h3 className="font-medium">Warnungen</h3>
            </div>
            <ul className="list-disc list-inside space-y-1 text-sm text-yellow-600">
              {warnings.map((warning, index) => (
                <li key={index}>{warning}</li>
              ))}
            </ul>
          </div>
        )}
        {errors.length === 0 && warnings.length === 0 && (
          <div className="bg-green-50 border border-green-200 rounded-lg p-4">
            <div className="flex items-center gap-2 text-green-700">
              <CheckCircle2 className="h-5 w-5" />
              <span className="font-medium">Alle Daten sind gültig</span>
            </div>
          </div>
        )}
      </div>
    );
  };

  const renderDataPreview = (sheetName: string, sheetData: any[]) => {
    if (!sheetData || sheetData.length === 0) {
      return (
        <div className="text-center py-8 text-muted-foreground">
          Keine Daten verfügbar
        </div>
      );
    }

    const headers = Object.keys(sheetData[0]);
    const previewData = sheetData.slice(0, 5);

    return (
      <div className="overflow-x-auto">
        <table className="min-w-full divide-y divide-gray-200">
          <thead className="bg-gray-50">
            <tr>
              {headers.map((header) => (
                <th
                  key={header}
                  className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                >
                  {header}
                </th>
              ))}
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {previewData.map((row, rowIndex) => (
              <tr key={rowIndex}>
                {headers.map((header) => (
                  <td
                    key={header}
                    className="px-6 py-4 whitespace-nowrap text-sm text-gray-900"
                  >
                    {row[header]}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
        {sheetData.length > 5 && (
          <div className="text-center py-2 text-sm text-muted-foreground">
            Zeige {previewData.length} von {sheetData.length} Zeilen
          </div>
        )}
      </div>
    );
  };

  return (
    <div className="space-y-6">
      <Tabs value={activeTab} onValueChange={setActiveTab}>
        <TabsList className="grid w-full grid-cols-3">
          <TabsTrigger value="executive-summary">Executive Summary</TabsTrigger>
          <TabsTrigger value="market-research">Marktforschung</TabsTrigger>
          <TabsTrigger value="production">Produktion</TabsTrigger>
        </TabsList>

        <TabsContent value="executive-summary">
          <Card>
            <CardHeader>
              <CardTitle>Executive Summary</CardTitle>
            </CardHeader>
            <CardContent className="space-y-6">
              {renderValidationStatus("1) Executive Summary", data["1) Executive Summary"] || [])}
              {renderDataPreview("1) Executive Summary", data["1) Executive Summary"] || [])}
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="market-research">
          <Card>
            <CardHeader>
              <CardTitle>Marktforschung</CardTitle>
            </CardHeader>
            <CardContent className="space-y-6">
              {renderValidationStatus("2) Marktforschungsbericht", data["2) Marktforschungsbericht"] || [])}
              {renderDataPreview("2) Marktforschungsbericht", data["2) Marktforschungsbericht"] || [])}
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="production">
          <Card>
            <CardHeader>
              <CardTitle>Produktion</CardTitle>
            </CardHeader>
            <CardContent className="space-y-6">
              <div className="grid grid-cols-1 gap-6">
                <div>
                  <h3 className="text-lg font-medium mb-2">Produktionsbericht</h3>
                  {renderValidationStatus("productionReport", data["productionReport"] || [])}
                  {renderDataPreview("productionReport", data["productionReport"] || [])}
                </div>
                
                <div>
                  <h3 className="text-lg font-medium mb-2">Fertigungsanlagen</h3>
                  {renderValidationStatus("productionEquipment", data["productionEquipment"] || [])}
                  {renderDataPreview("productionEquipment", data["productionEquipment"] || [])}
                </div>
              </div>
            </CardContent>
          </Card>
        </TabsContent>
      </Tabs>

      <div className="flex justify-end gap-4">
        <Button variant="outline" onClick={onCancel}>
          Abbrechen
        </Button>
        <Button onClick={onConfirm}>
          Import bestätigen
        </Button>
      </div>
    </div>
  );
} 