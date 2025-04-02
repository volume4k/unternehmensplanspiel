"use client"

import { useState } from "react"
import { useRouter } from "next/navigation"
import { DataPreview } from "@/components/ui/data-preview"
import { Button } from "@/components/ui/button"
import { Upload, FileSpreadsheet } from "lucide-react"
import { trpc } from "@/utils/trpc"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"

export default function ImportPage() {
  const router = useRouter()
  const [excelData, setExcelData] = useState<any>(null)
  const [isLoading, setIsLoading] = useState(false)
  const [selectedFile, setSelectedFile] = useState<File | null>(null)

  const parseExcelMutation = trpc.excel.parseExcel.useMutation()
  const importDataMutation = trpc.excel.importData.useMutation()

  const handleFileSelect = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0]
    if (file) {
      setSelectedFile(file)
    }
  }

  const handleFileUpload = async () => {
    if (!selectedFile) return

    setIsLoading(true)
    try {
      const arrayBuffer = await selectedFile.arrayBuffer()
      const uint8Array = new Uint8Array(arrayBuffer)
      const data = await parseExcelMutation.mutateAsync({ 
        fileBuffer: Array.from(uint8Array) 
      })
      setExcelData(data)
    } catch (error) {
      console.error("Fehler beim Hochladen:", error)
      // TODO: Fehlerbehandlung implementieren
    } finally {
      setIsLoading(false)
    }
  }

  const handleConfirm = async () => {
    if (!excelData) return

    setIsLoading(true)
    try {
      await importDataMutation.mutateAsync({ data: excelData })
      router.push("/dashboard")
    } catch (error) {
      console.error("Fehler beim Importieren:", error)
      // TODO: Fehlerbehandlung implementieren
    } finally {
      setIsLoading(false)
    }
  }

  const handleCancel = () => {
    router.push("/")
  }

  return (
    <div className="container mx-auto py-8">
      <div className="max-w-4xl mx-auto space-y-8">
        <div className="text-center">
          <h1 className="text-3xl font-bold mb-4">Daten importieren</h1>
          <p className="text-muted-foreground">
            Laden Sie eine Excel-Datei hoch, um die Daten zu importieren
          </p>
        </div>

        {!excelData ? (
          <Card>
            <CardHeader>
              <CardTitle>Excel-Datei auswählen</CardTitle>
              <CardDescription>
                Wählen Sie eine Excel-Datei aus, die die zu importierenden Daten enthält
              </CardDescription>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="flex items-center justify-center w-full">
                <label
                  htmlFor="file-upload"
                  className="flex flex-col items-center justify-center w-full h-64 border-2 border-dashed rounded-lg cursor-pointer bg-gray-50 hover:bg-gray-100"
                >
                  <div className="flex flex-col items-center justify-center pt-5 pb-6">
                    <FileSpreadsheet className="w-12 h-12 mb-4 text-gray-500" />
                    <p className="mb-2 text-sm text-gray-500">
                      <span className="font-semibold">Klicken Sie zum Auswählen</span> oder ziehen Sie die Datei hierher
                    </p>
                    <p className="text-xs text-gray-500">XLS oder XLSX</p>
                  </div>
                  <input
                    id="file-upload"
                    type="file"
                    accept=".xls,.xlsx"
                    onChange={handleFileSelect}
                    className="hidden"
                  />
                </label>
              </div>
              {selectedFile && (
                <div className="flex justify-center">
                  <Button
                    onClick={handleFileUpload}
                    disabled={isLoading}
                    className="w-full sm:w-auto"
                  >
                    {isLoading ? (
                      <div className="flex items-center gap-2">
                        <div className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin" />
                        Wird verarbeitet...
                      </div>
                    ) : (
                      <div className="flex items-center gap-2">
                        <Upload className="w-4 h-4" />
                        Datei hochladen
                      </div>
                    )}
                  </Button>
                </div>
              )}
            </CardContent>
          </Card>
        ) : (
          <DataPreview
            data={excelData}
            onConfirm={handleConfirm}
            onCancel={handleCancel}
          />
        )}
      </div>
    </div>
  )
} 