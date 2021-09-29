//load main home title
gsap.to('.home_sub', {duration: 1, y: -40});

const boxes = gsap.utils.toArray('.box');

//Load pages on scroll
const LoadPage = ()=>{
   

    gsap.set(boxes, {autoAlpha: 0, y: 80})

    boxes.forEach((box, i)=>{
        const anim = gsap.to(box, {duration: 2, autoAlpha: 1, y: 0, paused:true});
    
        ScrollTrigger.create({
            trigger: box,
            end: 'bottom bottom',
            onEnter: self => {
                self.progress === 1 ? anim.progress(1) : anim.play();
                //console.log(self)
                self.isActive === true ? anim.play(): {};    
            },
            onRefresh: ref=>{
                console.log(ref)
            }
        })
    })
}

LoadPage();