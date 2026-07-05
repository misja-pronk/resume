import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import type { APIContext } from 'astro';

export async function GET(context: APIContext) {
  const posts = (await getCollection('posts', ({ data }) => !data.draft)).sort(
    (a, b) => b.data.date.valueOf() - a.data.date.valueOf(),
  );

  return rss({
    title: 'Misja Pronk — Field Notes',
    description:
      'Engineering memos from the field: Databricks, platform engineering, dbt and data platforms in practice.',
    site: new URL('/resume/', context.site ?? 'https://misja-pronk.github.io'),
    items: posts.map((post) => ({
      title: post.data.title,
      description: post.data.summary,
      pubDate: post.data.date,
      link: `/resume/blog/${post.id}/`,
    })),
    customData: '<language>en</language>',
  });
}
