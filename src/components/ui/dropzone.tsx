"use client";

import { useState, useCallback } from "react";
import { useDropzone } from "react-dropzone";
import { Upload, FileSpreadsheet, X } from "lucide-react";
import * as XLSX from "xlsx";

interface DropzoneProps {
  onFileAccepted: (data: any) => void;
}

export function Dropzone({ onFileAccepted }: DropzoneProps) {
  const [file, setFile] = useState<File | null>(null);
  const [error, setError] = useState<string | null>(null);

  const onDrop = useCallback((acceptedFiles: File[]) => {
    const file = acceptedFiles[0];
    if (!file) return;

    // Check file type
    if (!file.name.match(/\.(xlsx|xls)$/)) {
      setError("Bitte laden Sie nur Excel-Dateien (.xlsx oder .xls) hoch.");
      return;
    }

    setFile(file);
    setError(null);

    const reader = new FileReader();
    reader.onload = (e) => {
      try {
        const data = e.target?.result;
        const workbook = XLSX.read(data, { type: "binary" });
        const sheetNames = workbook.SheetNames;
        const sheets = sheetNames.map((name) => {
          const sheet = workbook.Sheets[name];
          return {
            name,
            data: XLSX.utils.sheet_to_json(sheet, { header: 1 }),
          };
        });
        onFileAccepted(sheets);
      } catch (err) {
        setError("Fehler beim Lesen der Excel-Datei.");
      }
    };
    reader.readAsBinaryString(file);
  }, [onFileAccepted]);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": [".xlsx"],
      "application/vnd.ms-excel": [".xls"],
    },
    maxFiles: 1,
  });

  const removeFile = () => {
    setFile(null);
    setError(null);
  };

  return (
    <div className="w-full">
      <div
        {...getRootProps()}
        className={`border-2 border-dashed rounded-lg p-8 text-center cursor-pointer transition-all duration-200
          ${isDragActive ? "border-blue-500 bg-blue-50" : "border-gray-300 hover:border-gray-400"}
          ${error ? "border-red-500 bg-red-50" : ""}`}
      >
        <input {...getInputProps()} />
        {file ? (
          <div className="flex items-center justify-center gap-3">
            <FileSpreadsheet className="w-8 h-8 text-blue-500" />
            <span className="text-sm font-medium text-gray-700">{file.name}</span>
            <button
              onClick={(e) => {
                e.stopPropagation();
                removeFile();
              }}
              className="ml-2 p-1.5 hover:bg-gray-100 rounded-full transition-colors"
            >
              <X className="w-4 h-4 text-gray-500" />
            </button>
          </div>
        ) : (
          <div className="flex flex-col items-center gap-3">
            <div className="p-3 bg-gray-50 rounded-full">
              <Upload className="w-8 h-8 text-gray-400" />
            </div>
            <div>
              <p className="text-sm font-medium text-gray-700">
                {isDragActive
                  ? "Lassen Sie die Datei hier fallen..."
                  : "Ziehen Sie eine Excel-Datei hierher"}
              </p>
              <p className="text-xs text-gray-500 mt-1">
                oder klicken Sie zum Auswählen
              </p>
            </div>
            <p className="text-xs text-gray-500">
              Unterstützte Formate: .xlsx, .xls
            </p>
          </div>
        )}
      </div>
      {error && (
        <p className="mt-3 text-sm text-red-500 text-center font-medium">{error}</p>
      )}
    </div>
  );
} 