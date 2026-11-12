# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_132`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_132/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 114 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '1' (LT) duration 137 frames exceeds threshold 90 frames [start=141, end=277].
> - Validation warning: Action 'Action_ZoneBlock' for track '13' (RG) duration 166 frames exceeds threshold 90 frames [start=141, end=306].
> - Action 'Action_None' range [138-172] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [141-153] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [156-169] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [186-236] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [243-254] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [256-277] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-169] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-224] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [148-286] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [307-321] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-325] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [141-163] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [141-162] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [198-218] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-83] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-227] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-288] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-66] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-122] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-212] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [138-237] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-40] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-103] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-64] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-82] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-105] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-206] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-27] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-99] for track '12' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [138-153] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-167] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-190] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-81] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-119] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [141-224] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [233-247] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-309] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-283] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [174-179] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [182-185] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [200-235] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-249] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-281] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-327] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-175] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-182] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-198] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-202] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-258] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-265] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-275] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-260] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-267] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-284] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [288-290] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-239] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [261-265] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-262] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-268] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-288] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-251] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-276] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-298] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-315] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-328] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-278] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-281] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-290] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-294] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-264] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-274] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-312] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-320] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-329] for track '36' has 1 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.