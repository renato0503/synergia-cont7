import re

add_head = """    <script src="https://cdn.jsdelivr.net/gh/gitbrent/pptxgenjs@3.12.0/libs/jszip.min.js"></script>
    <script src="https://cdn.jsdelivr.net/gh/gitbrent/pptxgenjs@3.12.0/dist/pptxgen.bundle.js"></script>
"""

add_nav = """    <div class="nav-controls">
        <a href="index.html" class="btn-nav"><i class="ph ph-house"></i> Menu Principal</a>
        <button onclick="exportPPTX('Grupo_X_Synergia')" class="btn-nav" style="border: none;"><i class="ph ph-presentation-chart"></i> Exportar PPTX</button>
    </div>
"""

add_script = """
    <script>
        async function exportPPTX(groupName) {
            alert("Gerando arquivo PowerPoint... Isso pode levar alguns segundos.");
            let pres = new PptxGenJS();
            pres.layout = 'LAYOUT_16x9';
            
            let slides = document.querySelectorAll('.slide');
            for(let i = 0; i < slides.length; i++) {
                let slideElem = slides[i];
                let slide = pres.addSlide();
                
                let isCover = slideElem.classList.contains('cover-slide');
                slide.background = { fill: 'FFFFFF' }; 
                
                let splitImage = slideElem.querySelector('.split-image');
                let bgUrl = null;
                
                if(splitImage) {
                    let bgImg = window.getComputedStyle(splitImage).backgroundImage;
                    let urlMatch = bgImg.match(/url\\(['"]?(.*?)['"]?\\)/);
                    if(urlMatch && urlMatch[1]) bgUrl = urlMatch[1];
                } else if(isCover) {
                    let bgImg = window.getComputedStyle(slideElem).backgroundImage;
                    let urlMatch = bgImg.match(/url\\(['"]?(.*?)['"]?\\)/);
                    if(urlMatch && urlMatch[1]) bgUrl = urlMatch[1];
                }
                
                if (isCover) {
                    slide.background = { fill: '0F172A' };
                    if(bgUrl) {
                        try {
                            slide.addImage({ path: bgUrl, x:0, y:0, w:'100%', h:'100%', sizing: {type: 'cover'} });
                            slide.addShape(pres.ShapeType.rect, { x:0, y:0, w:'100%', h:'100%', fill:{color:'0F172A', transparency:30} });
                        } catch(e) {}
                    }
                    
                    let h2 = slideElem.querySelector('h2');
                    let ps = slideElem.querySelectorAll('p');
                    
                    if (h2) slide.addText(h2.innerText, { x:1, y:2, w:'80%', h:1.5, fontSize:44, color:'FFFFFF', bold:true, align:'center' });
                    
                    let yPos = 3.5;
                    ps.forEach(p => {
                        if(p.innerText.trim() !== '') {
                            slide.addText(p.innerText, { x:1, y:yPos, w:'80%', h:1, fontSize:20, color:'CBD5E1', align:'center' });
                            yPos += 1;
                        }
                    });
                } else {
                    let isLeftImage = splitImage && splitImage.classList.contains('left');
                    
                    if(bgUrl) {
                        let imgX = isLeftImage ? 0 : 5;
                        try {
                            slide.addImage({ path: bgUrl, x:imgX, y:0, w:5, h:5.625, sizing: {type: 'cover'} });
                        } catch(e) {}
                    }
                    
                    let textX = (bgUrl && isLeftImage) ? 5.5 : 0.5;
                    let textW = bgUrl ? 4 : 9;
                    
                    let h2 = slideElem.querySelector('h2');
                    if (h2) slide.addText(h2.innerText, { x:textX, y:0.5, w:textW, h:1, fontSize:32, color:'0F172A', bold:true });
                    
                    let yPos = 1.6;
                    let ps = slideElem.querySelectorAll('p, li');
                    ps.forEach(p => {
                        if(p.innerText.trim() !== '') {
                            let isLi = p.tagName.toLowerCase() === 'li';
                            slide.addText(p.innerText, { x:textX + (isLi?0.2:0), y:yPos, w:textW - (isLi?0.2:0), h:0.5, fontSize:16, color:'64748B', bullet: isLi });
                            yPos += 0.6;
                        }
                    });
                }
            }
            pres.writeFile({ fileName: groupName + ".pptx" });
        }
    </script>
</body>
"""

for idx, file in enumerate(['grupo1.html', 'grupo2.html', 'grupo3.html'], 1):
    with open(f"c:/Users/Renato/Documents/Synergia - Cont7/{file}", "r", encoding="utf-8") as f:
        content = f.read()
    
    if "pptxgenjs" not in content:
        content = content.replace("</head>", add_head + "</head>")
        
        # Replace nav controls
        old_nav = '<div class="nav-controls"><a href="index.html" class="btn-nav"><i class="ph ph-house"></i> Menu Principal</a></div>'
        content = content.replace(old_nav, add_nav.replace("Grupo_X_Synergia", f"Grupo_{idx}_Synergia"))
        
        # Add script before </body>
        content = content.replace("</body>", add_script)
        
        with open(f"c:/Users/Renato/Documents/Synergia - Cont7/{file}", "w", encoding="utf-8") as f:
            f.write(content)
            print(f"Updated {file}")
