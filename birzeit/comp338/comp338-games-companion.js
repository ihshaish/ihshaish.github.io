'use strict';
/* ============================================================================
   COMP338 Games & Adversarial Search companion - interactive widgets.
   Vanilla JS, no dependencies. Sections: tree visualiser (minimax / alpha-beta /
   ordering / exercise), evaluation calculator, playable minimax tic-tac-toe,
   spoilers, and scroll-spy navigation.
============================================================================ */

/* ---------- tree specs ---------- */
const L = v => ({ leaf: v });
const N = (role, ch) => ({ role, ch });

// Canonical 3-level tree (root MAX, three MIN, three leaves each).
// Drawn left-to-right; minimax root = max(3,2,1) = 3. Under left-to-right
// alpha-beta it prunes 4 of the 9 leaves.
const TREE_AIMA = () => N('max', [
  N('min', [L(3), L(12), L(8)]),
  N('min', [L(2), L(4), L(6)]),
  N('min', [L(1), L(14), L(5)]),
]);

// Three reorderings of the SAME subtrees for the ordering demo.
const SUB_A = () => N('min', [L(3), L(12), L(8)]);  // value 3
const SUB_B = () => N('min', [L(2), L(4), L(6)]);   // value 2
const SUB_C = () => N('min', [L(1), L(14), L(5)]);  // value 1
const ORDERINGS = {
  best:  () => N('max', [SUB_A(), SUB_B(), SUB_C()]), // 5 leaves read, 4 pruned
  orig:  () => N('max', [SUB_B(), SUB_A(), SUB_C()]), // 7 read, 2 pruned
  worst: () => N('max', [SUB_C(), SUB_B(), SUB_A()]), // 9 read, 0 pruned
};

// Jarrar's exercise tree: A max / min / max / min / leaves.
const TREE_EX = () => N('max', [
  N('min', [                                  // B
    N('max', [ N('min',[L(10),L(11)]), N('min',[L(9),L(12)]) ]),   // C
    N('max', [ N('min',[L(14),L(15)]), N('min',[L(13),L(14)]) ]),  // J
  ]),
  N('min', [                                  // Q
    N('max', [ N('min',[L(15),L(2)]), N('min',[L(4),L(1)]) ]),     // R
    N('max', [ N('min',[L(3),L(22)]), N('min',[L(24),L(25)]) ]),   // Y
  ]),
]);

/* ---------- layout ---------- */
function buildLayout(spec) {
  const nodes = {}; let leafIdx = 0; let maxD = 0;
  (function rec(s, id, depth) {
    maxD = Math.max(maxD, depth);
    const isLeaf = s.leaf !== undefined;
    const o = { id, depth, role: isLeaf ? 'leaf' : s.role, isLeaf, children: [] };
    nodes[id] = o;
    if (isLeaf) { o.leafVal = s.leaf; o.x = leafIdx++; }
    else {
      s.ch.forEach((c, i) => { const cid = id + '.' + i; o.children.push(cid); rec(c, cid, depth + 1); });
      o.x = o.children.reduce((a, cid) => a + nodes[cid].x, 0) / o.children.length;
    }
  })(spec, 'r', 0);
  return { nodes, leafCount: leafIdx, maxDepth: maxD };
}

/* ---------- event generation ---------- */
function genMinimax(spec) {
  const ev = [];
  (function rec(s, id) {
    ev.push({ t: 'enter', id });
    if (s.leaf !== undefined) { ev.push({ t: 'leaf', id, v: s.leaf }); return s.leaf; }
    let best = s.role === 'max' ? -Infinity : Infinity;
    const cvals = [];
    for (let i = 0; i < s.ch.length; i++) {
      const v = rec(s.ch[i], id + '.' + i);
      cvals.push(v);
      best = s.role === 'max' ? Math.max(best, v) : Math.min(best, v);
      ev.push({ t: 'partial', id, v: best });
    }
    ev.push({ t: 'set', id, v: best, vals: cvals, role: s.role });
    return best;
  })(spec, 'r');
  return ev;
}

function genAlphaBeta(spec) {
  const ev = [];
  (function rec(s, id, alpha, beta) {
    ev.push({ t: 'enter', id, alpha, beta });
    if (s.leaf !== undefined) { ev.push({ t: 'leaf', id, v: s.leaf }); return s.leaf; }
    if (s.role === 'max') {
      let v = -Infinity;
      const cvals = [];
      for (let i = 0; i < s.ch.length; i++) {
        const cv = rec(s.ch[i], id + '.' + i, alpha, beta);
        cvals.push(cv);
        v = Math.max(v, cv);
        ev.push({ t: 'partial', id, v });
        if (v >= beta) {
          for (let j = i + 1; j < s.ch.length; j++) ev.push({ t: 'prune', id: id + '.' + j });
          ev.push({ t: 'cut', id, who: 'beta', v, beta });
          break;
        }
        alpha = Math.max(alpha, v);
        ev.push({ t: 'ab', id, alpha, beta });
      }
      ev.push({ t: 'set', id, v, vals: cvals, role: 'max' });
      return v;
    } else {
      let v = Infinity;
      const cvals = [];
      for (let i = 0; i < s.ch.length; i++) {
        const cv = rec(s.ch[i], id + '.' + i, alpha, beta);
        cvals.push(cv);
        v = Math.min(v, cv);
        ev.push({ t: 'partial', id, v });
        if (v <= alpha) {
          for (let j = i + 1; j < s.ch.length; j++) ev.push({ t: 'prune', id: id + '.' + j });
          ev.push({ t: 'cut', id, who: 'alpha', v, alpha });
          break;
        }
        beta = Math.min(beta, v);
        ev.push({ t: 'ab', id, alpha, beta });
      }
      ev.push({ t: 'set', id, v, vals: cvals, role: 'min' });
      return v;
    }
  })(spec, 'r', -Infinity, Infinity);
  return ev;
}

function principalVariation(spec) {
  // returns Set of edge keys "parent>child" on the minimax-optimal line
  const set = new Set();
  function val(s) {
    if (s.leaf !== undefined) return s.leaf;
    const vs = s.ch.map(val);
    return s.role === 'max' ? Math.max(...vs) : Math.min(...vs);
  }
  (function rec(s, id) {
    if (s.leaf !== undefined) return;
    const vs = s.ch.map(val);
    const target = s.role === 'max' ? Math.max(...vs) : Math.min(...vs);
    const i = vs.findIndex(v => v === target);
    set.add(id + '>' + id + '.' + i);
    rec(s.ch[i], id + '.' + i);
  })(spec, 'r');
  return set;
}

/* ---------- rendering ---------- */
const fmt = v => (v === Infinity ? '+∞' : v === -Infinity ? '−∞' : v);

function renderTree(spec, layout, state, mode) {
  const { nodes, leafCount, maxDepth } = layout;
  const gapX = 70, marginL = 100, marginT = 42, gapY = Math.max(86, mode === 'ex' ? 78 : 96);
  const W = marginL + (leafCount - 1) * gapX + 44;
  const H = marginT + maxDepth * gapY + 52;
  const px = x => marginL + x * gapX;
  const py = d => marginT + d * gapY;
  const tw = 15, th = 13; // triangle half-width / height
  let svg = `<svg viewBox="0 0 ${W} ${H}" width="${W}" preserveAspectRatio="xMidYMid meet">`;

  // row labels (alternate MAX/MIN by depth; leaves row labelled)
  const rootRole = spec.role || 'max';
  for (let d = 0; d <= maxDepth; d++) {
    let lab;
    if (d === maxDepth) lab = 'leaves';
    else lab = ((d % 2 === 0) === (rootRole === 'max')) ? 'MAX' : 'MIN';
    svg += `<text class="t-rowlab" x="6" y="${py(d) + 5}">${lab}</text>`;
  }

  // edges
  for (const id in nodes) {
    const n = nodes[id];
    for (const cid of n.children) {
      const c = nodes[cid];
      let cls = 't-edge';
      if (state.pruned.has(cid)) cls += ' pruned';
      else if (state.pv && state.pv.has(id + '>' + cid)) cls += ' on-pv';
      svg += `<line class="${cls}" x1="${px(n.x)}" y1="${py(n.depth) + th}" x2="${px(c.x)}" y2="${py(c.depth) - th}"/>`;
    }
  }

  // nodes
  for (const id in nodes) {
    const n = nodes[id];
    const cx = px(n.x), cy = py(n.depth);
    const prunedHere = isPruned(state.pruned, id);
    let cls = 't-node ' + (n.role === 'leaf' ? 'max' : n.role);
    if (prunedHere) cls += ' pruned';
    else if (state.current === id) cls += ' current';
    else if (state.values[id] !== undefined && !n.isLeaf) cls += ' settled';
    let pts;
    if (n.role === 'min') pts = `${cx - tw},${cy - th} ${cx + tw},${cy - th} ${cx},${cy + th}`;     // down
    else pts = `${cx - tw},${cy + th} ${cx + tw},${cy + th} ${cx},${cy - th}`;                        // up (max & leaf)
    svg += `<polygon class="${cls}" points="${pts}"/>`;

    if (n.isLeaf) {
      svg += `<text class="t-leaf-val" x="${cx}" y="${cy + th + 17}" text-anchor="middle">${prunedHere ? '' : (state.values[id] !== undefined ? n.leafVal : '')}</text>`;
    } else {
      const v = state.values[id];
      if (v !== undefined && !prunedHere) {
        const fresh = (state.current === id) ? ' fresh' : '';
        svg += `<text class="t-val${fresh}" x="${cx}" y="${cy - th - 9}" text-anchor="middle">${fmt(v)}</text>`;
      }
      // alpha/beta window shown below the node (alpha-beta mode only)
      if (mode !== 'mm' && state.ab[id] && !prunedHere) {
        const ab = state.ab[id];
        svg += `<text class="t-ab" x="${cx}" y="${cy + th + 16}" text-anchor="middle">[${fmt(ab.a)}, ${fmt(ab.b)}]</text>`;
      }
    }
    if (state.cut[id]) {
      svg += `<text class="t-cut" x="${cx + tw + 6}" y="${cy + 5}" text-anchor="start">✂ ${state.cut[id]}-cut</text>`;
    }
  }
  svg += `</svg>`;
  return svg;
}

function isPruned(prunedSet, id) {
  for (const p of prunedSet) if (id === p || id.startsWith(p + '.')) return true;
  return false;
}

/* ---------- narration ---------- */
function narrate(e, layout, mode) {
  const isLeaf = e.id && layout.nodes[e.id] && layout.nodes[e.id].isLeaf;
  const role = e.id && layout.nodes[e.id] ? layout.nodes[e.id].role : '';
  switch (e.t) {
    case 'enter':
      if (mode !== 'mm' && e.alpha !== undefined)
        return { what: `Enter node with window [${fmt(e.alpha)}, ${fmt(e.beta)}].`, why: role === 'max' ? 'A MAX node: it will raise &alpha; as it finds better children, and cut if a child reaches &beta;.' : role === 'min' ? 'A MIN node: it will lower &beta; as it finds smaller children, and cut if a child drops to &alpha;.' : 'Descending the leftmost unexplored branch (depth-first).' };
      return { what: 'Descend to the next node.', why: 'Minimax explores depth-first, left to right, all the way to a leaf before backing up.' };
    case 'leaf':
      return { what: `Leaf evaluated: utility = <strong>${e.v}</strong>.`, why: 'A terminal position. Its utility is read directly (here it is given).' };
    case 'partial':
      return { what: `Running value at this ${role.toUpperCase()} node: <strong>${fmt(e.v)}</strong>.`, why: role === 'max' ? 'MAX keeps the largest child seen so far.' : 'MIN keeps the smallest child seen so far.' };
    case 'ab':
      return { what: `Window tightened to [${fmt(e.alpha)}, ${fmt(e.beta)}].`, why: 'These bounds travel down to the children: anything outside the window cannot affect the result.' };
    case 'prune':
      return { what: `Branch pruned (skipped entirely).`, why: 'These leaves are never evaluated; they cannot change the value backed up to the parent.' };
    case 'cut':
      return e.who === 'beta'
        ? { what: `<strong>&beta;-cut.</strong> Value ${fmt(e.v)} &ge; &beta; (${fmt(e.beta)}).`, why: 'This MAX node is already too good: the MIN parent above has a reply at least as good for itself, so it will never allow MAX to come here. Stop.' }
        : { what: `<strong>&alpha;-cut.</strong> Value ${fmt(e.v)} &le; &alpha; (${fmt(e.alpha)}).`, why: 'This MIN node is already too low: the MAX parent above has a move at least this good, so it will never come here. Stop.' };
    case 'set':
      if (e.id === 'r') return { what: `<strong>Root value = ${fmt(e.v)}.</strong> Done.`, why: 'This is the minimax value: the best MAX can guarantee against optimal play. The red line is the principal variation.' };
      { const r = e.role || role, op = r === 'max' ? 'max' : 'min', list = (e.vals || []).map(fmt).join(', ');
        return { what: `${r.toUpperCase()} node keeps the ${r === 'max' ? 'largest' : 'smallest'} child: <strong>${op}(${list}) = ${fmt(e.v)}</strong>.`, why: `That value is backed up to the parent. ${r === 'max' ? 'MAX' : 'MIN'} compared its ${(e.vals || []).length} explored ${(e.vals || []).length === 1 ? 'child' : 'children'} and took the ${r === 'max' ? 'maximum' : 'minimum'}.` }; }
  }
  return { what: '', why: '' };
}

/* ---------- tree widget controller ---------- */
function makeTreeWidget(key, getSpec, mode0) {
  const host = document.querySelector(`[data-tree="${key}"]`);
  const fb = document.querySelector(`[data-tree-fb="${key}"]`);
  if (!host) return null;
  const w = { key, mode: mode0, idx: 0, timer: null };

  function rebuild() {
    w.spec = getSpec(w);
    w.layout = buildLayout(w.spec);
    w.events = w.mode === 'mm' ? genMinimax(w.spec) : genAlphaBeta(w.spec);
    w.pv = principalVariation(w.spec);
    w.idx = 0;
    draw();
  }
  function curState() {
    const st = { values: {}, current: null, ab: {}, pruned: new Set(), cut: {}, pv: null };
    let rootSet = false;
    for (let i = 0; i < w.idx; i++) {
      const e = w.events[i];
      if (e.t === 'enter') { st.current = e.id; if (e.alpha !== undefined) st.ab[e.id] = { a: e.alpha, b: e.beta }; }
      else if (e.t === 'leaf') { st.values[e.id] = e.v; st.current = e.id; }
      else if (e.t === 'partial') { st.values[e.id] = e.v; st.current = e.id; }
      else if (e.t === 'ab') { st.ab[e.id] = { a: e.alpha, b: e.beta }; }
      else if (e.t === 'prune') { st.pruned.add(e.id); }
      else if (e.t === 'cut') { st.cut[e.id] = e.who; st.current = e.id; }
      else if (e.t === 'set') { st.values[e.id] = e.v; st.current = e.id; if (e.id === 'r') rootSet = true; }
    }
    if (rootSet) st.pv = w.pv;
    return st;
  }
  function draw() {
    const st = curState();
    host.innerHTML = renderTree(w.spec, w.layout, st, w.mode);
    // feedback
    if (fb) {
      if (w.idx === 0) fb.innerHTML = `<div class="what-happened">Ready.</div><div class="why">Press <strong>Step</strong> to back values up one node at a time, or <strong>Play all</strong> to watch it run.</div>`;
      else { const n = narrate(w.events[w.idx - 1], w.layout, w.mode); fb.innerHTML = `<div class="what-happened">${n.what}</div><div class="why">${n.why}</div>`; }
    }
    updateStats();
  }
  function updateStats() {
    const seen = w.events.slice(0, w.idx).filter(e => e.t === 'leaf').length;
    const pruned = w.events.slice(0, w.idx).filter(e => e.t === 'prune').length;
    const rootEv = w.events.slice(0, w.idx).reverse().find(e => e.t === 'set' && e.id === 'r');
    setStat(`${key}-seen`, seen);
    setStat(`${key}-total`, w.layout.leafCount);
    setStat(`${key}-pruned`, pruned);
    setStat(`${key}-root`, rootEv ? fmt(rootEv.v) : '–');
  }
  function setStat(name, val) { document.querySelectorAll(`[data-tree-stat="${name}"]`).forEach(el => el.textContent = val); }
  function stop() { if (w.timer) { clearInterval(w.timer); w.timer = null; } }

  w.rebuild = rebuild;
  w.step = () => { stop(); if (w.idx < w.events.length) { w.idx++; draw(); } };
  w.reset = () => { stop(); w.idx = 0; draw(); };
  w.play = () => { stop(); w.timer = setInterval(() => { if (w.idx < w.events.length) { w.idx++; draw(); } else stop(); }, 650); };
  rebuild();
  return w;
}

/* ---------- wire tree widgets ---------- */
const TREE_WIDGETS = {};
document.addEventListener('DOMContentLoaded', () => {
  TREE_WIDGETS.mm = makeTreeWidget('mm', () => TREE_AIMA(), 'mm');
  TREE_WIDGETS.ab = makeTreeWidget('ab', () => TREE_AIMA(), 'ab');
  TREE_WIDGETS.ord = makeTreeWidget('ord', (w) => ORDERINGS[(document.querySelector('[data-ord-select]') || {}).value || 'best'](), 'ab');
  TREE_WIDGETS.ex = makeTreeWidget('ex', (w) => TREE_EX(), (document.querySelector('[data-ex-mode]') || {}).value || 'mm');

  document.querySelectorAll('[data-tree-ctl]').forEach(btn => {
    btn.addEventListener('click', () => {
      const w = TREE_WIDGETS[btn.dataset.treeCtl]; if (!w) return;
      const a = btn.dataset.action;
      if (a === 'step') w.step(); else if (a === 'reset') w.reset(); else if (a === 'play') w.play();
    });
  });
  const ordSel = document.querySelector('[data-ord-select]');
  if (ordSel) ordSel.addEventListener('change', () => TREE_WIDGETS.ord.rebuild());
  const exSel = document.querySelector('[data-ex-mode]');
  if (exSel) exSel.addEventListener('change', () => { TREE_WIDGETS.ex.mode = exSel.value; TREE_WIDGETS.ex.rebuild(); });

  initEvalCalc();
  initPlay();
  initSpoilers();
  initScrollSpy();
});

/* ============================================================================
   Evaluation-function calculator (tic-tac-toe open-lines heuristic)
============================================================================ */
const TTT_LINES = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
function initEvalCalc() {
  const board = document.querySelector('[data-eval-board]');
  if (!board) return;
  const cells = []; const state = Array(9).fill('');
  for (let i = 0; i < 9; i++) {
    const b = document.createElement('button');
    b.className = 'ttt-cell'; b.type = 'button';
    b.addEventListener('click', () => { state[i] = state[i] === '' ? 'X' : state[i] === 'X' ? 'O' : ''; render(); });
    board.appendChild(b); cells.push(b);
  }
  const clearBtn = document.querySelector('[data-eval-clear]');
  if (clearBtn) clearBtn.addEventListener('click', () => { state.fill(''); render(); });
  function openFor(p, opp) { return TTT_LINES.filter(ln => !ln.some(i => state[i] === opp)).length; }
  function render() {
    cells.forEach((c, i) => { c.textContent = state[i]; c.className = 'ttt-cell' + (state[i] === 'X' ? ' x' : state[i] === 'O' ? ' o' : ''); });
    const ox = openFor('X', 'O'), oo = openFor('O', 'X'), e = ox - oo;
    set('[data-eval="x"]', ox); set('[data-eval="o"]', oo); set('[data-eval="total"]', (e > 0 ? '+' : '') + e);
    const msg = document.querySelector('[data-eval="msg"]');
    if (msg) {
      let txt;
      if (state.every(s => s === '')) txt = 'Empty board: X and O both have all 8 lines open, so E = 0. A fair start.';
      else if (e > 0) txt = `E = +${e}: this position favours <strong>X</strong> (MAX). X threatens more lines than O.`;
      else if (e < 0) txt = `E = ${e}: this position favours <strong>O</strong> (MIN). O threatens more lines than X.`;
      else txt = 'E = 0: the two players threaten equally many lines. Even.';
      msg.innerHTML = `<div class="what-happened">${txt}</div><div class="why">A line counts as open for a player only if the opponent has no mark on it. Minimax would back up exactly this number from the position at depth 0.</div>`;
    }
  }
  function set(sel, v) { const el = document.querySelector(sel); if (el) el.textContent = v; }
  render();
}

/* ============================================================================
   Playable tic-tac-toe vs. full minimax (O is optimal; you are X, you move first)
============================================================================ */
function tttWinner(b) {
  for (const [a, c, d] of TTT_LINES) if (b[a] && b[a] === b[c] && b[a] === b[d]) return b[a];
  return b.every(x => x) ? 'draw' : null;
}
function tttMinimax(b, depth, oToMove) {
  const w = tttWinner(b);
  if (w === 'O') return 10 - depth;
  if (w === 'X') return depth - 10;
  if (w === 'draw') return 0;
  if (oToMove) {
    let best = -Infinity;
    for (let i = 0; i < 9; i++) if (!b[i]) { b[i] = 'O'; best = Math.max(best, tttMinimax(b, depth + 1, false)); b[i] = ''; }
    return best;
  } else {
    let best = Infinity;
    for (let i = 0; i < 9; i++) if (!b[i]) { b[i] = 'X'; best = Math.min(best, tttMinimax(b, depth + 1, true)); b[i] = ''; }
    return best;
  }
}
function bestO(b) {
  let best = -Infinity, move = -1, scores = {};
  for (let i = 0; i < 9; i++) if (!b[i]) { b[i] = 'O'; const v = tttMinimax(b, 1, false); b[i] = ''; scores[i] = v; if (v > best) { best = v; move = i; } }
  return { move, scores, best };
}
function initPlay() {
  const board = document.querySelector('[data-play-board]');
  if (!board) return;
  const statusEl = document.querySelector('[data-play-status]');
  const showChk = document.querySelector('[data-play-show]');
  const newBtn = document.querySelector('[data-play-ctl="new"]');
  let b = Array(9).fill(''), over = false, lastScores = null;
  const cells = [];
  for (let i = 0; i < 9; i++) {
    const c = document.createElement('button'); c.className = 'ttt-cell'; c.type = 'button';
    c.addEventListener('click', () => humanMove(i));
    board.appendChild(c); cells.push(c);
  }
  function setStatus(txt, cls) { if (statusEl) { statusEl.textContent = txt; statusEl.className = 'ttt-status' + (cls ? ' ' + cls : ''); } }
  function render() {
    const win = tttWinner(b);
    const winLine = (win === 'X' || win === 'O') ? TTT_LINES.find(([a, c, d]) => b[a] === win && b[c] === win && b[d] === win) : null;
    cells.forEach((c, i) => {
      c.textContent = b[i];
      c.className = 'ttt-cell' + (b[i] === 'X' ? ' x' : b[i] === 'O' ? ' o' : '') + (winLine && winLine.includes(i) ? ' win' : '');
      c.disabled = over || !!b[i];
      if (showChk && showChk.checked && !over && !b[i] && lastScores && lastScores[i] !== undefined) {
        c.textContent = (lastScores[i] > 0 ? '+' : '') + lastScores[i];
        c.style.fontSize = '15px'; c.style.color = 'var(--grey)';
      } else { c.style.fontSize = ''; c.style.color = ''; }
    });
  }
  function humanMove(i) {
    if (over || b[i]) return;
    b[i] = 'X'; lastScores = null;
    let w = tttWinner(b);
    if (w) return finish(w);
    // O replies with minimax
    const res = bestO(b);
    lastScores = res.scores;
    b[res.move] = 'O';
    w = tttWinner(b);
    if (w) return finish(w);
    setStatus('Your move (X).');
    render();
  }
  function finish(w) {
    over = true;
    if (w === 'X') setStatus('You win?! That should be impossible; report a bug.', 'win');
    else if (w === 'O') setStatus('O wins. Minimax punished a slip.', 'lose');
    else setStatus('Draw: the best you can force against optimal play.', 'draw');
    render();
  }
  function reset() { b = Array(9).fill(''); over = false; lastScores = null; setStatus('You are X. Click any square to move.'); render(); }
  if (newBtn) newBtn.addEventListener('click', reset);
  if (showChk) showChk.addEventListener('change', render);
  reset();
}

/* ============================================================================
   Spoilers + scroll-spy nav
============================================================================ */
function initSpoilers() {
  document.querySelectorAll('[data-spoiler]').forEach(el => {
    el.addEventListener('click', () => el.classList.add('shown'));
  });
}
function initScrollSpy() {
  const links = Array.from(document.querySelectorAll('.topnav .nav-link'));
  const map = {};
  links.forEach(a => { const id = a.getAttribute('href').slice(1); const s = document.getElementById(id); if (s) map[id] = a; });
  const sections = Object.keys(map).map(id => document.getElementById(id));
  function onScroll() {
    let active = sections[0];
    const y = window.scrollY + 120;
    for (const s of sections) if (s.offsetTop <= y) active = s;
    links.forEach(a => a.classList.remove('active'));
    if (active && map[active.id]) map[active.id].classList.add('active');
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}
