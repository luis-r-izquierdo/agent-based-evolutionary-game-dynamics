(* Content-type: application/vnd.wolfram.cdf.text *)

(*** Wolfram CDF File ***)
(* http://www.wolfram.com/cdf *)

(* CreatedBy='Mathematica 11.2' *)

(***************************************************************************)
(*                                                                         *)
(*                                                                         *)
(*  Under the Wolfram FreeCDF terms of use, this file and its content are  *)
(*  bound by the Creative Commons BY-SA Attribution-ShareAlike license.    *)
(*                                                                         *)
(*        For additional information concerning CDF licensing, see:        *)
(*                                                                         *)
(*         www.wolfram.com/cdf/adopting-cdf/licensing-options.html         *)
(*                                                                         *)
(*                                                                         *)
(***************************************************************************)

(*CacheID: 234*)
(* Internal cache information:
NotebookFileLineBreakTest
NotebookFileLineBreakTest
NotebookDataPosition[      1088,         20]
NotebookDataLength[     78618,       1701]
NotebookOptionsPosition[     78611,       1690]
NotebookOutlinePosition[     79044,       1707]
CellTagsIndexPosition[     79001,       1704]
WindowFrame->Normal*)

(* Beginning of Notebook Content *)
Notebook[{

Cell[CellGroupData[{
Cell["\<\
The single-sampling \[OpenCurlyDoubleQuote]imitate-if-better\
\[CloseCurlyDoubleQuote] dynamics with 3 strategies\
\>", "Title",
 CellChangeTimes->{{3.517752365493416*^9, 3.5177523895997944`*^9}, {
  3.5177525177231226`*^9, 3.5177525185701714`*^9}, {3.675106345819964*^9, 
  3.675106362557843*^9}, {3.675157602463681*^9, 3.6751576670118923`*^9}, {
  3.675424905497168*^9, 
  3.6754249184968967`*^9}},ExpressionUUID->"45272ac0-d37b-4e10-a13a-\
3a7b69a4cdd3"],

Cell[TextData[{
 "\nBy ",
 Cell[BoxData[
  FormBox[
   ButtonBox[
    RowBox[{"Luis", " ", 
     RowBox[{"R", ".", " ", "Izquierdo"}]}],
    BaseStyle->"Hyperlink",
    ButtonData->{
      URL["http://luis.izqui.org"], None},
    ButtonNote->"http://luis.izqui.org"], TraditionalForm]],ExpressionUUID->
  "60daa6a8-f9c2-449a-9231-1729043d1f47"],
 ", ",
 Cell[BoxData[
  FormBox[
   ButtonBox[
    RowBox[{"Segismundo", " ", 
     RowBox[{"S", ".", " ", "Izquierdo"}]}],
    BaseStyle->"Hyperlink",
    ButtonData->{
      URL["http://www.segis.izqui.org"], None},
    ButtonNote->"http://www.segis.izqui.org"], TraditionalForm]],
  ExpressionUUID->"2918cd11-e5db-4b61-98b4-a8c37d97e6ba"],
 " and ",
 ButtonBox["William H. Sandholm",
  BaseStyle->"Hyperlink",
  ButtonData->{
    URL["http://www.ssc.wisc.edu/~whs/"], None},
  ButtonNote->"http://www.ssc.wisc.edu/~whs/"]
}], "Subtitle",
 CellChangeTimes->{{3.5177524023105216`*^9, 3.5177524217326326`*^9}, {
  3.517752471921503*^9, 3.5177524892894964`*^9}, {3.71775741578417*^9, 
  3.717757415789565*^9}, {3.717757453409417*^9, 
  3.717757538864567*^9}},ExpressionUUID->"92bdfc6c-e106-4622-b712-\
56b7a92269ef"],

Cell[BoxData[Cell[TextData[{
  "This demonstration shows the phase portrait of the single-sampling \
\[OpenCurlyDoubleQuote]Imitate if better\[CloseCurlyDoubleQuote] dynamics \
with 3 strategies for large populations, in the 2-dimensional simplex. \n\n\
Consider a population of agents who, in every time-step, are randomly matched \
in couples for an interaction that can be modelled as a symmetric 3\[Times]3 \
game. The (ordinal) preferences over outcomes for the row agent are \
summarised in the payoff matrix ",
  Cell[BoxData[
   FormBox[
    SubscriptBox["a", "ij"], TraditionalForm]], "InlineMath",ExpressionUUID->
   "9a062b8f-e15c-4429-86cf-c62197fa098a"],
  " where higher numbers denote higher preference. At the end of every \
time-step, one randomly selected agent revises her strategy, and her revision \
rule is as follows: \[OpenCurlyDoubleQuote]I look at another (randomly \
selected) agent; if and only if I prefer her last outcome to my last outcome, \
I adopt her strategy\[CloseCurlyDoubleQuote]. (This is the so-called \
single-sampling \[OpenCurlyDoubleQuote]Imitate if better\
\[CloseCurlyDoubleQuote] rule.) With probability \[Mu] the revising agent \
adopts a random strategy rather than the one prescribed by the previous rule. \
\n\nThe demonstration shows the mean dynamic for the agent-based model \
described above. One unit of time in the mean dynamic corresponds to one \
revision for each agent in the population on average. The program also \
calculates the critical points of the system, and their corresponding \
eigenvalues (which are helpful to assess the dynamic stability of the \
critical point).\n\nThis model is analyzed in detail by Izquierdo and \
Izquierdo, (2013, \[OpenCurlyDoubleQuote]Stochastic approximation to \
understand simple\[NonBreakingSpace]simulation models\[CloseCurlyDoubleQuote] \
",
  StyleBox["Journal of Statistical Physics",
   FontSlant->"Italic"],
  ", ",
  StyleBox["151",
   FontWeight->"Bold"],
  "(1):254\[Dash]276. ",
  ButtonBox["http://dx.doi.org/10.1007/s10955-012-0654-z",
   BaseStyle->"Hyperlink",
   ButtonData->{
     URL["http://dx.doi.org/10.1007/s10955-012-0654-z"], None},
   ButtonNote->"http://dx.doi.org/10.1007/s10955-012-0654-z"],
  ")"
 }], "ManipulateCaption",
  CellChangeTimes->{{3.5177293167771044`*^9, 3.517729329448829*^9}, {
   3.5177298041399803`*^9, 3.517729942883916*^9}, {3.5177299794400063`*^9, 
   3.51773001376897*^9}, {3.517730075818519*^9, 3.517730094328578*^9}, {
   3.5177302522836123`*^9, 3.517730313329104*^9}, {3.517730460187504*^9, 
   3.517730529818486*^9}, {3.5177451453814487`*^9, 3.517745167202697*^9}, {
   3.517746642443076*^9, 3.517746713078116*^9}, {3.517746747979112*^9, 
   3.517746860605554*^9}, {3.5177469113844585`*^9, 3.517746916155731*^9}},
  ExpressionUUID->"ffb72dec-1f62-468f-9a0d-cb1058d4cc0c"]], "Text",
 CellChangeTimes->{{3.5177653878123274`*^9, 3.517765390591486*^9}, {
  3.517765592084011*^9, 3.5177656106060705`*^9}, {3.5178485190824604`*^9, 
  3.5178485190824604`*^9}, {3.5180038880270824`*^9, 3.5180038929253626`*^9}, {
  3.6751575498716087`*^9, 3.675157555076517*^9}, {3.6751576753239193`*^9, 
  3.675157680518661*^9}, {3.675157725771698*^9, 3.675157727587717*^9}, {
  3.675157918064557*^9, 3.675157947192068*^9}, {3.675158193748836*^9, 
  3.675158271669978*^9}, {3.6751583181371183`*^9, 3.675158496184235*^9}, {
  3.67515859153183*^9, 3.675158672902338*^9}, {3.675424653304303*^9, 
  3.675424707015566*^9}, {3.6754247499905863`*^9, 3.675424894963792*^9}, {
  3.675424951650319*^9, 3.6754249611679296`*^9}, {3.717757335430447*^9, 
  3.717757335430501*^9}, {3.7270686639875727`*^9, 3.727068775650284*^9}},
 FontWeight->"Bold",
 Background->GrayLevel[
  1],ExpressionUUID->"ef210b5b-4039-4ea1-90a3-de83d9bd10c3"],

Cell[BoxData[
 TagBox[
  StyleBox[
   DynamicModuleBox[{$CellContext`a11$$ = 2, $CellContext`a12$$ = 
    0, $CellContext`a13$$ = 1, $CellContext`a21$$ = 1, $CellContext`a22$$ = 
    2, $CellContext`a23$$ = 0, $CellContext`a31$$ = 0, $CellContext`a32$$ = 
    1, $CellContext`a33$$ = 2, $CellContext`step$$ = 
    0.125, $CellContext`tMax$$ = 5, $CellContext`update$$ = 
    0, $CellContext`\[Mu]$$ = 0, Typeset`show$$ = True, 
    Typeset`bookmarkList$$ = {
    "\"Rock, Paper, Scissors\"" :> {$CellContext`a11$$ = 
       1, $CellContext`a12$$ = 0, $CellContext`a13$$ = 2, $CellContext`a21$$ = 
       2, $CellContext`a22$$ = 1, $CellContext`a23$$ = 0, $CellContext`a31$$ = 
       0, $CellContext`a32$$ = 2, $CellContext`a33$$ = 
       1, $CellContext`update$$ = 100, $CellContext`\[Mu]$$ = 0.0001}, 
     "\"4 critical points\"" :> {$CellContext`a11$$ = 0, $CellContext`a12$$ = 
       1, $CellContext`a13$$ = 1, $CellContext`a21$$ = 1, $CellContext`a22$$ = 
       1, $CellContext`a23$$ = 1, $CellContext`a31$$ = 1, $CellContext`a32$$ = 
       1, $CellContext`a33$$ = 0, $CellContext`update$$ = 
       110, $CellContext`\[Mu]$$ = 0}, 
     "\"Critical points and regions\"" :> {$CellContext`a11$$ = 
       1, $CellContext`a12$$ = 1, $CellContext`a13$$ = 0, $CellContext`a21$$ = 
       1, $CellContext`a22$$ = 1, $CellContext`a23$$ = 1, $CellContext`a31$$ = 
       0, $CellContext`a32$$ = 1, $CellContext`a33$$ = 
       1, $CellContext`update$$ = 120, $CellContext`\[Mu]$$ = 0}, 
     "\"Internal critical regions\"" :> {$CellContext`a11$$ = 
       0, $CellContext`a12$$ = 1, $CellContext`a13$$ = 0, $CellContext`a21$$ = 
       1, $CellContext`a22$$ = 0, $CellContext`a23$$ = 1, $CellContext`a31$$ = 
       0, $CellContext`a32$$ = 1, $CellContext`a33$$ = 
       0, $CellContext`update$$ = 130, $CellContext`\[Mu]$$ = 0}, 
     "\"Critical regions only\"" :> {$CellContext`a11$$ = 
       2, $CellContext`a12$$ = 0, $CellContext`a13$$ = 2, $CellContext`a21$$ = 
       2, $CellContext`a22$$ = 2, $CellContext`a23$$ = 2, $CellContext`a31$$ = 
       2, $CellContext`a32$$ = 2, $CellContext`a33$$ = 
       2, $CellContext`update$$ = 140, $CellContext`\[Mu]$$ = 0}, 
     "\"All critical\"" :> {$CellContext`a11$$ = 1, $CellContext`a12$$ = 
       1, $CellContext`a13$$ = 1, $CellContext`a21$$ = 1, $CellContext`a22$$ = 
       1, $CellContext`a23$$ = 1, $CellContext`a31$$ = 1, $CellContext`a32$$ = 
       1, $CellContext`a33$$ = 1, $CellContext`update$$ = 
       150, $CellContext`\[Mu]$$ = 0}}, Typeset`bookmarkMode$$ = "Menu", 
    Typeset`animator$$, Typeset`animvar$$ = 1, Typeset`name$$ = 
    "\"untitled\"", Typeset`specs$$ = {{{
       Hold[$CellContext`update$$], 0}, 0, 100}, {{
       Hold[$CellContext`\[Mu]$$], 0.01}, 0, 1, 0.25}, {{
       Hold[$CellContext`tMax$$], 5}, 0, 10, 5}, {{
       Hold[$CellContext`step$$], 0.125}, {0.0625, 0.125, 0.25, 1}}, {{
       Hold[$CellContext`a11$$], 2, 
       "\!\(\*SubscriptBox[\(a\), \(\(1\)\(\[CenterDot]\)\)]\)"}, {0, 1, 2, 3,
       4, 5, 6, 7, 8}}, {{
       Hold[$CellContext`a12$$], 0, ""}, {0, 1, 2, 3, 4, 5, 6, 7, 8}}, {{
       Hold[$CellContext`a13$$], 1, ""}, {0, 1, 2, 3, 4, 5, 6, 7, 8}}, {{
       Hold[$CellContext`a21$$], 1, 
       "\!\(\*SubscriptBox[\(a\), \(\(2\)\(\[CenterDot]\)\)]\)"}, {0, 1, 2, 3,
       4, 5, 6, 7, 8}}, {{
       Hold[$CellContext`a22$$], 2, ""}, {0, 1, 2, 3, 4, 5, 6, 7, 8}}, {{
       Hold[$CellContext`a23$$], 0, ""}, {0, 1, 2, 3, 4, 5, 6, 7, 8}}, {{
       Hold[$CellContext`a31$$], 0, 
       "\!\(\*SubscriptBox[\(a\), \(\(3\)\(\[CenterDot]\)\)]\)"}, {0, 1, 2, 3,
       4, 5, 6, 7, 8}}, {{
       Hold[$CellContext`a32$$], 1, ""}, {0, 1, 2, 3, 4, 5, 6, 7, 8}}, {{
       Hold[$CellContext`a33$$], 2, ""}, {0, 1, 2, 3, 4, 5, 6, 7, 8}}, {
      Hold[
       Grid[{{
          Style["payoffs (\!\(\*SubscriptBox[\(a\), \(ij\)]\))", Bold]}, {
         " ", SpanFromLeft}, {
          Manipulate`Place[1], 
          Manipulate`Place[2], 
          Manipulate`Place[3]}, {
          Manipulate`Place[4], 
          Manipulate`Place[5], 
          Manipulate`Place[6]}, {
          Manipulate`Place[7], 
          Manipulate`Place[8], 
          Manipulate`Place[9]}}, Alignment -> Left, Spacings -> {0, 0}]], 
      Manipulate`Dump`ThisIsNotAControl}, {
      Hold[
       Button["Update", 
        Increment[$CellContext`update$$], ImageSize -> {150, 30}]], 
      Manipulate`Dump`ThisIsNotAControl}, {
      Hold[
       Style["prob. random strategy", Bold]], 
      Manipulate`Dump`ThisIsNotAControl}, {{
       Hold[$CellContext`\[Mu]$$], 0}, 0, 1, 0.001}, {
      Hold[
       Style["trajectories", Bold]], Manipulate`Dump`ThisIsNotAControl}, {{
       Hold[$CellContext`tMax$$], 5, "\!\(\*SubscriptBox[\(t\), \(max\)]\)"}, 
      0, 10, 0.1}, {{
       Hold[$CellContext`step$$], 0.125, "show"}, {
      0.0625 -> "many", 0.125 -> "some", 0.25 -> "few", 1 -> "none"}}}, 
    Typeset`size$$ = {430., {253., 259.}}, Typeset`update$$ = 0, 
    Typeset`initDone$$, Typeset`skipInitDone$$ = 
    False, $CellContext`update$113065$$ = 0, $CellContext`\[Mu]$113066$$ = 
    0, $CellContext`tMax$113067$$ = 0, $CellContext`step$113068$$ = 
    0, $CellContext`a11$113069$$ = 0, $CellContext`a12$113070$$ = 
    0, $CellContext`a13$113071$$ = 0, $CellContext`a21$113072$$ = 
    0, $CellContext`a22$113073$$ = 0, $CellContext`a23$113074$$ = 0}, 
    DynamicBox[Manipulate`ManipulateBoxes[
     2, StandardForm, 
      "Variables" :> {$CellContext`a11$$ = 2, $CellContext`a12$$ = 
        0, $CellContext`a13$$ = 1, $CellContext`a21$$ = 1, $CellContext`a22$$ = 
        2, $CellContext`a23$$ = 0, $CellContext`a31$$ = 0, $CellContext`a32$$ = 
        1, $CellContext`a33$$ = 2, $CellContext`step$$ = 
        0.125, $CellContext`tMax$$ = 5, $CellContext`update$$ = 
        0, $CellContext`\[Mu]$$ = 0}, "ControllerVariables" :> {
        Hold[$CellContext`update$$, $CellContext`update$113065$$, 0], 
        Hold[$CellContext`\[Mu]$$, $CellContext`\[Mu]$113066$$, 0], 
        Hold[$CellContext`tMax$$, $CellContext`tMax$113067$$, 0], 
        Hold[$CellContext`step$$, $CellContext`step$113068$$, 0], 
        Hold[$CellContext`a11$$, $CellContext`a11$113069$$, 0], 
        Hold[$CellContext`a12$$, $CellContext`a12$113070$$, 0], 
        Hold[$CellContext`a13$$, $CellContext`a13$113071$$, 0], 
        Hold[$CellContext`a21$$, $CellContext`a21$113072$$, 0], 
        Hold[$CellContext`a22$$, $CellContext`a22$113073$$, 0], 
        Hold[$CellContext`a23$$, $CellContext`a23$113074$$, 0]}, 
      "OtherVariables" :> {
       Typeset`show$$, Typeset`bookmarkList$$, Typeset`bookmarkMode$$, 
        Typeset`animator$$, Typeset`animvar$$, Typeset`name$$, 
        Typeset`specs$$, Typeset`size$$, Typeset`update$$, Typeset`initDone$$,
         Typeset`skipInitDone$$}, "Body" :> 
      Module[{$CellContext`initialPoints$, $CellContext`A$ = \
{{$CellContext`a11$$, $CellContext`a12$$, $CellContext`a13$$}, \
{$CellContext`a21$$, $CellContext`a22$$, $CellContext`a23$$}, \
{$CellContext`a31$$, $CellContext`a32$$, $CellContext`a33$$}}, \
$CellContext`listOfProjectedTrajectories$, $CellContext`listOfArrows$, \
$CellContext`graphWithTrajectories$, $CellContext`background$, \
$CellContext`critical$, $CellContext`criticalPoints$, \
$CellContext`criticalRegions$, $CellContext`allStrategiesEqual$, \
$CellContext`t$, $CellContext`x$, $CellContext`y$, $CellContext`x1$, \
$CellContext`x2$, $CellContext`x3$}, $CellContext`update$$; \
$CellContext`allStrategiesEqual$ = 
         And[$CellContext`a11$$ == $CellContext`a21$$ == $CellContext`a31$$, \
$CellContext`a12$$ == $CellContext`a22$$ == $CellContext`a32$$, \
$CellContext`a13$$ == $CellContext`a23$$ == $CellContext`a33$$]; \
$CellContext`listOfProjectedTrajectories$ = If[$CellContext`tMax$$ > 0, 
           Flatten[
            Table[
             $CellContext`Simplex2DCoord[
              $CellContext`Trajectory[
               
               N[{$CellContext`initx1, $CellContext`initx2, 
                 
                 1 - $CellContext`initx1 - $CellContext`initx2}], \
$CellContext`A$, $CellContext`\[Mu]$$, \
$CellContext`tMax$$][$CellContext`t$]], {$CellContext`initx1, 0, 
              1, $CellContext`step$$}, {$CellContext`initx2, 0, 
              1 - $CellContext`initx1, $CellContext`step$$}], 1], 
           (SlotSequence[1]& )[]]; $CellContext`listOfArrows$ = 
         If[$CellContext`tMax$$ >= 0.1, 
           Flatten[
            Map[Table[{
               Arrowheads[0.03], 
               Arrow[{
                 ReplaceAll[#, $CellContext`t$ -> $CellContext`i], 
                 
                 ReplaceAll[#, $CellContext`t$ -> $CellContext`i + 
                   0.1]}]}, {$CellContext`i, 0.2, $CellContext`tMax$$ - 0.1, 
               3}]& , $CellContext`listOfProjectedTrajectories$], 1], 
           (SlotSequence[1]& )[]]; $CellContext`graphWithTrajectories$ = 
         If[$CellContext`tMax$$ > 0, 
           ParametricPlot[
            
            Evaluate[$CellContext`listOfProjectedTrajectories$], \
{$CellContext`t$, 0, $CellContext`tMax$$}, PlotStyle -> Black], 
           (SlotSequence[1]& )[]]; $CellContext`background$ = DensityPlot[
           Norm[
            $CellContext`Simplex2DCoord[
             $CellContext`ExpectedChange[
              $CellContext`Simplex2DInverseCoord[{$CellContext`y1, \
$CellContext`y2}], $CellContext`A$, $CellContext`\[Mu]$$]]], {$CellContext`y1,
             0, 1}, {$CellContext`y2, 0, Sqrt[3]/2}, ImageSize -> {400, 275}, 
           ColorFunction -> "Rainbow", RegionFunction -> 
           Function[{$CellContext`y1, $CellContext`y2, $CellContext`z}, 
             
             And[$CellContext`y2 < Sqrt[3] $CellContext`y1, $CellContext`y2 < 
              Sqrt[3] (1 - $CellContext`y1)]], BoundaryStyle -> 
           Directive[Black, Thick], Frame -> False, AspectRatio -> Sqrt[3]/2, 
           PlotRange -> {{-0.1, 1 + 0.1}, {-0.1, Sqrt[3]/2 + 
              0.1}}]; $CellContext`critical$ = 
         Reduce[{$CellContext`ExpectedChange[{$CellContext`x1$, \
$CellContext`x2$, $CellContext`x3$}, $CellContext`A$, 
              Rationalize[$CellContext`\[Mu]$$]] == 0, 0 <= $CellContext`x1$ <= 
            1, 0 <= $CellContext`x2$ <= 1, 0 <= $CellContext`x3$ <= 
            1, $CellContext`x1$ + $CellContext`x2$ + $CellContext`x3$ == 
            1}, {$CellContext`x1$, $CellContext`x2$, $CellContext`x3$}, Reals,
            Backsubstitution -> True]; $CellContext`criticalPoints$ = Select[{
            ToRules[$CellContext`critical$]}, 
           ListQ]; $CellContext`criticalRegions$ = Map[Apply[List, #]& , 
           Select[{
             ToRules[$CellContext`critical$]}, Not[
             ListQ[#]]& ]]; Pane[
          Column[{
            
            Show[{$CellContext`background$, \
$CellContext`graphWithTrajectories$, 
              Graphics[$CellContext`listOfArrows$], 
              If[$CellContext`criticalPoints$ != {}, 
               Graphics[{
                 EdgeForm[Thick], Red, 
                 Map[Disk[
                   $CellContext`Simplex2DCoord[#], 0.03]& , 
                  N[
                   
                   ReplaceAll[{$CellContext`x1$, $CellContext`x2$, \
$CellContext`x3$}, $CellContext`criticalPoints$]]]}], 
               (SlotSequence[1]& )[]], 
              If[
               And[$CellContext`criticalRegions$ != {}, 
                Not[$CellContext`allStrategiesEqual$]], 
               Map[Plot[
                 ReplaceAll[$CellContext`y$, #], {$CellContext`x$, 0, 1}, 
                 PlotStyle -> Directive[Red, 
                   Thickness[0.01]]]& , 
                Flatten[
                 Map[Solve[#, $CellContext`y$, Reals]& , 
                  
                  ReplaceAll[$CellContext`criticalRegions$, {$CellContext`x1$ -> 
                    2 ($CellContext`y$/Sqrt[3]), $CellContext`x2$ -> 
                    1 - $CellContext`x$ - $CellContext`y$/Sqrt[
                    3], $CellContext`x3$ -> $CellContext`x$ - $CellContext`y$/
                    Sqrt[3]}]]]], 
               (SlotSequence[1]& )[]], 
              Graphics[{
                Inset[
                 Style["\!\(\*SubscriptBox[\(x\), \(1\)]\) = 1", 18, Bold], {
                 0.65, 0.9}], 
                Inset[
                 Style["\!\(\*SubscriptBox[\(x\), \(2\)]\) = 1", 18, Bold], {
                 0, -0.06}], 
                Inset[
                 Style["\!\(\*SubscriptBox[\(x\), \(3\)]\) = 1", 18, Bold], {
                 1, -0.06}]}]}, 
             PlotRange -> {{-0.1, 1 + 0.1}, {-0.1, Sqrt[3]/2 + 0.1}}, Frame -> 
             False, Axes -> False], 
            If[$CellContext`criticalPoints$ != {}, 
             Column[{
               Text[
                Style["critical points", Red, Bold, 12]], 
               Text[
                Row[{
                  TableForm[
                   N[
                    
                    ReplaceRepeated[{$CellContext`x1$, $CellContext`x2$, \
$CellContext`x3$}, $CellContext`criticalPoints$], 3], TableHeadings -> {None, {
                    Style[
                    Subscript[
                    Style["x", Italic], 1], 12], 
                    Style[
                    Subscript[
                    Style["x", Italic], 2], 12], 
                    Style[
                    Subscript[
                    Style["x", Italic], 3], 12]}}, TableSpacing -> {1, 1}, 
                   TableAlignments -> {Left, Bottom}], 
                  TableForm[
                   Chop[
                    Map[Eigenvalues[
                    $CellContext`Jacob[#, $CellContext`A$, \
$CellContext`\[Mu]$$]]& , 
                    N[
                    
                    ReplaceRepeated[{$CellContext`x1$, $CellContext`x2$}, \
$CellContext`criticalPoints$], 3]]], TableHeadings -> {None, {
                    Style[
                    "\!\(\*SubscriptBox[\(\[Lambda]\), \(1\)]\)", Bold, 12], 
                    Style[
                    "\!\(\*SubscriptBox[\(\[Lambda]\), \(2\)]\)", Bold, 12]}},
                    TableSpacing -> {1, 1}, 
                   TableAlignments -> {Right, Bottom}]}, "   "], 
                BaseStyle -> {12}]}, Alignment -> Center, Spacings -> 1, 
              Frame -> True]], 
            If[$CellContext`criticalRegions$ != {}, 
             Column[{
               Text[
                Style["critical regions", Red, Bold, 12]], 
               Text[
                Row[{
                  TableForm[
                   
                   ReplaceAll[$CellContext`criticalRegions$, \
{$CellContext`x1$ -> Text[
                    Subscript[
                    Style["x", Italic], 1]], $CellContext`x2$ -> Text[
                    Subscript[
                    Style["x", Italic], 2]], $CellContext`x3$ -> Text[
                    Subscript[
                    Style["x", Italic], 3]]}], TableSpacing -> {1, 1}, 
                   TableAlignments -> {Left, Bottom}]}], BaseStyle -> {12}]}, 
              Alignment -> Center, Spacings -> 1, Frame -> True]]}, {
           Center, Top}], ImageSize -> {430, 512}]], 
      "Specifications" :> {{{$CellContext`update$$, 0}, 0, 100, ControlType -> 
         None}, {{$CellContext`\[Mu]$$, 0.01}, 0, 1, 0.25, ControlType -> 
         None}, {{$CellContext`tMax$$, 5}, 0, 10, 5, ControlType -> 
         None}, {{$CellContext`step$$, 0.125}, {0.0625, 0.125, 0.25, 1}, 
         ControlType -> 
         None}, {{$CellContext`a11$$, 2, 
          "\!\(\*SubscriptBox[\(a\), \(\(1\)\(\[CenterDot]\)\)]\)"}, {0, 1, 2,
          3, 4, 5, 6, 7, 8}, ControlType -> PopupMenu, ImageSize -> {43, 19}, 
         ControlPlacement -> 1}, {{$CellContext`a12$$, 0, ""}, {0, 1, 2, 3, 4,
          5, 6, 7, 8}, ControlType -> PopupMenu, ImageSize -> {43, 19}, 
         ControlPlacement -> 2}, {{$CellContext`a13$$, 1, ""}, {0, 1, 2, 3, 4,
          5, 6, 7, 8}, ControlType -> PopupMenu, ImageSize -> {43, 19}, 
         ControlPlacement -> 
         3}, {{$CellContext`a21$$, 1, 
          "\!\(\*SubscriptBox[\(a\), \(\(2\)\(\[CenterDot]\)\)]\)"}, {0, 1, 2,
          3, 4, 5, 6, 7, 8}, ControlType -> PopupMenu, ImageSize -> {43, 19}, 
         ControlPlacement -> 4}, {{$CellContext`a22$$, 2, ""}, {0, 1, 2, 3, 4,
          5, 6, 7, 8}, ControlType -> PopupMenu, ImageSize -> {43, 19}, 
         ControlPlacement -> 5}, {{$CellContext`a23$$, 0, ""}, {0, 1, 2, 3, 4,
          5, 6, 7, 8}, ControlType -> PopupMenu, ImageSize -> {43, 19}, 
         ControlPlacement -> 
         6}, {{$CellContext`a31$$, 0, 
          "\!\(\*SubscriptBox[\(a\), \(\(3\)\(\[CenterDot]\)\)]\)"}, {0, 1, 2,
          3, 4, 5, 6, 7, 8}, ControlType -> PopupMenu, ImageSize -> {43, 19}, 
         ControlPlacement -> 7}, {{$CellContext`a32$$, 1, ""}, {0, 1, 2, 3, 4,
          5, 6, 7, 8}, ControlType -> PopupMenu, ImageSize -> {43, 19}, 
         ControlPlacement -> 8}, {{$CellContext`a33$$, 2, ""}, {0, 1, 2, 3, 4,
          5, 6, 7, 8}, ControlType -> PopupMenu, ImageSize -> {43, 19}, 
         ControlPlacement -> 9}, 
        Grid[{{
           Style["payoffs (\!\(\*SubscriptBox[\(a\), \(ij\)]\))", Bold]}, {
          " ", SpanFromLeft}, {
           Manipulate`Place[1], 
           Manipulate`Place[2], 
           Manipulate`Place[3]}, {
           Manipulate`Place[4], 
           Manipulate`Place[5], 
           Manipulate`Place[6]}, {
           Manipulate`Place[7], 
           Manipulate`Place[8], 
           Manipulate`Place[9]}}, Alignment -> Left, Spacings -> {0, 0}], 
        Delimiter, 
        Button["Update", 
         Increment[$CellContext`update$$], ImageSize -> {150, 30}], Delimiter, 
        Style[
        "prob. random strategy", Bold], {{$CellContext`\[Mu]$$, 0}, 0, 1, 
         0.001, ImageSize -> Small, Appearance -> "Labeled"}, Delimiter, 
        Style[
        "trajectories", 
         Bold], {{$CellContext`tMax$$, 5, 
          "\!\(\*SubscriptBox[\(t\), \(max\)]\)"}, 0, 10, 0.1, ImageSize -> 
         Small, Appearance -> 
         "Labeled"}, {{$CellContext`step$$, 0.125, "show"}, {
         0.0625 -> "many", 0.125 -> "some", 0.25 -> "few", 1 -> "none"}}, 
        Delimiter}, 
      "Options" :> {
       SynchronousUpdating -> False, Alignment -> {Center, Top}, 
        ControlPlacement -> Left, 
        TrackedSymbols :> {$CellContext`\[Mu]$$, $CellContext`update$$, \
$CellContext`tMax$$, $CellContext`step$$}, 
        AutorunSequencing -> {{2, 10}, {3, 10}, {4, 10}}, ControlPlacement -> 
        Left, ContinuousAction -> False}, "DefaultOptions" :> {}],
     ImageSizeCache->{654., {283., 289.}},
     SingleEvaluation->True],
    Deinitialization:>None,
    DynamicModuleValues:>{},
    Initialization:>({$CellContext`Simplex2DCoord[{
          Pattern[$CellContext`x1, 
           Blank[]], 
          Pattern[$CellContext`x2, 
           Blank[]], 
          Pattern[$CellContext`x3, 
           Blank[]]}] := $CellContext`x2 {0, 0} + $CellContext`x3 {1, 
          0} + $CellContext`x1 {1/2, Sqrt[3]/2}, $CellContext`Trajectory[
         Pattern[$CellContext`initialPoint, 
          Blank[List]], 
         Pattern[$CellContext`A, 
          Blank[]], 
         Pattern[$CellContext`m, 
          Blank[]], 
         Pattern[$CellContext`time, 
          Blank[]]] := Module[{$CellContext`x}, 
         NDSolveValue[{
          Derivative[
            1][$CellContext`x][$CellContext`t] == $CellContext`ExpectedChange[
             $CellContext`x[$CellContext`t], $CellContext`A, $CellContext`m], \
$CellContext`x[
            0] == $CellContext`initialPoint}, $CellContext`x, {$CellContext`t,
            0, $CellContext`time}]], 
       Attributes[Derivative] = {
        NHoldAll, ReadProtected}, $CellContext`ExpectedChange[
         Pattern[$CellContext`x, 
          Blank[]], 
         Pattern[$CellContext`A, 
          Blank[]], 
         Pattern[$CellContext`m, 
          Blank[]]] := ((1 - $CellContext`m) $CellContext`x) Dot[
           Map[Dot[$CellContext`x, 
             Dot[
              Sign[
              ConstantArray[#, {3, 
                 3}] - $CellContext`A], $CellContext`x]]& , $CellContext`A, {
            2}], $CellContext`x] + $CellContext`m (
          ConstantArray[
           1/3, 3] - $CellContext`x), $CellContext`Simplex2DInverseCoord[{
          Pattern[$CellContext`y1, 
           Blank[]], 
          Pattern[$CellContext`y2, 
           Blank[]]}] := {0, 1, 
         0} + $CellContext`y1 {0, -1, 1} + $CellContext`y2 {
          2/Sqrt[3], (-1)/Sqrt[3], (-1)/Sqrt[3]}, 
       Attributes[PlotRange] = {ReadProtected}, 
       Attributes[Subscript] = {NHoldRest}, 
       Subscript[Notebook$$32$16559`w, 1] = CompressedData["
1:eJxTTMoPSmVhYGDgAmIQzQzFxmBw2R5CP7afNRMEdtqPio+Kj4qPio+Kj4qP
io+Kj4qPio+KY4oDAHflTEY=
        "], Subscript[Notebook$$32$16559`w, 2] = 6, $CellContext`Jacob[{
          Pattern[$CellContext`x, 
           Blank[]], 
          Pattern[$CellContext`y, 
           Blank[]]}, 
         Pattern[$CellContext`A, 
          Blank[]], 
         Pattern[$CellContext`m, 
          Blank[]]] := Module[{$CellContext`x1, $CellContext`x2}, 
         ReplaceAll[
          Evaluate[
           D[
            Most[
             $CellContext`ExpectedChange[{$CellContext`x1, $CellContext`x2, 
               1 - $CellContext`x1 - $CellContext`x2}, $CellContext`A, \
$CellContext`m]], {{$CellContext`x1, $CellContext`x2}}]], {$CellContext`x1 -> \
$CellContext`x, $CellContext`x2 -> $CellContext`y}]]}; 
     Typeset`initDone$$ = True),
    SynchronousInitialization->True,
    UndoTrackedVariables:>{Typeset`show$$, Typeset`bookmarkMode$$},
    UnsavedVariables:>{Typeset`initDone$$},
    UntrackedVariables:>{Typeset`size$$}], "Manipulate",
   Deployed->True,
   StripOnInput->False],
  Manipulate`InterpretManipulate[1]]], "Output",
 CellChangeTimes->{3.729017855381763*^9},
 TextAlignment->Center,ExpressionUUID->"537cfb0a-1760-4baa-bef5-99181f3acf58"],

Cell[CellGroupData[{

Cell["Source code", "Section",
 CellChangeTimes->{{3.5177649723305626`*^9, 
  3.5177649882424726`*^9}},ExpressionUUID->"bba0367a-42e5-4757-932d-\
7512a71f9565"],

Cell[BoxData[{
 RowBox[{
  RowBox[{
   RowBox[{"Clear", "[", "\"\<Global`*\>\"", "]"}], ";"}], 
  "\[IndentingNewLine]"}], "\[IndentingNewLine]", 
 RowBox[{
  RowBox[{
   RowBox[{"Simplex2DCoord", "[", 
    RowBox[{"{", 
     RowBox[{"x1_", ",", " ", "x2_", ",", " ", "x3_"}], "}"}], "]"}], " ", ":=", 
   RowBox[{
    RowBox[{"x2", "*", 
     RowBox[{"{", 
      RowBox[{"0", ",", " ", "0"}], "}"}]}], " ", "+", " ", 
    RowBox[{"x3", "*", 
     RowBox[{"{", 
      RowBox[{"1", ",", " ", "0"}], "}"}]}], " ", "+", " ", 
    RowBox[{"x1", "*", 
     RowBox[{"{", 
      RowBox[{
       RowBox[{"1", "/", "2"}], ",", " ", 
       RowBox[{
        SqrtBox["3"], "/", "2"}]}], "}"}]}]}]}], ";"}], "\[IndentingNewLine]", 
 RowBox[{
  RowBox[{
   RowBox[{
    RowBox[{"Simplex2DInverseCoord", "[", 
     RowBox[{"{", 
      RowBox[{"y1_", ",", "y2_"}], "}"}], "]"}], ":=", 
    RowBox[{
     RowBox[{"{", 
      RowBox[{"0", ",", "1", ",", "0"}], "}"}], "+", 
     RowBox[{"y1", "*", 
      RowBox[{"{", 
       RowBox[{"0", ",", 
        RowBox[{"-", "1"}], ",", "1"}], "}"}]}], "+", 
     RowBox[{"y2", "*", 
      RowBox[{"{", 
       RowBox[{
        RowBox[{"2", "/", 
         SqrtBox["3"]}], ",", 
        RowBox[{
         RowBox[{"-", "1"}], "/", 
         SqrtBox["3"]}], ",", 
        RowBox[{
         RowBox[{"-", "1"}], "/", 
         SqrtBox["3"]}]}], "}"}]}]}]}], ";"}], 
  "\[IndentingNewLine]"}], "\[IndentingNewLine]", 
 RowBox[{
  RowBox[{
   RowBox[{
    RowBox[{"ExpectedChange", "[", 
     RowBox[{"x_", ",", "A_", ",", "m_"}], "]"}], ":=", 
    RowBox[{
     RowBox[{
      RowBox[{"(", 
       RowBox[{"1", "-", "m"}], ")"}], "*", "x", "*", 
      RowBox[{
       RowBox[{"Map", "[", 
        RowBox[{
         RowBox[{
          RowBox[{"x", ".", 
           RowBox[{"(", 
            RowBox[{
             RowBox[{"Sign", "[", 
              RowBox[{
               RowBox[{"ConstantArray", "[", 
                RowBox[{"#", ",", 
                 RowBox[{"{", 
                  RowBox[{"3", ",", "3"}], "}"}]}], "]"}], "-", "A"}], "]"}], 
             ".", "x"}], ")"}]}], "&"}], ",", "A", ",", 
         RowBox[{"{", "2", "}"}]}], "]"}], ".", "x"}]}], "+", 
     RowBox[{"m", 
      RowBox[{"(", 
       RowBox[{
        RowBox[{"ConstantArray", "[", 
         RowBox[{
          RowBox[{"1", "/", "3"}], ",", "3"}], "]"}], "-", "x"}], ")"}]}]}]}],
    ";"}], "\[IndentingNewLine]"}], "\[IndentingNewLine]", 
 RowBox[{
  RowBox[{
   RowBox[{
    RowBox[{"Jacob", "[", 
     RowBox[{
      RowBox[{"{", 
       RowBox[{"x_", ",", "y_"}], "}"}], ",", "A_", ",", "m_"}], "]"}], ":=", 
    RowBox[{"Module", "[", 
     RowBox[{
      RowBox[{"{", 
       RowBox[{"x1", ",", "x2"}], "}"}], ",", 
      RowBox[{
       RowBox[{"(", 
        RowBox[{"Evaluate", "[", 
         RowBox[{"D", "[", 
          RowBox[{
           RowBox[{"Most", "[", 
            RowBox[{"ExpectedChange", "[", 
             RowBox[{
              RowBox[{"{", 
               RowBox[{"x1", ",", "x2", ",", 
                RowBox[{"1", "-", "x1", "-", "x2"}]}], "}"}], ",", "A", ",", 
              "m"}], "]"}], "]"}], ",", 
           RowBox[{"{", 
            RowBox[{"{", 
             RowBox[{"x1", ",", "x2"}], "}"}], "}"}]}], "]"}], "]"}], ")"}], "/.", 
       RowBox[{"{", 
        RowBox[{
         RowBox[{"x1", "->", "x"}], ",", 
         RowBox[{"x2", "->", "y"}]}], "}"}]}]}], "]"}]}], ";"}], 
  "\[IndentingNewLine]"}], "\[IndentingNewLine]", 
 RowBox[{
  RowBox[{
   RowBox[{
    RowBox[{"Trajectory", "[", 
     RowBox[{"initialPoint_List", ",", "A_", ",", "m_", ",", "time_"}], "]"}],
     ":=", 
    RowBox[{"Module", "[", 
     RowBox[{
      RowBox[{"{", "x", "}"}], ",", "\[IndentingNewLine]", 
      RowBox[{"NDSolveValue", "[", "\[IndentingNewLine]", 
       RowBox[{
        RowBox[{"{", 
         RowBox[{
          RowBox[{
           RowBox[{
            RowBox[{"x", "'"}], "[", "t", "]"}], "\[Equal]", 
           RowBox[{"ExpectedChange", "[", 
            RowBox[{
             RowBox[{"x", "[", "t", "]"}], ",", "A", ",", "m"}], "]"}]}], ",", 
          RowBox[{
           RowBox[{"x", "[", "0", "]"}], "==", "initialPoint"}]}], "}"}], ",",
         "\[IndentingNewLine]", "x", ",", 
        RowBox[{"{", 
         RowBox[{"t", ",", "0", ",", "time"}], "}"}]}], "]"}]}], 
     "\[IndentingNewLine]", "]"}]}], ";"}], "\[IndentingNewLine]", 
  "\[IndentingNewLine]"}], "\[IndentingNewLine]", 
 RowBox[{"Manipulate", "[", 
  RowBox[{
   RowBox[{"Module", "[", 
    RowBox[{
     RowBox[{"{", "\[IndentingNewLine]", 
      RowBox[{"initialPoints", ",", "\[IndentingNewLine]", 
       RowBox[{"A", "=", 
        RowBox[{"{", 
         RowBox[{
          RowBox[{"{", 
           RowBox[{"a11", ",", "a12", ",", "a13"}], "}"}], ",", 
          RowBox[{"{", 
           RowBox[{"a21", ",", "a22", ",", "a23"}], "}"}], ",", 
          RowBox[{"{", 
           RowBox[{"a31", ",", "a32", ",", "a33"}], "}"}]}], "}"}]}], ",", 
       "listOfProjectedTrajectories", ",", "listOfArrows", ",", 
       "graphWithTrajectories", ",", "background", ",", "critical", ",", 
       "criticalPoints", ",", "criticalRegions", ",", "allStrategiesEqual", 
       ",", "t", ",", "x", ",", "y", ",", "x1", ",", "x2", ",", "x3"}], 
      "\[IndentingNewLine]", "}"}], ",", "\[IndentingNewLine]", 
     "\[IndentingNewLine]", 
     RowBox[{"update", ";", "\[IndentingNewLine]", "\[IndentingNewLine]", 
      RowBox[{"allStrategiesEqual", "=", 
       RowBox[{"And", "[", 
        RowBox[{
         RowBox[{"a11", "\[Equal]", "a21", "==", "a31"}], ",", 
         RowBox[{"a12", "==", "a22", "==", "a32"}], ",", 
         RowBox[{"a13", "==", "a23", "==", "a33"}]}], "]"}]}], ";", 
      "\[IndentingNewLine]", "\[IndentingNewLine]", 
      RowBox[{"listOfProjectedTrajectories", "=", 
       RowBox[{"If", "[", 
        RowBox[{
         RowBox[{"tMax", ">", "0"}], ",", 
         RowBox[{"Flatten", "[", 
          RowBox[{
           RowBox[{"Table", "[", 
            RowBox[{
             RowBox[{"Simplex2DCoord", "[", 
              RowBox[{
               RowBox[{"Trajectory", "[", 
                RowBox[{
                 RowBox[{"N", "[", 
                  RowBox[{"{", 
                   RowBox[{"initx1", ",", "initx2", ",", 
                    RowBox[{"1", "-", "initx1", "-", "initx2"}]}], "}"}], 
                  "]"}], ",", "A", ",", "\[Mu]", ",", "tMax"}], "]"}], "[", 
               "t", "]"}], "]"}], ",", 
             RowBox[{"{", 
              RowBox[{"initx1", ",", "0", ",", "1", ",", "step"}], "}"}], ",", 
             RowBox[{"{", 
              RowBox[{"initx2", ",", "0", ",", 
               RowBox[{"1", "-", "initx1"}], ",", "step"}], "}"}]}], "]"}], 
           ",", "1"}], "]"}], ",", 
         RowBox[{
          RowBox[{"##", "&"}], "[", "]"}]}], "]"}]}], ";", 
      "\[IndentingNewLine]", "\[IndentingNewLine]", 
      RowBox[{"listOfArrows", "=", 
       RowBox[{"If", "[", 
        RowBox[{
         RowBox[{"tMax", "\[GreaterEqual]", "0.1"}], ",", 
         RowBox[{"Flatten", "[", 
          RowBox[{
           RowBox[{"Map", "[", 
            RowBox[{
             RowBox[{
              RowBox[{"Table", "[", 
               RowBox[{
                RowBox[{"{", 
                 RowBox[{
                  RowBox[{"Arrowheads", "[", "0.03", "]"}], ",", 
                  RowBox[{"Arrow", "[", 
                   RowBox[{"{", 
                    RowBox[{
                    RowBox[{"#", "/.", 
                    RowBox[{"t", "->", "i"}]}], ",", 
                    RowBox[{"#", "/.", 
                    RowBox[{"t", "->", 
                    RowBox[{"(", 
                    RowBox[{"i", "+", "0.1"}], ")"}]}]}]}], "}"}], "]"}]}], 
                 "}"}], ",", 
                RowBox[{"{", 
                 RowBox[{"i", ",", "0.2", ",", 
                  RowBox[{"tMax", "-", "0.1"}], ",", "3"}], "}"}]}], "]"}], 
              "&"}], ",", "listOfProjectedTrajectories"}], "]"}], ",", "1"}], 
          "]"}], ",", 
         RowBox[{
          RowBox[{"##", "&"}], "[", "]"}]}], "]"}]}], ";", 
      "\[IndentingNewLine]", "\[IndentingNewLine]", 
      RowBox[{"graphWithTrajectories", "=", 
       RowBox[{"If", "[", 
        RowBox[{
         RowBox[{"tMax", ">", "0"}], ",", 
         RowBox[{"ParametricPlot", "[", 
          RowBox[{
           RowBox[{"Evaluate", "[", "listOfProjectedTrajectories", "]"}], ",", 
           RowBox[{"{", 
            RowBox[{"t", ",", "0", ",", "tMax"}], "}"}], ",", 
           RowBox[{"PlotStyle", "->", "Black"}]}], "]"}], ",", 
         RowBox[{
          RowBox[{"##", "&"}], "[", "]"}]}], "]"}]}], ";", 
      "\[IndentingNewLine]", 
      RowBox[{"background", "=", 
       RowBox[{"DensityPlot", "[", 
        RowBox[{
         RowBox[{"Norm", "[", 
          RowBox[{"Simplex2DCoord", "[", 
           RowBox[{"ExpectedChange", "[", 
            RowBox[{
             RowBox[{"Simplex2DInverseCoord", "[", 
              RowBox[{"{", 
               RowBox[{"y1", ",", "y2"}], "}"}], "]"}], ",", "A", ",", 
             "\[Mu]"}], "]"}], "]"}], "]"}], ",", 
         RowBox[{"{", 
          RowBox[{"y1", ",", "0", ",", "1"}], "}"}], ",", 
         RowBox[{"{", 
          RowBox[{"y2", ",", "0", ",", 
           FractionBox[
            SqrtBox["3"], "2"]}], "}"}], ",", 
         RowBox[{"ImageSize", "\[Rule]", 
          RowBox[{"{", 
           RowBox[{"400", ",", "275"}], "}"}]}], ",", 
         RowBox[{"ColorFunction", "\[Rule]", "\"\<Rainbow\>\""}], ",", 
         RowBox[{"RegionFunction", "->", 
          RowBox[{"Function", "[", 
           RowBox[{
            RowBox[{"{", 
             RowBox[{"y1", ",", "y2", ",", "z"}], "}"}], ",", 
            RowBox[{
             RowBox[{"y2", "<", 
              RowBox[{
               SqrtBox["3"], "y1"}]}], "&&", 
             RowBox[{"y2", "<", 
              RowBox[{
               SqrtBox["3"], 
               RowBox[{"(", 
                RowBox[{"1", "-", "y1"}], ")"}]}]}]}]}], "]"}]}], ",", 
         RowBox[{"BoundaryStyle", "->", 
          RowBox[{"Directive", "[", 
           RowBox[{"Black", ",", "Thick"}], "]"}]}], ",", 
         RowBox[{"Frame", "->", "False"}], ",", 
         RowBox[{"AspectRatio", "->", 
          FractionBox[
           SqrtBox["3"], "2"]}], ",", 
         RowBox[{"PlotRange", "->", 
          RowBox[{"{", 
           RowBox[{
            RowBox[{"{", 
             RowBox[{
              RowBox[{"-", "0.1"}], ",", 
              RowBox[{"1", "+", "0.1"}]}], "}"}], ",", 
            RowBox[{"{", 
             RowBox[{
              RowBox[{"-", "0.1"}], ",", 
              RowBox[{
               FractionBox[
                SqrtBox["3"], "2"], "+", "0.1"}]}], "}"}]}], "}"}]}]}], 
        "]"}]}], ";", "\[IndentingNewLine]", "\[IndentingNewLine]", 
      RowBox[{"critical", "=", 
       RowBox[{"Reduce", "[", 
        RowBox[{
         RowBox[{"{", 
          RowBox[{
           RowBox[{
            RowBox[{"ExpectedChange", "[", 
             RowBox[{
              RowBox[{"{", 
               RowBox[{"x1", ",", "x2", ",", "x3"}], "}"}], ",", "A", ",", 
              RowBox[{"Rationalize", "[", "\[Mu]", "]"}]}], "]"}], "==", 
            "0"}], ",", 
           RowBox[{"0", "<=", "x1", "<=", "1"}], ",", 
           RowBox[{"0", "<=", "x2", "<=", "1"}], ",", 
           RowBox[{"0", "<=", "x3", "<=", "1"}], ",", 
           RowBox[{
            RowBox[{"x1", "+", "x2", "+", "x3"}], "==", "1"}]}], "}"}], ",", 
         RowBox[{"{", 
          RowBox[{"x1", ",", "x2", ",", "x3"}], "}"}], ",", "Reals", ",", 
         RowBox[{"Backsubstitution", "->", "True"}]}], "]"}]}], ";", 
      "\[IndentingNewLine]", 
      RowBox[{"criticalPoints", "=", 
       RowBox[{"Select", "[", 
        RowBox[{
         RowBox[{"List", "[", 
          RowBox[{"ToRules", "[", "critical", "]"}], "]"}], ",", "ListQ"}], 
        "]"}]}], ";", "\[IndentingNewLine]", 
      RowBox[{"criticalRegions", "=", 
       RowBox[{"Map", "[", 
        RowBox[{
         RowBox[{
          RowBox[{"Apply", "[", 
           RowBox[{"List", ",", "#"}], "]"}], "&"}], ",", 
         RowBox[{"Select", "[", 
          RowBox[{
           RowBox[{"List", "[", 
            RowBox[{"ToRules", "[", "critical", "]"}], "]"}], ",", 
           RowBox[{
            RowBox[{"Not", "[", 
             RowBox[{"ListQ", "[", "#", "]"}], "]"}], "&"}]}], "]"}]}], 
        "]"}]}], ";", "\[IndentingNewLine]", "\[IndentingNewLine]", 
      RowBox[{"Pane", "[", 
       RowBox[{
        RowBox[{"Column", "[", 
         RowBox[{
          RowBox[{"{", "\[IndentingNewLine]", 
           RowBox[{
            RowBox[{"Show", "[", 
             RowBox[{
              RowBox[{"{", 
               RowBox[{"background", ",", "graphWithTrajectories", ",", 
                RowBox[{"Graphics", "[", "listOfArrows", "]"}], ",", 
                RowBox[{"If", "[", 
                 RowBox[{
                  RowBox[{"criticalPoints", "\[NotEqual]", 
                   RowBox[{"{", "}"}]}], ",", 
                  RowBox[{"Graphics", "[", 
                   RowBox[{"{", 
                    RowBox[{
                    RowBox[{"EdgeForm", "[", "Thick", "]"}], ",", "Red", ",", 
                    RowBox[{
                    RowBox[{"(", 
                    RowBox[{
                    RowBox[{"Disk", "[", 
                    RowBox[{
                    RowBox[{"Simplex2DCoord", "[", "#", "]"}], ",", "0.03"}], 
                    "]"}], "&"}], ")"}], "/@", 
                    RowBox[{"(", 
                    RowBox[{"N", "[", 
                    RowBox[{
                    RowBox[{"{", 
                    RowBox[{"x1", ",", "x2", ",", "x3"}], "}"}], "/.", 
                    "criticalPoints"}], "]"}], ")"}]}]}], "}"}], "]"}], ",", 
                  RowBox[{
                   RowBox[{"##", "&"}], "[", "]"}]}], "]"}], ",", 
                "\[IndentingNewLine]", 
                RowBox[{"If", "[", 
                 RowBox[{
                  RowBox[{
                   RowBox[{"criticalRegions", "\[NotEqual]", 
                    RowBox[{"{", "}"}]}], "&&", 
                   RowBox[{"Not", "[", "allStrategiesEqual", "]"}]}], ",", 
                  RowBox[{"Map", "[", 
                   RowBox[{
                    RowBox[{
                    RowBox[{"Plot", "[", 
                    RowBox[{
                    RowBox[{"y", "/.", "#"}], ",", 
                    RowBox[{"{", 
                    RowBox[{"x", ",", "0", ",", "1"}], "}"}], ",", 
                    RowBox[{"PlotStyle", "\[Rule]", 
                    RowBox[{"Directive", "[", 
                    RowBox[{"Red", ",", 
                    RowBox[{"Thickness", "[", "0.01", "]"}]}], "]"}]}]}], 
                    "]"}], "&"}], ",", 
                    RowBox[{"Flatten", "@", 
                    RowBox[{"Map", "[", 
                    RowBox[{
                    RowBox[{
                    RowBox[{"Solve", "[", 
                    RowBox[{"#", ",", "y", ",", "Reals"}], "]"}], "&"}], ",", 
                    RowBox[{"criticalRegions", "/.", 
                    RowBox[{"{", 
                    RowBox[{
                    RowBox[{"x1", "\[Rule]", 
                    FractionBox[
                    RowBox[{"2", " ", "y"}], 
                    SqrtBox["3"]]}], ",", 
                    RowBox[{"x2", "\[Rule]", 
                    RowBox[{"(", 
                    RowBox[{"1", "-", "x", "-", 
                    FractionBox["y", 
                    SqrtBox["3"]]}], ")"}]}], ",", 
                    RowBox[{"x3", "\[Rule]", 
                    RowBox[{"(", 
                    RowBox[{"x", "-", 
                    FractionBox["y", 
                    SqrtBox["3"]]}], ")"}]}]}], "}"}]}]}], "]"}]}]}], "]"}], 
                  ",", 
                  RowBox[{
                   RowBox[{"##", "&"}], "[", "]"}]}], "]"}], ",", 
                "\[IndentingNewLine]", 
                RowBox[{"Graphics", "[", 
                 RowBox[{"{", 
                  RowBox[{
                   RowBox[{"Inset", "[", 
                    RowBox[{
                    RowBox[{"Style", "[", 
                    RowBox[{
                    "\"\<\!\(\*SubscriptBox[\(x\), \(1\)]\) = 1\>\"", ",", 
                    "18", ",", "Bold"}], "]"}], ",", 
                    RowBox[{"{", 
                    RowBox[{"0.65", ",", "0.9"}], "}"}]}], "]"}], ",", 
                   RowBox[{"Inset", "[", 
                    RowBox[{
                    RowBox[{"Style", "[", 
                    RowBox[{
                    "\"\<\!\(\*SubscriptBox[\(x\), \(2\)]\) = 1\>\"", ",", 
                    "18", ",", "Bold"}], "]"}], ",", 
                    RowBox[{"{", 
                    RowBox[{"0", ",", 
                    RowBox[{"-", "0.06"}]}], "}"}]}], "]"}], ",", 
                   RowBox[{"Inset", "[", 
                    RowBox[{
                    RowBox[{"Style", "[", 
                    RowBox[{
                    "\"\<\!\(\*SubscriptBox[\(x\), \(3\)]\) = 1\>\"", ",", 
                    "18", ",", "Bold"}], "]"}], ",", 
                    RowBox[{"{", 
                    RowBox[{"1", ",", 
                    RowBox[{"-", "0.06"}]}], "}"}]}], "]"}]}], "}"}], "]"}]}],
                "}"}], ",", 
              RowBox[{"PlotRange", "->", 
               RowBox[{"{", 
                RowBox[{
                 RowBox[{"{", 
                  RowBox[{
                   RowBox[{"-", "0.1"}], ",", 
                   RowBox[{"1", "+", "0.1"}]}], "}"}], ",", 
                 RowBox[{"{", 
                  RowBox[{
                   RowBox[{"-", "0.1"}], ",", 
                   RowBox[{
                    FractionBox[
                    SqrtBox["3"], "2"], "+", "0.1"}]}], "}"}]}], "}"}]}], ",", 
              RowBox[{"Frame", "->", "False"}], ",", 
              RowBox[{"Axes", "\[Rule]", "False"}]}], "]"}], ",", 
            "\[IndentingNewLine]", 
            RowBox[{"If", "[", 
             RowBox[{
              RowBox[{"criticalPoints", "\[NotEqual]", 
               RowBox[{"{", "}"}]}], ",", 
              RowBox[{"Column", "[", 
               RowBox[{
                RowBox[{"{", "\[IndentingNewLine]", 
                 RowBox[{
                  RowBox[{"Text", "@", 
                   RowBox[{"Style", "[", 
                    RowBox[{
                    "\"\<critical points\>\"", ",", "Red", ",", "Bold", ",", 
                    "12"}], "]"}]}], ",", "\[IndentingNewLine]", 
                  RowBox[{"Text", "[", 
                   RowBox[{
                    RowBox[{"Row", "[", 
                    RowBox[{
                    RowBox[{"{", 
                    RowBox[{
                    RowBox[{"TableForm", "[", 
                    RowBox[{
                    RowBox[{"N", "[", 
                    RowBox[{
                    RowBox[{
                    RowBox[{"{", 
                    RowBox[{"x1", ",", "x2", ",", "x3"}], "}"}], "//.", 
                    "criticalPoints"}], ",", "3"}], "]"}], ",", 
                    RowBox[{"TableHeadings", "->", 
                    RowBox[{"{", 
                    RowBox[{"None", ",", 
                    RowBox[{"{", 
                    RowBox[{
                    RowBox[{"Style", "[", 
                    RowBox[{
                    SubscriptBox[
                    RowBox[{"Style", "[", 
                    RowBox[{"\"\<x\>\"", ",", "Italic"}], "]"}], "1"], ",", 
                    "12"}], "]"}], ",", 
                    RowBox[{"Style", "[", 
                    RowBox[{
                    SubscriptBox[
                    RowBox[{"Style", "[", 
                    RowBox[{"\"\<x\>\"", ",", "Italic"}], "]"}], "2"], ",", 
                    "12"}], "]"}], ",", 
                    RowBox[{"Style", "[", 
                    RowBox[{
                    SubscriptBox[
                    RowBox[{"Style", "[", 
                    RowBox[{"\"\<x\>\"", ",", "Italic"}], "]"}], "3"], ",", 
                    "12"}], "]"}]}], "}"}]}], "}"}]}], ",", 
                    RowBox[{"TableSpacing", "->", 
                    RowBox[{"{", 
                    RowBox[{"1", ",", "1"}], "}"}]}], ",", 
                    RowBox[{"TableAlignments", "->", 
                    RowBox[{"{", 
                    RowBox[{"Left", ",", "Bottom"}], "}"}]}]}], "]"}], ",", 
                    "\[IndentingNewLine]", 
                    RowBox[{"TableForm", "[", 
                    RowBox[{
                    RowBox[{"Chop", "@", 
                    RowBox[{"Map", "[", 
                    RowBox[{
                    RowBox[{
                    RowBox[{"Eigenvalues", "[", 
                    RowBox[{"Jacob", "[", 
                    RowBox[{"#", ",", "A", ",", "\[Mu]"}], "]"}], "]"}], 
                    "&"}], ",", 
                    RowBox[{"N", "[", 
                    RowBox[{
                    RowBox[{
                    RowBox[{"{", 
                    RowBox[{"x1", ",", "x2"}], "}"}], "//.", 
                    "criticalPoints"}], ",", "3"}], "]"}]}], "]"}]}], ",", 
                    RowBox[{"TableHeadings", "->", 
                    RowBox[{"{", 
                    RowBox[{"None", ",", 
                    RowBox[{"{", 
                    RowBox[{
                    RowBox[{"Style", "[", 
                    RowBox[{
                    "\"\<\!\(\*SubscriptBox[\(\[Lambda]\), \(1\)]\)\>\"", ",",
                     "Bold", ",", "12"}], "]"}], ",", 
                    RowBox[{"Style", "[", 
                    RowBox[{
                    "\"\<\!\(\*SubscriptBox[\(\[Lambda]\), \(2\)]\)\>\"", ",",
                     "Bold", ",", "12"}], "]"}]}], "}"}]}], "}"}]}], ",", 
                    RowBox[{"TableSpacing", "->", 
                    RowBox[{"{", 
                    RowBox[{"1", ",", "1"}], "}"}]}], ",", 
                    RowBox[{"TableAlignments", "->", 
                    RowBox[{"{", 
                    RowBox[{"Right", ",", "Bottom"}], "}"}]}]}], "]"}]}], 
                    "}"}], ",", "\"\<   \>\""}], "]"}], ",", 
                    RowBox[{"BaseStyle", "\[Rule]", 
                    RowBox[{"{", "12", "}"}]}]}], "]"}]}], "}"}], ",", 
                RowBox[{"Alignment", "->", "Center"}], ",", 
                RowBox[{"Spacings", "->", "1"}], ",", 
                RowBox[{"Frame", "->", "True"}]}], "]"}]}], "]"}], ",", 
            "\[IndentingNewLine]", 
            RowBox[{"If", "[", 
             RowBox[{
              RowBox[{"criticalRegions", "\[NotEqual]", 
               RowBox[{"{", "}"}]}], ",", 
              RowBox[{"Column", "[", 
               RowBox[{
                RowBox[{"{", "\[IndentingNewLine]", 
                 RowBox[{
                  RowBox[{"Text", "@", 
                   RowBox[{"Style", "[", 
                    RowBox[{
                    "\"\<critical regions\>\"", ",", "Red", ",", "Bold", ",", 
                    "12"}], "]"}]}], ",", "\[IndentingNewLine]", 
                  RowBox[{"Text", "[", 
                   RowBox[{
                    RowBox[{"Row", "[", 
                    RowBox[{"{", 
                    RowBox[{"TableForm", "[", 
                    RowBox[{
                    RowBox[{"criticalRegions", "/.", 
                    RowBox[{"{", 
                    RowBox[{
                    RowBox[{"x1", "\[Rule]", 
                    RowBox[{"Text", "[", 
                    SubscriptBox[
                    RowBox[{"Style", "[", 
                    RowBox[{"\"\<x\>\"", ",", "Italic"}], "]"}], "1"], 
                    "]"}]}], ",", 
                    RowBox[{"x2", "\[Rule]", 
                    RowBox[{"Text", "[", 
                    SubscriptBox[
                    RowBox[{"Style", "[", 
                    RowBox[{"\"\<x\>\"", ",", "Italic"}], "]"}], "2"], 
                    "]"}]}], ",", 
                    RowBox[{"x3", "\[Rule]", 
                    RowBox[{"Text", "[", 
                    SubscriptBox[
                    RowBox[{"Style", "[", 
                    RowBox[{"\"\<x\>\"", ",", "Italic"}], "]"}], "3"], 
                    "]"}]}]}], "}"}]}], ",", 
                    RowBox[{"TableSpacing", "->", 
                    RowBox[{"{", 
                    RowBox[{"1", ",", "1"}], "}"}]}], ",", 
                    RowBox[{"TableAlignments", "->", 
                    RowBox[{"{", 
                    RowBox[{"Left", ",", "Bottom"}], "}"}]}]}], "]"}], "}"}], 
                    "]"}], ",", 
                    RowBox[{"BaseStyle", "\[Rule]", 
                    RowBox[{"{", "12", "}"}]}]}], "]"}]}], "}"}], ",", 
                RowBox[{"Alignment", "->", "Center"}], ",", 
                RowBox[{"Spacings", "->", "1"}], ",", 
                RowBox[{"Frame", "->", "True"}]}], "]"}]}], "]"}]}], 
           "\[IndentingNewLine]", "}"}], ",", 
          RowBox[{"{", 
           RowBox[{"Center", ",", "Top"}], "}"}]}], "]"}], ",", 
        RowBox[{"ImageSize", "\[Rule]", 
         RowBox[{"{", 
          RowBox[{"430", ",", "512"}], "}"}]}]}], "]"}]}]}], 
    "\[IndentingNewLine]", "\[IndentingNewLine]", "]"}], ",", 
   "\[IndentingNewLine]", "\[IndentingNewLine]", 
   RowBox[{"{", 
    RowBox[{
     RowBox[{"{", 
      RowBox[{"update", ",", "0"}], "}"}], ",", "0", ",", "100", ",", 
     RowBox[{"ControlType", "\[Rule]", "None"}]}], "}"}], ",", 
   "\[IndentingNewLine]", "\[IndentingNewLine]", 
   RowBox[{"{", 
    RowBox[{
     RowBox[{"{", 
      RowBox[{"\[Mu]", ",", "0.01"}], "}"}], ",", "0", ",", "1", ",", "0.25", 
     ",", 
     RowBox[{"ControlType", "\[Rule]", "None"}]}], "}"}], ",", 
   RowBox[{"(*", " ", 
    RowBox[{"Only", " ", "for", " ", "Autorun"}], "*)"}], 
   "\[IndentingNewLine]", 
   RowBox[{"{", 
    RowBox[{
     RowBox[{"{", 
      RowBox[{"tMax", ",", "5"}], "}"}], ",", "0", ",", "10", ",", "5", ",", 
     RowBox[{"ControlType", "\[Rule]", "None"}]}], "}"}], ",", 
   RowBox[{"(*", " ", 
    RowBox[{"Only", " ", "for", " ", "Autorun"}], "*)"}], 
   "\[IndentingNewLine]", 
   RowBox[{"{", 
    RowBox[{
     RowBox[{"{", 
      RowBox[{"step", ",", "0.125"}], "}"}], ",", 
     RowBox[{"{", 
      RowBox[{"0.0625", ",", "0.125", ",", "0.25", ",", "1"}], "}"}], ",", 
     RowBox[{"ControlType", "\[Rule]", "None"}]}], "}"}], ",", 
   RowBox[{"(*", " ", 
    RowBox[{"Only", " ", "for", " ", "Autorun"}], "*)"}], 
   "\[IndentingNewLine]", "\[IndentingNewLine]", 
   RowBox[{"Grid", "[", 
    RowBox[{
     RowBox[{"{", "\[IndentingNewLine]", 
      RowBox[{
       RowBox[{"{", 
        RowBox[{"Style", "[", 
         RowBox[{
         "\"\<payoffs (\!\(\*SubscriptBox[\(a\), \(ij\)]\))\>\"", ",", 
          "Bold"}], "]"}], "}"}], ",", 
       RowBox[{"{", 
        RowBox[{"\"\< \>\"", ",", "SpanFromLeft"}], "}"}], ",", 
       "\[IndentingNewLine]", 
       RowBox[{"{", 
        RowBox[{
         RowBox[{"Control", "[", 
          RowBox[{"{", 
           RowBox[{
            RowBox[{"{", 
             RowBox[{
             "a11", ",", "2", ",", 
              "\"\<\!\(\*SubscriptBox[\(a\), \
\(\(1\)\(\[CenterDot]\)\)]\)\>\""}], "}"}], ",", 
            RowBox[{"Range", "[", 
             RowBox[{"0", ",", "8"}], "]"}], ",", "PopupMenu", ",", 
            RowBox[{"ImageSize", "\[Rule]", 
             RowBox[{"{", 
              RowBox[{"43", ",", "19"}], "}"}]}]}], "}"}], "]"}], " ", ",", 
         "\[IndentingNewLine]", 
         RowBox[{"Control", "[", 
          RowBox[{"{", 
           RowBox[{
            RowBox[{"{", 
             RowBox[{"a12", ",", "0", ",", "\"\<\>\""}], "}"}], ",", 
            RowBox[{"Range", "[", 
             RowBox[{"0", ",", "8"}], "]"}], ",", "PopupMenu", ",", 
            RowBox[{"ImageSize", "\[Rule]", 
             RowBox[{"{", 
              RowBox[{"43", ",", "19"}], "}"}]}]}], "}"}], "]"}], ",", 
         "\[IndentingNewLine]", 
         RowBox[{"Control", "[", 
          RowBox[{"{", 
           RowBox[{
            RowBox[{"{", 
             RowBox[{"a13", ",", "1", ",", "\"\<\>\""}], "}"}], ",", 
            RowBox[{"Range", "[", 
             RowBox[{"0", ",", "8"}], "]"}], ",", "PopupMenu", ",", 
            RowBox[{"ImageSize", "\[Rule]", 
             RowBox[{"{", 
              RowBox[{"43", ",", "19"}], "}"}]}]}], "}"}], "]"}]}], "}"}], 
       ",", "\[IndentingNewLine]", 
       RowBox[{"{", 
        RowBox[{
         RowBox[{"Control", "[", 
          RowBox[{"{", 
           RowBox[{
            RowBox[{"{", 
             RowBox[{
             "a21", ",", "1", ",", 
              "\"\<\!\(\*SubscriptBox[\(a\), \
\(\(2\)\(\[CenterDot]\)\)]\)\>\""}], "}"}], ",", 
            RowBox[{"Range", "[", 
             RowBox[{"0", ",", "8"}], "]"}], ",", "PopupMenu", ",", 
            RowBox[{"ImageSize", "\[Rule]", 
             RowBox[{"{", 
              RowBox[{"43", ",", "19"}], "}"}]}]}], "}"}], "]"}], " ", ",", 
         "\[IndentingNewLine]", 
         RowBox[{"Control", "[", 
          RowBox[{"{", 
           RowBox[{
            RowBox[{"{", 
             RowBox[{"a22", ",", "2", ",", "\"\<\>\""}], "}"}], ",", 
            RowBox[{"Range", "[", 
             RowBox[{"0", ",", "8"}], "]"}], ",", "PopupMenu", ",", 
            RowBox[{"ImageSize", "\[Rule]", 
             RowBox[{"{", 
              RowBox[{"43", ",", "19"}], "}"}]}]}], "}"}], "]"}], ",", 
         "\[IndentingNewLine]", 
         RowBox[{"Control", "[", 
          RowBox[{"{", 
           RowBox[{
            RowBox[{"{", 
             RowBox[{"a23", ",", "0", ",", "\"\<\>\""}], "}"}], ",", 
            RowBox[{"Range", "[", 
             RowBox[{"0", ",", "8"}], "]"}], ",", "PopupMenu", ",", 
            RowBox[{"ImageSize", "\[Rule]", 
             RowBox[{"{", 
              RowBox[{"43", ",", "19"}], "}"}]}]}], "}"}], "]"}]}], "}"}], 
       ",", "\[IndentingNewLine]", 
       RowBox[{"{", 
        RowBox[{
         RowBox[{"Control", "[", 
          RowBox[{"{", 
           RowBox[{
            RowBox[{"{", 
             RowBox[{
             "a31", ",", "0", ",", 
              "\"\<\!\(\*SubscriptBox[\(a\), \
\(\(3\)\(\[CenterDot]\)\)]\)\>\""}], "}"}], ",", 
            RowBox[{"Range", "[", 
             RowBox[{"0", ",", "8"}], "]"}], ",", "PopupMenu", ",", 
            RowBox[{"ImageSize", "\[Rule]", 
             RowBox[{"{", 
              RowBox[{"43", ",", "19"}], "}"}]}]}], "}"}], "]"}], " ", ",", 
         "\[IndentingNewLine]", 
         RowBox[{"Control", "[", 
          RowBox[{"{", 
           RowBox[{
            RowBox[{"{", 
             RowBox[{"a32", ",", "1", ",", "\"\<\>\""}], "}"}], ",", 
            RowBox[{"Range", "[", 
             RowBox[{"0", ",", "8"}], "]"}], ",", "PopupMenu", ",", 
            RowBox[{"ImageSize", "\[Rule]", 
             RowBox[{"{", 
              RowBox[{"43", ",", "19"}], "}"}]}]}], "}"}], "]"}], ",", 
         "\[IndentingNewLine]", 
         RowBox[{"Control", "[", 
          RowBox[{"{", 
           RowBox[{
            RowBox[{"{", 
             RowBox[{"a33", ",", "2", ",", "\"\<\>\""}], "}"}], ",", 
            RowBox[{"Range", "[", 
             RowBox[{"0", ",", "8"}], "]"}], ",", "PopupMenu", ",", 
            RowBox[{"ImageSize", "\[Rule]", 
             RowBox[{"{", 
              RowBox[{"43", ",", "19"}], "}"}]}]}], "}"}], "]"}]}], "}"}]}], 
      "\[IndentingNewLine]", "}"}], ",", 
     RowBox[{"Alignment", "\[Rule]", "Left"}], ",", 
     RowBox[{"Spacings", "\[Rule]", 
      RowBox[{"{", 
       RowBox[{"0", ",", "0"}], "}"}]}]}], "]"}], " ", ",", 
   "\[IndentingNewLine]", "Delimiter", "\[IndentingNewLine]", ",", 
   "\[IndentingNewLine]", 
   RowBox[{"Button", "[", 
    RowBox[{"\"\<Update\>\"", ",", 
     RowBox[{"update", "++"}], ",", 
     RowBox[{"ImageSize", "\[Rule]", 
      RowBox[{"{", 
       RowBox[{"150", ",", "30"}], "}"}]}]}], "]"}], ",", 
   "\[IndentingNewLine]", "Delimiter", "\[IndentingNewLine]", ",", 
   "\[IndentingNewLine]", 
   RowBox[{"Style", "[", 
    RowBox[{"\"\<prob. random strategy\>\"", ",", "Bold"}], "]"}], ",", 
   "\[IndentingNewLine]", 
   RowBox[{"Control", "[", 
    RowBox[{"{", 
     RowBox[{
      RowBox[{"{", 
       RowBox[{"\[Mu]", ",", "0"}], "}"}], ",", "0", ",", "1", ",", "0.001", 
      " ", ",", 
      RowBox[{"ImageSize", "\[Rule]", "Small"}], " ", ",", 
      RowBox[{"Appearance", "\[Rule]", "\"\<Labeled\>\""}]}], "}"}], "]"}], 
   ",", "\[IndentingNewLine]", "Delimiter", "\[IndentingNewLine]", ",", 
   "\[IndentingNewLine]", 
   RowBox[{"Style", "[", 
    RowBox[{"\"\<trajectories\>\"", ",", "Bold"}], "]"}], ",", 
   "\[IndentingNewLine]", 
   RowBox[{"Control", "[", 
    RowBox[{"{", 
     RowBox[{
      RowBox[{"{", 
       RowBox[{
       "tMax", ",", "5", ",", 
        "\"\<\!\(\*SubscriptBox[\(t\), \(max\)]\)\>\""}], "}"}], ",", "0", 
      ",", "10", ",", "0.1", ",", 
      RowBox[{"ImageSize", "\[Rule]", "Small"}], " ", ",", 
      RowBox[{"Appearance", "\[Rule]", "\"\<Labeled\>\""}]}], "}"}], "]"}], 
   ",", "\[IndentingNewLine]", 
   RowBox[{"Control", "[", 
    RowBox[{"{", 
     RowBox[{
      RowBox[{"{", 
       RowBox[{"step", ",", "0.125", ",", "\"\<show\>\""}], "}"}], ",", 
      RowBox[{"{", 
       RowBox[{
        RowBox[{"0.0625", "\[Rule]", "\"\<many\>\""}], ",", 
        RowBox[{"0.125", "\[Rule]", "\"\<some\>\""}], ",", 
        RowBox[{"0.25", "\[Rule]", "\"\<few\>\""}], ",", 
        RowBox[{"1", "\[Rule]", "\"\<none\>\""}]}], "}"}]}], "}"}], "]"}], 
   ",", "\[IndentingNewLine]", "Delimiter", "\[IndentingNewLine]", ",", 
   "\[IndentingNewLine]", "\[IndentingNewLine]", 
   RowBox[{"SaveDefinitions", "->", "True"}], ",", 
   RowBox[{"SynchronousUpdating", "->", "False"}], ",", 
   RowBox[{"Alignment", "\[Rule]", 
    RowBox[{"{", 
     RowBox[{"Center", ",", "Top"}], "}"}]}], " ", ",", "\[IndentingNewLine]", 
   RowBox[{"ControlPlacement", "\[Rule]", "Left"}], ",", " ", 
   RowBox[{"TrackedSymbols", "\[RuleDelayed]", 
    RowBox[{"{", 
     RowBox[{"\[Mu]", ",", "update", ",", "tMax", ",", "step"}], "}"}]}], ",", 
   RowBox[{"Bookmarks", "\[Rule]", 
    RowBox[{"{", 
     RowBox[{
      RowBox[{"\"\<Rock, Paper, Scissors\>\"", "\[RuleDelayed]", 
       RowBox[{"{", 
        RowBox[{
         RowBox[{"a11", "=", "1"}], ",", 
         RowBox[{"a12", "=", "0"}], ",", 
         RowBox[{"a13", "=", "2"}], ",", 
         RowBox[{"a21", "=", "2"}], ",", 
         RowBox[{"a22", "=", "1"}], ",", 
         RowBox[{"a23", "=", "0"}], ",", 
         RowBox[{"a31", "=", "0"}], ",", 
         RowBox[{"a32", "=", "2"}], ",", 
         RowBox[{"a33", "=", "1"}], ",", 
         RowBox[{"update", "=", "100"}], ",", 
         RowBox[{"\[Mu]", "=", "0.0001`"}]}], "}"}]}], ",", 
      RowBox[{"\"\<4 critical points\>\"", "\[RuleDelayed]", 
       RowBox[{"{", 
        RowBox[{
         RowBox[{"a11", "=", "0"}], ",", 
         RowBox[{"a12", "=", "1"}], ",", 
         RowBox[{"a13", "=", "1"}], ",", 
         RowBox[{"a21", "=", "1"}], ",", 
         RowBox[{"a22", "=", "1"}], ",", 
         RowBox[{"a23", "=", "1"}], ",", 
         RowBox[{"a31", "=", "1"}], ",", 
         RowBox[{"a32", "=", "1"}], ",", 
         RowBox[{"a33", "=", "0"}], ",", 
         RowBox[{"update", "=", "110"}], ",", 
         RowBox[{"\[Mu]", "=", "0"}]}], "}"}]}], ",", 
      RowBox[{"\"\<Critical points and regions\>\"", "\[RuleDelayed]", 
       RowBox[{"{", 
        RowBox[{
         RowBox[{"a11", "=", "1"}], ",", 
         RowBox[{"a12", "=", "1"}], ",", 
         RowBox[{"a13", "=", "0"}], ",", 
         RowBox[{"a21", "=", "1"}], ",", 
         RowBox[{"a22", "=", "1"}], ",", 
         RowBox[{"a23", "=", "1"}], ",", 
         RowBox[{"a31", "=", "0"}], ",", 
         RowBox[{"a32", "=", "1"}], ",", 
         RowBox[{"a33", "=", "1"}], ",", 
         RowBox[{"update", "=", "120"}], ",", 
         RowBox[{"\[Mu]", "=", "0"}]}], "}"}]}], ",", 
      RowBox[{"\"\<Internal critical regions\>\"", "\[RuleDelayed]", 
       RowBox[{"{", 
        RowBox[{
         RowBox[{"a11", "=", "0"}], ",", 
         RowBox[{"a12", "=", "1"}], ",", 
         RowBox[{"a13", "=", "0"}], ",", 
         RowBox[{"a21", "=", "1"}], ",", 
         RowBox[{"a22", "=", "0"}], ",", 
         RowBox[{"a23", "=", "1"}], ",", 
         RowBox[{"a31", "=", "0"}], ",", 
         RowBox[{"a32", "=", "1"}], ",", 
         RowBox[{"a33", "=", "0"}], ",", 
         RowBox[{"update", "=", "130"}], ",", 
         RowBox[{"\[Mu]", "=", "0"}]}], "}"}]}], ",", 
      RowBox[{"\"\<Critical regions only\>\"", "\[RuleDelayed]", 
       RowBox[{"{", 
        RowBox[{
         RowBox[{"a11", "=", "2"}], ",", 
         RowBox[{"a12", "=", "0"}], ",", 
         RowBox[{"a13", "=", "2"}], ",", 
         RowBox[{"a21", "=", "2"}], ",", 
         RowBox[{"a22", "=", "2"}], ",", 
         RowBox[{"a23", "=", "2"}], ",", 
         RowBox[{"a31", "=", "2"}], ",", 
         RowBox[{"a32", "=", "2"}], ",", 
         RowBox[{"a33", "=", "2"}], ",", 
         RowBox[{"update", "=", "140"}], ",", 
         RowBox[{"\[Mu]", "=", "0"}]}], "}"}]}], ",", "\[IndentingNewLine]", 
      RowBox[{"\"\<All critical\>\"", "\[RuleDelayed]", 
       RowBox[{"{", 
        RowBox[{
         RowBox[{"a11", "=", "1"}], ",", 
         RowBox[{"a12", "=", "1"}], ",", 
         RowBox[{"a13", "=", "1"}], ",", 
         RowBox[{"a21", "=", "1"}], ",", 
         RowBox[{"a22", "=", "1"}], ",", 
         RowBox[{"a23", "=", "1"}], ",", 
         RowBox[{"a31", "=", "1"}], ",", 
         RowBox[{"a32", "=", "1"}], ",", 
         RowBox[{"a33", "=", "1"}], ",", 
         RowBox[{"update", "=", "150"}], ",", 
         RowBox[{"\[Mu]", "=", "0"}]}], "}"}]}]}], "}"}]}], ",", " ", 
   RowBox[{"AutorunSequencing", "\[Rule]", 
    RowBox[{"{", 
     RowBox[{
      RowBox[{"{", 
       RowBox[{"2", ",", "10"}], "}"}], ",", 
      RowBox[{"{", 
       RowBox[{"3", ",", "10"}], "}"}], ",", 
      RowBox[{"{", 
       RowBox[{"4", ",", "10"}], "}"}]}], "}"}]}], ",", 
   RowBox[{"ControlPlacement", "\[Rule]", "Left"}], ",", 
   RowBox[{"ContinuousAction", "\[Rule]", "False"}]}], "]"}]}], "Input",
 CellChangeTimes->{{3.5177649899175687`*^9, 3.517765016881111*^9}, 
   3.517765433882962*^9, {3.5177720989091797`*^9, 3.517772112819976*^9}, {
   3.5178485337152863`*^9, 3.517848546164108*^9}, {3.5178485852109766`*^9, 
   3.5178486252562466`*^9}, {3.517848726484824*^9, 3.5178487709293027`*^9}, {
   3.51784890020673*^9, 3.5178489085059443`*^9}, {3.5178499729001684`*^9, 
   3.5178499732421875`*^9}, {3.517850019397828*^9, 3.517850033934659*^9}, 
   3.5178500824734354`*^9, {3.5178509247266097`*^9, 3.5178509249976254`*^9}, 
   3.5178509585525446`*^9, {3.5178510009769707`*^9, 3.5178510261614113`*^9}, {
   3.517851102121756*^9, 3.5178511113922863`*^9}, {3.517851156605872*^9, 
   3.517851172671791*^9}, {3.517851241548731*^9, 3.5178512418757496`*^9}, {
   3.5178512834041247`*^9, 3.5178513443266096`*^9}, {3.5178514223770733`*^9, 
   3.5178514451223745`*^9}, {3.517851477661236*^9, 3.517851481707467*^9}, {
   3.5178515239788847`*^9, 3.51785153280939*^9}, 3.517851657135501*^9, {
   3.5178516930705566`*^9, 3.5178517123246574`*^9}, {3.5178528684407835`*^9, 
   3.517852887310863*^9}, {3.517852928634227*^9, 3.5178529416209693`*^9}, {
   3.5178530226916065`*^9, 3.517853041617689*^9}, {3.5178530774147367`*^9, 
   3.517853106534402*^9}, {3.517853207231161*^9, 3.5178532648124547`*^9}, {
   3.5178533490792747`*^9, 3.5178533546385927`*^9}, {3.5179103874541416`*^9, 
   3.5179103877121563`*^9}, {3.517989390832556*^9, 3.5179894225562115`*^9}, {
   3.517989505645975*^9, 3.5179895211056023`*^9}, {3.517989583614912*^9, 
   3.517989651677831*^9}, {3.5179896933455043`*^9, 3.517989694827507*^9}, {
   3.5179897509564056`*^9, 3.5179897527192087`*^9}, {3.517989789628874*^9, 
   3.517989795588084*^9}, {3.517989847567375*^9, 3.517989862262601*^9}, {
   3.517989927111915*^9, 3.517989934818329*^9}, {3.5180036059719496`*^9, 
   3.518003690168765*^9}, {3.5180089598038397`*^9, 3.518008972075542*^9}, {
   3.518009569746727*^9, 3.518009658588808*^9}, {3.5180097680550694`*^9, 
   3.5180097798207426`*^9}, 3.675102749055737*^9, {3.6751027942677193`*^9, 
   3.675102812014542*^9}, {3.675104599038797*^9, 3.675104622120105*^9}, {
   3.675104662518434*^9, 3.675104666750762*^9}, {3.675104715771476*^9, 
   3.675104775381583*^9}, {3.67510480629979*^9, 3.67510481983331*^9}, {
   3.675104854247465*^9, 3.675104862861793*^9}, {3.675104964156741*^9, 
   3.675104968081799*^9}, {3.675104998907962*^9, 3.675105003592559*^9}, {
   3.675105109275042*^9, 3.6751053041367683`*^9}, {3.6751055143339167`*^9, 
   3.6751055293662863`*^9}, {3.6751055731728487`*^9, 3.675105585370893*^9}, {
   3.675105784673706*^9, 3.675105803462735*^9}, {3.675162807679421*^9, 
   3.67516294889307*^9}, 3.675163064358203*^9, {3.6751631129657907`*^9, 
   3.6751631626594143`*^9}, {3.6751631955544357`*^9, 3.675163226533833*^9}, {
   3.675163299482375*^9, 3.675163302567346*^9}, 3.675163369167389*^9, 
   3.675163514075395*^9, {3.675163629471439*^9, 3.675163636033428*^9}, 
   3.675163679044606*^9, {3.675163769642267*^9, 3.675163783231119*^9}, {
   3.675163823799273*^9, 3.6751638856125593`*^9}, {3.675163942344112*^9, 
   3.675163968516382*^9}, {3.675164114145379*^9, 3.675164117381914*^9}, {
   3.675164148394026*^9, 3.6751641748356867`*^9}, {3.6751642050474653`*^9, 
   3.675164277435401*^9}, {3.675164344884411*^9, 3.675164345536216*^9}, {
   3.675164492451386*^9, 3.675164506449596*^9}, {3.675165300900325*^9, 
   3.675165329088236*^9}, {3.67516589775023*^9, 3.6751659032203417`*^9}, {
   3.6751659448026533`*^9, 3.675165957585558*^9}, {3.6751660272482777`*^9, 
   3.675166045769417*^9}, {3.675166474835659*^9, 3.67516649015479*^9}, {
   3.675166537056847*^9, 3.675166565920053*^9}, 3.675166647228095*^9, {
   3.675166726551978*^9, 3.6751667366876173`*^9}, {3.675166767108039*^9, 
   3.67516676789394*^9}, {3.6751668572823963`*^9, 3.6751668774560423`*^9}, {
   3.6751670422049103`*^9, 3.675167165550479*^9}, {3.675167210881773*^9, 
   3.6751672376651287`*^9}, {3.675167270707543*^9, 3.675167279314309*^9}, {
   3.675167325777096*^9, 3.675167359320531*^9}, {3.675167416017816*^9, 
   3.675167423974381*^9}, {3.675167523961323*^9, 3.6751675243817377`*^9}, {
   3.675168061751882*^9, 3.675168081133791*^9}, {3.675168137830262*^9, 
   3.675168157005898*^9}, {3.6751681914726067`*^9, 3.675168193799448*^9}, {
   3.675168229129724*^9, 3.6751683838690643`*^9}, {3.675168415396925*^9, 
   3.6751684616964293`*^9}, {3.675168492169201*^9, 3.675168498970173*^9}, 
   3.675172280103561*^9, 3.6751723293645897`*^9, {3.675172387049673*^9, 
   3.675172442239832*^9}, {3.6751724777464*^9, 3.675172479453219*^9}, {
   3.675172564882509*^9, 3.675172583815221*^9}, 3.675172613834222*^9, {
   3.675178316511939*^9, 3.6751783429870443`*^9}, {3.675178389944132*^9, 
   3.675178393125104*^9}, {3.675178546287726*^9, 3.675178547307358*^9}, {
   3.675178643281725*^9, 3.675178735740169*^9}, {3.675178790487821*^9, 
   3.675178835294874*^9}, {3.675178873735293*^9, 3.6751788781414824`*^9}, {
   3.675178912639916*^9, 3.67517891291043*^9}, 3.675179016663126*^9, 
   3.675179149177664*^9, {3.675179208564567*^9, 3.675179217887003*^9}, {
   3.6751794512628517`*^9, 3.675179451922551*^9}, {3.675179763240896*^9, 
   3.6751798047176533`*^9}, {3.675179939961968*^9, 3.675179946914133*^9}, {
   3.675180020075574*^9, 3.6751800260178013`*^9}, 3.675180090687839*^9, {
   3.675180151706963*^9, 3.675180155082489*^9}, {3.675180379050935*^9, 
   3.675180456203888*^9}, {3.675180542263756*^9, 3.6751805469015303`*^9}, {
   3.675180993755871*^9, 3.675181016154235*^9}, {3.675181143693408*^9, 
   3.6751811483556356`*^9}, {3.67518231090136*^9, 3.675182326986512*^9}, {
   3.6751824029320993`*^9, 3.675182423150496*^9}, {3.675185742667939*^9, 
   3.675185788726593*^9}, 3.675185853779872*^9, 3.6751859098655367`*^9, {
   3.675185977203401*^9, 3.675185985606103*^9}, {3.675186026935664*^9, 
   3.6751860274055033`*^9}, {3.675186065638688*^9, 3.675186066660214*^9}, {
   3.675186133826723*^9, 3.675186154512472*^9}, {3.67518621695772*^9, 
   3.675186217049902*^9}, {3.675186283733131*^9, 3.675186322341742*^9}, {
   3.675186455328361*^9, 3.6751864609290323`*^9}, {3.67518658809995*^9, 
   3.67518662696929*^9}, {3.675187188737474*^9, 3.675187320178164*^9}, {
   3.6751873768811626`*^9, 3.675187377262354*^9}, {3.67518746842796*^9, 
   3.6751875547095118`*^9}, {3.6751876835979233`*^9, 
   3.6751876938633432`*^9}, {3.6751877642425823`*^9, 
   3.6751878774488173`*^9}, {3.675208364432146*^9, 3.67520838265466*^9}, {
   3.675208428214725*^9, 3.675208476222425*^9}, {3.6752085119226007`*^9, 
   3.675208564224614*^9}, {3.6752086017529697`*^9, 3.675208613319458*^9}, {
   3.6752087236815767`*^9, 3.675208732414612*^9}, 3.675208793983383*^9, {
   3.6752089280999823`*^9, 3.675208935505187*^9}, {3.6752092647299128`*^9, 
   3.675209272174265*^9}, {3.675209410015353*^9, 3.675209436556963*^9}, {
   3.675209599846531*^9, 3.675209611864071*^9}, {3.675209687342573*^9, 
   3.6752097128988457`*^9}, {3.675209829643876*^9, 3.675209832089484*^9}, {
   3.675209886594841*^9, 3.675209917532686*^9}, {3.675210013612068*^9, 
   3.675210108805848*^9}, {3.6752101703631983`*^9, 3.675210177761278*^9}, {
   3.675210212654537*^9, 3.675210231354724*^9}, {3.675210280665544*^9, 
   3.675210333584814*^9}, {3.6752103821115093`*^9, 3.6752103835827427`*^9}, {
   3.675210440850787*^9, 3.6752104449220877`*^9}, {3.6752105038426437`*^9, 
   3.675210519682291*^9}, {3.675210626095495*^9, 3.675210643868153*^9}, {
   3.67521070127433*^9, 3.675210707696218*^9}, {3.6752109798786993`*^9, 
   3.67521101854597*^9}, {3.675211502645727*^9, 3.675211514468315*^9}, 
   3.675211547307724*^9, {3.6752116043169937`*^9, 3.675211630643908*^9}, {
   3.675211688074218*^9, 3.675211755883542*^9}, {3.675211791115922*^9, 
   3.675211892904337*^9}, {3.6752119236564417`*^9, 3.6752119262214327`*^9}, {
   3.675211966230033*^9, 3.67521202584042*^9}, 3.675212071475219*^9, {
   3.6752121148579884`*^9, 3.6752121162135067`*^9}, {3.675294758990252*^9, 
   3.675294786870713*^9}, {3.675294838567115*^9, 3.675294932952346*^9}, 
   3.675295136628007*^9, {3.675295325984969*^9, 3.675295336776352*^9}, {
   3.6752954559970913`*^9, 3.6752955935396137`*^9}, {3.675295631573821*^9, 
   3.675295695560417*^9}, 3.675295805147553*^9, {3.675295872150901*^9, 
   3.6752958760551653`*^9}, 3.675295912163211*^9, 3.67529606754173*^9, {
   3.675296116036118*^9, 3.675296128164963*^9}, {3.6752961594763393`*^9, 
   3.675296160424473*^9}, {3.675296311791485*^9, 3.6752963359091187`*^9}, 
   3.675296435082603*^9, {3.675296502211545*^9, 3.675296516515533*^9}, {
   3.67529655261629*^9, 3.6752965616338997`*^9}, {3.6752965965580883`*^9, 
   3.6752966133243713`*^9}, {3.675296874450775*^9, 3.6752970962228117`*^9}, {
   3.6752971309059563`*^9, 3.675297250740993*^9}, {3.6752973043167553`*^9, 
   3.6752973096093483`*^9}, {3.67529737891772*^9, 3.6752973831742773`*^9}, {
   3.6752974493246393`*^9, 3.675297457211294*^9}, {3.675297566817646*^9, 
   3.675297569929867*^9}, {3.675297763479575*^9, 3.675297765989545*^9}, {
   3.6752979291920557`*^9, 3.675297934631959*^9}, {3.675298166779756*^9, 
   3.6752981764394627`*^9}, {3.675383623151412*^9, 3.675383689164967*^9}, {
   3.675383745941086*^9, 3.675383793569787*^9}, {3.6753838351458693`*^9, 
   3.675383835709927*^9}, {3.67538393024376*^9, 3.67538393366572*^9}, {
   3.675383993349169*^9, 3.675384026369598*^9}, {3.675384076536252*^9, 
   3.6753842133223133`*^9}, {3.675384295801578*^9, 3.6753843636525917`*^9}, {
   3.675384402129974*^9, 3.675384402254492*^9}, {3.6753845639295673`*^9, 
   3.675384568752591*^9}, {3.675384609347207*^9, 3.675384653007216*^9}, {
   3.675384708607424*^9, 3.675384712509701*^9}, {3.675384821785334*^9, 
   3.675384860979155*^9}, {3.6753848937073812`*^9, 3.6753849278490353`*^9}, {
   3.675385055917172*^9, 3.675385065641973*^9}, {3.675385160491825*^9, 
   3.675385190781549*^9}, {3.6753852363155622`*^9, 3.675385259733971*^9}, {
   3.6753852937082872`*^9, 3.675385306384241*^9}, {3.675422158192226*^9, 
   3.675422162257881*^9}, {3.6754222026014357`*^9, 3.6754222793838263`*^9}, {
   3.6754224252633*^9, 3.6754224499876757`*^9}, {3.67542252590385*^9, 
   3.675422682025778*^9}, {3.675422712063715*^9, 3.67542276284066*^9}, {
   3.675422834147614*^9, 3.675422899238347*^9}, {3.6754229701490173`*^9, 
   3.6754229925486593`*^9}, {3.675424508876302*^9, 3.675424516633699*^9}, {
   3.675426054490243*^9, 3.675426065231003*^9}, {3.675443604225565*^9, 
   3.675443628121565*^9}, {3.6772641669923553`*^9, 3.677264179724074*^9}, {
   3.6772642117960043`*^9, 3.677264243080739*^9}, {3.677264303810183*^9, 
   3.67726437121273*^9}, 3.677317720069524*^9, {3.67731775244348*^9, 
   3.677317755817498*^9}, {3.677318548832623*^9, 3.67731855270411*^9}, 
   3.67731859124115*^9, {3.67731866930385*^9, 3.677318705624124*^9}, {
   3.6773194233622828`*^9, 3.677319486604702*^9}, {3.7177610984833403`*^9, 
   3.7177611125802298`*^9}, {3.717856315814966*^9, 3.717856340396748*^9}, 
   3.718427696861578*^9, 3.718462902220702*^9, {3.718462945423148*^9, 
   3.718462955870867*^9}, 3.722688548692524*^9, {3.72271012527628*^9, 
   3.7227101313079357`*^9}, {3.722710386631114*^9, 3.722710387133795*^9}, {
   3.722765732589745*^9, 3.722765784631795*^9}, {3.722765836325492*^9, 
   3.722765909839347*^9}, {3.72706860163619*^9, 3.7270686157034893`*^9}, 
   3.729016317515798*^9, {3.729016404704863*^9, 3.729016420635425*^9}, 
   3.7290168071839046`*^9, {3.729016838042747*^9, 3.7290168537063417`*^9}, {
   3.7290170585961533`*^9, 3.729017061037243*^9}, {3.729017315805149*^9, 
   3.729017319225726*^9}, {3.729017358060417*^9, 3.7290173702771893`*^9}, {
   3.729017738529376*^9, 
   3.729017776139761*^9}},ExpressionUUID->"b6721db6-e437-4d42-ac4c-\
615cc432f927"]
}, Closed]]
}, Open  ]]
},
WindowSize->{1512, 911},
WindowMargins->{{Automatic, 254}, {163, Automatic}},
FrontEndVersion->"11.2 for Mac OS X x86 (32-bit, 64-bit Kernel) (September \
10, 2017)",
StyleDefinitions->FrontEnd`FileName[{"Creative"}, "NaturalColor.nb", 
  CharacterEncoding -> "UTF-8"]
]
(* End of Notebook Content *)

(* Internal cache information *)
(*CellTagsOutline
CellTagsIndex->{}
*)
(*CellTagsIndex
CellTagsIndex->{}
*)
(*NotebookFileOutline
Notebook[{
Cell[CellGroupData[{
Cell[1510, 35, 467, 9, 61, "Title",ExpressionUUID->"45272ac0-d37b-4e10-a13a-3a7b69a4cdd3"],
Cell[1980, 46, 1161, 34, 40, "Subtitle",ExpressionUUID->"92bdfc6c-e106-4622-b712-56b7a92269ef"],
Cell[3144, 82, 3755, 63, 404, "Text",ExpressionUUID->"ef210b5b-4039-4ea1-90a3-de83d9bd10c3"],
Cell[6902, 147, 21857, 432, 599, "Output",ExpressionUUID->"537cfb0a-1760-4baa-bef5-99181f3acf58"],
Cell[CellGroupData[{
Cell[28784, 583, 160, 3, 73, "Section",ExpressionUUID->"bba0367a-42e5-4757-932d-7512a71f9565"],
Cell[28947, 588, 49636, 1098, 2409, "Input",ExpressionUUID->"c2724515-58fb-4193-8dd2-ca937eac9e8a"]
}, Closed]]
}, Open  ]]
}
]
*)

(* NotebookSignature PuDV0EyvBBowJCKZlZJA00cd *)
