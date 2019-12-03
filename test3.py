import re


s = '<span style="font-size:16px;font-family:宋体">诺贝尔物理学奖获得者艾伯特·詹奥吉认为：创新就是和别人看同样的东西却能</span><span ' \
    'style="text-decoration:underline;"><span style="font-size:16px;font-family:\'Calibri\',' \
    'sans-serif">&nbsp;&nbsp;&nbsp; </span></span><span ' \
    'style="font-size:16px;font-family:宋体">不同的事情。</span></p></p></div>  <div data-v-8cf065b0="" class="images-wrap" ' \
    'style="display: none;"></div></div></div> <!----> <div data-v-8cf065b0="" class="subject_node"><div ' \
    'data-v-8cf065b0="" class="nodeLab"><label data-v-8cf065b0="" class="clearfix"><div data-v-8cf065b0="" class="fl ' \
    'ffff" style="padding: 10px 0px;"><input data-v-8cf065b0="" type="radio" class="mr30" value="16742829"> <img ' \
    'data-v-8cf065b0="" src="//image.zhihuishu.com/zhs_yufa_150820/ablecommons/demo/201907' \
    '/e777864488a343b28e258392fd6a28dc.png" class="flagChecked"></div> <span data-v-8cf065b0="" class="mr10 ABCase" ' \
    'style="padding: 10px 0px;">A.</span> <div data-v-8cf065b0="" class="node_detail examquestions-answer fl" ' \
    'style="padding: 10px 0px;"><span style="font-size:16px;font-family:宋体">说出</span></div></label></div><div ' \
    'data-v-8cf065b0="" class="nodeLab"><label data-v-8cf065b0="" class="clearfix"><div data-v-8cf065b0="" class="fl ' \
    'ffff" style="padding: 10px 0px;"><input data-v-8cf065b0="" type="radio" class="mr30" value="16742828"> <img ' \
    'data-v-8cf065b0="" src="//image.zhihuishu.com/zhs_yufa_150820/ablecommons/demo/201907' \
    '/e777864488a343b28e258392fd6a28dc.png" class="flagChecked"></div> <span data-v-8cf065b0="" class="mr10 ABCase" ' \
    'style="padding: 10px 0px;">B.</span> <div data-v-8cf065b0="" class="node_detail examquestions-answer fl" ' \
    'style="padding: 10px 0px;"><span style="font-size:16px;font-family:宋体">做出</span><br></div></label></div><div ' \
    'data-v-8cf065b0="" class="nodeLab"><label data-v-8cf065b0="" class="clearfix"><div data-v-8cf065b0="" class="fl ' \
    'ffff" style="padding: 10px 0px;"><input data-v-8cf065b0="" type="radio" class="mr30" value="16742830"> <img ' \
    'data-v-8cf065b0="" src="//image.zhihuishu.com/zhs_yufa_150820/ablecommons/demo/201907' \
    '/134c9fe76fac4b76ace068fdc8b95f07.png" class="flagChecked"></div> <span data-v-8cf065b0="" class="mr10 ABCase ' \
    'onChecked" style="padding: 10px 0px;">C.</span> <div data-v-8cf065b0="" class="node_detail examquestions-answer ' \
    'fl onChecked" style="padding: 10px 0px;"><span ' \
    'style="font-size:16px;font-family:宋体">想出</span></div></label></div></div></div> <!----> <!----> <!----> <!----> ' \
    '<!----> <!----> <!----></div><div data-v-11c7ae5e=""><div data-v-8cf065b0="" data-v-11c7ae5e="" ' \
    'class="examPaper_subject mt20"><input data-v-8cf065b0="" type="hidden" value="[]"> <input data-v-8cf065b0="" ' \
    'type="hidden" value="false"> <div data-v-8cf065b0="" class="subject_stem clearfix"><div data-v-8cf065b0="" ' \
    'class="subject_type_describe fl"><div data-v-8cf065b0="" class="subject_num fl"><span data-v-8cf065b0="" ' \
    'id="anchor_5097911">2.</span></div> <div data-v-8cf065b0="" class="subject_type_annex"><span data-v-8cf065b0="" ' \
    'class="subject_type"><span data-v-8cf065b0="">【单选题】</span> <span data-v-8cf065b0="">(2分)</span></span></div> ' \
    '<div data-v-8cf065b0="" class="subject_describe"><p data-v-8cf065b0=""><p><span ' \
    'style="font-size:16px;font-family:宋体">用熟悉的眼光看陌生的事物，通过<span ' \
    'style="text-decoration:underline;">&nbsp;&nbsp;&nbsp;&nbsp; </span>来实现创新。</span><br></p></p></div>  <div ' \
    'data-v-8cf065b0="" class="images-wrap" style="display: none;"></div></div></div> <!----> <div data-v-8cf065b0="" ' \
    'class="subject_node"><div data-v-8cf065b0="" class="nodeLab"><label data-v-8cf065b0="" class="clearfix"><div ' \
    'data-v-8cf065b0="" class="fl ffff" style="padding: 10px 0px;"><input data-v-8cf065b0="" type="radio" ' \
    'class="mr30" value="16742840"> <img data-v-8cf065b0="" ' \
    'src="//image.zhihuishu.com/zhs_yufa_150820/ablecommons/demo/201907/e777864488a343b28e258392fd6a28dc.png" ' \
    'class="flagChecked"></div> <span data-v-8cf065b0="" class="mr10 ABCase" style="padding: 10px 0px;">A.</span> ' \
    '<div data-v-8cf065b0="" class="node_detail examquestions-answer fl" style="padding: 10px 0px;"><span ' \
    'style="font-size:16px;font-family:宋体">不放过任何细节 </span></div></label></div><div data-v-8cf065b0="" ' \
    'class="nodeLab"><label data-v-8cf065b0="" class="clearfix"><div data-v-8cf065b0="" class="fl ffff" ' \
    'style="padding: 10px 0px;"><input data-v-8cf065b0="" type="radio" class="mr30" value="16742843"> <img ' \
    'data-v-8cf065b0="" src="//image.zhihuishu.com/zhs_yufa_150820/ablecommons/demo/201907' \
    '/e777864488a343b28e258392fd6a28dc.png" class="flagChecked"></div> <span data-v-8cf065b0="" class="mr10 ABCase" ' \
    'style="padding: 10px 0px;">B.</span> <div data-v-8cf065b0="" class="node_detail examquestions-answer fl" ' \
    'style="padding: 10px 0px;"><span style="font-size:16px;line-height:150%;font-family:宋体">探索、深思</span></div' \
    '></label></div><div data-v-8cf065b0="" class="nodeLab"><label data-v-8cf065b0="" class="clearfix"><div ' \
    'data-v-8cf065b0="" class="fl ffff" style="padding: 10px 0px;"><input data-v-8cf065b0="" type="radio" ' \
    'class="mr30" value="16742841"> <img data-v-8cf065b0="" ' \
    'src="//image.zhihuishu.com/zhs_yufa_150820/ablecommons/demo/201907/e777864488a343b28e258392fd6a28dc.png" ' \
    'class="flagChecked"></div> <span data-v-8cf065b0="" class="mr10 ABCase" style="padding: 10px 0px;">C.</span> ' \
    '<div data-v-8cf065b0="" class="node_detail examquestions-answer fl" style="padding: 10px 0px;"><span ' \
    'style="font-size:16px;font-family:宋体">发现问题</span><br></div></label></div><div data-v-8cf065b0="" ' \
    'class="nodeLab"><label data-v-8cf065b0="" class="clearfix"><div data-v-8cf065b0="" class="fl ffff" ' \
    'style="padding: 10px 0px;"><input data-v-8cf065b0="" type="radio" class="mr30" value="16742842"> <img ' \
    'data-v-8cf065b0="" src="//image.zhihuishu.com/zhs_yufa_150820/ablecommons/demo/201907' \
    '/e777864488a343b28e258392fd6a28dc.png" class="flagChecked"></div> <span data-v-8cf065b0="" class="mr10 ABCase" ' \
    'style="padding: 10px 0px;">D.</span> <div data-v-8cf065b0="" class="node_detail examquestions-answer fl" ' \
    'style="padding: 10px 0px;"><span style="font-size:16px;font-family:宋体">类比、联想 ' \
    '</span><br></div></label></div></div></div> <!----> <!----> <!----> <!----> <!----> <!----> <!----></div><div ' \
    'data-v-11c7ae5e=""><!----> <div data-v-11c7ae5e="" class="examPaper_subject mt20"><input type="hidden" ' \
    'value="false"> <div class="subject_stem clearfix"><div class="subject_type_describe fl"><div class="subject_num ' \
    'fl"><span id="anchor_5097973">3</span></div> <div class="subject_type_annex"><span ' \
    'class="subject_type"><span>【多选题】</span> <span>(2分)</span></span></div> <div class="subject_describe"><p><p ' \
    'style="text-indent: 32px; line-height: 150%;"><span style="font-size:16px;line-height:150%;font-family: ' \
    '宋体">创造力=K×创造性×知识量<sup>2</sup>，创造性等于<span style="text-decoration:underline;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp' \
    ';&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>之和。</span></p></p></div>  <div ' \
    'class="images-wrap" style="display: none;"></div></div></div> <!----> <div class="subject_node"><div ' \
    'class="nodeLab"><label class="clearfix" style="font-size: 14px; color: rgb(42, 42, 42);"><div class="fl" ' \
    'style="padding: 10px 0px;"><input type="checkbox" class="mr30" value="16743074"> <img ' \
    'src="//image.zhihuishu.com/zhs_yufa_150820/ablecommons/demo/201907/39942f89b8454813857cafba124207bd.png" ' \
    'class="flagChecked"> <span class="mr10">A.</span></div> <div class="node_detail examquestions-answer fl" ' \
    'style="padding: 10px 0px;"><span style="font-size:16px;font-family:宋体">创新方法</span></div></label></div><div ' \
    'class="nodeLab"><label class="clearfix" style="font-size: 14px; color: rgb(42, 42, 42);"><div class="fl" ' \
    'style="padding: 10px 0px;"><input type="checkbox" class="mr30" value="16743072"> <img ' \
    'src="//image.zhihuishu.com/zhs_yufa_150820/ablecommons/demo/201907/39942f89b8454813857cafba124207bd.png" ' \
    'class="flagChecked"> <span class="mr10">B.</span></div> <div class="node_detail examquestions-answer fl" ' \
    'style="padding: 10px 0px;"><span style="font-size:16px;font-family:宋体">创造性思维</span> '

rifa = re.findall(r'(<span style="font-size:16px;font-family:\s*?宋体">|'
                  r'<span style="font-size:16px;line-height:150%;font-family:\s*?宋体">)([\u4e00-\u9fa5，：·]{10,100}?)<', s)
for i in rifa:
    print(i[1])
