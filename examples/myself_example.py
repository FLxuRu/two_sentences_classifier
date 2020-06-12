
import sys
import os
import math

CUR_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.abspath(os.path.join(CUR_PATH, '../')))


import pandas as pd
from two_sentences_classifier.word_embeddings import EmbeddingsModel, RelationModelEmbeddings


if __name__ == "__main__":
    model_path = '/nas/lishengping/relation_models/activate_cls_abs_model0531_15'
    # model_path = '/nas/lishengping/two_classifier_models/two_sentences_classifier_model0427'
    model = RelationModelEmbeddings(model_path)

    #     sentences = ['你要去干嘛', '你今天去公司吗', "我想去旅游", "五一都干嘛了", "明天又要上班了", "要去吃饭了", "你喜欢打篮球吗"]

    #     # sentences = [
    #     #     '你要去干嘛||你今天去公司吗', '你今天去公司吗||你今天去公司吗', "我想去旅游||你今天去公司吗", "五一都干嘛了||你今天去公司吗",
    #     #     "明天又要上班了||你今天去公司吗", "要去吃饭了||你今天去公司吗", "你喜欢打篮球吗||你今天去公司吗"
    #     # ]
    #     sentences = sentences
    #     # sentences_mean_vector, sentences_vector_modes = model.embeddings(sentences, split='||')
    #     sentences_mean_vector, sentences_vector_modes = model.embeddings(sentences)

    #     print(f'sentences_mean_vector = {sentences_mean_vector}')
    #     print(f'sentences_vector_modes = {sentences_vector_modes}')

    # sentences = [
    #     '你要去干嘛||你今天去公司吗', '你今天去公司吗||你今天去公司吗', "我想去旅游||你今天去公司吗", "五一都干嘛了||你今天去公司吗",
    #     "明天又要上班了||你今天去公司吗", "要去吃饭了||你今天去公司吗", "你喜欢打篮球吗||你今天去公司吗"
    # ] * 2
    sentences = [
'"那要看你说的话题能不能引起我的兴趣。。如果让我觉得索然无味，和浸泡在温柔乡里完全没有可比性，我可不会答应。""我们聊聊郭小姐。。夫君打算什么时候把TA迎娶过门？"',
#  '"魔剑哪有等到用完了再磨的？。许久没有宠幸，我看看是不是都快长合了。""夫君还是没个正经。"',
 '"嗯！。娶回袁家小姐，我就能把你们也娶进门。到时你可就没有理由不给我碰。""你就这么想碰我？"',
 '"多了个人？。你见了XX？""那个壮汉叫XX？"',
 '"才回来就逼着我学剑，也亏你有这样的精力。。不如坐下喝杯茶，陪我说说话儿再说。""夫君不会是怕苦，不打算去了？"',
 '"怎么都在收拾东西？""大夫人说夫君明天一早就要离开许都，家中上下都在收拾行装，我俩寻思着，XX必定是要追随夫君去淮南，因此下令让TA们把行装收拾妥了。只等夫君一声令下，明天就能开拔。"',
 '"怎么了？。哪里不妥？""公子有没有发觉，TA的杀气很重？。我本来是要去见父亲，却偶然遇见了TA……"',
 '"没有！。XX姐姐说我是个女儿家，不该经常到街市上抛头露脸。""TA是不是少说了一句话？。看来不是TA少说，而是你少学了。。XX是不是说你将来也要嫁给我，既然是XX的儿媳，就不该像街市上的女子一样整天在外面闲走？"',
 '"夫君最近不忙了？""该办的事情已经办的差不多了。。也没什么特别要忙的。"',
 '"只要夫君想学，还有闲暇，我当然会倾囊相授。。不过父亲交代的这套，却是要先学会。""成。。什么时候教我？"',
 '"没有。。我只是想为你分忧……""你上了战场，我才真的担心。。以后我再出征，你们任何人都不许跟着。"',
 '"倒也不是。。姐妹们都能看得出，TA对XX还是有所钟情。""既然有所钟情，怎么又不肯见TA？。难不成TA对我强行促成这桩婚事有些微词？"',
 '"公子的手段我也知道些。。我去问父亲的时候，你已经带着大军离开。""哪能？你看我一脸真诚，怎么可能骗你？"',
 '"我说心里不安稳，公子还强行调戏，哪有半点做夫君的模样？""肯定是你最近心思太多。。这时候想起我是你的夫君来了，到现在为止，我可还没行使过夫君的权利。"']

    sentences = [
        # '"竟然是XX和开明兽。。考，之前的恩怨不是一笔勾销了啊，怎么还来找我的麻烦，当真以为我好欺负啊。""老公，这两头神兽怎么来了？"',
#  '"老婆，你现在今非昔比了，成为神者，就不能呆在翠烟门了，把门主之位让出去，然后跟我在一起吧。""禅让门主，为什么啊？"',
 '"仙颜露的商标被人抢注了，也不知道是哪个孙子在背后故意整蛊我，我施展占卜术，竟然窥视不到对方的任何行踪，看来也是一个高手中的高手。""那我跟你一起去。"',
 '"我刚加入神宗，就跟TA见过一次面，能熟到哪儿去？。好了，不讨论这个了，XX是魅惑术，烟花是风之力，烟水是再生术，那烟月呢？""四月同样是在玉女神功领域造诣高深，但是TA并没有像三水那样领悟这种神奇的再生术，而TA领悟的，倒是跟你的那种神念术非常类似。"',
 '"我这次跟你一同前往，会指出这些药材在什么地方能够采集到，以后仙颜露的供货渠道，就交给翠烟门负责了，没问题吧？""翠烟门是隐居门派，你让门内弟子给你供货？"',
 '"诗诗，你会做饭吗？""呃......我不会。"',
 '"我没有骗你，我是在考虑，如何接受这个残酷而又无奈的现实。""呃......什么意思？"',
 '"更快，""秘术的施展就在于用意念來操控，神者的神力等于就是高手的内力，内力越强，就越厉害，换言之，神力越强，神者就越强大，诗诗，你现在就试着操控神力，"',
#  '"老公，出大事了。""又怎么了？"',
 '"说的有理！""XX的战斗力丝毫不亚于我，如果我没有收服神兽XX，并且不把我的压箱底杀手锏亮出来的话，我都不是XX的对手，TA这样的实力，对付五级高手，一挑五都没问题。有蛊魔蟾的情况下，以一敌十也是绰绰有余，虽然蛊魔蟾被杀，可XX的实力依旧不可小觑，给TA5000人的任务量，根本就不算多。五级高手不多，二级三级四级的却是多的很，遇到那些等级低的，XX一套技能能秒杀一群！"',
 '"......""抗议无效！"',
 '"你......你再敢像今天早上那样强迫我，我就一剑劈死你。""好啊，这才头一天开始，你就计划着谋杀亲夫呢，你这样恶毒的女人，吓得我都不敢要你了。"',
#  '"熔岩兽，难道也是神兽，你们这么多七级巅峰联手对付TA都不行？""熔岩兽是普通灵兽，不是神兽，问题在于TA足足修炼了3万3000年，实力可怕至极。"',
 '"XX已经受过太多的苦难，我不希望TA再受什么苦难，XX，你要好好教导TA，不能让TA走邪路。""那是必须的，我肯定好好【捣】TA。"'
 ]
    sentences_vector_modes, pred_label = model.classifiy(sentences, chunk_nums=5, split='""')
    print(f'pred_label = {pred_label}')
    print(f'sentences_vector_modes = {sentences_vector_modes}')