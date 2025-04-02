import { initTRPC, TRPCError } from '@trpc/server';
import { NextRequest } from 'next/server';

const t = initTRPC.create();

export const router = t.router;
export const publicProcedure = t.procedure;

export interface Context {
  req: NextRequest;
}

export const createContext = async (opts: { req: NextRequest }) => {
  return {
    req: opts.req,
  };
};

export const handleError = (error: unknown) => {
  if (error instanceof TRPCError) {
    return error;
  }
  return new TRPCError({
    code: 'INTERNAL_SERVER_ERROR',
    message: 'Ein unerwarteter Fehler ist aufgetreten',
  });
}; 