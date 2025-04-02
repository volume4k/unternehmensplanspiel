"use client";

import { useState } from "react";
import { Dropzone } from "@/components/ui/dropzone";
import { Navbar } from "@/components/ui/navbar";

export default function Home() {
  const [sheets, setSheets] = useState<any[]>([]);

  const handleFileAccepted = (data: any) => {
    setSheets(data);
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <Navbar />
      <main className="container mx-auto px-4 py-8">
        <div className="max-w-4xl mx-auto">
          <div className="bg-white rounded-xl shadow-sm p-8 mb-8">
            <div className="text-center mb-8">
              <h1 className="text-3xl font-bold text-gray-900 mb-4">
                Excel Upload der aktuellen Berichte
              </h1>
              <p className="text-gray-600">
                Hier die Excel-Datei hochladen, um die aktuellen Daten aus verschiedenen Blättern zu extrahieren und darauf basierend Szenarien zu erstellen und zu simulieren.
              </p>
            </div>

            <Dropzone onFileAccepted={handleFileAccepted} />
          </div>

          {sheets.length > 0 && (
            <div className="space-y-8">
              <h2 className="text-2xl font-semibold text-gray-900">
                Gefundene Blätter
              </h2>
              <div className="space-y-6">
                {sheets.map((sheet, index) => (
                  <div
                    key={index}
                    className="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden"
                  >
                    <div className="px-6 py-4 border-b border-gray-200">
                      <h3 className="text-lg font-medium text-gray-900">
                        {sheet.name}
                      </h3>
                    </div>
                    <div className="overflow-x-auto">
                      <table className="min-w-full divide-y divide-gray-200">
                        <thead>
                          <tr>
                            {sheet.data[0]?.map((header: string, i: number) => (
                              <th
                                key={i}
                                className="px-6 py-3 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                              >
                                {header}
                              </th>
                            ))}
                          </tr>
                        </thead>
                        <tbody className="bg-white divide-y divide-gray-200">
                          {sheet.data.slice(1).map((row: any[], rowIndex: number) => (
                            <tr key={rowIndex} className="hover:bg-gray-50">
                              {row.map((cell: any, cellIndex: number) => (
                                <td
                                  key={cellIndex}
                                  className="px-6 py-4 whitespace-nowrap text-sm text-gray-500"
                                >
                                  {cell}
                                </td>
                              ))}
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
      </main>
    </div>
  );
}
