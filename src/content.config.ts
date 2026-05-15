import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

export const collections = {
	work: defineCollection({
		loader: glob({ base: './case-studies', pattern: '**/*.md' }),
		schema: z.object({
			title: z.string(),
			subtitle: z.string(),
			hero_image: z.string().optional(),
			client: z.string(),
			year: z.string(),
			duration: z.string(),
			tools: z.array(z.string()),
		}),
	}),
};
