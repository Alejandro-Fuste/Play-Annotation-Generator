# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_359`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_359/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 720: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [141–158], lower_priority='Action_DownBlock' annotated_start=144, effective_Action_DownBlock_start=159.
> - Action 'Action_None' range [141-236] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-266] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [141-289] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-294] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-285] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-262] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-226] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-218] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-307] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [314-329] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-233] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-238] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-219] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-275] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [187-247] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [159-161] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [174-204] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [206-212] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-270] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [144-190] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [213-214] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-276] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [144-149] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [158-162] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [167-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [186-196] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [201-204] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [144-194] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-278] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-203] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-253] for track '22' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [255-268] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-261] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [206-229] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [231-239] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-240] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [243-244] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-271] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [247-268] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-270] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [288-289] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-323] for track '31' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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