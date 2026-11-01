# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_256`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_256/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 69 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [20–33], lower_priority='Action_ZoneBlock' annotated_start=23, effective_Action_ZoneBlock_start=34.
> - Action 'Action_None' range [20-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-61] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-148] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [93-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-124] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-105] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-132] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-87] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [72-152] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-159] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-101] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-127] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-121] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-134] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-128] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-95] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-29] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-51] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [60-61] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-28] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-125] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-77] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-83] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-107] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [115-139] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-126] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-178] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '25' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.