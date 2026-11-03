# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `StopAndGo_37`
- **Input XML**: `outputs/batch/StopAndGo/StopAndGo/StopAndGo_37/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/StopAndGo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 49 |
| Player Tracks | 49 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 138 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_None' range [8-108] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-114] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-257] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-225] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-233] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-46] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-66] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-73] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-29] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [52-198] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [204-216] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [8-58] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [63-109] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-113] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-178] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-193] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-117] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [128-133] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [137-142] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-54] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [56-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [122-143] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [154-155] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [158-159] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-101] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-125] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [94-137] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [140-141] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [148-149] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [164-165] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [172-179] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [182-185] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [188-190] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-17] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [19-30] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [37-269] for track '14' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [8-20] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-220] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [232-256] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-214] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [8-16] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-29] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-95] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-110] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [8-20] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-123] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-171] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-45] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-269] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-44] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-93] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-129] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [86-106] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-130] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-98] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-93] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-106] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-131] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-139] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-150] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-158] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-231] for track '27' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [138-143] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-161] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-167] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-209] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-214] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-268] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-201] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-252] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-255] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-269] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-202] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-175] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-188] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-229] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-248] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [251-261] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-184] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-213] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-204] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-216] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-243] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-246] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-269] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-240] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-245] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [248-254] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [260-262] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-241] for track '43' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [249-253] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-269] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-252] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-260] for track '46' has 1 frames without a visible bounding box.
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
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.
> - Play definition: no definition found for 'Play_Pass_StopAndGo'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.