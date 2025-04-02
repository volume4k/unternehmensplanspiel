import { NextResponse } from "next/server"
import * as XLSX from "xlsx"

export async function POST(request: Request) {
  try {
    const formData = await request.formData()
    const file = formData.get("file") as File

    if (!file) {
      return NextResponse.json(
        { error: "Keine Datei hochgeladen" },
        { status: 400 }
      )
    }

    const buffer = await file.arrayBuffer()
    const workbook = XLSX.read(buffer, { type: "array" })

    const data: { [key: string]: any[] } = {}

    // Verarbeite jedes Sheet
    workbook.SheetNames.forEach((sheetName) => {
      const worksheet = workbook.Sheets[sheetName]
      const jsonData = XLSX.utils.sheet_to_json(worksheet, { header: 1 })

      // Überspringe leere Zeilen und Header
      const rows = jsonData.filter((row: any[]) => row.length > 0)
      if (rows.length <= 1) return

      // Extrahiere Header und Daten
      const headers = rows[0] as string[]
      const sheetData = rows.slice(1).map((row: any[]) => {
        const obj: { [key: string]: any } = {}
        headers.forEach((header, index) => {
          obj[header] = row[index]
        })
        return obj
      })

      // Normalisiere den Sheet-Namen
      const normalizedName = sheetName.toLowerCase().replace(/\s+/g, "-")
      data[normalizedName] = sheetData
    })

    return NextResponse.json(data)
  } catch (error) {
    console.error("Fehler beim Parsen der Excel-Datei:", error)
    return NextResponse.json(
      { error: "Fehler beim Parsen der Excel-Datei" },
      { status: 500 }
    )
  }
} 