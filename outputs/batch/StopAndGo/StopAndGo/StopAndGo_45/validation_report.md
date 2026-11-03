# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `StopAndGo_45`
- **Input XML**: `outputs/batch/StopAndGo/StopAndGo/StopAndGo_45/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/StopAndGo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 46 |
| Player Tracks | 46 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 175 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [16–29], lower_priority='Action_PassBlock' annotated_start=19, effective_Action_PassBlock_start=30.
> - Action 'Action_None' range [16-135] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-142] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-162] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-73] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-85] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-118] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-161] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-167] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-172] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [79-118] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [123-131] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [133-134] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-215] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-118] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-123] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-37] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-38] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-41] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-131] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-137] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-154] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-171] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-269] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-42] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-66] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-171] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-177] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-203] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-218] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-246] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-257] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-149] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-164] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-172] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-190] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-197] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-203] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-223] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [228-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-260] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [16-29] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-34] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [95-99] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [102-103] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [117-135] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [138-141] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [143-155] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [160-165] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [176-178] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-41] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-91] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-99] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-111] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-149] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [151-168] for track '13' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [16-32] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [19-28] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [19-40] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [59-65] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-44] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-49] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-59] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-136] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-149] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-155] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-206] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-269] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [19-36] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [98-99] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [105-107] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-26] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-35] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-22] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-31] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-87] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-100] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-81] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-135] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-141] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-186] for track '22' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-203] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-209] for track '23' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [212-260] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-99] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-106] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-160] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-108] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-116] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-173] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-187] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-198] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-130] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-124] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-130] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-171] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-168] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [168-172] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-189] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-205] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [182-269] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-193] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-269] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-195] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-207] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-234] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-269] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-216] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-238] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-212] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-216] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-217] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-226] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-237] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-241] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-255] for track '40' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-231] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-235] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-255] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-233] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-246] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [258-263] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-267] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-269] for track '45' has 1 frames without a visible bounding box.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Play definition: no definition found for 'Play_Pass_StopAndGo'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.