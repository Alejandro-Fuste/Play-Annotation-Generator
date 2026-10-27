# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_146`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_146/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 146 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 294: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_PreSnap' range [0-30] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-63] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-318] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-256] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-309] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-318] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [340-353] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-29] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-99] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-152] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-155] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-160] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-164] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-176] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-206] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-216] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-94] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-133] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-157] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [193-194] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [204-212] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [216-217] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [219-257] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-260] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [174-257] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [258-264] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-132] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-159] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-195] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-199] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-289] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [214-262] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [264-265] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [274-280] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [293-294] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [299-303] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [327-334] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-45] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-58] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-84] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-90] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-215] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-220] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-272] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-309] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [174-178] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [180-187] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [200-202] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-13] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-33] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-45] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-74] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-85] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-91] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-107] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' for track '14' starts at frame 174, but the player has no visible bounding box on this frame.
> - Action 'Action_DownBlock' range [174-202] for track '14' has 5 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [209-257] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-82] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-156] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-168] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-176] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-204] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-209] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-219] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-266] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-301] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-359] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-64] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-70] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-113] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-168] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [169-176] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-217] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-91] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-135] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-138] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-168] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '17' starts at frame 169, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [169-169] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-174] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-204] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [209-224] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-185] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-267] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [269-272] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-125] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-129] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-173] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' for track '19' starts at frame 174, but the player has no visible bounding box on this frame.
> - Action 'Action_PullLeadBlock' range [174-176] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [182-191] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [211-220] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-193] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [229-268] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [278-282] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-204] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-220] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-264] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-308] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-211] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-240] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-205] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-345] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-344] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-290] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-325] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-286] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-312] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-359] for track '30' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.