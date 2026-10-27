# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_118`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_118/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '6' (LG) duration 101 frames exceeds threshold 90 frames [start=216, end=316].
> - Action 'Action_DownBlock' range [216-251] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [253-264] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-252] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-419] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-243] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-413] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-233] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-353] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [216-232] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [238-256] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [257-408] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [216-316] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-340] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-419] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-369] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-419] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-229] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-300] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-302] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-307] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [309-313] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-333] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-231] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-340] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-119] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [219-403] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [406-412] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [317-384] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-190] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-199] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-321] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-314] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-419] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [273-290] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [289-391] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-370] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-320] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-411] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-419] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-315] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-329] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [332-419] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [333-336] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-340] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-415] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-372] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-376] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-385] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [395-396] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [398-406] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [409-415] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [403-406] for track '29' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.