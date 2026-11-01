# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_355`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_355/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 91 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [3–18], lower_priority='Action_ZoneBlock' annotated_start=6, effective_Action_ZoneBlock_start=19.
> - Action 'Action_None' range [3-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-39] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-84] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-104] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [49-153] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-112] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-117] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-179] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-90] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-180] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-168] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-180] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-101] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-139] for track '10' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [141-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-169] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-120] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-43] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-99] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-32] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-24] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-61] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-118] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [6-91] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-158] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-174] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [6-91] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-109] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-180] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [92-106] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-180] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [3-15] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [25-28] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [30-32] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [37-42] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-97] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [100-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-17] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-46] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [48-49] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-14] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-124] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-180] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [47-71] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-112] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-169] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [67-163] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [103-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-128] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-149] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-155] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-160] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-180] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-180] for track '32' has 1 frames without a visible bounding box.
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