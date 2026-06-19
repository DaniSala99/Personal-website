import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const about = defineCollection({
	loader: glob({ pattern: 'about.md', base: './input' }),
	schema: z.object({
		name: z.string(),
		tagline: z.string(),
		avatar: z.string().optional(),
		location: z.string(),
		email: z.string(),
		linkedin: z.string().optional(),
		github: z.string().optional(),
		certifications: z.array(z.string()).optional(),
		languages: z.array(z.string()).optional(),
	}),
});

const workExperience = defineCollection({
	loader: glob({ pattern: '*.md', base: './input/work' }),
	schema: z.object({
		title: z.string(),
		company: z.string(),
		start: z.string(),
		end: z.string().nullable(),
		skills: z.array(z.string()).optional(),
	}),
});

const education = defineCollection({
	loader: glob({ pattern: '*.md', base: './input/education' }),
	schema: z.object({
		degree: z.string(),
		institution: z.string(),
		location: z.string().optional(),
		start: z.number(),
		end: z.number().nullable(),
		grade: z.string().nullable().optional(),
		description: z.string().optional(),
	}),
});

const projects = defineCollection({
	loader: glob({ pattern: '*.{md,mdx}', base: './input/projects' }),
	schema: z.object({
		title: z.string(),
		subtitle: z.string(),
		hero_image: z.string().optional(),
		client: z.string(),
		year: z.string(),
		duration: z.string(),
		tools: z.array(z.string()),
	}),
});

const portfolio = defineCollection({
	loader: glob({ pattern: '*.md', base: './input/portfolio' }),
	schema: z.object({
		title: z.string(),
		year: z.string(),
		type: z.string(),
		description: z.string(),
		tools: z.array(z.string()),
		repo: z.string().optional(),
		url: z.string().optional(),
	}),
});

export const collections = { about, workExperience, education, projects, portfolio };
