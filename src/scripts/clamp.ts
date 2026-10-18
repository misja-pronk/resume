// On phones, long lists show only their first few items until "show all" is pressed.
// The list's section carries `data-clamp`; items past the cut-off carry `.clamp-extra`.

function label(section: HTMLElement) {
  const btn = section.querySelector<HTMLButtonElement>('.clamp-toggle');
  if (!btn) return;
  const clamped = section.classList.contains('is-clamped');
  btn.textContent = clamped ? btn.dataset.more! : btn.dataset.less!;
  btn.setAttribute('aria-expanded', String(!clamped));
}

document.querySelectorAll<HTMLElement>('[data-clamp]').forEach((section) => {
  section.classList.add('is-clamped');
  label(section);
  section.querySelector('.clamp-toggle')?.addEventListener('click', () => {
    const clamping = section.classList.toggle('is-clamped');
    label(section);
    if (clamping) section.scrollIntoView({ block: 'start' });
  });
});

/** A filter other than "all" shows every match, so the clamp steps aside. */
export function setFiltered(section: HTMLElement | null, filtered: boolean) {
  if (!section) return;
  section.classList.toggle('is-filtered', filtered);
  section.classList.add('is-clamped');
  label(section);
}
