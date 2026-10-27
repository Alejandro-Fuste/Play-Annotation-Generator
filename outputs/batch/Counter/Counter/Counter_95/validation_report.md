# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_95`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_95/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 85 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '16' (RG) duration 99 frames exceeds threshold 90 frames [start=108, end=206].
> - Segment 'Action_DownBlock' for track '17' has invalid range: start=108, end=100. Clamping end to start.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [101–115], lower_priority='Action_DownBlock' annotated_start=108, effective_Action_DownBlock_start=116.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [101–115], lower_priority='Action_SnapReceive' annotated_start=101, effective_Action_SnapReceive_start=116.
> - Action 'Action_None' range [101-159] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-238] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-269] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-263] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-184] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [108-195] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-144] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-209] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-158] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-226] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [125-137] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-161] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-174] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-190] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [108-121] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-269] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-182] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-201] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-206] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-139] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-121] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-144] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-184] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-245] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [247-255] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-260] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-268] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-257] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-212] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-231] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-231] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-240] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-250] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-257] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-253] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [253-261] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-262] for track '33' has 2 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.