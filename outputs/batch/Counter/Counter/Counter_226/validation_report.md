# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_226`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_226/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 101 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 454: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '3' (LG) duration 104 frames exceeds threshold 90 frames [start=129, end=232].
> - Validation warning: Action 'Action_PullBlock' for track '4' (RG) duration 104 frames exceeds threshold 90 frames [start=129, end=232].
> - Validation warning: Action 'Action_DownBlock' for track '10' (C) duration 104 frames exceeds threshold 90 frames [start=129, end=232].
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [126–142], lower_priority='Action_DownBlock' annotated_start=129, effective_Action_DownBlock_start=143.
> - Action 'Action_None' range [126-302] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-171] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [134-177] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [183-354] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [129-152] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [155-163] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-324] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [129-232] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-311] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-225] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-232] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-312] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-217] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-300] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [126-142] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [144-181] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [126-220] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [129-167] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-240] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-330] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-145] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-197] for track '15' has 6 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [129-132] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-121] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-160] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-359] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-125] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [126-164] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-206] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-239] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-147] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-359] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-202] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-359] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-229] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [236-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-221] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-245] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-265] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-346] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-359] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [238-358] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-359] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [261-262] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-262] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-275] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-285] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-300] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-310] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-347] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-351] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-296] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-301] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [314-315] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-321] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-326] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-351] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [335-337] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-357] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-337] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-339] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-355] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-359] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-348] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [350-357] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-353] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [351-354] for track '39' has 1 frames without a visible bounding box.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.