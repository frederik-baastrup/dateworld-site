add_action('rest_api_init',function(){
 $perm=function(){return current_user_can('manage_options');};
 register_rest_route('dw/v1','/scan',['methods'=>'POST','permission_callback'=>$perm,'callback'=>function($r){
  $u=$r['url'];$res=wp_remote_get($u,['timeout'=>20,'redirection'=>5,'user-agent'=>'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120 Safari/537.36','headers'=>['Accept-Language'=>'da-DK,da;q=0.9']]);
  if(is_wp_error($res))return ['err'=>$res->get_error_message()];
  $h=wp_remote_retrieve_body($res);$base=$u;$out=[];
  if(preg_match_all('/<img[^>]+>/i',$h,$m))foreach($m[0] as $t){if(stripos($t,'logo')!==false&&preg_match('/\ssrc=["\']([^"\']+)/i',$t,$s))$out[]=['img',$s[1]];}
  if(preg_match_all('/<svg\b.*?<\/svg>/is',$h,$m))foreach($m[0] as $i=>$t){$pre=substr($h,max(0,strpos($h,$t)-300),300);if(stripos($pre.$t,'logo')!==false)$out[]=['svg',strlen($t),$i];}
  if(preg_match('/property=["\']og:image["\'][^>]*content=["\']([^"\']+)/i',$h,$s))$out[]=['og',$s[1]];
  if(preg_match('/rel=["\']apple-touch-icon[^>]*href=["\']([^"\']+)/i',$h,$s))$out[]=['icon',$s[1]];
  return ['code'=>wp_remote_retrieve_response_code($res),'len'=>strlen($h),'c'=>array_slice($out,0,8)];}]);
 register_rest_route('dw/v1','/grab',['methods'=>'POST','permission_callback'=>$perm,'callback'=>function($r){
  $dir=wp_upload_dir()['basedir'].'/dw-logos';wp_mkdir_p($dir);$name=sanitize_file_name($r['name']);
  if(!empty($r['svgfrom'])){$res=wp_remote_get($r['svgfrom'],['timeout'=>20,'user-agent'=>'Mozilla/5.0 Chrome/120']);preg_match_all('/<svg\b.*?<\/svg>/is',wp_remote_retrieve_body($res),$m);$b=$m[0][(int)$r['idx']];if(strpos($b,'xmlns=')===false)$b=preg_replace('/<svg/','<svg xmlns="http://www.w3.org/2000/svg"',$b,1);}
  elseif(!empty($r['data'])){$b=base64_decode($r['data']);}
  else{$res=wp_remote_get($r['url'],['timeout'=>20,'user-agent'=>'Mozilla/5.0 Chrome/120']);$b=wp_remote_retrieve_body($res);}
  if(!$b)return ['err'=>'empty'];file_put_contents($dir.'/'.$name,$b);return ['ok'=>strlen($b),'url'=>wp_upload_dir()['baseurl'].'/dw-logos/'.$name];}]);
});
