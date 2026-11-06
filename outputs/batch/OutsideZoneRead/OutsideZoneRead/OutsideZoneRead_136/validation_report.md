# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_136`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_136/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 96 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [20–34], lower_priority='Action_ZoneBlock' annotated_start=23, effective_Action_ZoneBlock_start=35.
> - Action 'Action_None' range [20-55] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-144] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-106] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-239] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [20-119] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-144] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-147] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-144] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-11] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [23-42] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [48-52] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-161] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-176] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [23-66] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [68-69] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-37] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-128] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_ReadEdgeDefender' range [39-46] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [51-56] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [93-122] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [124-153] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [159-162] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [20-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-63] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-122] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [23-34] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [37-74] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [20-27] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [40-42] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [58-84] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [23-32] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-36] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-60] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-71] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-95] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-55] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-239] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-230] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-100] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-239] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-100] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-135] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-144] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-157] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-207] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [79-176] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-239] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-109] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-125] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-132] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-168] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-206] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-217] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-187] for track '36' has 1 frames without a visible bounding box.
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
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.