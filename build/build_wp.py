import re,os,json,shutil,html
PUB='/home/claude/dateworld-site/public'
T='/home/claude/wp/dateworld'
if os.path.exists(T): shutil.rmtree(T)
os.makedirs(T+'/img')
for f in os.listdir(PUB+'/img'): shutil.copy(PUB+'/img/'+f,T+'/img/'+f)
pages=[]
for r,d,fs in os.walk(PUB):
    if 'index.html' in fs and '/img' not in r: pages.append('/'+os.path.relpath(r,PUB).replace('.','').strip('/')+'/' if r!=PUB else '/')
pages=sorted(set(p.replace('//','/') for p in pages))
styles=[];seen=set()
front=open(PUB+'/index.html',encoding='utf-8').read()
head=front[:front.index('</head>')]
links=''.join(l for l in re.findall(r'<link[^>]+>',head) if 'canonical' not in l)
def fixsrc(s): return re.sub(r'(src|href)="/img/',r'\1="/wp-content/themes/dateworld/img/',s).replace("url(/img/","url(/wp-content/themes/dateworld/img/")
menujs=None;out=[]
for p in pages:
    t=open(PUB+(p if p!='/' else '/')+'index.html',encoding='utf-8').read()
    for st in re.findall(r'<style>(.*?)</style>',t,re.S):
        k=hash(st)
        if k not in seen: seen.add(k);styles.append(st)
    title=html.unescape(re.search(r'<title>(.*?)</title>',t,re.S).group(1))
    dm=re.search(r'<meta name="description" content="([^"]*)"',t); desc=html.unescape(dm.group(1)) if dm else ''
    main=t[t.index('<main'):t.index('</main>')+7]
    after=t[t.index('</footer>')+9:t.index('</body>')]
    scs=re.findall(r'<script>(.*?)</script>',after,re.S)
    for s in scs:
        if 'var panels=' in s: menujs=s
    extra=re.sub(r'<script>(?:(?!</script>).)*?var panels=.*?</script>','',after,flags=re.S)
    content=fixsrc(main+extra)
    slug='forside' if p=='/' else p.strip('/')
    out.append(dict(slug=slug,title=title,desc=desc,content='<!-- wp:html -->\n'+content+'\n<!-- /wp:html -->'))
css=fixsrc('\n'.join(styles))
open(T+'/style.css','w',encoding='utf-8').write('/*\nTheme Name: Dateworld\nAuthor: Mondae\nVersion: 1.0\n*/\n'+css+'\n'+open('/home/claude/dateworld-site/build/wp_extra.css').read())
top=front[front.index('<body'):front.index('<main')] if '<main' in front else ''
# header markup = from <body...> to just before <main>
body_open=re.search(r'<body[^>]*>',front).group(0)
top_markup=front[front.index(body_open)+len(body_open):front.index('<main')]
foot=front[front.index('<footer'):front.index('</footer>')+9]
open(T+'/header.php','w',encoding='utf-8').write('<!DOCTYPE html>\n<html lang="da">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'+links+'\n<?php wp_head(); ?>\n</head>\n'+body_open.replace('<body','<body <?php body_class(); ?>',1).replace('<body <?php body_class(); ?> class=','<body class=')+'\n'+fixsrc(top_markup))
open(T+'/footer.php','w',encoding='utf-8').write(fixsrc(foot)+'\n<script>'+menujs+'</script>\n<?php wp_footer(); ?>\n</body>\n</html>\n')
tpl="<?php get_header(); while(have_posts()){the_post(); echo apply_filters('the_content',get_the_content());} get_footer();"
for f in ['index.php','page.php','single.php']: open(T+'/'+f,'w').write(tpl)
open(T+'/functions.php','w').write(r'''<?php
add_theme_support('title-tag');
remove_filter('the_content','wpautop');remove_filter('the_content','wptexturize');
remove_action('wp_head','print_emoji_detection_script',7);remove_action('wp_print_styles','print_emoji_styles');
add_action('wp_enqueue_scripts',function(){wp_enqueue_style('dateworld',get_stylesheet_uri(),[],'1.0');wp_dequeue_style('wp-block-library');wp_dequeue_style('global-styles');wp_dequeue_style('classic-theme-styles');},100);
add_action('init',function(){foreach(['dw_title','dw_desc'] as $k){register_post_meta('page',$k,['show_in_rest'=>true,'single'=>true,'type'=>'string','auth_callback'=>function(){return current_user_can('edit_pages');}]);}});
add_filter('pre_get_document_title',function($t){if(is_singular()){$v=get_post_meta(get_the_ID(),'dw_title',true);if($v)return $v;}return $t;},99);
add_action('wp_head',function(){if(is_singular()){$d=get_post_meta(get_the_ID(),'dw_desc',true);if($d)echo '<meta name="description" content="'.esc_attr($d).'">'."\n";}},1);
add_filter('show_admin_bar','__return_false');
''')
json.dump(out,open('/home/claude/dateworld-site/public/wp-export/pages.json','w') if os.path.isdir('/home/claude/dateworld-site/public/wp-export') else open('/tmp/pages.json','w'),ensure_ascii=False)
print(len(out),'pages', len(css)//1024,'KB css', menujs is not None)
