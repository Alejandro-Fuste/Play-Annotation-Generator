# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_64`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_64/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 105 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 399 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 130: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 130: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 399 as fallback play end.
> - Action 'Action_PullBlock' range [315-340] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [346-366] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [315-366] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [367-383] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-136] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-140] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-146] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-190] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [342-399] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [312-376] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-399] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [312-323] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-335] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-372] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-385] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-399] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [312-399] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [315-327] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [367-374] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-368] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-373] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-81] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-100] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-104] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-114] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-150] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-158] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-162] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-167] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-343] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-354] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [360-361] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-364] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-154] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-196] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-311] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' for track '15' starts at frame 312, but the player has no visible bounding box on this frame.
> - Action 'Action_BallSnap' range [312-312] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-399] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [312-381] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [383-385] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-223] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-242] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-273] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [308-309] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-313] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-330] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-338] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-45] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-53] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [312-338] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [343-348] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-133] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-177] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-216] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-229] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-282] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-297] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-316] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-290] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-326] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-338] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-349] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-359] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [319-399] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [343-399] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [351-353] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-399] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [382-394] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [384-396] for track '29' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.