# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_84`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_84/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 85 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Segment 'Action_BallCarry' for track '7' has invalid range: start=250, end=247. Clamping end to start.
> - Overlapping action conflict at frame 212 for track '17': 'Action_BallSnap' vs 'Action_PullBlock'. Overriding with 'Action_PullBlock'.
> - Action 'Action_PreSnap' range [0-211] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-287] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-134] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-289] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-359] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-131] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [212-235] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-109] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-117] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-335] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-247] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-148] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-246] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-211] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [212-297] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-312] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-336] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-359] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [212-229] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-130] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-152] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-66] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-103] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-107] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [212-298] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-359] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-25] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-37] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-122] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-243] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-158] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-163] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-226] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-263] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-280] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [285-289] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-211] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-220] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-283] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [286-355] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-234] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-236] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-243] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-323] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [246-247] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-337] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-359] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-353] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-359] for track '33' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.