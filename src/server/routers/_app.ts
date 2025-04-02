import { router } from '../trpc';
import { excelRouter } from './excel';

export const appRouter = router({
  excel: excelRouter,
});

export type AppRouter = typeof appRouter; 