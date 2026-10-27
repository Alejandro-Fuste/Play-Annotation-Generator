# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `Counter_391`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_391/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 89 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_DownBlock' at frame 75 targets track ID 'LG', but it is not found in XML.
> - Event 'Action_DownBlock' at frame 75 targets track ID 'LT', but it is not found in XML.
> - Event 'Action_PullBlock' at frame 75 targets track ID 'RG', but it is not found in XML.
> - Event 'Action_PullLeadBlock' at frame 75 targets track ID 'H', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 784: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [73–92], lower_priority='Action_DownBlock' annotated_start=75, effective_Action_DownBlock_start=93.
> - Action 'Action_None' range [73-153] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-171] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-186] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-141] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-238] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [73-129] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [122-123] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-93] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-98] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [73-81] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-169] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-46] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-54] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-59] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-68] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-71] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-105] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [73-78] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [144-145] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [153-154] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-98] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-111] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-116] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-135] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-135] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-154] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-167] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-176] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-140] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-166] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-184] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-163] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-235] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-167] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-171] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-184] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-209] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-218] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-234] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-190] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-204] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-220] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-227] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-231] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-197] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-215] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-205] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-220] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-239] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-225] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-233] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-239] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-233] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-233] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-239] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-239] for track '38' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.