import { NextResponse } from "next/server"
import { prisma } from "@/lib/prisma"

export async function POST(request: Request) {
  try {
    const data = await request.json()

    // Erstelle einen neuen BusinessPeriod-Eintrag
    const businessPeriod = await prisma.businessPeriod.create({
      data: {
        // Executive Summary
        executiveSummary: {
          create: {
            stockPrice: data["executive-summary"][0]?.stockPrice || 0,
            totalRevenue: data["executive-summary"][0]?.totalRevenue || 0,
            // Weitere Felder...
          },
        },
        // Market Research
        marketResearch: {
          create: {
            competitors: data["market-research"] || [],
            // Weitere Felder...
          },
        },
        // Production
        production: {
          create: {
            metrics: data["production"] || [],
            // Weitere Felder...
          },
        },
        // Weitere Bereiche...
      },
    })

    return NextResponse.json(businessPeriod)
  } catch (error) {
    console.error("Fehler beim Importieren der Daten:", error)
    return NextResponse.json(
      { error: "Fehler beim Importieren der Daten" },
      { status: 500 }
    )
  }
} 