"use client";

import Link from "next/link";
import { FileSpreadsheet } from "lucide-react";

export function Navbar() {
  return (
    <nav className="bg-white border-b border-gray-200">
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          <div className="flex items-center">
            <Link href="/" className="flex items-center space-x-2">
              <FileSpreadsheet className="w-8 h-8 text-blue-500" />
              <span className="text-xl font-semibold text-gray-900">Unternehmensplanspiel</span>
            </Link>
          </div>
          <div className="flex items-center space-x-4">
            <Link
              href="/"
              className="text-gray-600 hover:text-gray-900 px-3 py-2 rounded-md text-sm font-medium"
            >
              Home
            </Link>
            <Link
              href="/about"
              className="text-gray-600 hover:text-gray-900 px-3 py-2 rounded-md text-sm font-medium"
            >
              Über uns
            </Link>
          </div>
        </div>
      </div>
    </nav>
  );
} 