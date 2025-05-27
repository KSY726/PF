document.addEventListener('DOMContentLoaded', () => {
    const hamburgerMenu = document.querySelector('.hamburger-menu');
    const sidebar = document.querySelector('.sidebar');
    const closeButton = document.querySelector('.close-button');
    const sidebarNavLinks = document.querySelectorAll('.sidebar-nav a');

    // 햄버거 메뉴 클릭 시 사이드바 열기
    hamburgerMenu.addEventListener('click', () => {
        sidebar.classList.add('active');
        document.body.style.overflow = 'hidden'; // 스크롤 방지
    });

    // 닫기 버튼 클릭 시 사이드바 닫기
    closeButton.addEventListener('click', () => {
        sidebar.classList.remove('active');
        document.body.style.overflow = ''; // 스크롤 허용
    });

    // 사이드바 메뉴 링크 클릭 시 사이드바 닫기 (메뉴 이동 후)
    sidebarNavLinks.forEach(link => {
        link.addEventListener('click', () => {
            // 사이드바 닫기
            sidebar.classList.remove('active');
            document.body.style.overflow = ''; // 스크롤 허용

            // 부드러운 스크롤 (anchor 링크 이동)
            const targetId = link.getAttribute('href').substring(1); // # 제외한 ID
            const targetElement = document.getElementById(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    // 사이드바 외부 클릭 시 닫기 (선택 사항: 데스크톱에서 유용)
    document.addEventListener('click', (event) => {
        // 햄버거 메뉴나 사이드바 자체가 아닌 곳을 클릭했을 때
        if (!sidebar.contains(event.target) && !hamburgerMenu.contains(event.target) && sidebar.classList.contains('active')) {
            sidebar.classList.remove('active');
            document.body.style.overflow = '';
        }
    });

    // ESC 키 눌렀을 때 사이드바 닫기
    document.addEventListener('keydown', (event) => {
        if (event.key === 'Escape' && sidebar.classList.contains('active')) {
            sidebar.classList.remove('active');
            document.body.style.overflow = '';
        }
    });
});