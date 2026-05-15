// @ts-check
import { defineConfig } from 'astro/config';

function rehypeImgToFigure() {
	return (tree) => {
		function walk(node) {
			if (!node.children) return;
			for (let i = 0; i < node.children.length; i++) {
				const child = node.children[i];
				if (child.type === 'element' && child.tagName === 'img') {
					const alt = (child.properties && child.properties.alt) || '';
					node.children[i] = {
						type: 'element',
						tagName: 'figure',
						properties: { className: ['img-placeholder'] },
						children: alt
							? [
									{
										type: 'element',
										tagName: 'figcaption',
										properties: {},
										children: [{ type: 'text', value: alt }],
									},
								]
							: [],
					};
				} else {
					walk(child);
				}
			}
		}
		walk(tree);
	};
}

export default defineConfig({
	markdown: {
		rehypePlugins: [rehypeImgToFigure],
	},
});
