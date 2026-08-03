import json

with open('assets/projects_data.json', 'r', encoding='utf-8') as f:
    projects = json.load(f)

json_str = json.dumps(projects, ensure_ascii=False, indent=4)

header = """/* ==========================================================================
   교통국 중점 추진사업 총괄보고 대시보드 - JavaScript Logic
   ========================================================================== */

// Embedded full dataset to ensure 100% offline & file:// protocol compatibility
const EMBEDDED_PROJECTS_DATA = """

body = """;

let projectsData = [];
let activeDept = 'all';
let activeTag = 'all';
let currentSearch = '';
let currentSelectedProject = null;
const RAW_PDF_FILENAME = "(8.3.) 중점사업 추진사업 점검 보고회 자료(교통국 수정)_최최종.pdf";

// Initialize Dashboard when DOM is ready
document.addEventListener('DOMContentLoaded', async () => {
    initTheme();
    await loadProjectsData();
    initEventListeners();
    initLightboxInteractions();
});

// Load Dataset
async function loadProjectsData() {
    try {
        const response = await fetch('assets/projects_data.json');
        if (!response.ok) throw new Error('Failed to load JSON data');
        const data = await response.json();
        if (data && data.length > 0) {
            projectsData = data;
        } else {
            projectsData = EMBEDDED_PROJECTS_DATA;
        }
    } catch (err) {
        console.warn('Fetch fallback to embedded 13 projects dataset:', err);
        projectsData = EMBEDDED_PROJECTS_DATA;
    }

    renderKPI();
    renderDeptBar();
    renderProjects();
}

// Render KPI Summary Section
function renderKPI() {
    const totalCount = projectsData.length;
    const checkCount = projectsData.filter(p => p.tags.includes('지속추진') || p.tags.includes('점검사업')).length;
    const suppCount = projectsData.filter(p => p.tags.includes('2회추경')).length;

    let totalBudget = 0;
    projectsData.forEach(p => {
        if (p.budgetNum) {
            totalBudget += p.budgetNum;
        }
    });

    document.getElementById('kpi-total-count').textContent = totalCount;
    document.getElementById('kpi-check-count').textContent = checkCount;
    document.getElementById('kpi-supp-count').textContent = suppCount;
    document.getElementById('kpi-budget-total').textContent = Math.round(totalBudget).toLocaleString();

    // Update pill counts
    document.getElementById('count-all').textContent = totalCount;
    document.getElementById('count-policy').textContent = projectsData.filter(p => p.dept === '교통정책과').length;
    document.getElementById('count-transit').textContent = projectsData.filter(p => p.dept === '대중교통과').length;
    document.getElementById('count-parking').textContent = projectsData.filter(p => p.dept === '주차관리과').length;
    document.getElementById('count-road').textContent = projectsData.filter(p => p.dept === '도로건설과').length;
}

// Render Department Analytics Bar
function renderDeptBar() {
    const container = document.getElementById('dept-bar-container');
    if (!container) return;

    const depts = [
        { name: '교통정책과', key: 'dept-policy', color: '#2563eb' },
        { name: '대중교통과', key: 'dept-transit', color: '#059669' },
        { name: '주차관리과', key: 'dept-parking', color: '#7c3aed' },
        { name: '도로건설과', key: 'dept-road', color: '#d97706' }
    ];

    const total = projectsData.length;
    let barHTML = `<div class="dept-bar-group">`;
    let legendHTML = `<div class="dept-legend-row">`;

    depts.forEach(d => {
        const count = projectsData.filter(p => p.dept === d.name).length;
        const pct = ((count / total) * 100).toFixed(1);
        if (count > 0) {
            barHTML += `
                <div class="dept-segment ${d.key}" style="width: ${pct}%;" 
                     title="${d.name}: ${count}건 (${pct}%)"
                     onclick="filterByDept('${d.name}')">
                    ${d.name} ${count}건
                </div>
            `;
        }
        legendHTML += `
            <div class="legend-item">
                <span class="legend-dot" style="background-color: ${d.color};"></span>
                <span>${d.name} (${count}건)</span>
            </div>
        `;
    });

    barHTML += `</div>`;
    legendHTML += `</div>`;
    container.innerHTML = barHTML + legendHTML;
}

// Render Project Cards Grid
function renderProjects() {
    const container = document.getElementById('project-cards-container');
    const emptyState = document.getElementById('empty-state');

    // Filter Logic
    const filtered = projectsData.filter(p => {
        if (activeDept !== 'all' && p.dept !== activeDept) return false;

        if (activeTag !== 'all') {
            if (!p.tags.includes(activeTag)) return false;
        }

        if (currentSearch.trim() !== '') {
            const query = currentSearch.toLowerCase();
            const matchTitle = p.title.toLowerCase().includes(query);
            const matchLocation = (p.location || '').toLowerCase().includes(query);
            const matchDept = p.dept.toLowerCase().includes(query);
            const matchPurpose = (p.purpose || '').toLowerCase().includes(query);
            if (!matchTitle && !matchLocation && !matchDept && !matchPurpose) return false;
        }

        return true;
    });

    if (filtered.length === 0) {
        container.innerHTML = '';
        emptyState.style.display = 'flex';
        return;
    }

    emptyState.style.display = 'none';

    container.innerHTML = filtered.map(p => {
        const tagsHTML = p.tags.map(t => `<span class="tag-badge badge-${t}">${t}</span>`).join('');
        const pdfLabel = p.pdfPageLabel || `P.${p.pdfPage || 1}`;
        const pdfUrl = `${RAW_PDF_FILENAME}#page=${p.pdfPage || 1}`;

        return `
            <article class="project-card">
                <div class="card-header-bar">
                    <div class="card-no-group">
                        <span class="card-no-badge">${p.no}</span>
                        <span class="card-pdf-pill" title="원본 PDF ${pdfLabel} 확대보기" onclick="event.stopPropagation(); openPdfPagesForProject('${p.id}')">
                            📄 PDF ${pdfLabel}
                        </span>
                    </div>
                    <div class="card-tags">${tagsHTML}</div>
                </div>

                <div class="card-body">
                    <!-- Project Title Clickable -> Triggers Detail Modal -->
                    <a class="card-title-link" onclick="openDetailModal('${p.id}')" title="사업 상세 정보 보기">
                        <span>${p.title}</span>
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
                    </a>

                    <div class="card-meta-list">
                        <div class="meta-row">
                            <span class="meta-label">담당부서</span>
                            <span class="meta-val">${p.dept} (☎${p.phone})</span>
                        </div>
                        <div class="meta-row">
                            <span class="meta-label">사업위치</span>
                            <span class="meta-val">${p.location}</span>
                        </div>
                        <div class="meta-row">
                            <span class="meta-label">총사업비</span>
                            <span class="meta-val highlight-budget">${p.budgetTotal}</span>
                        </div>
                        <div class="meta-row">
                            <span class="meta-label">사업규모</span>
                            <span class="meta-val">${p.scope}</span>
                        </div>
                    </div>

                    <!-- Reference Photo Thumbnail Clickable -> Triggers Image Lightbox -->
                    <div class="card-image-box" onclick="openLightbox('${p.image}', '${escapeHtml(p.title)} - 참고사진')" title="클릭하면 큰 사진으로 확대합니다">
                        <img src="${p.image}" alt="${p.imageCaption || p.title}" loading="lazy">
                        <div class="card-image-overlay">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/><line x1="11" y1="8" x2="11" y2="14"/><line x1="8" y1="11" x2="14" y2="11"/></svg>
                            <span>참고사진 확대보기</span>
                        </div>
                    </div>
                </div>

                <div class="card-footer">
                    <button class="btn btn-outline" onclick="openDetailModal('${p.id}')">
                        상세 현황 보기
                    </button>
                    <button type="button" class="btn btn-pdf" onclick="event.stopPropagation(); openPdfPagesForProject('${p.id}')" title="원본 PDF ${pdfLabel} 바로 확대보기">
                        📄 원본 PDF
                    </button>
                </div>
            </article>
        `;
    }).join('');
}

// View Mode State
let currentView = 'card';

// Switch between Card and Table view
function switchView(mode) {
    currentView = mode;
    const cardContainer = document.getElementById('project-cards-container');
    const tableContainer = document.getElementById('project-table-container');
    const cardBtn = document.getElementById('view-card-btn');
    const tableBtn = document.getElementById('view-table-btn');

    if (mode === 'card') {
        cardContainer.style.display = '';
        tableContainer.style.display = 'none';
        cardBtn.classList.add('active');
        tableBtn.classList.remove('active');
    } else {
        cardContainer.style.display = 'none';
        tableContainer.style.display = '';
        cardBtn.classList.remove('active');
        tableBtn.classList.add('active');

        const filtered = projectsData.filter(p => {
            if (activeDept !== 'all' && p.dept !== activeDept) return false;
            if (activeTag !== 'all' && !p.tags.includes(activeTag)) return false;
            if (currentSearch.trim() !== '') {
                const query = currentSearch.toLowerCase();
                if (!p.title.toLowerCase().includes(query) &&
                    !(p.location || '').toLowerCase().includes(query) &&
                    !p.dept.toLowerCase().includes(query) &&
                    !(p.purpose || '').toLowerCase().includes(query)) return false;
            }
            return true;
        });
        renderTableView(filtered);
    }
}

// Render Table View — 보고서 형식 (사업유형 / 주요내용 / 참고사진)
function renderTableView(filtered) {
    const tableContainer = document.getElementById('project-table-container');
    if (!tableContainer) return;

    if (!filtered || filtered.length === 0) {
        tableContainer.innerHTML = '<p style="text-align:center;padding:2rem;color:var(--text-muted);">조건에 맞는 사업이 없습니다.</p>';
        return;
    }

    const ALL_TAG_TYPES = ['지속추진', '점검사업', '2회추경'];

    // Filter to only projects that have at least one of the defined type tags
    const typeFiltered = filtered.filter(p => {
        return p.tags.some(tag => ['지속추진', '점검사업', '2회추경'].includes(tag));
    });
    const rows = typeFiltered.map(p => {
        // 사업유형 열: 각 유형별 체크박스 표시
        const typeChecks = ALL_TAG_TYPES
            .filter(t => p.tags.includes(t))
            .map(t => {
                const color = t === '지속추진' ? '#2563eb' : t === '점검사업' ? '#059669' : '#d97706';
                return `<div style="display:flex;align-items:center;gap:0.35rem;margin-bottom:0.3rem;font-size:0.8rem;color:${color};font-weight:700;">
                    <span style="display:inline-flex;align-items:center;justify-content:center;width:15px;height:15px;border:1.5px solid ${color};border-radius:3px;background:${color};color:#fff;font-size:0.6rem;">✓</span>
                    ${t}
                </div>`;
            }).join('');

        // 주요내용: 사업명, 총사업비, 사업내용(scope), 추진실적(achievements) 일부
        const achHTML = (() => {
            if (!p.achievements || p.achievements.length === 0) return '';
            const items = p.achievements.slice(0, 3).map(item => {
                const text = typeof item === 'object' ? (item.text || '') : item;
                return `<div style="display:flex;gap:0.4rem;align-items:flex-start;margin-top:0.25rem;">
                    <span style="color:var(--primary-color);font-weight:700;flex-shrink:0;margin-top:1px;">○</span>
                    <span style="color:var(--text-main);font-size:0.82rem;line-height:1.5;">${text}</span>
                </div>`;
            }).join('');
            return `<div style="margin-top:0.5rem;padding-top:0.4rem;border-top:1px dashed var(--border-color);">
                <div style="font-size:0.75rem;font-weight:700;color:var(--text-muted);margin-bottom:0.2rem;">▣ 추진실적</div>
                ${items}
            </div>`;
        })();

        const scheduleHTML = (() => {
            if (!p.schedule || p.schedule.length === 0) return '';
            const items = p.schedule.slice(0, 2).map(s =>
                `<div style="display:flex;gap:0.4rem;align-items:flex-start;margin-top:0.2rem;">
                    <span style="color:#d97706;font-weight:700;flex-shrink:0;">○</span>
                    <span style="color:var(--text-muted);font-size:0.8rem;line-height:1.5;">${s}</span>
                </div>`
            ).join('');
            return `<div style="margin-top:0.4rem;">
                <div style="font-size:0.75rem;font-weight:700;color:var(--text-muted);margin-bottom:0.2rem;">▣ 향후계획</div>
                ${items}
            </div>`;
        })();

        return `<tr onclick="openDetailModal('${p.id}')" style="cursor:pointer;border-bottom:1px solid var(--border-color);transition:background 0.15s;"
                    onmouseover="this.style.background='rgba(99,102,241,0.07)'"
                    onmouseout="this.style.background=''">
            <td style="padding:1rem 1rem;vertical-align:top;width:130px;min-width:130px;border-right:1px solid var(--border-color);">
                ${typeChecks}
            </td>
            <td style="padding:1rem 1.4rem;vertical-align:top;">
                <div style="display:flex;align-items:center;gap:0.6rem;margin-bottom:0.5rem;">
                    <span style="background:var(--primary-color);color:#fff;font-size:0.75rem;font-weight:700;padding:0.15rem 0.55rem;border-radius:999px;white-space:nowrap;">${p.no}</span>
                    <span style="font-size:1.05rem;font-weight:800;color:var(--text-main);">사 업 명 : ${p.title}</span>
                </div>
                <div style="font-size:0.9rem;color:var(--text-muted);margin-bottom:0.25rem;">
                    <span style="font-weight:700;color:var(--text-main);">○ 총사업비 : </span><span style="font-weight:700;color:#d97706;">${p.budgetTotal}</span>
                </div>
                <div style="font-size:0.9rem;color:var(--text-muted);margin-bottom:0.25rem;">
                    <span style="font-weight:700;color:var(--text-main);">○ 사업내용 : </span>${p.scope}
                </div>
                ${achHTML}
                ${scheduleHTML}
            </td>
            <td style="padding:1rem 0.8rem;vertical-align:top;width:170px;min-width:170px;border-left:1px solid var(--border-color);text-align:center;">
                <img src="${p.image}" alt="${p.title}"
                     style="width:155px;height:105px;object-fit:cover;border-radius:var(--radius-sm);border:1px solid var(--border-color);cursor:pointer;"
                     onclick="event.stopPropagation(); openLightbox('${p.image}', '${escapeHtml(p.title)} - 참고사진')"
                     title="클릭하여 사진 확대보기">
                <div style="font-size:0.75rem;color:var(--text-muted);margin-top:0.4rem;line-height:1.4;">${p.imageCaption || p.title}</div>
            </td>
        </tr>`;
    }).join('');

    tableContainer.innerHTML = `
        <div style="overflow-x:auto;border-radius:var(--radius-md);box-shadow:var(--shadow-md);border:1.5px solid var(--border-color);">
            <table style="width:100%;border-collapse:collapse;font-size:0.9rem;">
                <thead>
                    <tr style="background:#f8f9fa;color:var(--text-main);border-bottom:2px solid #333;">
                        <th style="padding:0.7rem 1rem;text-align:center;width:130px;min-width:130px;font-size:0.9rem;font-weight:700;border-right:1px solid #ccc;border-left:1px solid #ccc;">사업유형</th>
                        <th style="padding:0.7rem 1.4rem;text-align:center;font-size:0.9rem;font-weight:700;border-right:1px solid #ccc;">주요내용</th>
                        <th style="padding:0.7rem 0.8rem;text-align:center;width:170px;min-width:170px;font-size:0.9rem;font-weight:700;border-right:1px solid #ccc;">참고사진</th>
                    </tr>
                </thead>
                <tbody>${rows}</tbody>
            </table>
        </div>
        <p style="text-align:right;font-size:0.75rem;color:var(--text-muted);margin-top:0.5rem;padding-right:0.5rem;">
            ※ 항목 클릭 시 상세 정보를 확인할 수 있습니다.
        </p>`;
}

function openDetailModal(projId) {
    const project = projectsData.find(p => p.id === projId);
    if (!project) return;

    currentSelectedProject = project;

    document.getElementById('modal-no').textContent = project.no;
    document.getElementById('modal-title').textContent = project.title;
    document.getElementById('modal-dept').textContent = `${project.dept} (☎${project.phone})`;
    document.getElementById('modal-location').textContent = project.location || '-';
    document.getElementById('modal-budget').textContent = project.budgetTotal;
    document.getElementById('modal-beneficiaries').textContent = project.beneficiaries || '-';

    // PDF page image & links inside modal
    const pdfPage = project.pdfPage || 1;
    const pdfLabel = project.pdfPageLabel || `P.${pdfPage}`;
    const pdfPages = project.pdfPages || [pdfPage];
    const pdfUrl = `${RAW_PDF_FILENAME}#page=${pdfPage}`;
    
    const pdfText = document.getElementById('modal-pdf-btn-text');
    const pdfExternalLink = document.getElementById('pdf-external-link');
    const pdfIndicator = document.getElementById('pdf-page-indicator');
    const modalFooterPdfPageNum = document.getElementById('modal-footer-pdf-page-num');

    if (pdfText) pdfText.textContent = `원본 PDF (${pdfLabel})`;
    if (pdfExternalLink) pdfExternalLink.href = pdfUrl;
    if (pdfIndicator) pdfIndicator.textContent = `원본 PDF 보고서 (${pdfLabel})`;
    if (modalFooterPdfPageNum) modalFooterPdfPageNum.textContent = pdfLabel;

    // Render Tab 2 Pages
    const pagesContainer = document.getElementById('modal-pdf-pages-container');
    if (pagesContainer) {
        pagesContainer.innerHTML = pdfPages.map((pg, idx) => `
            <div class="pdf-page-card" style="margin-bottom: 1.5rem; background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 1.25rem; text-align: center; box-shadow: var(--shadow-sm);">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 0.75rem; padding-bottom: 0.5rem; border-bottom: 1px dashed var(--border-color);">
                    <span style="font-weight: 700; color: var(--primary-color); font-size: 0.95rem;">📄 페이지 ${idx + 1} / ${pdfPages.length} (PDF Page ${pg})</span>
                    <div style="display:flex; gap:0.5rem;">
                        <button type="button" class="btn btn-sm btn-primary" onclick="openPdfPage(${pg}, '${escapeHtml(project.title)} - P.${pg}')">
                            🔍 확대보기 (P.${pg})
                        </button>
                        <a href="assets/pdf_pages/page_${pg}.png" download="${escapeHtml(project.title)}_PDF_Page_${pg}.png" class="btn btn-sm btn-outline">
                            💾 다운로드
                        </a>
                    </div>
                </div>
                <img src="assets/pdf_pages/page_${pg}.png" alt="${escapeHtml(project.title)} Page ${pg}" 
                     onclick="openPdfPage(${pg}, '${escapeHtml(project.title)} - P.${pg}')"
                     title="클릭 시 라이트박스 뷰어로 확대보기"
                     style="max-width:100%; max-height:650px; object-fit:contain; cursor:pointer; border-radius:var(--radius-sm); border:1px solid var(--border-color); box-shadow:var(--shadow-md);">
                <div style="margin-top:0.5rem; font-size:0.8rem; color:var(--text-muted);">🔍 이미지를 클릭하면 자유로운 확대/축소/이동(Lightbox) 뷰어로 크게 열립니다.</div>
            </div>
        `).join('');
    }

    // Reset Modal Tab to Info
    switchModalTab('info');

    // Tags
    const tagsContainer = document.getElementById('modal-tags');
    tagsContainer.innerHTML = project.tags.map(t => `<span class="tag-badge badge-${t}">${t}</span>`).join('');

    // Purpose & Scope
    document.getElementById('modal-purpose').textContent = project.purpose || '중점추진사업 지속점검 및 시민 교통편의 증진';
    document.getElementById('modal-scope').textContent = project.scope || '-';

    // Budget Table
    const budgetWrap = document.getElementById('modal-budget-table-wrap');
    if (project.budgetBreakdown) {
        let rows = '';
        for (const [key, val] of Object.entries(project.budgetBreakdown)) {
            rows += `<tr><th>${key}</th><td>${val}</td></tr>`;
        }
        budgetWrap.innerHTML = `
            <table class="budget-table">
                <thead>
                    <tr><th>구분 / 재원</th><th>금액 및 비율</th></tr>
                </thead>
                <tbody>${rows}</tbody>
            </table>
        `;
    } else {
        budgetWrap.innerHTML = `<div class="detail-desc-box">총사업비: ${project.budgetTotal}</div>`;
    }

    // Achievements
    const achList = document.getElementById('modal-achievements');
    achList.innerHTML = renderAchievementItems(project.achievements);

    // Schedule
    const schList = document.getElementById('modal-schedule');
    schList.innerHTML = (project.schedule || []).map(s => `<li>${s}</li>`).join('');

    // Sub-Projects for Parking (proj-5)
    const subSection = document.getElementById('modal-subprojects-section');
    const subContainer = document.getElementById('modal-subprojects-container');
    if (project.subProjects && project.subProjects.length > 0) {
        subSection.style.display = 'block';
        subContainer.innerHTML = project.subProjects.map(sp => `
            <div class="subproject-item-card">
                <div class="subproject-thumb" onclick="openLightbox('${sp.image}', '${escapeHtml(sp.name)}')">
                    <img src="${sp.image}" alt="${sp.name}">
                    <div class="card-image-overlay"><span>확대</span></div>
                </div>
                <div class="subproject-info">
                    <div class="subproject-name">${sp.name}</div>
                    <div><b>사업비:</b> ${sp.budget} (${sp.capacity})</div>
                    <div><b>상태:</b> <span class="tag-badge badge-지속추진">${sp.status}</span></div>
                    <div><b>계획:</b> ${sp.plan}</div>
                </div>
            </div>
        `).join('');
    } else {
        subSection.style.display = 'none';
    }

    // Image
    const modalImg = document.getElementById('modal-img');
    modalImg.src = project.image;
    document.getElementById('modal-img-caption').textContent = project.imageCaption || `${project.title} 참고사진`;

    // Show Modal
    const modal = document.getElementById('detail-modal');
    modal.classList.add('active');
    modal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
}

function switchModalTab(tabName) {
    const infoTab = document.getElementById('modal-tab-content-info');
    const pdfTab = document.getElementById('modal-tab-content-pdf');
    const infoBtn = document.getElementById('tab-info-btn');
    const pdfBtn = document.getElementById('tab-pdf-btn');

    if (tabName === 'info') {
        infoTab.style.display = 'block';
        pdfTab.style.display = 'none';
        infoBtn.classList.add('active');
        pdfBtn.classList.remove('active');
    } else if (tabName === 'pdf') {
        infoTab.style.display = 'none';
        pdfTab.style.display = 'block';
        infoBtn.classList.remove('active');
        pdfBtn.classList.add('active');
    }
}

function closeDetailModal() {
    const modal = document.getElementById('detail-modal');
    modal.classList.remove('active');
    modal.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
}

function openLightboxFromModal() {
    if (currentSelectedProject) {
        openLightbox(currentSelectedProject.image, `${currentSelectedProject.title} - ${currentSelectedProject.imageCaption || '참고사진'}`);
    }
}

// Lightbox Zoom & Pan State Variables
let currentZoom = 1.0;
let currentTranslateX = 0;
let currentTranslateY = 0;
let isDragging = false;
let startX = 0;
let startY = 0;

function updateZoomTransform() {
    const wrapper = document.getElementById('lightbox-img-wrapper');
    const badge = document.getElementById('zoom-level-badge');
    if (wrapper) {
        wrapper.style.transform = `translate(${currentTranslateX}px, ${currentTranslateY}px) scale(${currentZoom})`;
    }
    if (badge) {
        badge.textContent = `${Math.round(currentZoom * 100)}%`;
    }
}

function zoomIn() {
    currentZoom = Math.min(currentZoom + 0.25, 4.0);
    updateZoomTransform();
}

function zoomOut() {
    currentZoom = Math.max(currentZoom - 0.25, 0.5);
    updateZoomTransform();
}

function resetZoom() {
    currentZoom = 1.0;
    currentTranslateX = 0;
    currentTranslateY = 0;
    updateZoomTransform();
}

function toggleNativeFullscreen() {
    const modal = document.getElementById('lightbox-modal');
    if (!document.fullscreenElement) {
        if (modal.requestFullscreen) {
            modal.requestFullscreen();
        } else if (modal.webkitRequestFullscreen) {
            modal.webkitRequestFullscreen();
        }
    } else {
        if (document.exitFullscreen) {
            document.exitFullscreen();
        } else if (document.webkitExitFullscreen) {
            document.webkitExitFullscreen();
        }
    }
}

let lightboxPagesList = [];
let lightboxPageIndex = 0;
let lightboxBaseTitle = "";

const SUMMARY_SLIDES_LIST = [
    'assets/summary/slide_1.jpg',
    'assets/summary/slide_2.jpg',
    'assets/summary/slide_3.jpg',
    'assets/summary/slide_4.jpg',
    'assets/summary/slide_5.jpg',
    'assets/summary/slide_6.jpg',
    'assets/summary/slide_7.jpg',
    'assets/summary/slide_8.jpg',
    'assets/summary/slide_9.jpg'
];

function openSummarySlidesModal() {
    openLightbox(
        SUMMARY_SLIDES_LIST[0],
        '교통국 중점사업 요약 설명 (1/9)',
        SUMMARY_SLIDES_LIST,
        0,
        '교통국 중점사업 요약 설명'
    );
}

function openRoadMapModal() {
    openLightbox(
        'assets/road_map/road_map.jpg',
        '교통국 도로 사업 지도',
        null,
        0,
        '교통국 도로 사업 지도'
    );
}

function openLightbox(imgSrc, caption, pagesList = null, pageIndex = 0, baseTitle = "") {
    const lightbox = document.getElementById('lightbox-modal');
    const imgEl = document.getElementById('lightbox-img');
    const captionEl = document.getElementById('lightbox-caption');
    const downloadLink = document.getElementById('lightbox-download-link');
    const titleEl = document.getElementById('lightbox-title');
    const prevBtn = document.getElementById('lightbox-prev-btn');
    const nextBtn = document.getElementById('lightbox-next-btn');

    lightboxPagesList = pagesList || [];
    lightboxPageIndex = pageIndex;
    lightboxBaseTitle = baseTitle || caption || "";

    imgEl.src = imgSrc;
    captionEl.textContent = caption || '참고사진';
    titleEl.textContent = caption ? `${caption} 확대보기` : '참고사진 확대보기';
    downloadLink.href = imgSrc;
    downloadLink.setAttribute('download', (caption || 'project_photo').replace(/[\\/\\?%*:|"<>]/g, '_') + '.png');

    // Multi-page navigation buttons (이전 페이지 / 다음 페이지)
    if (lightboxPagesList && lightboxPagesList.length > 1) {
        if (prevBtn) {
            prevBtn.style.display = 'flex';
            prevBtn.disabled = (lightboxPageIndex <= 0);
        }
        if (nextBtn) {
            nextBtn.style.display = 'flex';
            nextBtn.disabled = (lightboxPageIndex >= lightboxPagesList.length - 1);
        }
    } else {
        if (prevBtn) prevBtn.style.display = 'none';
        if (nextBtn) nextBtn.style.display = 'none';
    }

    resetZoom();

    lightbox.classList.add('active');
    lightbox.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
}

function navigateLightboxPage(delta) {
    if (!lightboxPagesList || lightboxPagesList.length <= 1) return;
    
    const newIdx = lightboxPageIndex + delta;
    if (newIdx < 0 || newIdx >= lightboxPagesList.length) return;

    lightboxPageIndex = newIdx;
    const pg = lightboxPagesList[lightboxPageIndex];
    
    let pageImgSrc = '';
    let caption = '';
    let downloadName = '';
    
    if (typeof pg === 'string' && (pg.includes('/') || pg.includes('.'))) {
        pageImgSrc = pg;
        caption = `${lightboxBaseTitle} (${lightboxPageIndex + 1}/${lightboxPagesList.length})`;
        downloadName = `${lightboxBaseTitle}_${lightboxPageIndex + 1}.jpg`;
    } else {
        pageImgSrc = `assets/pdf_pages/page_${pg}.png`;
        caption = `${lightboxBaseTitle} - 원본 PDF 보고서 (P.${pg}) (${lightboxPageIndex + 1}/${lightboxPagesList.length})`;
        downloadName = `${lightboxBaseTitle}_P${pg}.png`;
    }

    const imgEl = document.getElementById('lightbox-img');
    const captionEl = document.getElementById('lightbox-caption');
    const downloadLink = document.getElementById('lightbox-download-link');
    const titleEl = document.getElementById('lightbox-title');
    const prevBtn = document.getElementById('lightbox-prev-btn');
    const nextBtn = document.getElementById('lightbox-next-btn');

    imgEl.src = pageImgSrc;
    captionEl.textContent = caption;
    titleEl.textContent = `${caption} 확대보기`;
    downloadLink.href = pageImgSrc;
    downloadLink.setAttribute('download', downloadName.replace(/[\\/\\?%*:|"<>]/g, '_'));

    if (prevBtn) prevBtn.disabled = (lightboxPageIndex <= 0);
    if (nextBtn) nextBtn.disabled = (lightboxPageIndex >= lightboxPagesList.length - 1);

    resetZoom();
}

function closeLightbox() {
    const lightbox = document.getElementById('lightbox-modal');
    lightbox.classList.remove('active');
    lightbox.setAttribute('aria-hidden', 'true');
    resetZoom();

    if (document.fullscreenElement) {
        if (document.exitFullscreen) document.exitFullscreen();
    }

    const detailModal = document.getElementById('detail-modal');
    if (!detailModal.classList.contains('active')) {
        document.body.style.overflow = '';
    }
}

function initLightboxInteractions() {
    const stage = document.getElementById('lightbox-stage');
    if (!stage) return;

    // Wheel zoom
    stage.addEventListener('wheel', (e) => {
        e.preventDefault();
        const delta = e.deltaY < 0 ? 0.15 : -0.15;
        currentZoom = Math.min(Math.max(currentZoom + delta, 0.5), 4.0);
        updateZoomTransform();
    }, { passive: false });

    // Drag to pan (Mouse)
    stage.addEventListener('mousedown', (e) => {
        if (e.target.closest('.lightbox-toolbar') || e.target.closest('.lightbox-fullscreen-bar') || e.target.closest('.lightbox-nav-btn')) return;
        isDragging = true;
        startX = e.clientX - currentTranslateX;
        startY = e.clientY - currentTranslateY;
        stage.classList.add('dragging');
    });

    window.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        currentTranslateX = e.clientX - startX;
        currentTranslateY = e.clientY - startY;
        updateZoomTransform();
    });

    window.addEventListener('mouseup', () => {
        if (isDragging) {
            isDragging = false;
            stage.classList.remove('dragging');
        }
    });

    // Touch Events for Tablets & Mobile (Pan, Pinch Zoom, Swipe)
    let touchStartX = 0;
    let touchStartY = 0;
    let initialPinchDist = 0;
    let initialZoomOnPinch = 1.0;
    let isTouchDragging = false;

    stage.addEventListener('touchstart', (e) => {
        if (e.target.closest('.lightbox-toolbar') || e.target.closest('.lightbox-fullscreen-bar') || e.target.closest('.lightbox-nav-btn')) return;

        if (e.touches.length === 1) {
            isTouchDragging = true;
            touchStartX = e.touches[0].clientX;
            touchStartY = e.touches[0].clientY;
            startX = touchStartX - currentTranslateX;
            startY = touchStartY - currentTranslateY;
        } else if (e.touches.length === 2) {
            isTouchDragging = false;
            initialPinchDist = Math.hypot(
                e.touches[0].clientX - e.touches[1].clientX,
                e.touches[0].clientY - e.touches[1].clientY
            );
            initialZoomOnPinch = currentZoom;
        }
    }, { passive: true });

    stage.addEventListener('touchmove', (e) => {
        if (e.touches.length === 1 && isTouchDragging) {
            currentTranslateX = e.touches[0].clientX - startX;
            currentTranslateY = e.touches[0].clientY - startY;
            updateZoomTransform();
        } else if (e.touches.length === 2 && initialPinchDist > 0) {
            const dist = Math.hypot(
                e.touches[0].clientX - e.touches[1].clientX,
                e.touches[0].clientY - e.touches[1].clientY
            );
            const scale = dist / initialPinchDist;
            currentZoom = Math.min(Math.max(initialZoomOnPinch * scale, 0.5), 4.0);
            updateZoomTransform();
        }
    }, { passive: true });

    stage.addEventListener('touchend', (e) => {
        if (isTouchDragging && e.changedTouches.length === 1) {
            const diffX = e.changedTouches[0].clientX - touchStartX;
            const diffY = e.changedTouches[0].clientY - touchStartY;

            // Horizontal swipe to navigate when not heavily zoomed
            if (currentZoom <= 1.2 && Math.abs(diffX) > 50 && Math.abs(diffY) < 100) {
                if (diffX < 0) {
                    navigateLightboxPage(1);
                } else {
                    navigateLightboxPage(-1);
                }
            }
        }
        isTouchDragging = false;
        initialPinchDist = 0;
    });

    // Double click toggle zoom
    stage.addEventListener('dblclick', (e) => {
        if (e.target.closest('.lightbox-toolbar') || e.target.closest('.lightbox-fullscreen-bar') || e.target.closest('.lightbox-nav-btn')) return;
        if (currentZoom === 1.0) {
            currentZoom = 2.0;
        } else {
            resetZoom();
            return;
        }
        updateZoomTransform();
    });

    // Keyboard navigation (Arrow keys & Escape)
    window.addEventListener('keydown', (e) => {
        const lightbox = document.getElementById('lightbox-modal');
        if (!lightbox || !lightbox.classList.contains('active')) return;

        if (e.key === 'ArrowLeft') {
            navigateLightboxPage(-1);
        } else if (e.key === 'ArrowRight') {
            navigateLightboxPage(1);
        } else if (e.key === 'Escape') {
            closeLightbox();
        }
    });

function openPdfPage(pageNum, title, pagesList = null, pageIndex = 0) {
    const pageImgSrc = `assets/pdf_pages/page_${pageNum}.png`;
    const totalCount = (pagesList && pagesList.length > 1) ? ` (${pageIndex + 1}/${pagesList.length})` : '';
    const caption = title ? `${title} - 원본 PDF 보고서 (P.${pageNum})${totalCount}` : `원본 PDF 보고서 (P.${pageNum})${totalCount}`;
    openLightbox(pageImgSrc, caption, pagesList, pageIndex, title);
}

function openProjectPdfInLightbox(projId, startPageIndex = 0) {
    const project = projectsData.find(p => p.id === projId);
    if (!project) return;
    const pages = project.pdfPages || [project.pdfPage || 1];
    const pageIndex = Math.min(Math.max(startPageIndex, 0), pages.length - 1);
    const pg = pages[pageIndex];
    openPdfPage(pg, project.title, pages, pageIndex);
}

function openCurrentPdfPageInLightbox() {
    if (currentSelectedProject) {
        openProjectPdfInLightbox(currentSelectedProject.id, 0);
    }
}

function openPdfPagesForProject(projId) {
    openDetailModal(projId);
    switchModalTab('pdf');
}

    window.zoomIn = zoomIn;
    window.zoomOut = zoomOut;
    window.resetZoom = resetZoom;
    window.toggleNativeFullscreen = toggleNativeFullscreen;
    window.openLightbox = openLightbox;
    window.closeLightbox = closeLightbox;
    window.navigateLightboxPage = navigateLightboxPage;
    window.openLightboxFromModal = openLightboxFromModal;
    window.openPdfPage = openPdfPage;
    window.openProjectPdfInLightbox = openProjectPdfInLightbox;
    window.openCurrentPdfPageInLightbox = openCurrentPdfPageInLightbox;
    window.openPdfPagesForProject = openPdfPagesForProject;
    window.openSummarySlidesModal = openSummarySlidesModal;
    window.openRoadMapModal = openRoadMapModal;
}

// Filter Event Listeners
function initEventListeners() {
    const searchInput = document.getElementById('search-input');
    const clearBtn = document.getElementById('clear-search-btn');

    searchInput.addEventListener('input', (e) => {
        currentSearch = e.target.value;
        clearBtn.style.display = currentSearch ? 'block' : 'none';
        renderProjects();
    });

    clearBtn.addEventListener('click', () => {
        searchInput.value = '';
        currentSearch = '';
        clearBtn.style.display = 'none';
        renderProjects();
    });

    // Dept Pills
    const deptPills = document.querySelectorAll('#dept-pills .pill-btn');
    deptPills.forEach(pill => {
        pill.addEventListener('click', () => {
            deptPills.forEach(p => p.classList.remove('active'));
            pill.classList.add('active');
            activeDept = pill.dataset.dept;
            renderProjects();
        });
    });

    // Tag Pills
    const tagPills = document.querySelectorAll('#tag-pills .pill-btn');
    tagPills.forEach(pill => {
        pill.addEventListener('click', () => {
            tagPills.forEach(p => p.classList.remove('active'));
            pill.classList.add('active');
            activeTag = pill.dataset.tag;
            renderProjects();
        });
    });

    // Close Modals on ESC Key or Backdrop Click
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            closeLightbox();
            closeDetailModal();
        }
    });

    document.getElementById('detail-modal').addEventListener('click', (e) => {
        if (e.target.id === 'detail-modal') closeDetailModal();
    });

    document.getElementById('lightbox-modal').addEventListener('click', (e) => {
        if (e.target.id === 'lightbox-modal') closeLightbox();
    });

    // Theme Toggle
    document.getElementById('theme-toggle-btn').addEventListener('click', toggleTheme);
}

function filterByDept(deptName) {
    activeDept = deptName;
    const deptPills = document.querySelectorAll('#dept-pills .pill-btn');
    deptPills.forEach(pill => {
        if (pill.dataset.dept === deptName) {
            pill.classList.add('active');
        } else {
            pill.classList.remove('active');
        }
    });
    renderProjects();
    document.getElementById('cards-section').scrollIntoView({ behavior: 'smooth' });
}

function resetFilters() {
    activeDept = 'all';
    activeTag = 'all';
    currentSearch = '';

    document.getElementById('search-input').value = '';
    document.getElementById('clear-search-btn').style.display = 'none';

    document.querySelectorAll('#dept-pills .pill-btn').forEach(p => {
        p.classList.toggle('active', p.dataset.dept === 'all');
    });
    document.querySelectorAll('#tag-pills .pill-btn').forEach(p => {
        p.classList.toggle('active', p.dataset.tag === 'all');
    });

    renderProjects();
}

// Dark Mode Theme Handler
function initTheme() {
    const savedTheme = localStorage.getItem('transport_dashboard_theme') || 'light';
    document.body.className = `theme-${savedTheme}`;
}

function toggleTheme() {
    const currentTheme = document.body.classList.contains('theme-dark') ? 'dark' : 'light';
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    document.body.className = `theme-${newTheme}`;
    localStorage.setItem('transport_dashboard_theme', newTheme);
}

// Utility
function escapeHtml(str) {
    if (!str) return '';
    return str.replace(/'/g, "\\'").replace(/"/g, '&quot;');
}

function renderAchievementItems(achievements) {
    if (!achievements || achievements.length === 0) return '';
    return achievements.map(item => {
        if (typeof item === 'object' && item !== null) {
            const parentText = item.text || item.title || '';
            const childrenHTML = (item.children || item.items || []).map(child => `<li class="sub-item">${child}</li>`).join('');
            return `<li class="parent-item">
                <div class="parent-text">${parentText}</div>
                ${childrenHTML ? `<ul class="sub-detail-list">${childrenHTML}</ul>` : ''}
            </li>`;
        } else if (typeof item === 'string') {
            if (item.startsWith('○ ') || item.startsWith('O ')) {
                return `<li class="parent-item"><div class="parent-text">${item.replace(/^[○O]\\s*/, '')}</div></li>`;
            } else if (item.startsWith('  - ') || item.startsWith('- ')) {
                return `<li class="sub-item">${item.replace(/^(\\s*-\\s*)/, '')}</li>`;
            }
            return `<li>${item}</li>`;
        }
        return `<li>${item}</li>`;
    }).join('');
}
"""

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(header + json_str + body)

print("Generated app.js with embedded data!")
